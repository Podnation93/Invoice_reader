# Invoice Reader

**Invoice Reader** is a Windows desktop application designed to batch-process PDF invoices. It uses intelligent OCR to find and extract data, even from poorly formatted or scanned documents, and consolidates all extracted data into a single, pre-formatted CSV file.

## 1. Core Features

* **Batch Processing:** Add multiple PDF files or entire folders at once.
* **Intelligent Extraction:** Uses contextual and pattern-based logic (not just fixed labels) to find data.
* **Single CSV Output:** Collates all data from all invoices into one CSV file matching a specific header format.
* **Simple UI:** A clean "drag-and-drop" or "Add Files" interface with a "Start Extraction" button.
* **Error Logging:** Skips unreadable/password-protected files and logs them in a separate `extraction_log.txt`.

## 2. CSV Output Format (Critical Requirement)

The final CSV output **must** use the following headers, in this exact order.

*ContactName,EmailAddress,POAddressLine1,POAddressLine2,POAddressLine3,POAddressLine4,POCity,PORegion,POPostalCode,POCountry,*InvoiceNumber,Reference,*InvoiceDate,*DueDate,InventoryItemCode,*Description,*Quantity,*UnitAmount,Discount,*AccountCode,*TaxType,TrackingName1,TrackingOption1,TrackingName2,TrackingOption2,Currency,BrandingTheme


## 3. Line Item & Data Duplication Logic

* **One Row Per Line Item:** If one invoice has 5 items in its table, it will create 5 separate rows in the CSV.
* **Data Duplication:** Invoice-level data (like `*InvoiceNumber`, `*ContactName`, `*InvoiceDate`) **must be duplicated** on every single row associated with that invoice.
* **Blank Fields:** If a specific field (e.g., `Reference`) is not found on the invoice, that column in the CSV must be left blank. The column order must be maintained.

## 4. Intelligent Data Recognition (Contextual Logic)

The extractor **must not** fail if a label (e.g., "Invoice #") is missing. It must use a "waterfall" of contextual logic.

* **`*ContactName` / `POAddress...`:**
    * **Logic:** Search for formatted address blocks (2-5 lines of text). The first line of the block is the `*ContactName`, and subsequent lines are `POAddress...`.
    * **Context:** Prioritize blocks found near keywords like "To:", "Bill To:", or "Customer:", but find the block even if those words are missing.

* **`*InvoiceNumber`:**
    * **Logic:** If "Invoice #" is missing, search for short alphanumeric strings (e.g., "INV-1045", "AB-003") that are not dates or currency.
    * **Context:** Usually located in the top-right quadrant of the document.

* **`*InvoiceDate` / `*DueDate`:**
    * **Logic:** Use pattern matching (Regex) to find *all* dates (`dd/mm/yyyy`, `mm/dd/yy`, `Month dd, yyyy`).
    * **Classification:** The date on the same line as the word "**Due**" is the `*DueDate`. The *other* primary date is the `*InvoiceDate`.

* **Line Items (The Table):**
    * **Logic:** Find the main data table by identifying its structure (columns of text, numbers, and currency).
    * **Extraction:** Extract every row from this table, mapping them to `*Description`, `*Quantity`, and `*UnitAmount`.
