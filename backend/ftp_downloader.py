import os
import ftplib
from datetime import datetime, timedelta
from urllib.parse import urlparse
from config import FINANCIAL_DATA_FOLDER, OPERATORS_DATA_FOLDER

class FTPDownloader:
    def __init__(self, ftp_url):
        self.ftp_url = ftp_url
        parsed_url = urlparse(ftp_url)
        self.host = parsed_url.netloc
        # Mantém o caminho completo incluindo o prefixo 'FTP'
        self.path = parsed_url.path

    def connect(self):
        """Estabelece conexão com o servidor FTP"""
        try:
            self.ftp = ftplib.FTP(self.host)
            self.ftp.login()
            self.ftp.set_pasv(True)
            # Navega para o diretório correto
            if self.path:
                # Divide o caminho em componentes e navega um por um
                path_parts = [p for p in self.path.split('/') if p]
                for part in path_parts:
                    try:
                        self.ftp.cwd(part)
                    except ftplib.error_perm as e:
                        print(f"Falha ao mudar para o diretório {part}: {str(e)}")
                        raise
        except Exception as e:
            print(f"Erro de conexão FTP: {str(e)}")
            raise

    def download_financial_data(self):
        """Baixa os arquivos dos últimos 2 anos do diretório de demonstrações contábeis"""
        os.makedirs(FINANCIAL_DATA_FOLDER, exist_ok=True)
        self.connect()
        
        try:
            # Lista todos os arquivos e diretórios
            entries = []
            self.ftp.dir(entries.append)
            
            # Filtra os diretórios dos últimos 2 anos e 2023
            current_year = datetime.now().year
            target_years = [str(year) for year in range(2023, current_year + 1)]
            
            for entry in entries:
                # Analisa a entrada do diretório
                parts = entry.split()
                if len(parts) >= 9:
                    name = ' '.join(parts[8:])
                    if any(year in name for year in target_years):
                        try:
                            # Tenta entrar no diretório do ano
                            self.ftp.cwd(name)
                            # Lista os arquivos no diretório do ano
                            year_files = self.ftp.nlst()
                            
                            # Cria o diretório do ano localmente se não existir
                            year_dir = os.path.join(FINANCIAL_DATA_FOLDER, name)
                            os.makedirs(year_dir, exist_ok=True)
                            
                            for file in year_files:
                                try:
                                    # Baixa o arquivo
                                    local_file = os.path.join(year_dir, file)
                                    with open(local_file, 'wb') as fp:
                                        self.ftp.retrbinary(f'RETR {file}', fp.write)
                                    print(f'Baixado: {name}/{file}')
                                except ftplib.error_perm as e:
                                    print(f'Erro ao baixar {file}: {str(e)}')
                                except Exception as e:
                                    print(f'Erro ao processar {file}: {str(e)}')
                            
                            # Volta para o diretório pai
                            self.ftp.cwd('..')
                        except ftplib.error_perm as e:
                            print(f'Erro ao acessar diretório {name}: {str(e)}')
                        except Exception as e:
                            print(f'Erro ao processar diretório {name}: {str(e)}')
        
        finally:
            self.ftp.quit()

    def download_operators_data(self):
        """Baixa os dados cadastrais das Operadoras Ativas no formato CSV"""
        os.makedirs(OPERATORS_DATA_FOLDER, exist_ok=True)
        self.connect()
        
        try:
            files = self.ftp.nlst()
            
            # Baixa o arquivo CSV mais recente
            csv_files = [f for f in files if f.endswith('.csv')]
            if csv_files:
                latest_file = max(csv_files)
                local_file = os.path.join(OPERATORS_DATA_FOLDER, latest_file)
                
                with open(local_file, 'wb') as fp:
                    self.ftp.retrbinary(f'RETR {latest_file}', fp.write)
                print(f'Baixado: {latest_file}')
        
        finally:
            self.ftp.quit()