from langdetect import detect_langs

def detect_language(text):
    """Detecta el idioma del texto y devuelve los idiomas con una probabilidad superior al 30%."""
    langs = detect_langs(text)
    
    LANGUAGE_DICT = {
        'es': 'Español', 'en': 'Inglés', 'fr': 'Francés', 'de': 'Alemán',
        'it': 'Italiano', 'pt': 'Portugués', 'ru': 'Ruso', 'zh': 'Chino',
        'ar': 'Árabe', 'ja': 'Japonés', 'ko': 'Coreano', 'hi': 'Hindi',
    }
    
    return {
        LANGUAGE_DICT.get(lang.lang, lang.lang): lang.prob
        for lang in langs if lang.prob > 0.3
    }

