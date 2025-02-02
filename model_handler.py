from transformers import pipeline

def load_qa_model():
    """
    Loads a pre-trained QA model for medical queries.
    """
    return pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def answer_question(model, question, context):
    """
    Uses the QA model to answer a question given a context.
    """
    result = model(question=question, context=context)
    return result["answer"]
