"""
Invoice Reader - Main Application
Batch-process PDF invoices with intelligent OCR extraction
"""

import sys
import os
from pathlib import Path
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QLabel, QProgressBar, QFileDialog,
    QMessageBox
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QDragEnterEvent, QDropEvent

from pdf_processor import PDFProcessor
from ocr_extractor import OCRExtractor
from csv_generator import CSVGenerator
from logger import ErrorLogger


class ProcessingThread(QThread):
    """Background thread for processing invoices"""
    progress_update = pyqtSignal(int, int)  # current, total
    status_update = pyqtSignal(str)
    finished = pyqtSignal(str, list)  # output_path, errors

    def __init__(self, pdf_files, output_path):
        super().__init__()
        self.pdf_files = pdf_files
        self.output_path = output_path
        self.pdf_processor = PDFProcessor()
        self.ocr_extractor = OCRExtractor()
        self.csv_generator = CSVGenerator()
        self.error_logger = ErrorLogger()

    def run(self):
        """Process all PDF files and generate CSV"""
        all_invoice_data = []
        errors = []

        total = len(self.pdf_files)

        for idx, pdf_path in enumerate(self.pdf_files, 1):
            self.status_update.emit(f"Processing {Path(pdf_path).name}...")
            self.progress_update.emit(idx, total)

            try:
                # Convert PDF to images
                images = self.pdf_processor.pdf_to_images(pdf_path)

                if not images:
                    error_msg = f"Failed to convert PDF to images: {pdf_path}"
                    errors.append(error_msg)
                    self.error_logger.log_error(pdf_path, error_msg)
                    continue

                # Extract data using OCR
                invoice_data = self.ocr_extractor.extract_invoice_data(images, pdf_path)

                if invoice_data:
                    all_invoice_data.extend(invoice_data)
                else:
                    error_msg = f"No data extracted from: {pdf_path}"
                    errors.append(error_msg)
                    self.error_logger.log_error(pdf_path, error_msg)

            except Exception as e:
                error_msg = f"Error processing {pdf_path}: {str(e)}"
                errors.append(error_msg)
                self.error_logger.log_error(pdf_path, error_msg)

        # Generate CSV output
        if all_invoice_data:
            self.status_update.emit("Generating CSV output...")
            output_file = self.csv_generator.generate_csv(all_invoice_data, self.output_path)
            self.finished.emit(output_file, errors)
        else:
            self.finished.emit("", errors)


