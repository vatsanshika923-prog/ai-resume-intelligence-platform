from src.parser.pdf_parser import extract_text_from_pdf
from src.parser.text_cleaner import clean_text

from src.semantic.semantic_matcher import (
    calculate_similarity
)


# Resume Processing

pdf_path = "data/raw/AnshikaVats_Resume.pdf"

raw_text = extract_text_from_pdf(
    pdf_path
)

resume_text = clean_text(
    raw_text
)


# JD Processing

with open(
    "data/job_descriptions/ai_engineer_jd.txt",
    "r",
    encoding="utf-8"
) as file:

    jd_text = file.read()


# Semantic Matching

similarity_score = calculate_similarity(
    resume_text,
    jd_text
)

print("\n===== SEMANTIC MATCH SCORE =====\n")

print(
    f"Semantic Similarity: {similarity_score}%"
)