from PyPDF2 import PdfReader
import re
import os

def extract_images_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    image_folder = os.path.splitext(pdf_file)[0]  # Use the pdf stem as the folder name

    if not os.path.exists(image_folder):
        os.mkdir(image_folder)

    count = 0

    for page in reader.pages:
        for index, image_file_object in enumerate(page.images):
            # Use the first 50 characters of the description as the file name
            image_file_name = re.sub(r'\W+', '_', image_file_object.description)[:50]
            image_file_path = os.path.join(image_folder, f"{count}_{image_file_name}.png")
            with open(image_file_path, "wb") as fp:
                fp.write(image_file_object.data)
            count += 1


extract_images_from_pdf('MAINTENANCE & TUNE-UP.pdf')
