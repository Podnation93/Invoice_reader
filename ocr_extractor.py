"""
OCR Extractor Module
Intelligent, context-aware data extraction from invoice images
"""

import re
from pathlib import Path
import pytesseract
import cv2
import numpy as np
from datetime import datetime


class OCRExtractor:
    """Extracts invoice data using intelligent OCR and contextual logic"""

    def __init__(self):
        # Regex patterns for data extraction
        self.date_patterns = [
            r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b',  # DD/MM/YYYY or MM/DD/YYYY
            r'\b\d{4}[/-]\d{1,2}[/-]\d{1,2}\b',  # YYYY-MM-DD
            r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2},? \d{4}\b',  # Month DD, YYYY
            r'\b\d{1,2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{4}\b',  # DD Month YYYY
        ]

        self.invoice_number_patterns = [
            r'\b(?:INV|inv|Invoice|INVOICE)[- #:]*([A-Z0-9-]+)\b',
            r'\b([A-Z]{2,}-\d{3,})\b',  # Pattern like AB-12345
            r'\b(#?\d{4,})\b',  # Simple number sequence
        ]

        self.currency_pattern = r'[$£€¥]\s*\d+[,.]?\d*'
        self.amount_pattern = r'\d+[,.]?\d{0,2}'

    def extract_invoice_data(self, images, pdf_path):
        """
        Extract all invoice data from PDF images

        Args:
            images (list): List of PIL Image objects
            pdf_path (str): Original PDF path for reference

        Returns:
            list: List of dictionaries containing invoice line item data
        """
        all_line_items = []

        for page_num, image in enumerate(images, 1):
            # Convert PIL image to OpenCV format
            cv_image = self.pil_to_cv2(image)

            # Extract text using OCR
            text = self.extract_text(cv_image)

            if not text:
                continue

            # Extract invoice-level data
            contact_name = self.extract_contact_name(text)
            address_lines = self.extract_address(text)
            invoice_number = self.extract_invoice_number(text)
            invoice_date, due_date = self.extract_dates(text)

            # Extract line items from the table
            line_items = self.extract_line_items(text, cv_image)

            # If we found line items, create CSV rows
            if line_items:
                for item in line_items:
                    row_data = {
                        # Invoice-level data (duplicated for each line item)
                        'ContactName': contact_name,
                        'EmailAddress': '',
                        'POAddressLine1': address_lines[0] if len(address_lines) > 0 else '',
                        'POAddressLine2': address_lines[1] if len(address_lines) > 1 else '',
                        'POAddressLine3': address_lines[2] if len(address_lines) > 2 else '',
                        'POAddressLine4': address_lines[3] if len(address_lines) > 3 else '',
                        'POCity': address_lines[4] if len(address_lines) > 4 else '',
                        'PORegion': '',
                        'POPostalCode': '',
                        'POCountry': '',
                        'InvoiceNumber': invoice_number,
                        'Reference': '',
                        'InvoiceDate': invoice_date,
                        'DueDate': due_date,

                        # Line item data
                        'InventoryItemCode': item.get('code', ''),
                        'Description': item.get('description', ''),
                        'Quantity': item.get('quantity', ''),
                        'UnitAmount': item.get('unit_amount', ''),
                        'Discount': '',
                        'AccountCode': '',
                        'TaxType': '',
                        'TrackingName1': '',
                        'TrackingOption1': '',
                        'TrackingName2': '',
                        'TrackingOption2': '',
                        'Currency': '',
                        'BrandingTheme': '',
                    }
                    all_line_items.append(row_data)

        return all_line_items

    def pil_to_cv2(self, pil_image):
        """Convert PIL Image to OpenCV format"""
        return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    def extract_text(self, cv_image):
        """Extract text from image using Tesseract OCR"""
        try:
            # Convert to grayscale
            gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

            # Apply threshold to get better OCR results
            _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            # Extract text
            text = pytesseract.image_to_string(thresh)

            return text
        except Exception as e:
            print(f"Error extracting text: {e}")
            return ""

    def extract_contact_name(self, text):
        """
        Extract contact name using contextual logic

        Logic: Look for formatted address blocks. The first line is typically the contact name.
        Prioritize blocks near keywords like "To:", "Bill To:", "Customer:"
        """
        lines = text.split('\n')

        # Keywords that often precede customer information
        customer_keywords = ['to:', 'bill to:', 'customer:', 'client:', 'billed to:', 'invoice to:']

        for i, line in enumerate(lines):
            line_lower = line.lower().strip()

            # Check if this line contains a customer keyword
            if any(keyword in line_lower for keyword in customer_keywords):
                # The next non-empty line is likely the contact name
                for j in range(i + 1, min(i + 5, len(lines))):
                    potential_name = lines[j].strip()
                    if potential_name and len(potential_name) > 2:
                        # Filter out common non-name patterns
                        if not re.match(r'^\d', potential_name):  # Don't start with digit
                            return potential_name

        # Fallback: Look for lines in the upper portion that look like names
        # (capitalized words, not too short, not too long)
        for i, line in enumerate(lines[:15]):  # Search first 15 lines
            line = line.strip()
            if 10 <= len(line) <= 50 and not re.match(r'^\d', line):
                # Check if it looks like a name (has capital letters)
                if re.search(r'[A-Z][a-z]+\s+[A-Z]', line):
                    return line

        return ""

    def extract_address(self, text):
        """
        Extract address lines using contextual logic

        Logic: Find address blocks (2-5 lines of text) near customer information
        """
        lines = text.split('\n')
        address_lines = []

        customer_keywords = ['to:', 'bill to:', 'customer:', 'client:', 'billed to:']

        for i, line in enumerate(lines):
            line_lower = line.lower().strip()

            # Check if this line contains a customer keyword
            if any(keyword in line_lower for keyword in customer_keywords):
                # Extract the next 2-5 lines as address
                for j in range(i + 2, min(i + 7, len(lines))):  # Skip name, get address
                    addr_line = lines[j].strip()
                    if addr_line and len(addr_line) > 2:
                        # Stop if we hit what looks like another section
                        if any(keyword in addr_line.lower() for keyword in ['invoice', 'date', 'number', 'amount']):
                            break
                        address_lines.append(addr_line)

                if address_lines:
                    break

        return address_lines

    def extract_invoice_number(self, text):
        """
        Extract invoice number using contextual logic

        Logic: Try multiple patterns. Look in the top-right quadrant typically.
        Don't rely on the label "Invoice #" being present.
        """
        lines = text.split('\n')

        # First, try to find explicit invoice number with label
        for pattern in self.invoice_number_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                # Return the captured group or the match
                return match.group(1) if match.lastindex else match.group(0)

        # Fallback: Look for alphanumeric strings in first 10 lines (header area)
        # that match common invoice number patterns
        for line in lines[:10]:
            # Look for patterns like: INV-123, AB-456, #12345
            match = re.search(r'([A-Z]{2,}-\d{3,}|#\d{4,}|\d{5,})', line)
            if match:
                potential_num = match.group(1)
                # Verify it's not a date or phone number
                if not re.search(r'\d{4}[-/]\d{2}[-/]\d{2}', potential_num):
                    return potential_num

        return ""

    def extract_dates(self, text):
        """
        Extract invoice date and due date using contextual logic

        Logic:
        - Find all dates using pattern matching
        - The date near "Due" keyword is the due date
        - The other primary date is the invoice date
        """
        lines = text.split('\n')
        all_dates = []
        due_date = ""
        invoice_date = ""

        # Find all dates in the text
        for line in lines:
            for pattern in self.date_patterns:
                matches = re.findall(pattern, line, re.IGNORECASE)
                for match in matches:
                    # Check if this line contains "due"
                    if 'due' in line.lower():
                        due_date = match
                    else:
                        all_dates.append(match)

        # Invoice date is typically the first date found (that's not the due date)
        if all_dates and not invoice_date:
            invoice_date = all_dates[0]

        return invoice_date, due_date

    def extract_line_items(self, text, cv_image):
        """
        Extract line items from the invoice table

        Logic: Find the main data table by identifying its structure
        (columns of text, numbers, and currency values)
        """
        line_items = []

        # Use pytesseract to get detailed position data
        try:
            data = pytesseract.image_to_data(cv_image, output_type=pytesseract.Output.DICT)

            # Group text by vertical position to find table rows
            rows = self.group_text_by_rows(data)

            # Find table header
            table_start = self.find_table_start(rows)

            if table_start == -1:
                # Fallback: simple text parsing
                return self.extract_line_items_simple(text)

            # Extract rows from the table
            for i in range(table_start + 1, len(rows)):
                row_data = rows[i]

                # Check if this looks like a table row (has numbers/amounts)
                if self.is_table_row(row_data):
                    item = self.parse_table_row(row_data)
                    if item:
                        line_items.append(item)
                else:
                    # If we encounter too many non-table rows, we've left the table
                    break

        except Exception as e:
            print(f"Error extracting line items: {e}")
            # Fallback to simple extraction
            return self.extract_line_items_simple(text)

        return line_items

    def group_text_by_rows(self, ocr_data):
        """Group OCR text by vertical position (rows)"""
        rows = {}

        for i, text in enumerate(ocr_data['text']):
            if text.strip():
                top = ocr_data['top'][i]
                left = ocr_data['left'][i]

                # Group by vertical position (within 10 pixels)
                row_key = round(top / 10) * 10

                if row_key not in rows:
                    rows[row_key] = []

                rows[row_key].append({
                    'text': text,
                    'left': left,
                    'top': top
                })

        # Sort rows by vertical position
        sorted_rows = [rows[key] for key in sorted(rows.keys())]

        return sorted_rows

    def find_table_start(self, rows):
        """Find where the table starts (usually after a header row)"""
        table_keywords = ['description', 'item', 'quantity', 'qty', 'amount', 'price', 'total']

        for i, row in enumerate(rows):
            row_text = ' '.join([word['text'].lower() for word in row])

            # Check if this row contains table header keywords
            if any(keyword in row_text for keyword in table_keywords):
                return i

        return -1

    def is_table_row(self, row_data):
        """Check if a row looks like a table row (contains numbers/amounts)"""
        row_text = ' '.join([word['text'] for word in row_data])

        # Table rows typically have at least one number and some text
        has_number = bool(re.search(r'\d', row_text))
        has_text = bool(re.search(r'[a-zA-Z]{2,}', row_text))

        return has_number and has_text

    def parse_table_row(self, row_data):
        """Parse a table row into line item components"""
        # Sort by horizontal position
        sorted_words = sorted(row_data, key=lambda x: x['left'])

        texts = [word['text'] for word in sorted_words]
        row_text = ' '.join(texts)

        # Try to identify components
        description = ""
        quantity = ""
        unit_amount = ""
        item_code = ""

        # Find amounts (rightmost numbers are usually amounts)
        amounts = re.findall(r'\d+[.,]?\d{0,2}', row_text)

        if amounts:
            unit_amount = amounts[-1]  # Last amount is unit price
            if len(amounts) > 1:
                quantity = amounts[-2]  # Second to last is quantity

        # Description is typically the text (non-numeric) parts
        description_parts = []
        for text in texts:
            if not re.match(r'^[\d.,]+$', text):  # Not just numbers
                description_parts.append(text)

        description = ' '.join(description_parts[:5])  # Limit description length

        # Only return if we have at least description and amount
        if description and (unit_amount or quantity):
            return {
                'code': item_code,
                'description': description,
                'quantity': quantity if quantity else '1',
                'unit_amount': unit_amount
            }

        return None

    def extract_line_items_simple(self, text):
        """Fallback: Simple line item extraction from text"""
        line_items = []
        lines = text.split('\n')

        # Look for lines that contain both text and numbers
        for line in lines:
            line = line.strip()

            # Skip empty lines and header-like lines
            if not line or len(line) < 10:
                continue

            # Look for lines with amounts (contain currency or decimal numbers)
            if re.search(r'\d+[.,]\d{2}', line):
                # Try to split into description and amounts
                parts = line.split()

                if len(parts) >= 2:
                    # Extract amounts (numbers)
                    amounts = [p for p in parts if re.match(r'^\d+[.,]?\d*$', p)]

                    # Extract description (non-numeric parts)
                    desc_parts = [p for p in parts if not re.match(r'^[\d.,]+$', p)]

                    if desc_parts and amounts:
                        item = {
                            'code': '',
                            'description': ' '.join(desc_parts),
                            'quantity': amounts[0] if len(amounts) > 1 else '1',
                            'unit_amount': amounts[-1]
                        }
                        line_items.append(item)

        return line_items
