import os
import streamlit as st

from file_utils.extract_text_from_pdf import extract_text_from_pdf
from file_utils.save_pdf import save_pdf
from file_utils.save_csv import save_csv
from file_utils.save_screenshot import save_screenshot
from load_model import load_model, analyze_sentiment
from detect_language import detect_language

# Cargar el modelo y tokenizador
tokenizer, model = load_model()

# Configuración de directorios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(os.path.dirname(BASE_DIR), "./results")
SUBDIRECTORIOS = [
    "capturas", "csv_resultados", "csv_unitarios", "pdf_resultados", "pdf_historicos"
]

# Crear directorios si no existen
for subdir in SUBDIRECTORIOS:
    os.makedirs(os.path.join(RESULTS_DIR, subdir), exist_ok=True)

# Configuración de la interfaz
st.title("\U0001F31F Análisis de Sentimiento \U0001F31F")

# Inicializar valores por defecto en la sesión
session_defaults = {
    "user_input": "",
    "uploaded_file": None,
    "pdf_count": 0,
    "historic_pdf_created": False
}

for key, value in session_defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# Entrada de texto y subida de archivo
user_input = st.text_area(
    "\u270D Introduce el texto para analizar:",
    value=st.session_state.user_input,
    max_chars=5000
)

uploaded_file = st.file_uploader(
    "\U0001F4C2 O sube un archivo (TXT o PDF)", type=["txt", "pdf"]
)

# Manejo de archivo subido
if uploaded_file and uploaded_file != st.session_state.uploaded_file:
    if uploaded_file.type == "text/plain":
        st.session_state.user_input = uploaded_file.read().decode("utf-8")
    elif uploaded_file.type == "application/pdf":
        st.session_state.user_input = extract_text_from_pdf(uploaded_file)
    st.session_state.uploaded_file = uploaded_file

# Botones de acción
col1, col2, col3 = st.columns(3)

# Botón para analizar sentimiento
target="sentimiento"
with col1:
    if st.button("\U0001F50D Analizar Sentimiento"):
        if not user_input:
            st.warning("⚠️ Texto no ingresado. Por favor ingresa algún texto para analizar.")
        else:
            try:
                result, stars, _ = analyze_sentiment(user_input, tokenizer, model)
                st.session_state.result = result
                st.session_state.stars = stars
                st.session_state.detected_languages = detect_language(user_input)

                st.subheader("Resultado del análisis:")
                st.markdown(f"### {result} {'⭐' * stars}")
                st.write(
                    f"🌍 Idioma(s) detectado(s): {', '.join(st.session_state.detected_languages.keys())}"
                )
            except Exception as e:
                st.error(f"Error: {e}")

# Botón para generar un PDF con el resultado
with col2:
    if st.button("\U0001F4C4 Generar PDF"):
        if not user_input:
            st.warning("⚠️ No se puede generar PDF sin texto.")
        elif "result" in st.session_state:
            st.session_state.pdf_count += 1
            filename = f"resultado{st.session_state.pdf_count}.pdf"
            path = save_pdf(
                filename,
                os.path.join(RESULTS_DIR, "pdf_resultados"),
                result=st.session_state.result,
                stars=st.session_state.stars
            )
            st.success(f"✅ PDF guardado en: {path}")

# Botón para actualizar el histórico en PDF
with col3:
    if st.button("\U0001F4DA Historico PDF"):
        if not user_input:
            st.warning("⚠️ No se puede actualizar el histórico sin texto.")
        elif "result" in st.session_state:
            historic_path = save_pdf(
                "historico.pdf",
                os.path.join(RESULTS_DIR, "pdf_historicos"),
                historic=True,
                result=st.session_state.result,
                stars=st.session_state.stars
            )
            st.success(f"✅ Histórico actualizado en: {historic_path}")

# Botones adicionales
st.write("---")
cols = st.columns(4)

# Guardar en CSV Histórico
with cols[0]:
    if st.button("\U0001F4BE CSV Histórico"):
        if not user_input:
            st.warning("⚠️ No se puede guardar CSV sin texto.")
        elif "result" in st.session_state:
            csv_path = os.path.join(RESULTS_DIR, "csv_resultados", "resultados.csv")
            save_csv(csv_path, [
                user_input, st.session_state.result, st.session_state.stars
            ])
            st.success(f"✅ CSV guardado en: {csv_path}")

# Guardar en CSV Unitario
with cols[1]:
    if st.button("\U0001F4BE CSV Unitario"):
        if not user_input:
            st.warning("⚠️ No se puede guardar CSV sin texto.")
        elif "result" in st.session_state:
            unitario_dir = os.path.join(RESULTS_DIR, "csv_unitarios")
            count = len(os.listdir(unitario_dir)) + 1
            csv_path = os.path.join(unitario_dir, f"resultado_{count}.csv")
            save_csv(csv_path, [
                user_input, st.session_state.result, st.session_state.stars
            ])
            st.success(f"✅ CSV guardado en: {csv_path}")

# Capturar pantalla de resultados
with cols[2]:
    if st.button("\U0001F4F8 screenshot"):
        if not user_input:
            st.warning("⚠️ No se puede tomar captura sin texto.")
        elif "result" in st.session_state:
            capturas_dir = os.path.join(RESULTS_DIR, "capturas")
            count = len(os.listdir(capturas_dir)) + 1
            screenshot = save_screenshot(
                os.path.join(capturas_dir, f"captura_{count}.png")
            )
            st.success(f"✅ Captura guardada en: {screenshot}")

# Limpiar todos los campos de entrada
with cols[3]:
    if st.button("\U0001F9F9 Limpiar"):
        st.session_state.user_input = ""
        st.session_state.uploaded_file = None
        st.session_state.result = None
        st.session_state.stars = None
        st.rerun()
