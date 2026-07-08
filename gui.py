import tkinter as tk
from tkinter import filedialog, messagebox
from ocr import process_file

def select_file():
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("PDF Files", "*.pdf"),
            ("Image Files", "*.png *.jpg *.jpeg")
        ]
    )

    if not file_path:
        return

    try:
        process_file(file_path)
        messagebox.showinfo("Success", "Data extracted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Slip OCR Extractor")
root.geometry("500x250")

title = tk.Label(root, text="Slip OCR Extractor", font=("Arial", 18, "bold"))
title.pack(pady=20)

btn = tk.Button(root, text="Select PDF / Image", command=select_file, width=25, height=2)
btn.pack(pady=20)

root.mainloop()
