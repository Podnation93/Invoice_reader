"""
Error Logger Module
Logs errors and issues during PDF processing
"""

import os
from datetime import datetime
from pathlib import Path


class ErrorLogger:
    """Handles error logging to extraction_log.txt"""

    def __init__(self, log_file='extraction_log.txt'):
        self.log_file = log_file
        self.initialize_log()

    def initialize_log(self):
        """Initialize or clear the log file for a new session"""
        with open(self.log_file, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("Invoice Reader - Extraction Log\n")
            f.write(f"Session started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n\n")

    def log_error(self, pdf_path, error_message):
        """
        Log an error for a specific PDF file

        Args:
            pdf_path (str): Path to the PDF file that caused the error
            error_message (str): Description of the error
        """
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")
            f.write(f"File: {Path(pdf_path).name}\n")
            f.write(f"Full Path: {pdf_path}\n")
            f.write(f"Error: {error_message}\n")
            f.write("-" * 80 + "\n\n")

    def log_warning(self, pdf_path, warning_message):
        """
        Log a warning for a specific PDF file

        Args:
            pdf_path (str): Path to the PDF file
            warning_message (str): Description of the warning
        """
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] WARNING\n")
            f.write(f"File: {Path(pdf_path).name}\n")
            f.write(f"Warning: {warning_message}\n")
            f.write("-" * 80 + "\n\n")

    def log_success(self, pdf_path, line_items_count):
        """
        Log successful processing of a PDF

        Args:
            pdf_path (str): Path to the PDF file
            line_items_count (int): Number of line items extracted
        """
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] SUCCESS\n")
            f.write(f"File: {Path(pdf_path).name}\n")
            f.write(f"Extracted {line_items_count} line items\n")
            f.write("-" * 80 + "\n\n")

    def finalize_log(self, total_files, successful_files, failed_files):
        """
        Add summary to the end of the log

        Args:
            total_files (int): Total number of files processed
            successful_files (int): Number of successfully processed files
            failed_files (int): Number of failed files
        """
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("SUMMARY\n")
            f.write("=" * 80 + "\n")
            f.write(f"Total files processed: {total_files}\n")
            f.write(f"Successful: {successful_files}\n")
            f.write(f"Failed: {failed_files}\n")
            f.write(f"Session ended: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n")
