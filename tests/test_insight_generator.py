from src.parser.pdf_parser import extract_text_from_pdf
from src.parser.text_cleaner import clean_text
from src.parser.section_extractor import extract_sections

from src.extractor.skill_loader import load_skills
from src.extractor.skill_extractor import extract_skills

from src.matcher.skill_matcher import match_skills

from src.insights.insight_generator import generate_insights


# Resume Processing

pdf_path = "data/raw/AnshikaVats_Resume.pdf"

raw_text = extract_text_from_pdf(pdf_path)

cleaned_text = clean_text(raw_text)

sections = extract_sections(cleaned_text)

skills_db = load_skills(
    "data/skills/skills.txt"
)

resume_skills = extract_skills(
    sections["Skills"],
    skills_db
)


# JD Processing

with open(
    "data/job_descriptions/ai_engineer_jd.txt",
    "r",
    encoding="utf-8"
) as file:
    jd_text = file.read()

jd_skills = extract_skills(
    jd_text,
    skills_db
)


# Matching

match_result = match_skills(
    resume_skills,
    jd_skills
)


# Insights

insights = generate_insights(
    match_result
)

print("\n===== CANDIDATE INSIGHTS =====\n")

print(insights)