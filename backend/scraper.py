import requests 
from bs4 import BeautifulSoup 
from config import BASE_URL
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time

class Scraper:
    def __init__(self, url=BASE_URL):
        self.url = url
        self.session = requests.Session()
        # Configure retry strategy
        retry_strategy = Retry(
            total=3,  # number of retries
            backoff_factor=1,  # wait 1, 2, 4 seconds between retries
            status_forcelist=[500, 502, 503, 504, 404],  # HTTP status codes to retry on
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def get_pdf_links(self):
        """Faz o scraping e retorna uma lista de links dos PDFs"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }

        try:
            # Add a small delay before the request to avoid overwhelming the server
            time.sleep(2)
            
            response = self.session.get(
                self.url,
                headers=headers,
                timeout=30,  # Set timeout to 30 seconds
                verify=False,  # Verify SSL certificates
                allow_redirects=True  # Follow redirects
            )
            response.raise_for_status()
            
            print(f"Response status code: {response.status_code}")
            print(f"Response URL after redirects: {response.url}")
            
            # Check if we got HTML content
            content_type = response.headers.get('content-type', '')
            if 'text/html' not in content_type.lower():
                raise Exception(f"Unexpected content type: {content_type}")

            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)

            pdf_links = []
            for link in links:
                if ('Anexo I' in link.text or 'Anexo II' in link.text) and ('.pdf' in link['href'].lower()):
                    href = link['href']
                    if not href.startswith('http'):
                        if href.startswith('/'):
                            href = 'https://www.gov.br' + href
                        else:
                            href = 'https://www.gov.br/' + href
                    pdf_links.append(href)

            if not pdf_links:
                print("Warning: No PDF links found matching the criteria. This could mean the page structure has changed.")
                print("Available links:", [link.text for link in links if '.pdf' in link.get('href', '').lower()])

            return pdf_links

        except requests.exceptions.RequestException as e:
            print(f"Error during request: {str(e)}")
            raise Exception(f"Failed to access the page: {str(e)}")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise
