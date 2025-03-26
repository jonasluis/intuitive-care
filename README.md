# Teste 01: Web Scraping de PDFs

O primeiro teste implementa um web scraper automatizado para coletar PDFs do site destinado.

### Estrutura do Projeto

```
├── config.py
|── scraper.py
├── downloader.py
│── compressor.py
├── requirements.txt
└── main.py
```

### Componentes Principais

1. **`config.py`**
   - Configurações globais do projeto
   - URLs base e padrões de busca
   - Caminhos dos diretórios

2. **`scraper.py`**
   - Implementa o web scraping usando BeautifulSoup4
   - Extrai links dos PDFs do site
    
3. **`downloader.py`**
   - Gerencia o download dos PDFs

4. **`compressor.py`**
   - Compacta os PDFs baixados em arquivo ZIP
   - Implementa naming convention específico
   - Gerencia organização dos arquivos

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

### Dependências Principais

```txt
﻿beautifulsoup4==4.12.2
charset-normalizer==3.4.1
python-dotenv==1.0.0
requests==2.31.0
```
3. **Configurar Variáveis de Ambiente**
   Crie um arquivo `.env` na raiz do projeto com as seguintes variável:

```env
# URL base do site da ANS
BASE_URL=[cole_URL]
```

### Execução do Projeto

2. **Executar o Scraper**
```bash
python main.py
```

### Funcionalidades

1. **Web Scraping Inteligente**
   - Navegação automática pelo site
   - Identificação de PDFs relevantes
   - Extração de metadados dos arquivos

2. **Download Robusto**
   - Sistema de retry para downloads interrompidos
   - Verificação de integridade dos arquivos
   - Progress bar para acompanhamento

3. **Compressão Eficiente**
   - Compactação otimizada dos PDFs
   - Naming convention padronizado
   - Organização hierárquica dos arquivos

### Saída

O script gera:
1. PDFs baixados na pasta `pdfs/`
2. Arquivo ZIP compactado na raiz
3. Logs de execução detalhados
