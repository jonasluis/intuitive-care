import os
import requests
from config import PDF_FOLDER

class Downloader:
    def __init__(self, pdf_links):
        self.pdf_links = pdf_links

    def download_pdfs(self):
        """Baixa os arquivos PDF e os salva na pasta especificada."""
        os.makedirs(PDF_FOLDER, exist_ok=True)

        for pdf_url in self.pdf_links:
            pdf_name = pdf_url.split("/")[-1]
            pdf_path = os.path.join(PDF_FOLDER, pdf_name)

            response = requests.get(pdf_url)
            if response.status_code == 200:
                with open(pdf_path, 'wb') as pdf_file:
                    pdf_file.write(response.content)
                print(f"Baixado: {pdf_name}")
            else:
                print(f"Erro ao baixar {pdf_name}")
