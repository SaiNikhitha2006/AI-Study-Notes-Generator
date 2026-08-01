import PyPDF2

def read_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:          # Avoid errors if a page has no extractable text
                text += page_text + "\n"

        return text