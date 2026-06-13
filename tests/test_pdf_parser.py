from src.parser.pdf_parser import extract_text_from_pdf
from src.parser.text_cleaner import clean_text

pdf_path = "data/raw/AnshikaVats_Resume.pdf"

raw_text = extract_text_from_pdf(pdf_path)

cleaned_text = clean_text(raw_text)

print("=" * 50)
print(cleaned_text[:1000])
print("=" * 50)