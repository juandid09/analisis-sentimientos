import csv

def save_csv(csv_path, row_data):
    """
    Guarda una fila de datos en un archivo CSV.
    
    :param csv_path: Ruta del archivo CSV.
    :param row_data: Lista de datos a guardar como fila en el CSV.
    """
    print(f"Guardando CSV en: {csv_path}")
    
    try:
        with open(csv_path, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(row_data)
    except Exception as e:
        print(f"Error al guardar CSV: {e}")

