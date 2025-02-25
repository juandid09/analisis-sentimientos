import pytest
from src.load_model import load_model, analyze_sentiment
# from src.detect_language import detect_language  # (Descomentar si se necesita en el futuro)

@pytest.fixture(scope="module")
def model_and_tokenizer():
    """ Fixture para cargar el modelo y tokenizador antes de ejecutar las pruebas """
    tokenizer, model = load_model()
    return tokenizer, model

def test_analyze_sentiment(model_and_tokenizer):
    """
    Prueba la función analyze_sentiment asegurando que el análisis de sentimiento sea correcto.
    """
    tokenizer, model = model_and_tokenizer
    text = "Este es un texto positivo"

    # Ejecutar el análisis de sentimiento
    result, stars, _ = analyze_sentiment(text, tokenizer, model)

    # Verificar que el resultado sea "Positivo" o "Muy Positivo"
    assert result in ["Positivo", "Muy Positivo"], (
        f"se esperaba 'Positivo' o 'Muy Positivo', pero se obtuvo '{result}'"
    )

    # Verificar que las estrellas sean 4 o 5 (según la calibración del modelo)
    assert stars in [5], f"se esperaba 5 estrellas, pero se obtuvo {stars}"
