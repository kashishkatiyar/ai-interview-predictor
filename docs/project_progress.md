# AI Interview Coach – Project Progress

## Project Goal
Build a system that:
- Matches resumes with job descriptions (ATS simulation)
- Identifies skill gaps
- Generates interview questions
- Evaluates interview answers
- Predicts hiring probability


## Phase 1 – Data Cleaning & Preparation ✅ Completed

### Work Done
- Cleaned resume dataset
- Cleaned job descriptions
- Removed HTML and noise
- Created:
  - `clean_resume_text`
  - `clean_job_text`
- Performed basic EDA
- Saved processed datasets

### Output
- `data/processed/resume_clean.csv`
- `data/processed/jobs_clean.csv`


## Phase 2.1 – Semantic ATS Matching ✅ Completed

### Work Done
- SentenceTransformer embeddings
- Cosine similarity scoring
- Baseline ATS scoring

### Files
- `src/utils/embedding_utils.py`
- `src/matching/ats_matcher.py`


## Phase 2.2 – Skill-Based ATS Scoring ✅ Completed

### Work Done
- Skill matching logic
- Weighted scoring:
  - Semantic score
  - Skill score
  - Title score
- Confidence level logic

### Output Example
- Final Score
- Matched Skills
- Missing Skills
- Confidence Level


## Phase 2.3 – Domain-Aware ATS (In Progress)

### Work Done
- Domain detection using category
- Domain-based skill lists
- Fallback logic when job skills not found

### Files
- `domain_mapper.py`
- `skills_by_domain.py`
- `ats_matcher.py`


## Phase 2.4 – ATS Feature Expansion (Planned)

### Planned Improvements
- Experience matching
- Education matching
- Skill synonym matching


## Phase 2.5 – Feature Logging & Evaluation (Planned)

### Planned
- Save ATS outputs
- Build evaluation dataset
- Create visualizations


## Phase 3 – Interview Question Generation (Planned)

- LLM-based question generation


## Phase 4 – Interview Answer Evaluation (Planned)

### LLM Scoring
- Relevance
- Clarity
- Technical depth
- Confidence


## Phase 5 – Hiring Probability Model (Planned)

Machine learning model predicting:
- Interview success probability


## Phase 6 – Decision Engine (Planned)

Combines:
- ATS score
- Interview score

Outputs:
- Hiring probability
- Skill gaps
- Feedback


## Phase 7 – Web Application (Planned)

### Stack
- FastAPI or Flask
- MySQL
- Bootstrap frontend


## Phase 8 – GenAI Explanation Layer (Planned)

LLM explains:
- Skill gaps
- Resume improvements
- Interview feedback
