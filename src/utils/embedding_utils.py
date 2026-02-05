from sentence_transformers import SentenceTransformer
import numpy as np

# Load model once (important for performance)
_model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(texts):
    """
    Generate sentence embeddings for a list of texts.
    
    Args:
        texts (list[str] or str): Input text(s)
    
    Returns:
        np.ndarray: Embedding vectors
    """
    if isinstance(texts, str):
        texts = [texts]

    embeddings = _model.encode(texts, normalize_embeddings=True)
    return embeddings
