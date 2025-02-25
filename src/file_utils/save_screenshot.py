import pyautogui

def save_screenshot(screenshot_path):
    """ 
    Captura y guarda una captura de pantalla en la ruta especificada.

    Args:
        screenshot_path (str): Ruta donde se guardará la captura.

    Returns:
        str: Ruta del archivo guardado o mensaje de error.
    """

    print(f"Guardando captura en: {screenshot_path}")

    try:
        # Capturar la pantalla completa
        screenshot = pyautogui.screenshot()
        
        # Guardar la imagen en la ubicación especificada
        screenshot.save(screenshot_path)
        
        return screenshot_path  # Devolver la ruta del archivo guardado

    except Exception as e:
        error_message = f"Error al guardar captura de pantalla: {e}"
        print(error_message)
        return error_message  # Retornar el error para manejarlo mejor en la aplicación

