# PDF to Excel Converter (Offline)

Hey there! 👋

This is a simple offline PDF to Excel converter built in Python. It comes with a friendly GUI so you can easily turn any PDF with tables into an editable Excel spreadsheet without needing an internet connection.

Think of it as your little assistant for quickly analyzing PDF data! 📊

# Features

- Convert PDFs into Excel (.xlsx) in a few clicks
- Pick where to save your Excel files
- Simple GUI: Browse → Convert → Done!
- After conversion, choose to convert more PDFs or exit
- Fully offline no internet required

# What You Need

## Before you get started, make sure you have:
- Python 3.8+ installed
- The library camelot-py and pandas (pip install camelot-py pandas)
- Tkinter (comes with Python by default)
- Optional: PyInstaller if you want a standalone app

> Note: camelot may need Ghostscript installed if using lattice flavor on Windows/Linux. For most PDFs, stream flavor works without extra setup.

## How to Get It Running (Step by Step)

### 1. Clone the repository (or download it as ZIP):
```
git clone https://github.com/sharan-johijode-dotcom/PDF-to-Excel-Converter.git
cd PDF-to-Excel-Converter
```

# 2. Install the required library:
```
pip install camelot-py pandas
```

# 3. Run the app:
```
python pdf_to_excel_gui.py
```

# 4. Use it:

- Click “Select PDF & Convert”
- Pick your PDF
- Choose where to save the Excel file
- Wait a few seconds for the conversion
- A popup will ask: “Convert another file?”
    - Yes → pick another PDF
    - No → app closes

And that’s it! 🎉

## Make It a Standalone App (Optional)

Want to give it to friends or colleagues without them needing Python? You can make a single executable file:

# 1. Install PyInstaller:
```
pip install pyinstaller
```

# 2. Run this command :
```
Windows    -> pyinstaller --onefile --windowed --icon=icon.ico pdf_to_excel_gui.py
Mac        -> pyinstaller --onefile --windowed pdf_to_excel_gui.py
Linux/unix -> pyinstaller --onefile pdf_to_excel_gui.py
```

# 3. Find your app in the dist/ folder:
```
dist/pdf_to_excel_gui_v2(.exe/.app/.deb)
```
Double-click it and it runs just like a normal app (Windows).


## Things to Keep in Mind

- Works best with table-based PDFs. PDFs with irregular layouts may not convert perfectly.
- Scanned PDFs (images) aren’t supported yet as OCR is not included.
- Layout may not always be perfect, especially with complex or multi-page tables.
- Currently, you can only convert one PDF at a time.
- Fully offline, no internet required.
