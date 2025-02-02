from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np

# Load sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_most_similar_answer(query, qa_data):
    """
    Finds the most similar answer to the query using cosine similarity.
    """
    query_vector = model.encode([query])
    answers = [answer for _, answer in qa_data]
    answer_vectors = model.encode(answers)
    
    similarities = cosine_similarity(query_vector, answer_vectors)
    best_match_idx = np.argmax(similarities)
    
    return qa_data[best_match_idx][1]

# Entity Recognition (Optional)
import spacy

# Load spaCy NER model
nlp = spacy.load("en_core_web_sm")

def extract_medical_entities(text):
    """
    Extracts medical entities from text.
    """
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents]
    return entities
