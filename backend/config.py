from dotenv import load_dotenv
import os

# Carrega variáveis do arquivo .env
load_dotenv()

# URLs base
BASE_URL = os.getenv("BASE_URL")
FINANCIAL_DATA_URL = os.getenv("FINANCIAL_DATA_URL")
OPERATORS_DATA_URL = os.getenv("OPERATORS_DATA_URL")

# Diretórios
PDF_FOLDER = "pdfs"
FINANCIAL_DATA_FOLDER = "financial_data"
OPERATORS_DATA_FOLDER = "operators_data"
ZIP_FILE = "anexos.zip"
