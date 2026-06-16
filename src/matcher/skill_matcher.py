def match_skills(
    resume_skills: dict,
    jd_skills: dict
) -> dict:
    """
    Compare resume skills and JD skills.

    Args:
        resume_skills (dict)
        jd_skills (dict)

    Returns:
        dict
    """

    matched_skills = {}
    missing_skills = {}

    total_jd_skills = 0
    total_matched_skills = 0

    for category, jd_skill_list in jd_skills.items():

        resume_skill_list = resume_skills.get(
            category,
            []
        )

        matched = []
        missing = []

        for skill in jd_skill_list:

            total_jd_skills += 1

            if skill in resume_skill_list:
                matched.append(skill)
                total_matched_skills += 1

            else:
                missing.append(skill)

        if matched:
            matched_skills[category] = matched

        if missing:
            missing_skills[category] = missing

    if total_jd_skills == 0:
        match_score = 0

    else:
        match_score = round(
            (total_matched_skills / total_jd_skills) * 100,
            2
        )

    return {
        "match_score": match_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }