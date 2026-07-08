import re
import pytesseract
import pandas as pd
from PIL import Image
from pdf2image import convert_from_path

def extract_details(text):
    phone = ""

    phone_match = re.search(r'(\+91[\-\s]?)?[6-9]\d{9}', text)
    if phone_match:
        phone = phone_match.group()

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    name = lines[0] if len(lines) > 0 else ""
    address = " ".join(lines[1:5]) if len(lines) > 1 else ""

    return {
        "Name": name,
        "Phone": phone,
        "Address": address
    }

def process_file(file_path):
    text = ""

    if file_path.lower().endswith(".pdf"):
        pages = convert_from_path(file_path)
        for page in pages:
            text += pytesseract.image_to_string(page)
    else:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)

    data = extract_details(text)

    df = pd.DataFrame([data])
    df.to_excel("output.xlsx", index=False)

    return data
  
