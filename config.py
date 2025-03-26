from dotenv import load_dotenv
import os

# Carrega variáveis do arquivo .env
load_dotenv()

# Obtém a variável BASE_URL
BASE_URL = os.getenv("BASE_URL")
# Diretórios
PDF_FOLDER = "pdfs"
ZIP_FILE = "anexos.zip"
