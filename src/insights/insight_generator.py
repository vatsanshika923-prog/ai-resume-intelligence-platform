def generate_insights(match_result: dict) -> dict:
    """
    Generate candidate insights from matching results.

    Args:
        match_result (dict)

    Returns:
        dict
    """

    score = match_result["match_score"]

    missing_skills = match_result["missing_skills"]

    strengths = []
    recommendations = []

    if score >= 80:
        strengths.append(
            "Strong alignment with job requirements"
        )

    elif score >= 60:
        strengths.append(
            "Moderate alignment with job requirements"
        )

    else:
        strengths.append(
            "Needs significant skill improvement"
        )

    for category, skills in missing_skills.items():

        for skill in skills:

            recommendations.append(
                f"Learn {skill}"
            )

    return {
        "match_score": score,
        "strengths": strengths,
        "recommendations": recommendations
    }