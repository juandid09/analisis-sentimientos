import os
from src.file_utils.save_pdf import save_pdf
from src.file_utils.save_csv import save_csv
from src.file_utils.save_screenshot import save_screenshot
from src.file_utils.extract_text_from_pdf import extract_text_from_pdf
# from src.detect_language import detect_language  # (Descomentar si se necesita en el futuro)

# Configuración de directorios para almacenar los resultados de las pruebas
RESULTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_results")
os.makedirs(RESULTS_DIR, exist_ok=True)

def test_save_pdf():
    """
    Prueba la función save_pdf asegurando que el archivo PDF se guarde correctamente.
    """
    result = "Positivo"
    stars = 4
    filename = "test_result.pdf"

    # Guardar el PDF de prueba
    file_path = save_pdf(filename, RESULTS_DIR, result=result, stars=stars)

    # Verificar si el archivo PDF fue creado
    assert os.path.exists(file_path), f"El archivo PDF no fue guardado en {file_path}"

def test_save_csv():
    """
    Prueba la función save_csv asegurando que el archivo CSV se guarde correctamente
    y contenga los datos esperados.
    """
    row_data = ["Test text", "Positivo", 4]  # Datos de prueba
    csv_path = os.path.join(RESULTS_DIR, "test_result.csv")

    # Guardar los datos en el CSV
    save_csv(csv_path, row_data)

    # Verificar si el archivo CSV fue creado
    assert os.path.exists(csv_path), f"El archivo CSV no fue guardado en {csv_path}"

    # Leer el contenido del CSV y verificar que los datos sean correctos
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        lines = f.readlines()

    assert row_data[2] == int(lines[0].strip().split(",")[2]), "Los datos en el archivo CSV no coinciden"

def test_save_screenshot():
    """
    Prueba la función save_screenshot asegurando que se guarde correctamente una captura de pantalla.
    """
    screenshot_path = os.path.join(RESULTS_DIR, "test_screenshot.png")

    # Guardar la captura de pantalla
    save_screenshot(screenshot_path)

    # Verificar si la captura de pantalla fue guardada
    assert os.path.exists(screenshot_path), f"La captura de pantalla no fue guardada en {screenshot_path}"

def test_extract_text_from_pdf():
    """
    Prueba la función extract_text_from_pdf asegurando que extraiga correctamente el texto de un archivo PDF.
    """
    test_pdf_path = "./tests/test_files/test_pdf_file.pdf"  # Asegurar que este archivo exista en la ruta

    with open(test_pdf_path, "rb") as f:
        extracted_text = extract_text_from_pdf(f)

    # Verificar que el texto extraído no esté vacío
    assert len(extracted_text) > 0, "No se extrajo texto del PDF"
