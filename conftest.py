import sys
from pathlib import Path

# Establecer la ruta del directorio src
src_path = Path(__file__).resolve().parent.parent / "src"

# Agregar src al PYTHONPATH
sys.path.append(str(src_path)) 
