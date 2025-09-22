
# SvaraAI – AI/ML Engineer Internship Assignment

## 📄 Project Overview

This repository contains a complete solution for classifying prospect email replies into **negative, neutral, or positive** categories. The project demonstrates a full **ML/NLP pipeline**, from data preprocessing to model deployment, along with reasoning for design choices. The solution includes:

* **Part A – ML/NLP Pipeline**: Baseline model (Logistic Regression) and transformer-based model (DistilBERT) for text classification.
* **Part B – Deployment**: Wrapping the best-performing model in a REST API using FastAPI.
* **Part C – Reasoning**: Concise, professional answers to design and deployment questions.

---

## 🧩 Part A – ML/NLP Pipeline

### Step 1: Load & Preprocess Dataset

* Renamed columns for consistency.
* Cleaned text: lowercased, removed punctuation, trimmed spaces.
* Standardized labels and encoded them for ML compatibility.
* Split dataset into training and test sets.

### Step 2: Baseline Model – Logistic Regression + TF-IDF

* Extracted TF-IDF features from text.
* Trained a Logistic Regression classifier for baseline performance.
* Evaluated using **accuracy** and **weighted F1-score**.

**Results:**

* Accuracy: 0.995
* Weighted F1 Score: 0.995
* Strengths: Extremely fast, low resource requirements, interpretable.
* Limitations: Cannot capture complex semantic patterns.

### Step 3: Transformer Model – DistilBERT

* Tokenized text using the DistilBERT tokenizer.
* Converted datasets to HuggingFace Dataset format.
* Fine-tuned DistilBERT for 2 epochs on the labeled dataset.
* Evaluated using accuracy and weighted F1-score.

**Results:**

* Accuracy: 1.0 (100%)
* Weighted F1 Score: 1.0 (100%)
* Strengths: Context-aware embeddings, excels at nuanced and ambiguous text.
* Limitations: Larger model, higher computational requirements.

### Step 4: Model Comparison & Production Recommendation

* **Recommendation:** Deploy **DistilBERT** as the production model due to superior contextual understanding.
* Logistic Regression can serve as a lightweight fallback for low-resource scenarios.

---

## 🧩 Part B – Deployment Task (API)

### Objective

Deploy the best-performing model (DistilBERT) as a REST API, enabling external applications to request predictions programmatically.

### Implementation Details

* **Framework:** FastAPI
* **Endpoint:** `/predict`
* **Request Format:**

```json
{ "text": "Looking forward to the demo!" }
```

* **Response Format:**

```json
{ "label": "positive", "confidence": 0.87 }
```

* Model and tokenizer are loaded from `./distilbert_model`.
* Softmax is applied to logits to generate probabilities.
* W\&B logging is disabled for simplicity (`os.environ["WANDB_DISABLED"] = "true"`).

### Deliverables for Deployment

* `app.py`: Contains the FastAPI implementation.
* `README.md`: Instructions for running the API locally.
* Bonus: `requirements.txt` or Dockerfile can be included for containerized deployment.

---

## 🧩 Part C – Short Answer (Reasoning)


1. **Improving model with only 200 labeled replies:** Use data augmentation (paraphrasing, back-translation), transfer learning with DistilBERT, and semi-supervised learning.
2. **Ensuring safety and fairness:** Evaluate on diverse datasets, implement content filtering, monitor predictions, and conduct regular audits.
3. **Prompt design for cold email openers:** Include context (recipient’s name, company, role), examples of high-quality openers, and specify tone/style.

---

## ⚙️ Setup Instructions (Local Testing)

### 1. Clone the repository

```bash
git clone https://github.com/virajbhutada/SvaraAI-ML-NLP-Internship-Assignment.git
cd SvaraAI-ML-NLP-Internship-Assignment
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API locally

```bash
uvicorn app:app --reload
```

* Access the API at `http://127.0.0.1:8000/predict` using tools like **Postman** or **curl**.

### 5. Example Request

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{"text": "Looking forward to the demo!"}'
```

---

## 🏆 Deliverables

* `notebook.ipynb`: Complete ML/NLP pipeline (Part A).
* `app.py`: FastAPI application (Part B).
* `answers.md`: Reasoning answers (Part C).
* `requirements.txt`: Python dependencies for local deployment.

---

## 📈 Evaluation Criteria

1. **ML/NLP Pipeline**: Data preprocessing, feature engineering, model performance (accuracy & F1).
2. **Transformer Model Usage**: Proper tokenization, training, and evaluation of DistilBERT.
3. **Deployment**: Functional REST API, correct request/response handling, ease of local testing.
4. **Reasoning**: Professional, concise, and technically sound explanations.
5. **Code Quality**: Clean, well-commented, and organized notebook and scripts.

---

## 💡 Notes

* DistilBERT model is saved in `./distilbert_model` and can be reused for inference.
* The API is lightweight, and the notebook demonstrates end-to-end ML workflow from preprocessing to deployment.
* Optionally, Dockerfile can be added for containerized deployment.


