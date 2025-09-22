"""

## Part B – Deployment Task (API)
"""
# %%writefile app.py
# from fastapi import FastAPI
# from pydantic import BaseModel
# import torch
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# import torch.nn.functional as F
# import os
# 
# # Disable W&B
# os.environ["WANDB_DISABLED"] = "true"
# 
# app = FastAPI()
# 
# # Load model
# tokenizer = AutoTokenizer.from_pretrained("./distilbert_model")
# model = AutoModelForSequenceClassification.from_pretrained("./distilbert_model")
# 
# labels = ["negative", "neutral", "positive"]
# 
# class TextIn(BaseModel):
#     text: str
# 
# @app.post("/predict")
# def predict(data: TextIn):
#     inputs = tokenizer(data.text, return_tensors="pt", truncation=True)
#     outputs = model(**inputs)
#     probs = F.softmax(outputs.logits, dim=1)
#     label_idx = torch.argmax(probs).item()
#     confidence = probs[0][label_idx].item()
#     return {"label": labels[label_idx], "confidence": round(confidence, 2)}
#