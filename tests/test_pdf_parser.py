from src.parser.pdf_parser import extract_text_from_pdf
from src.parser.text_cleaner import clean_text
from src.parser.section_extractor import extract_sections

pdf_path = "data/raw/AnshikaVats_Resume.pdf"

raw_text = extract_text_from_pdf(pdf_path)

cleaned_text = clean_text(raw_text)
sections = extract_sections(cleaned_text)

for section_name, content in sections.items():
    print("\n")
    print("=" * 50)
    print(section_name.upper())
    print("=" * 50)
    print(content[:300])

print("=" * 50)
print(cleaned_text[:1000])
print("=" * 50)