# Importar la función a probar desde el módulo correcto
from src.detect_language import detect_language

def test_detect_language():
    """
    Prueba unitaria para la función detect_language.

    Se verifica que un texto en español sea detectado correctamente.
    """

    # Texto de prueba en español
    text = "Hola, ¿cómo estás?"

    # Ejecutar la detección de idioma
    languages = detect_language(text)

    # Verificar que el idioma detectado sea Español
    assert "Español" in languages, f"Esperado 'Español', pero se obtuvo {languages}"

