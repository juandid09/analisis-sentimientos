# Usa la imagen base de Python 3.12 slim (corregido el comentario)
FROM python:3.12-slim

# Instala dependencias del sistema
RUN apt-get update && apt-get install -y \
    libffi-dev \
    libssl-dev \
    python3-xlib \
    && rm -rf /var/lib/apt/lists/*

# Instala UV
RUN pip install --no-cache-dir uv>=0.6.2

# Crea un usuario no-root para seguridad
RUN useradd -m -d /main myuser && chown -R myuser:myuser /main
USER myuser
WORKDIR /main

# Copia los archivos de dependencias
COPY --chown=myuser:myuser pyproject.toml ./

# Instala dependencias del proyecto (usando la sintaxis correcta de UV)
RUN python -m uv pip install --system .

# Crea estructura de directorios con permisos adecuados
RUN mkdir -p results/{capturas,csv_resultados,csv_unitarios,pdf_historicos,pdf_resultados} && \
    chmod -R 755 results

# Copia el código fuente
COPY --chown=myuser:myuser src/ ./src/

# Puerto expuesto
EXPOSE 8501

# Comando para ejecutar Streamlit
CMD ["streamlit", "run", "src/main.py", "--server.port", "8501", "--server.address", "0.0.0.0"]