from load_model import analyze_sentiment

def get_sentiment_result(text, tokenizer, model):
    """Obtiene el resultado del análisis de sentimiento dado un texto."""
    result, stars, scores = analyze_sentiment(text, tokenizer, model)
    return result, stars, scores
