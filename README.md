# Análisis de Sentimientos
Este proyecto implementa un sistema de análisis de sentimientos utilizando modelos de Hugging Face, junto con las bibliotecas UV y Streamlit para el despliegue y la visualización de resultados. El modelo cuenta con El modelo nlptown/bert-base-multilingual-uncased-sentiment es un modelo de análisis de sentimientos basado en BERT. Clasifica textos en 5 niveles de sentimiento, desde muy negativo (1 estrella) hasta muy positivo (5 estrellas). Es multilingüe y ha sido entrenado con reseñas en los siguientes idiomas:

Inglés (150k reseñas)
Holandés (80k reseñas)
Alemán (137k reseñas)
Francés (140k reseñas)
Italiano (72k reseñas)
Español (50k reseñas)

## Descripción
El objetivo principal de este proyecto es desarrollar una aplicación que permita analizar el sentimiento de textos en español, clasificándolos como positivos, negativos o neutros. Para ello, se emplea un modelo preentrenado de Hugging Face.

## Características
- Análisis de Sentimientos: Clasificación de textos en categorías de sentimiento (positivo, negativo, neutro).
- Interfaz Web Interactiva: Utilización de Streamlit para proporcionar una interfaz amigable donde los usuarios pueden ingresar texto y obtener resultados de análisis en tiempo real.
- Despliegue Rápido: Implementación de UV para manejar las solicitudes de manera eficiente.

## Estructura del Proyecto
El repositorio está organizado de la siguiente manera:
- src/: Contiene el código fuente principal de la aplicación.
- models/: Almacena los modelos de Hugging Face utilizados para el análisis.
- tests/: Incluye pruebas unitarias y de integración para asegurar el correcto funcionamiento del sistema.
- assets/fonts/: Contiene las fuentes utilizadas en la interfaz de usuario.
- results/: Directorio destinado a almacenar los resultados generados por la aplicación.

## Observaciones 
- El archivo que se debe ejecutar esta en src/main.py este archivo es la GUI encargada de ejecutar todo el programa siguiendo el patron de desarrollo movelo, vista controlador. 
- el modelo cuenta con validaciones como si se ingresa texto y se sube un archivo el archivo tiene la prioridad y se sobreescribe tambien esta la validacion de que si no se ha ingresado el texto no realiza el analizis ni creacion de archivos.

## Recursos del Proyecto
Archivo Docker: https://drive.google.com/file/d/1rm4Fzgxyo2SnbJITbBjiLjpvRjWxXS5h/view

Tutorial: https://drive.google.com/file/d/1_yovclEGbwSK_R9l5P__CDqyQn9UVh4m/view

Repositorio GitHub: https://github.com/juandid09/analisis-sentimientos

Documentación: https://drive.google.com/file/d/1PR4EILWrFV_9LAV1msBqLS6NWhyEv2YE/view?usp=sharing

DataSet: https://drive.google.com/drive/folders/1DOcWALnlstm_s2iiXy6kvJkSFFAI3lom

Cronograma: https://drive.google.com/file/d/1tbOqLqiyfsRkJli00CGV9WxD9EVxuxFI/view?usp=sharing

Trello: https://trello.com/invite/b/67ab67f657485b812b1d7393/ATTI5262d7711fef9fd1a6c83bf16cb2958838F8D397/proyecto-final

## Requisitos
principalmente estas dependencias. 
- python 3.12 o superior
- uvicorn
- Streamlit
- transformers de Hugging Face
- torch

## Instalacion desde repositiorio
1. Clonar el repositorio:
  git clone https://github.com/juandid09/analisis-sentimientos.git
  cd analisis-sentimientos
2. Crear y activar un entorno virtual:
   uv init
   python -m venv env
   source env/bin/activate
3. ejecutar el proyecto desde el archivo main.py que contiene la interfaz grafica de usuario y desde este se ejecuta el proyecto respetado el patro MVC
   uv run streamlit run src/main.py
4. En caso de tener algun problema al correr el proyecto asegurate que las dependencias esten agregadas con uv add #nombre asi podemos agregar si una presenta erro antes se debe hacer yv remove #nombre

## Instalacion desde imagen dockert 
1. descargar la imagen docker analisis-sentimientos-streamlit-uv.tar
2. docker load -i analisis-sentimientos-streamlit-uv.tar
3. docker images
4. docker run -d -p 8501:8501 analisis-sentimientos-streamlit-uv
   
## Uso 
al ejecutatarse el proyecto se cuenta con dos opciones 
1. ingresar texto
2. subir archivo txt o pdf
- una vez se ingrese el texto o se suba el archivo se da clic en el boton analizar. En este momento el retornara la puntuacion con la emosion, Cabe señalar que existe una validacion que permite hacer una cosa a la vez evitando errores.
- una vez analizado retornara una calificacion y detectara el idioma con mas de 30% de probabilidad
- tambien estan las opciones de guardar pdf unitario, historico pdf, scv unitario,scv historico y pantallazo estas opciones permitiendo guardar los resultados de manera individual en un archivo en unas carpetas especificas creadas ya sea individualmente o por antesedente que agrupa los diferentes analisis.

## Explicación de los Archivos
### main. py: 
Implementa la interfaz gráfica en Streamlit, gestiona la carga de archivos, muestra resultados y contiene todos lo botones para generar archivos
### load_model.py: 
Carga el modelo BERT y el tokenizador para el análisis de sentimientos.
### detect_language.py:
Detecta el idioma del texto con una probabilidad mínima del 30%.
### sentiment_analysis.py:
Tokeniza el texto y lo analiza utilizando el modelo cargado en load_model.py
### extract_text_from_pdf.py:
Extrae texto de archivos PDF.
### save_csv.py / save_pdf.py
Guardan los resultados en archivos CSV y PDF, respectivamente.
### save_screenshot.py
Captura y guarda una imagen de los resultados.
### archivos directorios test 
son las pruebas que se ejecutan en pytets

## Licencia
se publica bajo la licencia la cual esta disponible aqui: [LICENSE.py](https://github.com/juandid09/analisis-sentimientos/blob/main/LICENSE)

## Contribuciones
si se ve producente hacer alguna observación, corrección  o contribución el proyecto esta en disponibilidad  de hacer fork y abrir un pull request.  
