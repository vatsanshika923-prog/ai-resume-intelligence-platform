from src.vector_db.chroma_manager import (
    add_resume,
    search_resumes
)


# Sample Resumes

resume_1 = """
Python
TensorFlow
Machine Learning
Natural Language Processing
"""

resume_2 = """
Java
Spring Boot
Microservices
Backend Development
"""

resume_3 = """
PyTorch
Deep Learning
LLMs
Computer Vision
"""


# Add Resumes

add_resume(
    "resume_1",
    resume_1
)

add_resume(
    "resume_2",
    resume_2
)

add_resume(
    "resume_3",
    resume_3
)


# Recruiter Query

results = search_resumes(
    "Natural Language Processing Engineer"
)


print("\n===== SEARCH RESULTS =====\n")

print(results)