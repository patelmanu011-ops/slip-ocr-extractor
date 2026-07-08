import os
import re
import pandas as pd
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

SUPPORTED_EXTENSIONS = (
    ".pdf",
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tif",
    ".tiff"
)

def extract_details(text):
    lines = [l.strip() for l in text.splitlines() if l.strip()]

    name = ""
    address = ""
    phone = ""

    phone_match = re.search(r'(\+91[\-\s]?)?[6-9]\d{9}', text)
    if phone_match:
        phone = phone_match.group()

    if len(lines) > 0:
        name = lines[0]

    if len(lines) > 1:
        address = " ".join(lines[1:6])

    return {
        "Name": name,
        "Phone": phone,
        "Address": address
    }
    def ocr_image(image):
    return pytesseract.image_to_string(image)

def process_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    text = ""

    if ext == ".pdf":
        pages = convert_from_path(file_path)
        for page in pages:
            text += ocr_image(page) + "\n"
    else:
        image = Image.open(file_path)
        text = ocr_image(image)

    return extract_details(text)
    
def process_folder(folder_path, output_file="output.xlsx"):
    results = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(SUPPORTED_EXTENSIONS):
            file_path = os.path.join(folder_path, filename)

            try:
                data = process_file(file_path)
                data["File"] = filename
                results.append(data)
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    df = pd.DataFrame(results)
    df.to_excel(output_file, index=False)

    return output_file
    if __name__ == "__main__":
    folder = input("Enter folder path: ").strip()

    if os.path.isdir(folder):
        output = process_folder(folder)
        print(f"Done! Excel saved as: {output}")
    else:
        print("Invalid folder path.")
