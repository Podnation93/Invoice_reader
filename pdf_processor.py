"""
PDF Processor Module
Converts PDF files to images for OCR processing
"""

import os
from pathlib import Path
from pdf2image import convert_from_path
from PIL import Image


class PDFProcessor:
    """Handles PDF to image conversion"""

    def __init__(self):
        self.dpi = 300  # High DPI for better OCR accuracy

    def pdf_to_images(self, pdf_path):
        """
        Convert a PDF file to a list of PIL Image objects

        Args:
            pdf_path (str): Path to the PDF file

        Returns:
            list: List of PIL Image objects, one per page
        """
        try:
            # Convert PDF to images
            images = convert_from_path(
                pdf_path,
                dpi=self.dpi,
                fmt='png',
                thread_count=4
            )

            # Preprocess images for better OCR
            processed_images = []
            for img in images:
                processed_img = self.preprocess_image(img)
                processed_images.append(processed_img)

            return processed_images

        except Exception as e:
            print(f"Error converting PDF {pdf_path}: {e}")
            return []

    def preprocess_image(self, image):
        """
        Preprocess image for better OCR accuracy

        Args:
            image (PIL.Image): Input image

        Returns:
            PIL.Image: Preprocessed image
        """
        # Convert to RGB if necessary
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # You can add more preprocessing here if needed:
        # - Contrast enhancement
        # - Noise reduction
        # - Deskewing
        # For now, we'll keep it simple

        return image

    def is_valid_pdf(self, pdf_path):
        """
        Check if a file is a valid PDF

        Args:
            pdf_path (str): Path to the file

        Returns:
            bool: True if valid PDF, False otherwise
        """
        if not os.path.exists(pdf_path):
            return False

        if not pdf_path.lower().endswith('.pdf'):
            return False

        # Try to open the file to verify it's not corrupted
        try:
            with open(pdf_path, 'rb') as f:
                header = f.read(5)
                # PDF files start with %PDF-
                return header == b'%PDF-'
        except Exception:
            return False
