# Teste 03: Banco de Dados


### Configuração do Ambiente

1. **Criar Ambiente Virtual**

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
ou .\venv\Scripts\activate.ps1 
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

3. Configure as variáveis de ambiente no arquivo `.env`:
```
BASE_URL=[Cole_url_aqui]
OPERATORS_DATA_URL=[cole_url_aqui_operadoras_ativas]
FINANCIAL_DATA_URL=[cole_url_aqui_demontracoes_contabeis]
```

## Estrutura do Projeto

- `main.py`: Script principal para executar o processo de coleta de dados
- `ftp_downloader.py`: Gerencia conexões FTP e download de arquivos
- `data_transformer.py`: Processa e transforma os dados baixados
- `compressor.py`: Gerencia a compressão de arquivos
- `scraper.py`: Utilitários de web scraping
- `database/`: Scripts SQL para operações de banco de dados
  - `create_tables.sql`: Criação do esquema do banco de dados
  - `import_and_analyze.sql`: Queries de importação e análise de dados
- `financial_data/`: Diretório para demonstrações financeiras baixadas
- `operators_data/`: Diretório para arquivos CSV de dados das operadoras

## Testando o Projeto

1. Execute o processo de coleta de dados:
```bash
python main.py
```
Isso irá:
- Conectar aos servidores FTP e baixar os dados necessários
- Baixar e processar demonstrações financeiras
- Baixar e processar dados das operadoras de saúde
- Transformar e preparar dados para importação no banco de dados

2. Importar dados para o MySQL:
- Crie o banco de dados e tabelas usando `database/create_tables.sql`
- Importe os arquivos CSV baixados usando `database/import_and_analyze.sql`

3. Verificar resultados:
- Verifique se as demonstrações financeiras foram baixadas para a pasta `financial_data`
- Verifique se os arquivos CSV das operadoras foram baixados para a pasta `operators_data`
- Execute as queries analíticas em `database/import_and_analyze.sql` para visualizar as principais operadoras

## Dependências

Todos os pacotes necessários estão listados em `requirements.txt`. As principais dependências incluem:
- MySQL Connector para operações de banco de dados
- Bibliotecas FTP para download de dados
- Bibliotecas de processamento de dados (pandas, pdfplumber)
- Ferramentas de web scraping (beautifulsoup4)