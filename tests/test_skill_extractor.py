from src.parser.pdf_parser import extract_text_from_pdf
from src.parser.text_cleaner import clean_text
from src.parser.section_extractor import extract_sections

from src.extractor.skill_loader import load_skills
from src.extractor.skill_extractor import extract_skills


pdf_path = "data/raw/AnshikaVats_Resume.pdf"

raw_text = extract_text_from_pdf(pdf_path)

cleaned_text = clean_text(raw_text)

sections = extract_sections(cleaned_text)

skills_db = load_skills("data/skills/skills.txt")

skills_section = sections["Skills"]

extracted_skills = extract_skills(
    skills_section,
    skills_db
)

print(extracted_skills)