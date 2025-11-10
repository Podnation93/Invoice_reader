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

**Commit on:** 2025-11-10 23:06:04
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:04
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:05
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:05
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:05
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:05
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:06
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:06
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:06
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:07
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:07
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:07
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:07
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:08
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:08
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:08
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:08
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:09
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:09
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:09
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:10
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:10
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:10
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:10
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:11
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:11
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:11
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:11
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:12
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:12
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:12
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:12
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:13
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:13
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:13
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:14
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:14
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:14
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:14
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:15
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:15
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:15
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:16
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:16
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:16
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:16
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:17
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:17
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:17
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:18
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:18
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:18
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:18
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:19
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:19
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:19
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:20
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:20
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:20
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:20
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:21
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:21
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:21
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:21
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:22
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:22
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:22
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:23
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:23
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:23
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:24
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:24
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:24
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:24
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:25
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:25
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:25
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:26
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:26
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:26
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:27
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:27
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:27
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:27
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:28
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:28
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:28
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:29
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:29
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:29
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:30
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:30
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:30
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:30
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:31
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:31
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:31
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:32
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:32
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:32
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:33
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:33
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:33
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:34
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:34
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:34
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:35
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:35
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:35
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:35
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:36
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:36
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:36
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:37
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:37
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:37
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:38
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:38
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:38
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:39
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:39
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:39
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:40
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:40
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:40
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:41
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:41
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:41
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:42
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:42
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:42
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:42
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:43
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:43
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:43
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:44
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:44
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:44
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:45
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:45
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:45
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:46
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:46
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:46
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:47
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:47
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:47
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:48
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:48
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:48
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:49
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:49
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:49
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:50
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:50
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:50
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:51
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:51
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:51
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:52
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:52
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:52
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:53
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:53
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:54
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:54
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:54
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:55
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:55
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:55
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:56
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:56
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:56
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:57
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:57
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:57
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:58
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:58
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:58
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:59
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:59
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:06:59
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:00
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:00
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:00
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:01
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:01
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:02
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:02
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:02
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:03
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:03
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:03
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:04
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:04
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:04
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:05
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:05
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:05
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:06
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:06
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:06
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:07
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:07
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:08
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:08
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:08
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:09
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:09
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:09
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:10
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:10
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:10
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:11
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:11
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:11
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:12
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:12
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:13
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:13
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:13
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:14
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:14
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:14
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:15
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:15
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:16
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:16
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:16
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:17
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:17
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:17
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:18
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:18
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:18
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:19
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:19
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:20
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:20
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:20
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:21
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:21
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:21
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:22
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:22
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:23
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:23
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:23
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:24
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:24
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:24
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:25
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:25
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:26
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:26
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:26
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:27
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:27
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:27
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:28
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:28
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:29
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:29
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:29
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:30
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:30
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:31
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:31
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:31
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:32
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:32
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:32
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:33
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:33
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:34
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:34
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:34
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:35
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:35
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:36
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:36
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:36
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:37
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:37
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:37
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:38
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:38
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:39
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:39
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:39
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:40
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:40
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:41
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:41
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:41
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:42
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:42
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:43
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:43
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:43
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:44
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:44
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:45
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:45
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:45
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:46
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:46
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:46
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:47
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:47
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:48
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:48
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:48
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:49
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:49
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:50
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:50
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:50
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:51
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:51
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:52
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:52
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:53
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:53
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:54
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:55
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:56
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:57
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:57
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:58
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:58
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:59
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:07:59
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:00
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:00
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:01
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:01
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:02
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:03
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:03
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:04
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:04
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:05
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:05
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:06
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:07
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:07
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:08
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:08
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:09
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:09
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:10
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:10
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:11
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:12
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:12
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:13
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:13
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:14
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:15
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:15
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:16
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:16
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:17
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:17
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:18
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:18
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:19
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:19
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:20
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:20
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:21
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:21
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:22
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:22
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:23
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:23
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:24
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:24
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:25
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:25
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:26
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:26
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:27
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:27
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:28
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:28
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:29
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:30
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:30
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:31
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:31
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:32
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:32
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:33
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:33
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:34
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:34
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:35
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:36
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:36
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:37
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:37
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:38
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:38
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:39
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:39
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:40
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:41
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:41
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:42
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:42
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:43
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:43
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:44
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:45
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:45
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:46
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:46
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:47
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:47
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:48
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:48
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:49
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:50
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:52
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:53
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:53
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:54
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:54
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:54
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:55
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:55
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:56
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:56
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:57
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:57
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:58
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:58
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:58
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:59
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:08:59
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:00
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:00
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:01
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:01
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:01
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:02
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:02
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:03
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:03
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:04
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:04
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:05
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:05
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:06
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:06
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:06
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:07
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:07
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:08
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:08
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:09
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:09
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:09
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:10
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:10
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:11
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:11
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:12
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:13
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:13
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:14
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:14
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---

**Commit on:** 2025-11-10 23:09:15
**Message:** Implement complete Invoice Reader application

- Created main.py with PyQt5 GUI (drag-and-drop, file selection, progress tracking)
- Implemented pdf_processor.py for PDF to image conversion with preprocessing
- Built ocr_extractor.py with intelligent, context-aware data extraction
  - Contact name and address extraction using contextual logic
  - Invoice number detection without relying on labels
  - Smart date extraction and classification (invoice date vs due date)
  - Table-based line item extraction with fallback mechanisms
- Created csv_generator.py for exact 27-column CSV format output
- Added logger.py for comprehensive error logging to extraction_log.txt

Features:
- Batch processing of multiple PDFs
- Intelligent OCR that handles missing labels and varied layouts
- One CSV row per line item with duplicated invoice-level data
- Background processing with progress updates
- Error handling and detailed logging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
---
