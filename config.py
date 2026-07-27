import os
from dotenv import load_dotenv


# ==========================================
# Cargar variables del archivo .env
# ==========================================

load_dotenv()


# ==========================================
# Configuración Gemini
# ==========================================

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "gemini-2.5-flash"
)


# ==========================================
# Rutas del proyecto
# ==========================================

DOCUMENTS_PATH = os.getenv(
    "DOCUMENTS_PATH",
    "documents"
)

EMBEDDINGS_PATH = os.getenv(
    "EMBEDDINGS_PATH",
    "embeddings"
)


# ==========================================
# Parámetros RAG
# ==========================================

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

TOP_K = 3


# ==========================================
# Validación
# ==========================================

if not GOOGLE_API_KEY:
    print(
        "⚠️ Advertencia: "
        "No se encontró GOOGLE_API_KEY."
    )