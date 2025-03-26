from scraper import Scraper
from downloader import Downloader
from compressor import Compressor

def main():
    # 1. Coletar os links dos PDFs
    scraper = Scraper()
    pdf_links = scraper.get_pdf_links()

    # 2. Baixar os PDFs
    downloader = Downloader(pdf_links)
    downloader.download_pdfs()

    # 3. Compactar os arquivos baixados
    compressor = Compressor()
    compressor.create_zip()

if __name__ == "__main__":
    main()
