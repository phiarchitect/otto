import os
import fitz  # PyMuPDF
from pathlib import Path

def extract_images(pdf_path):
    pdf_file = fitz.open(pdf_path)
    image_folder_path = Path(pdf_path).stem

    if not os.path.exists(image_folder_path):
        os.makedirs(image_folder_path)

    for i in range(len(pdf_file)):
        for img in pdf_file.get_page_images(i):
            xref = img[0]
            base = img[1]
            img_data = pdf_file.extract_image(xref)
            img_path = os.path.join(image_folder_path, f"{base}.png")
            with open(img_path, 'wb') as f:
                f.write(img_data['image'])

extract_images('MAINTENANCE & TUNE-UP.pdf')

