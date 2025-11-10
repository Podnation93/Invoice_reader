# Project "Invoice Reader" - Build & Development Log

This document outlines the technical stack, build procedures, and an automated log of all project commits.

## 1. Project Overview

This project is a Windows desktop application for PDF invoice data extraction. It is defined by the following goals:
1.  Batch-process PDF invoices.
2.  Use intelligent, context-aware OCR to extract data.
3.  Handle missing labels and varied invoice layouts.
4.  Export all data into a single, strictly-formatted CSV file.

For the full project brief, see `README.md`.

## 2. Build & Setup Instructions

This project will be built using **Python** with a **PyQt/Tkinter** GUI and the **Tesseract OCR engine**.

### Dependencies
A `requirements.txt` file will be maintained. Key libraries include:
* `pytesseract` (OCR engine wrapper)
* `opencv-python` (Image pre-processing)
* `pandas` (For CSV data manipulation)
* `PyQt5` (For the GUI)
* `pdf2image` (To convert PDFs to images for OCR)

### Setup Steps
1.  **Install Tesseract:**
    * Download and install the Tesseract OCR engine for Windows.
    * Ensure the `tesseract.exe` is added to your system's PATH.
2.  **Create Virtual Environment:**
    * `python -m venv venv`
    * `.\venv\Scripts\activate`
3.  **Install Dependencies:**
    * `pip install -r requirements.txt`
4.  **Run the Application:**
    * `python main.py`

## 3. Automated Development Log

**This log is updated automatically by a Git post-commit hook.** Do not edit this section manually.

---
*(Log starts here)*
