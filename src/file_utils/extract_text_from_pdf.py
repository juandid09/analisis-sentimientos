from PyPDF2 import PdfReader

def extract_text_from_pdf(file):
    """
    Extrae el texto de un archivo PDF.
    
    :param file: Archivo PDF subido.
    :return: Texto extraído del PDF o cadena vacía en caso de error.
    """
    print(f"Extrayendo texto del archivo PDF: {file.name}")
    
    try:
        reader = PdfReader(file)
        text = ""
        
        for page in reader.pages:
            text += page.extract_text() or ""
        
        return text
    except Exception as e:
        print(f"Error al extraer texto del PDF: {e}")
        return ""
