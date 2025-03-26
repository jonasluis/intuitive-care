from scraper import Scraper
from downloader import Downloader
from compressor import Compressor
from data_transformer import PdfDataTransformer

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

    pdf_path = "pdfs/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    output_csv = "dados_transformados.csv"
    output_zip = "Teste_Jonas_Luis.zip"
    transformer = PdfDataTransformer(pdf_path, output_csv, output_zip)
    transformer.executar()

if __name__ == "__main__":
    main()
