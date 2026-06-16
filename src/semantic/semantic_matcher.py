from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def calculate_similarity(
    resume_text: str,
    jd_text: str
) -> float:
    """
    Calculate semantic similarity between
    resume and job description.

    Args:
        resume_text (str)
        jd_text (str)

    Returns:
        float
    """

    resume_embedding = model.encode(
        resume_text,
        convert_to_tensor=True
    )

    jd_embedding = model.encode(
        jd_text,
        convert_to_tensor=True
    )

    similarity = cos_sim(
        resume_embedding,
        jd_embedding
    )

    return round(
        float(similarity[0][0]) * 100,
        2
    )