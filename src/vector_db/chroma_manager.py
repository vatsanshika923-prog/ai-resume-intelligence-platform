import chromadb


client = chromadb.Client()


collection = client.get_or_create_collection(
    name="resumes"
)


def add_resume(
    resume_id: str,
    resume_text: str
):
    """
    Add resume to ChromaDB.
    """

    collection.add(
        documents=[resume_text],
        ids=[resume_id]
    )


def search_resumes(
    query: str,
    n_results: int = 5
):
    """
    Search similar resumes.
    """

    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    return results