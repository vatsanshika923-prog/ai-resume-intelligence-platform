from src.parser.pdf_parser import extract_text_from_pdf
from src.parser.text_cleaner import clean_text

from src.vector_db.chroma_manager import (
    add_resume,
    search_resumes
)


# Load Resume

pdf_path = "data/raw/AnshikaVats_Resume.pdf"

raw_text = extract_text_from_pdf(
    pdf_path
)

cleaned_resume = clean_text(
    raw_text
)


# Store Resume

add_resume(
    "anshika_resume",
    cleaned_resume
)


# Recruiter Query

query = """
Machine Learning Engineer
with NLP, Deep Learning,
and TensorFlow experience
"""


results = search_resumes(
    query
)


print("\n===== REAL RESUME SEARCH =====\n")

print(results)