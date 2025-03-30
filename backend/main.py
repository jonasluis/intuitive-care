from scraper import Scraper
from downloader import Downloader
from config import FINANCIAL_DATA_URL, OPERATORS_DATA_URL, BASE_URL
from ftp_downloader import FTPDownloader

def main():
    # Baixa os PDFs do site da ANS
    scraper = Scraper(BASE_URL)
    pdf_links = scraper.get_pdf_links()
    downloader = Downloader(pdf_links)
    downloader.download_pdfs()

    # Baixa as demonstrações financeiras dos últimos 2 anos
    financial_downloader = FTPDownloader(FINANCIAL_DATA_URL)
    financial_downloader.download_financial_data()

    # Baixa os dados das operadoras de saúde ativas
    operators_downloader = FTPDownloader(OPERATORS_DATA_URL)
    operators_downloader.download_operators_data()

if __name__ == '__main__':
    main()
