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
├── data/                  # ignored (raw & processed datasets)
│   ├── raw/
│   └── processed/
├── Notebooks/
│   └── phase1_data_cleaning.ipynb
├── src/
│   └── utils/
│       ├── text_cleaning.py
│       └── embedding_utils.py
├── requirements.txt
├── .gitignore
└── README.md


## Project Phases
- Phase 1: Data inspection and preprocessing (resumes & job postings) ✅
- Phase 2: Resume–Job ATS matching (ML)
- Phase 3: Interview question generation (LLM)
- Phase 4: Interview answer scoring
- Phase 5: Hiring probability prediction
- Phase 6: Web application (Flask)

## Note
Raw datasets are excluded from this repository.

## Status
✅ Phase 1: Data inspection & preprocessing completed
🚧 Phase 2: Resume–Job ATS matching (In Progress)

