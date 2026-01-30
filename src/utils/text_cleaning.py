
import re

def clean_resume_text(text: str) -> str:
    """
    Minimal cleaning for resume text.
    Keeps meaning intact for LLMs and embeddings.
    """

    if not isinstance(text, str):
        return ""

    # lowercase
    text = text.lower()

    # remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    # remove unwanted characters (keep +, #, . for skills)
    text = re.sub(r"[^a-z0-9\s\+\#\.]", " ", text)

    # final trim
    text = text.strip()

    return text
