import tkinter as tk
from tkinter import filedialog, messagebox
import camelot
import pandas as pd

def convert_pdf_to_excel():
    while True:
        pdf_file = filedialog.askopenfilename(
            title="Select PDF file to convert",
            filetypes=[("PDF Files", "*.pdf")]
        )
        if not pdf_file:
            break

        save_file = filedialog.asksaveasfilename(
            title="Save Excel file as",
            defaultextension=".xlsx",
            filetypes=[("Excel Files", "*.xlsx")]
        )
        if not save_file:
            break

        try:
            # Try both flavors for maximum detection
            tables = camelot.read_pdf(pdf_file, pages='all', flavor='lattice')  # tables with borders
            if not tables:
                tables = camelot.read_pdf(pdf_file, pages='all', flavor='stream')  # tables without borders

            if len(tables) == 0:
                messagebox.showinfo("No Tables Found", "No tables could be detected in this PDF.")
                continue  # skip to next iteration

            # Write each table to a separate sheet
            with pd.ExcelWriter(save_file) as writer:
                for i, table in enumerate(tables):
                    sheet_name = f"Sheet{i+1}"
                    table.df.to_excel(writer, index=False, sheet_name=sheet_name)

            messagebox.showinfo("Success", f"PDF successfully converted to:\n{save_file}")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert PDF:\n{str(e)}")

        again = messagebox.askyesno("Convert Again?", "Do you want to convert another PDF?")
        if not again:
            break

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    convert_pdf_to_excel()
