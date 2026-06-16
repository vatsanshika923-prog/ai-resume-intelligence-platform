from fastapi import FastAPI, UploadFile, File
import tempfile
import os

from src.parser.pdf_parser import extract_text_from_pdf
from src.parser.text_cleaner import clean_text
from src.parser.section_extractor import extract_sections

from src.extractor.skill_loader import load_skills
from src.extractor.skill_extractor import extract_skills

from src.matcher.skill_matcher import match_skills
from src.insights.insight_generator import generate_insights


app = FastAPI(
    title="AI Resume Intelligence Platform",
    description="Resume Analysis and Semantic Search API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Resume Intelligence Platform API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/project-info")
def project_info():
    return {
        "project_name": "AI Resume Intelligence Platform",
        "version": "1.0.0",
        "features": [
            "Resume Parsing",
            "Skill Extraction",
            "Job Description Matching",
            "Candidate Insights",
            "Semantic Matching",
            "Vector Search"
        ]
    }


@app.get("/candidate-profile")
def candidate_profile():

    pdf_path = "data/raw/AnshikaVats_Resume.pdf"

    raw_text = extract_text_from_pdf(pdf_path)

    cleaned_text = clean_text(raw_text)

    sections = extract_sections(cleaned_text)

    skills_db = load_skills(
        "data/skills/skills.txt"
    )

    extracted_skills = extract_skills(
        sections.get("Skills", ""),
        skills_db
    )

    return {
        "summary": sections.get("Summary", ""),
        "education": sections.get("Education", ""),
        "projects": sections.get("Projects", ""),
        "skills": extracted_skills
    }


@app.get("/resume-jd-match")
def resume_jd_match():

    pdf_path = "data/raw/AnshikaVats_Resume.pdf"

    raw_text = extract_text_from_pdf(pdf_path)

    cleaned_text = clean_text(raw_text)

    sections = extract_sections(cleaned_text)

    skills_db = load_skills(
        "data/skills/skills.txt"
    )

    resume_skills = extract_skills(
        sections.get("Skills", ""),
        skills_db
    )

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

    result = match_skills(
        resume_skills,
        jd_skills
    )

    return result


@app.get("/candidate-insights")
def candidate_insights():

    pdf_path = "data/raw/AnshikaVats_Resume.pdf"

    raw_text = extract_text_from_pdf(pdf_path)

    cleaned_text = clean_text(raw_text)

    sections = extract_sections(cleaned_text)

    skills_db = load_skills(
        "data/skills/skills.txt"
    )

    resume_skills = extract_skills(
        sections.get("Skills", ""),
        skills_db
    )

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

    match_result = match_skills(
        resume_skills,
        jd_skills
    )

    insights = generate_insights(
        match_result
    )

    return insights

@app.post("/analyze-resume")
async def analyze_resume(
    file: UploadFile = File(...)
):

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )

    temp_file.write(
        await file.read()
    )

    temp_file.close()

    try:

        raw_text = extract_text_from_pdf(
            temp_file.name
        )

        cleaned_text = clean_text(
            raw_text
        )

        sections = extract_sections(
            cleaned_text
        )

        skills_db = load_skills(
            "data/skills/skills.txt"
        )

        extracted_skills = extract_skills(
            sections.get("Skills", ""),
            skills_db
        )

        return {
            "filename": file.filename,
            "summary": sections.get(
                "Summary",
                ""
            ),
            "education": sections.get(
                "Education",
                ""
            ),
            "projects": sections.get(
                "Projects",
                ""
            ),
            "skills": extracted_skills
        }

    finally:

        os.unlink(
            temp_file.name
        )


@app.post("/match-resume")
async def match_resume(
    file: UploadFile = File(...)
):

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )

    temp_file.write(
        await file.read()
    )

    temp_file.close()

    try:

        raw_text = extract_text_from_pdf(
            temp_file.name
        )

        cleaned_text = clean_text(
            raw_text
        )

        sections = extract_sections(
            cleaned_text
        )

        skills_db = load_skills(
            "data/skills/skills.txt"
        )

        resume_skills = extract_skills(
            sections.get("Skills", ""),
            skills_db
        )

        with open(
            "data/job_descriptions/ai_engineer_jd.txt",
            "r",
            encoding="utf-8"
        ) as jd_file:

            jd_text = jd_file.read()

        jd_skills = extract_skills(
            jd_text,
            skills_db
        )

        result = match_skills(
            resume_skills,
            jd_skills
        )

        return {
            "filename": file.filename,
            **result
        }

    finally:

        os.unlink(
            temp_file.name
        )