"""
CSV Generator Module
Generates CSV output with exact column format as specified
"""

import pandas as pd
from pathlib import Path


class CSVGenerator:
    """Generates CSV files with the required format"""

    def __init__(self):
        # Exact column order as specified in requirements
        self.columns = [
            'ContactName',
            'EmailAddress',
            'POAddressLine1',
            'POAddressLine2',
            'POAddressLine3',
            'POAddressLine4',
            'POCity',
            'PORegion',
            'POPostalCode',
            'POCountry',
            'InvoiceNumber',
            'Reference',
            'InvoiceDate',
            'DueDate',
            'InventoryItemCode',
            'Description',
            'Quantity',
            'UnitAmount',
            'Discount',
            'AccountCode',
            'TaxType',
            'TrackingName1',
            'TrackingOption1',
            'TrackingName2',
            'TrackingOption2',
            'Currency',
            'BrandingTheme'
        ]

    def generate_csv(self, invoice_data, output_path):
        """
        Generate CSV file from extracted invoice data

        Args:
            invoice_data (list): List of dictionaries containing invoice line items
            output_path (str): Path where CSV should be saved

        Returns:
            str: Path to the generated CSV file
        """
        if not invoice_data:
            raise ValueError("No invoice data to write to CSV")

        # Create DataFrame from invoice data
        df = pd.DataFrame(invoice_data)

        # Ensure all required columns exist (add empty columns if missing)
        for col in self.columns:
            if col not in df.columns:
                df[col] = ''

        # Reorder columns to match required format exactly
        df = df[self.columns]

        # Write to CSV
        df.to_csv(output_path, index=False)

        return output_path

    def validate_data(self, invoice_data):
        """
        Validate invoice data before CSV generation

        Args:
            invoice_data (list): List of dictionaries containing invoice line items

        Returns:
            tuple: (is_valid, error_messages)
        """
        errors = []

        if not invoice_data:
            errors.append("No invoice data provided")
            return False, errors

        # Check that each row has the basic required fields
        required_fields = ['ContactName', 'InvoiceNumber', 'InvoiceDate', 'Description', 'Quantity', 'UnitAmount']

        for i, row in enumerate(invoice_data):
            missing_fields = [field for field in required_fields if not row.get(field)]

            if missing_fields:
                errors.append(f"Row {i + 1} missing required fields: {', '.join(missing_fields)}")

        is_valid = len(errors) == 0
        return is_valid, errors
