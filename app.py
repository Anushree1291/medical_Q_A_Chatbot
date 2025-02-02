import streamlit as st
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the preprocessed Q&A data
def load_preprocessed_data(file_path):
    """
    Loads the preprocessed Q&A data from a JSON file.
    Args:
        file_path (str): Path to the JSON file.
    Returns:
        list: A list of question-answer pairs.
    """
    with open(file_path, "r") as f:
        return json.load(f)

# Function to retrieve the most relevant answer
def get_answer(user_query, qa_data):
    """
    Retrieves the most relevant answer for a given user query.
    Args:
        user_query (str): The user's query.
        qa_data (list): List of question-answer pairs.
    Returns:
        str: The most relevant answer.
    """
    # Build a TF-IDF vectorizer
    vectorizer = TfidfVectorizer().fit([q[0] for q in qa_data])  # Fit on all questions
    query_vector = vectorizer.transform([user_query])
    qa_vectors = vectorizer.transform([q[0] for q in qa_data])
    similarities = cosine_similarity(query_vector, qa_vectors).flatten()
    best_match_idx = similarities.argmax()
    return qa_data[best_match_idx][1]  # Return the answer of the best match

# Streamlit app
st.title("Medical Q&A Chatbot")
st.write("Ask a medical question, and the chatbot will provide answers based on the MedQuAD dataset.")

# Load data
qa_data = load_preprocessed_data("./qa_pairs.json")
st.write(f"Loaded {len(qa_data)} question-answer pairs.")

# User input
user_query = st.text_input("Your question:")
if user_query:
    answer = get_answer(user_query, qa_data)
    st.write(f"Answer: {answer}")
