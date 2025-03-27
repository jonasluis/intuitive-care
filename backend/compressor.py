import os
import zipfile
from config import PDF_FOLDER, ZIP_FILE

class Compressor:
    def __init__(self, zip_filename=ZIP_FILE, folder=PDF_FOLDER):
        self.zip_filename = zip_filename
        self.folder = folder

    def create_zip(self):
        """Compacta todos os PDFs em um único arquivo ZIP."""
        with zipfile.ZipFile(self.zip_filename, 'w') as zipf:
            for pdf_file in os.listdir(self.folder):
                zipf.write(os.path.join(self.folder, pdf_file), pdf_file)

        print(f"Arquivo ZIP criado: {self.zip_filename}")
