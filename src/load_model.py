import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import torch

from transformers import BertTokenizer, BertForSequenceClassification

MODEL_PATH = "./models/bert-base-multilingual-uncased-sentiment"

def load_model():
    """Carga el modelo y el tokenizador BERT para análisis de sentimiento."""
    try:
        tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
        model = BertForSequenceClassification.from_pretrained(MODEL_PATH)
        model.eval()
        return tokenizer, model
    except Exception as e:
        raise Exception(f"Error al cargar el modelo: {e}")

def analyze_sentiment(text, tokenizer, model):
    """Analiza el sentimiento del texto usando el modelo BERT."""
    inputs = tokenizer(
        text, return_tensors="pt", truncation=True, padding=True, max_length=512
    )
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    scores = outputs.logits.softmax(dim=1).tolist()[0]
    labels = ["Muy Negativo", "Negativo", "Neutral", "Positivo", "Muy Positivo"]
    max_score_idx = scores.index(max(scores))
    
    return labels[max_score_idx], max_score_idx + 1, scores
