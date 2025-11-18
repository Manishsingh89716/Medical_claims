import io
from PyPDF2 import PdfReader

def extract_pdf_text(pdf_bytes):
    """
    Reads PDF bytes and extracts raw text.
    """
    pdf = PdfReader(io.BytesIO(pdf_bytes))
    text = ""

    for page in pdf.pages:
        text += page.extract_text() or ""

    return text