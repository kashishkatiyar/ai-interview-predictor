# AI Interview Coach & Hiring Probability Engine

An end-to-end machine learning and GenAI project that simulates ATS screening,
generates interview questions, evaluates interview answers, and predicts hiring probability.

## Features
- Resume & Job Description Matching (ATS-style)
- AI-generated Interview Questions
- Interview Answer Evaluation
- Hiring Probability Prediction
- GenAI Feedback & Improvement Suggestions

## Tech Stack
- Python
- Machine Learning (XGBoost)
- NLP (Sentence Transformers)
- LLMs (via Hugging Face / Together AI)
- FastAPI / Flask
- MySQL
- Bootstrap (Frontend)

## Project Structure

AI_INTERVIEW_PREDICTOR/
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── phase1_data_cleaning.ipynb
│   └── phase2_ats_matching.ipynb
│
├── src/
│   ├── matching/
│   │   └── ats_matcher.py
│   └── utils/
│       ├── domain_mapper.py
│       ├── embedding_utils.py
│       ├── skills_by_domain.py
│       └── text_cleaning.py
│
├── docs/
│   └── project_progress.md
│
├── outputs/
│   └── examples/
│       ├── example_strong_match.json
│       ├── example_moderate_match.json
│       ├──example_low_match.json
│
├── requirements.txt
├── .gitignore
└── README.md


## Project Phases
- Phase 1: Data inspection and preprocessing (resumes & job postings) ✅
- Phase 2: Resume–Job ATS matching (ML)
- Phase 3: Interview question generation (LLM)
- Phase 4: Interview answer scoring
- Phase 5: Hiring probability model
- Phase 6: Decision Engine
- Phase 7: Web application (Flask)
- Phase 8 – GenAI Explanation Layer 

## Note
datasets are excluded from this repository.

## Status
✅ Phase 1: Data inspection & preprocessing completed
🚧 Phase 2: Resume–Job ATS matching (In Progress)

## Future Improvements
- ATS prediction logging
- Skill gap visualization
- Interview success prediction
