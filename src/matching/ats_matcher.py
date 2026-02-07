from sklearn.metrics.pairwise import cosine_similarity
from src.utils.embedding_utils import generate_embeddings
from src.utils.skills_list import SKILLS


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


def skill_match_score(resume_text, job_text):
    resume_text = resume_text.lower()
    job_text = job_text.lower()

    all_skills = []
    for category in SKILLS.values():
        all_skills.extend(category)

    job_skills = [skill for skill in all_skills if skill in job_text]
    matched_skills = [skill for skill in job_skills if skill in resume_text]

    if len(job_skills) == 0:
        return 0, []

    score = len(matched_skills) / len(job_skills)
    return score * 100, matched_skills


def title_match_score(resume_text, job_title):
    job_title = job_title.lower()
    resume_text = resume_text.lower()

    return 100 if job_title in resume_text else 0


def final_ats_score(resume_text, job_text, job_title):
    semantic_score = ats_match_score(resume_text, job_text)

    skill_score, matched_skills = skill_match_score(resume_text, job_text)

    title_score = title_match_score(resume_text, job_title)

    final_score = (
        0.7 * semantic_score +
        0.2 * skill_score +
        0.1 * title_score
    )

    return {
        "final_score": round(final_score, 2),
        "semantic_score": round(semantic_score, 2),
        "skill_score": round(skill_score, 2),
        "title_score": title_score,
        "matched_skills": matched_skills
    }
