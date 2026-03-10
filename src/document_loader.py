from pypdf import PdfReader
import os

def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    return text


if __name__ == "__main__":
    pdf_path = "data/Attention_is_all_you_need.pdf"
    document_text = load_pdf(pdf_path)

    print("Document loaded successfully!")
    print("First 500 characters:\n")
    print(document_text[:500])