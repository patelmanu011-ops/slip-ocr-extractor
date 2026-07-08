import tkinter as tk
from tkinter import filedialog, messagebox
from ocr import process_folder

def select_folder():
    folder = filedialog.askdirectory()

    if not folder:
        return

    try:
        output = process_folder(folder)
        messagebox.showinfo(
            "Success",
            f"Excel created successfully!\n\n{output}"
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Slip OCR Extractor")
root.geometry("500x250")

title = tk.Label(
    root,
    text="Slip OCR Extractor",
    font=("Arial", 18, "bold")
)
title.pack(pady=20)

btn = tk.Button(
    root,
    text="Select Folder",
    command=select_folder,
    width=25,
    height=2
)
btn.pack(pady=20)

root.mainloop()
