def extract_skills(skills_section: str, skills_db: dict) -> dict:
    """
    Extract skills from resume.

    Args:
        skills_section (str): Skills section text.
        skills_db (dict): Skills taxonomy.

    Returns:
        dict: Extracted categorized skills.
    """

    extracted_skills = {}

    skills_section = skills_section.lower()

    for category, skills in skills_db.items():

        matched_skills = []

        for skill in skills:

            if skill.lower() in skills_section:
                matched_skills.append(skill)

        if matched_skills:
            extracted_skills[category] = matched_skills

    return extracted_skills