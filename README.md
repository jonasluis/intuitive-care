# Teste 02: Transformação de Dados

Este projeto implementa um web scraper automatizado para coletar PDFs do site da ANS, processá-los e gerar saída de dados estruturados.

### Estrutura do Projeto

```
├── config.py          # Configurações globais e constantes
├── scraper.py         # Implementação do web scraping
├── downloader.py      # Gerenciamento de download de PDFs
├── compressor.py      # Utilitários de compressão de arquivos
├── data_transformer.py # Extração e transformação de dados PDF
├── requirements.txt   # Dependências do projeto
└── main.py           # Script principal de execução
```

### Componentes Principais

1. **`config.py`**
   - Configurações globais do projeto
   - URLs base e padrões de busca
   - Caminhos de diretórios

2. **`scraper.py`**
   - Implementa web scraping usando BeautifulSoup4
   - Extrai links de PDFs do site
   - Filtra documentos relevantes do Anexo I e Anexo II

3. **`downloader.py`**
   - Gerencia downloads de PDFs
   - Trata tentativas de download e casos de erro

4. **`compressor.py`**
   - Comprime PDFs baixados em formato ZIP
   - Implementa convenções específicas de nomenclatura
   - Gerencia organização de arquivos

5. **`data_transformer.py`**
   - Extrai dados tabulares dos PDFs
   - Transforma dados em formato CSV
   - Implementa limpeza e normalização de dados

### Configuração do Ambiente

1. **Criar Ambiente Virtual**

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

2. **Instalar Dependências**
```bash
pip install -r requirements.txt
```
**Caso o requirements.txt não funcione**

```bash
pip install --only-binary :all: beautifulsoup4 charset-normalizer python-dotenv requests pandas pdfplumber tabula-py openpyxl PyPDF2
```

### Dependências

```txt
beautifulsoup4==4.12.2
charset-normalizer==3.4.1
python-dotenv==1.0.0
requests==2.31.0
pandas==2.1.1
pdfplumber==0.10.2
tabula-py==2.7.0
openpyxl==3.1.2
PyPDF2==3.0.1
```

3. **Variáveis de Ambiente**
   Crie um arquivo `.env` na raiz do projeto com:

```env
# URL base do site da ANS
BASE_URL="[inserir_URL]"
```

### Executando o Projeto

1. **Executar o Script**
```bash
python main.py
```

### Funcionalidades

1. **Web Scraping Inteligente**
   - Navegação automatizada do site
   - Identificação e filtragem inteligente de PDFs
   - Foco específico em documentos do Anexo I e Anexo II

2. **Sistema Robusto de Download**
   - Tratamento confiável de download de PDFs
   - Verificação de integridade de arquivos
   - Tratamento de erros e novas tentativas

3. **Transformação de Dados**
   - Extração de tabelas de PDFs
   - Limpeza e normalização de dados
   - Geração de saída em CSV

4. **Compressão de Arquivos**
   - Compressão otimizada de PDFs
   - Convenção padronizada de nomenclatura
   - Organização hierárquica de arquivos

### Saída

O script gera:
1. PDFs baixados no diretório `pdfs/`
2. Dados transformados em formato CSV
3. Arquivo ZIP comprimido final no diretório raiz
4. Logs detalhados de execução
