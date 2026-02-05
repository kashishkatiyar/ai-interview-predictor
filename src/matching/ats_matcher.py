from sklearn.metrics.pairwise import cosine_similarity
from src.utils.embedding_utils import generate_embeddings


def ats_match_score(resume_text, job_text):
    """
    Compute ATS match score between resume and job description.
    
    Args:
        resume_text (str)
        job_text (str)
    
    Returns:
        float: ATS score (0–100)
    """
    resume_emb = generate_embeddings(resume_text)
    job_emb = generate_embeddings(job_text)

    score = cosine_similarity(resume_emb, job_emb)[0][0]
    return round(score * 100, 2)
