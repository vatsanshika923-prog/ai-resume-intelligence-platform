from src.extractor.skill_loader import load_skills
from src.extractor.skill_extractor import extract_skills


with open(
    "data/job_descriptions/ai_engineer_jd.txt",
    "r",
    encoding="utf-8"
) as file:
    jd_text = file.read()

print("\n===== JD TEXT =====\n")
print(jd_text)

skills_db = load_skills(
    "data/skills/skills.txt"
)

jd_skills = extract_skills(
    jd_text,
    skills_db
)

print("\n===== EXTRACTED JD SKILLS =====\n")
print(jd_skills)