class InvoiceReaderGUI(QMainWindow):
    """Main GUI window for Invoice Reader"""

    def __init__(self):
        super().__init__()
        self.pdf_files = []
        self.processing_thread = None
        self.init_ui()

    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("Invoice Reader - Batch PDF Processor")
        self.setGeometry(100, 100, 800, 600)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Title label
        title_label = QLabel("Invoice Reader")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; margin: 10px;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Instructions label
        instructions = QLabel(
            "Add PDF invoices using the buttons below or drag and drop files/folders here.\n"
            "Click 'Start Extraction' to process all files."
        )
        instructions.setAlignment(Qt.AlignCenter)
        instructions.setStyleSheet("margin: 10px; color: #666;")
        layout.addWidget(instructions)

        # Button row
        button_layout = QHBoxLayout()

        self.add_files_btn = QPushButton("Add PDF Files")
        self.add_files_btn.clicked.connect(self.add_files)
        button_layout.addWidget(self.add_files_btn)

        self.add_folder_btn = QPushButton("Add Folder")
        self.add_folder_btn.clicked.connect(self.add_folder)
        button_layout.addWidget(self.add_folder_btn)

        self.clear_btn = QPushButton("Clear All")
        self.clear_btn.clicked.connect(self.clear_files)
        button_layout.addWidget(self.clear_btn)

        layout.addLayout(button_layout)

        # File list widget
        list_label = QLabel("Selected PDF Files:")
        layout.addWidget(list_label)

        self.file_list = QListWidget()
        self.file_list.setAcceptDrops(True)
        self.file_list.setDragEnabled(True)
        layout.addWidget(self.file_list)

        # Enable drag and drop on main window
        self.setAcceptDrops(True)

        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)

        # Status label
        self.status_label = QLabel("Ready")
        self.status_label.setStyleSheet("margin: 5px; color: #007ACC;")
        layout.addWidget(self.status_label)

        # Start button
        self.start_btn = QPushButton("Start Extraction")
        self.start_btn.setStyleSheet(
            "background-color: #007ACC; color: white; font-size: 16px; "
            "padding: 10px; font-weight: bold;"
        )
        self.start_btn.clicked.connect(self.start_extraction)
        layout.addWidget(self.start_btn)

    def dragEnterEvent(self, event: QDragEnterEvent):
        """Handle drag enter event"""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        """Handle drop event"""
        urls = event.mimeData().urls()

        for url in urls:
            path = url.toLocalFile()

            if os.path.isfile(path) and path.lower().endswith('.pdf'):
                self.add_pdf_file(path)
            elif os.path.isdir(path):
                self.add_pdf_from_folder(path)

    def add_files(self):
        """Open file dialog to add PDF files"""
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Select PDF Files",
            "",
            "PDF Files (*.pdf)"
        )

        for file_path in files:
            self.add_pdf_file(file_path)

    def add_folder(self):
        """Open folder dialog to add all PDFs from a folder"""
        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Folder Containing PDFs"
        )

        if folder:
            self.add_pdf_from_folder(folder)

    def add_pdf_from_folder(self, folder_path):
        """Add all PDF files from a folder"""
        folder = Path(folder_path)
        pdf_files = list(folder.glob("*.pdf")) + list(folder.glob("*.PDF"))

        for pdf_file in pdf_files:
            self.add_pdf_file(str(pdf_file))

    def add_pdf_file(self, file_path):
        """Add a single PDF file to the list"""
        if file_path not in self.pdf_files:
            self.pdf_files.append(file_path)
            self.file_list.addItem(Path(file_path).name)
            self.status_label.setText(f"Added: {Path(file_path).name} | Total files: {len(self.pdf_files)}")

    def clear_files(self):
        """Clear all selected files"""
        self.pdf_files.clear()
        self.file_list.clear()
        self.status_label.setText("All files cleared")

    def start_extraction(self):
        """Start the extraction process"""
        if not self.pdf_files:
            QMessageBox.warning(
                self,
                "No Files",
                "Please add PDF files before starting extraction."
            )
            return

        # Get output file location
        output_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save CSV Output As",
            "invoice_data.csv",
            "CSV Files (*.csv)"
        )

        if not output_path:
            return

        # Disable buttons during processing
        self.set_buttons_enabled(False)
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.status_label.setText("Starting extraction...")

        # Start processing thread
        self.processing_thread = ProcessingThread(self.pdf_files, output_path)
        self.processing_thread.progress_update.connect(self.update_progress)
        self.processing_thread.status_update.connect(self.update_status)
        self.processing_thread.finished.connect(self.extraction_finished)
        self.processing_thread.start()

    def update_progress(self, current, total):
        """Update progress bar"""
        progress = int((current / total) * 100)
        self.progress_bar.setValue(progress)

    def update_status(self, status_text):
        """Update status label"""
        self.status_label.setText(status_text)

    def extraction_finished(self, output_file, errors):
        """Handle extraction completion"""
        self.set_buttons_enabled(True)
        self.progress_bar.setVisible(False)

        if output_file:
            msg = f"Extraction completed!\n\nOutput saved to:\n{output_file}\n\n"
            msg += f"Processed {len(self.pdf_files)} files"

            if errors:
                msg += f"\n\n{len(errors)} errors occurred. Check extraction_log.txt for details."

            QMessageBox.information(self, "Success", msg)
            self.status_label.setText(f"Completed: {len(self.pdf_files)} files processed")
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Extraction failed. No data was extracted.\nCheck extraction_log.txt for details."
            )
            self.status_label.setText("Extraction failed")

    def set_buttons_enabled(self, enabled):
        """Enable or disable all buttons"""
        self.add_files_btn.setEnabled(enabled)
        self.add_folder_btn.setEnabled(enabled)
        self.clear_btn.setEnabled(enabled)
        self.start_btn.setEnabled(enabled)


def main():
    """Main entry point"""
    app = QApplication(sys.argv)
    window = InvoiceReaderGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
