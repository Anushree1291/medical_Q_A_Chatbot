# Medical Q&A Chatbot using MedQuAD Dataset

## Overview
This project involves the development of a **Medical Q&A Chatbot** using the [MedQuAD dataset](https://github.com/abachaa/MedQuAD). The chatbot leverages advanced **Natural Language Processing (NLP)** techniques to answer medical queries by retrieving relevant information from a structured dataset of medical question-answer pairs.

## Features
- **Retrieval-based Answering:** Finds relevant answers using TF-IDF Vectorization and Sentence Transformers.
- **Medical Entity Recognition:** Utilizes **spaCy** to identify symptoms, diseases, and treatments in user queries.
- **User-Friendly Interface:** Built with **Streamlit** for easy interaction.
- **Analytics and Performance Tracking:** Evaluates answer relevance using similarity scores.
- **Transformer-Based QA Model:** Integrates **DistilBERT** for context-aware responses.

## Demo
[GitHub Repository](https://github.com/Anushree1291/medical_Q_A_Chatbot)

---

## Installation
### Prerequisites
Ensure you have Python 3.8+ installed along with the required dependencies:

```bash
pip install -r requirements.txt
```

### Running the Chatbot
```bash
streamlit run app.py
```

---

## Downloading and Extracting MedQuAD Dataset
To use the MedQuAD dataset, follow these steps:

### **Manual Download**
1. Go to [MedQuAD GitHub Repository](https://github.com/abachaa/MedQuAD).
2. Click on **"Code" > "Download ZIP"**.
3. Extract the ZIP file.
4. Move the extracted dataset to the `data/` folder inside this project.

### **Automated Download with Python**
Alternatively, you can use the following Python script to automate the process:

```python
import os
import zipfile
import requests

# Define paths
data_folder = "data"
zip_path = "MedQuAD.zip"
repo_url = "https://github.com/abachaa/MedQuAD/archive/refs/heads/master.zip"

# Create data folder if not exists
os.makedirs(data_folder, exist_ok=True)

# Download the ZIP file
print("Downloading MedQuAD dataset...")
response = requests.get(repo_url, stream=True)
with open(zip_path, "wb") as file:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            file.write(chunk)
print("Download complete.")

# Extract ZIP
print("Extracting files...")
with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(data_folder)

# Clean up ZIP file
os.remove(zip_path)
print(f"Dataset extracted to '{data_folder}' successfully!")
```

### **Run This Script**
Save this script as `download_medquad.py` inside your project folder and run:

```bash
python download_medquad.py
```

This will automatically download, extract, and place the dataset inside the `data/` folder.

---

## Dataset
The chatbot is powered by the **MedQuAD dataset**, a comprehensive medical knowledge base. The dataset includes structured medical Q&A pairs covering symptoms, diseases, treatments, and more.

**Processing Steps:**
- XML parsing to extract questions and answers.
- Data cleaning and preprocessing.
- Indexing for efficient retrieval.

---

## Model Architecture
### **Retrieval Mechanism:**
- **TF-IDF Vectorization:** Computes cosine similarity between queries and dataset questions.
- **Sentence Transformers:** Enhances retrieval accuracy by capturing semantic similarity.

### **Entity Recognition:**
- Uses **spaCy** for Named Entity Recognition (NER) to identify medical terms.

### **Question Answering:**
- **DistilBERT-based QA model** for answering questions in context.

---

## Application Development
- **Framework:** Built using **Streamlit** for an interactive web interface.
- **UI Features:** Simple text input for user queries and real-time answer retrieval.
- **Performance Monitoring:** Tracks response relevance and latency.

---

## Testing and Debugging
- Unit testing for retrieval accuracy.
- Integration testing for chatbot response coherence.
- Continuous improvements based on user feedback.

---

## Challenges and Solutions
| Challenge | Solution |
|-----------|----------|
| Handling complex queries with multiple entities | Used **spaCy** for entity recognition |
| Model performance on out-of-scope questions | Fine-tuned model with more specific medical data |

---

## Skills and Technologies Used
- **NLP & Text Processing:** TF-IDF, Sentence Transformers, spaCy
- **Machine Learning:** DistilBERT for question answering
- **Web Development:** Streamlit for UI design
- **Data Handling:** XML parsing, JSON processing

---

## Future Enhancements
- **Integration with a domain-specific LLM** for better contextual understanding.
- **Expanding dataset coverage** to include more medical topics.
- **Improving UI/UX** for enhanced user interaction.

---

## Contribution
Feel free to contribute by:
1. Forking the repository.
2. Creating feature branches.
3. Submitting pull requests.

---

## License
This project is licensed under the **MIT License**.

---

## Contact
For any questions or suggestions, reach out via [GitHub Issues](https://github.com/Anushree1291/medical_Q_A_Chatbot/issues).

---
