import requests 
from bs4 import BeautifulSoup 
from config import BASE_URL

class Scraper:
    def __init__(self, url=BASE_URL):
        self.url = url

    def get_pdf_links(self):
        """Faz o scraping e retorna uma lista de links dos PDFs"""
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception("Erro ao acessar a página!")

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)

        pdf_links = [link['href'] for link in links if 'Anexo I' in link.text or 'Anexo II' in link.text]

        return pdf_links
