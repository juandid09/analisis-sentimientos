import os
from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter

def save_pdf(filename, folder, historic=False, result=None, stars=None):
    """ 
    Guarda el análisis de sentimiento en un archivo PDF.
    
    Args:
        filename (str): Nombre del archivo PDF a generar.
        folder (str): Carpeta donde se guardará el PDF.
        historic (bool): Indica si se debe actualizar un archivo histórico existente.
        result (str): Resultado del análisis de sentimiento.
        stars (int): Cantidad de estrellas según el sentimiento detectado.
    
    Returns:
        str: Ruta del archivo PDF generado.
    """

    # Ajustar la carpeta en caso de ser un histórico
    if historic:
        folder = os.path.join(folder, "pdf_historicos")
    
    # Crear la carpeta si no existe
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, filename)

    # Crear un nuevo PDF con los resultados del análisis
    pdf = FPDF()
    pdf.add_page()

    # Agregar fuente personalizada para compatibilidad con caracteres especiales
    font_path = "./assets/fonts/dejavu-sans.book.ttf"  # Verificar que la ruta sea correcta
    pdf.add_font("DejaVuSans", "", font_path, uni=True)
    pdf.set_font("DejaVuSans", "", 12)

    # Agregar contenido al PDF
    pdf.cell(200, 10, txt="Resultado del Análisis de Sentimiento", ln=True, align='C')
    pdf.multi_cell(0, 10, txt=f"Sentimiento: {result} ({stars} estrellas)")

    # Manejo de archivo histórico (si aplica)
    if historic and os.path.exists(file_path):
        try:
            # Leer el archivo PDF existente
            existing_pdf = PdfReader(file_path)
            output_pdf = PdfWriter()

            # Agregar todas las páginas del PDF existente
            for page in existing_pdf.pages:
                output_pdf.add_page(page)

            # Guardar el nuevo análisis en un PDF temporal
            temp_path = os.path.join(folder, "temp.pdf")
            pdf.output(temp_path, "F")

            # Leer el PDF recién generado y agregarlo al histórico
            new_pdf = PdfReader(temp_path)
            output_pdf.add_page(new_pdf.pages[0])

            # Guardar el PDF final con el historial actualizado
            with open(file_path, "wb") as final_pdf:
                output_pdf.write(final_pdf)

            # Eliminar el archivo temporal
            os.remove(temp_path)
        except Exception as e:
            raise Exception(f"Error al actualizar el histórico: {e}")
    else:
        # Guardar el nuevo PDF normalmente
        pdf.output(file_path, "F")

    return file_path
