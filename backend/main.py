import argparse
import os
from scraper import Scraper
from downloader import Downloader
from compressor import Compressor
from config import FINANCIAL_DATA_URL, OPERATORS_DATA_URL, BASE_URL
from ftp_downloader import FTPDownloader
from data_transformer import PdfDataTransformer

def scrape_pdfs():
    # 1. Coletar os links dos PDFs
    scraper = Scraper()
    pdf_links = scraper.get_pdf_links()

    # 2. Baixar os PDFs
    downloader = Downloader(pdf_links)
    downloader.download_pdfs()

    # 3. Compactar os arquivos baixados
    compressor = Compressor()
    compressor.create_zip()

def transformar_dados():
    pdf_path = os.path.join("pdfs", "Anexo_I_Rol_2021RN_465.2021_RN627L3.2024.pdf")
    output_csv = "dados_transformados.csv"
    output_zip = "Teste_Jonas_Luis.zip"
    transformer = PdfDataTransformer(pdf_path, output_csv, output_zip)
    transformer.executar()



def download_financial():
    # Baixa as demonstrações financeiras dos últimos 2 anos
    financial_downloader = FTPDownloader(FINANCIAL_DATA_URL)
    financial_downloader.download_financial_data()

def download_operators():
    # Baixa os dados das operadoras de saúde ativas
    operators_downloader = FTPDownloader(OPERATORS_DATA_URL)
    operators_downloader.download_operators_data()

def main():
    parser = argparse.ArgumentParser(description="ANS Data Downloader")
    parser.add_argument("command", choices=["scrape", "download-financial", "transformar_dados", "download-operators", "all"],
                        help="Choose the operation to perform")

    args = parser.parse_args()

    if args.command == "scrape":
        scrape_pdfs()
    elif args.command == "transformar_dados":
        transformar_dados()
    elif args.command == "download-financial":
        download_financial()
    elif args.command == "download-operators":
        download_operators()
    elif args.command == "all":
        scrape_pdfs()
        transformar_dados()
        download_financial()
        download_operators()

if __name__ == "__main__":
    main()