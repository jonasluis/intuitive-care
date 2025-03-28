# Teste 04: API

Este projeto consiste em um sistema para coleta, processamento e visualização de dados de operadoras de saúde da ANS (Agência Nacional de Saúde Suplementar). O sistema é dividido em backend (Python/FastAPI) e frontend (Vue.js).

## Configuração do Ambiente

### Backend

1. **Criar e ativar ambiente virtual Python**

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
# ou
.\venv\Scripts\activate.ps1 (PowerShell)
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

2. **Instalar dependências**
```bash
pip install -r backend/requirements.txt
```
**Caso o requirements.txt não funcione**

```bash
pip install --only-binary :all: beautifulsoup4 charset-normalizer python-dotenv requests pandas pdfplumber tabula-py openpyxl PyPDF2
```

```bash
pip install fastapi uvicorn
pip install mysql-connector-python
```

3. **Configurar variáveis de ambiente**

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
```
BASE_URL="[Cole_url_aqui]"
OPERATORS_DATA_URL="[cole_url_aqui_operadoras_ativas]"
FINANCIAL_DATA_URL="[cole_url_aqui_demontracoes_contabeis]
```

### Frontend

1. **Instalar dependências**
```bash
cd frontend
npm install
# ou
yarn install
```

## Execução do Projeto

### Backend

1. **Executar o script principal para coleta de dados**

Este script faz o download dos PDFs do site da ANS, dados financeiros e dados de operadoras ativas.

```bash
python main.py
```

2. **Iniciar o servidor API**

```bash
python backend/run_api.py
```

O servidor API estará disponível em: http://127.0.0.1:8000

Endpoints disponíveis:
- `/buscar?nome={termo}` - Busca operadoras pelo nome

### Frontend

```bash
cd frontend
npm run dev
# ou
yarn dev
```

O frontend estará disponível em: http://localhost:5173

## Screenshots

### Interface de Busca de Operadoras

A imagem abaixo mostra a interface de busca de operadoras de saúde, onde é possível pesquisar por nome e visualizar informações como Registro ANS, CNPJ, Razão Social, Nome Fantasia e Modalidade.

![Interface de Busca de Operadoras](./images/operadoras_search.png)

## Estrutura do Projeto

### Backend

- **main.py**: Ponto de entrada principal que orquestra o processo de coleta de dados
- **api.py**: Implementação da API FastAPI para busca de operadoras
- **run_api.py**: Script para iniciar o servidor API
- **config.py**: Configurações e variáveis de ambiente
- **scraper.py**: Classe para web scraping do site da ANS
- **downloader.py**: Classe para download de arquivos PDF
- **ftp_downloader.py**: Classe para download de arquivos via FTP
- **data_transformer.py**: Processamento e transformação dos dados baixados
- **compressor.py**: Compressão de arquivos
- **database/**: Scripts SQL para operações de banco de dados
  - **create_tables.sql**: Criação do esquema do banco de dados
  - **import_and_analyze.sql**: Queries de importação e análise de dados

### Frontend

- **src/App.vue**: Componente principal da aplicação Vue
- **src/main.js**: Ponto de entrada do frontend, configuração do Vue e Vuetify
- **index.html**: Página HTML principal
- **vite.config.js**: Configuração do Vite (bundler)

### Diretórios de Dados

- **pdfs/**: Armazena os PDFs baixados
- **financial_data/**: Armazena os dados financeiros baixados
- **operators_data/**: Armazena os dados de operadoras baixados

## Fluxo de Funcionamento

1. O script `main.py` inicia o processo de coleta de dados:
   - Faz scraping do site da ANS para obter links de PDFs
   - Baixa os PDFs relevantes
   - Baixa dados financeiros via FTP
   - Baixa dados de operadoras ativas via FTP

2. Os dados são processados e transformados para o formato adequado

3. A API FastAPI disponibiliza endpoints para consulta dos dados

4. O frontend Vue.js consome a API e apresenta uma interface amigável para busca de operadoras

## Tecnologias Utilizadas

### Backend
- Python
- FastAPI
- BeautifulSoup4 (web scraping)
- Pandas (processamento de dados)
- FTPLib (download via FTP)
- Requests (requisições HTTP)

### Frontend
- Vue.js 3
- Axios (requisições HTTP)
- Vite (bundler)
