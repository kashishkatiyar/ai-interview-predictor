from sklearn.metrics.pairwise import cosine_similarity
from src.utils.embedding_utils import generate_embeddings
from src.utils.domain_mapper import map_domain
from src.utils.skills_by_domain import SKILLS_BY_DOMAIN


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

#The best ATS design actually combines both:
#Step 1 – Extract skills from job text  (if possible)
#Step 2 – If no skills found  (fallback to domain skills)

# 1. Detect domain
# 2. Try extracting skills from job description
# 3. If none found → fallback to domain skills
# 4. Match resume against selected skills

def skill_match_score(resume_text, job_text, category):
    resume_text = resume_text.lower()
    job_text = job_text.lower()

    # Step 1: Detect domain
    domain = map_domain(category)

    # Step 2: Load skills for that domain
    domain_skills = SKILLS_BY_DOMAIN.get(domain, [])

    # Step 3: Try finding skills in job description
    job_skills = [skill for skill in domain_skills if skill.lower() in job_text]

    # Step 4: Fallback logic
    if len(job_skills) > 0:
        skills_to_match = job_skills
        skill_source = "job description"
    else:
        skills_to_match = domain_skills
        skill_source = "domain fallback"

    # Step 5: Match resume skills
    matched_skills = [skill for skill in skills_to_match if skill.lower() in resume_text]
    missing_skills = list(set(skills_to_match) - set(matched_skills))

    # Step 6: Compute score
    if len(skills_to_match) == 0:
        return 0, [], [], domain

    score = len(matched_skills) / len(skills_to_match)

    # Debug prints (optional)
    print("Domain:", domain)
    print("Skill Source:", skill_source)
    print("Skills Used:", skills_to_match)
    print("Matched Skills:", matched_skills)

    return score * 100, matched_skills, missing_skills, domain



def title_match_score(resume_text, job_title):
    """Checks if job title appears in resume"""
    job_title = job_title.lower()
    resume_text = resume_text.lower()

    return 100 if job_title in resume_text else 0



def final_ats_score(resume_text, job_text, job_title, category):
    """Combines all scoring components"""

    semantic_score = ats_match_score(resume_text, job_text)

    skill_score, matched_skills, missing_skills, domain = skill_match_score(
        resume_text, job_text, category
    )

    title_score = title_match_score(resume_text, job_title)

    final_score = (
        0.7 * semantic_score +
        0.2 * skill_score +
        0.1 * title_score
    )
    

    # Confidence level
    if final_score < 40:
        confidence = "Low Match"
    elif final_score < 70:
        confidence = "Moderate Match"
    else:
        confidence = "Strong Match"

    return {
        "final_score": float(round(float(final_score),2)),
        "semantic_score": float(round(float(semantic_score),2)),
        "skill_score": round(skill_score, 2),
        "title_score": title_score,
        "confidence": confidence,
        "domain": domain,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }
