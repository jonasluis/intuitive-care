# Teste 03: Banco de Dados

Este projeto implementa ferramentas automatizadas para coleta, processamento e análise de dados de operadoras de saúde, incluindo web scraping, downloads FTP e operações de banco de dados.

## 🚀 Estrutura do Projeto

```
├── scraper.py # Utilitários de web scraping
│── data_transformer.py # Processa e transforma os dados baixados
│── compressor.py # Gerencia a compressão de arquivos
├── database/ # Scripts SQL para operações de banco de dados
│   ├── create_tables.sql # Criação do esquema do banco de dados
│   └── import_and_analyze.sql # Queries de importação e análise de dados
├── config.py # Configurações globais e constantes
│── ftp_downloader.py # Gerencia conexões FTP e download de arquivos
├── financial_data/ # Diretório para demonstrações financeiras baixadas
│── operators_data/ # Diretório para arquivos CSV de dados das operadoras
├── requirements.txt 
└── main.py Script principal para executar o processo de coleta de dados
```

### Configuração do Ambiente

1. **Criar Ambiente Virtual**

   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate    # CMD
   .\venv\Scripts\Activate.ps1 # PowerShell

   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Instalar Dependências**

   ```bash
   pip install -r requirements.txt
   ```

3. Crie e configure as variáveis de ambiente no arquivo `.env`:
```
BASE_URL="[Cole_url_aqui]"
OPERATORS_DATA_URL="[cole_url_aqui_operadoras_ativas]"
FINANCIAL_DATA_URL="[cole_url_aqui_demontracoes_contabeis]"
```

### Executando o Projeto

1. **Executar o Script**
```bash
python main.py
```

## 📦 Componentes Principais

### Coleta de Dados

- **Scraping de PDF**
  - Navegação automatizada e identificação de PDFs
  - Extração de metadados
  - Sistema robusto de download com mecanismo de retry
  - Acompanhamento de progresso

- **Downloads FTP**
  - Gerenciamento de conexões FTP seguras
  - Recuperação automatizada de arquivos
  - Verificação de integridade dos dados

### Processamento de Dados

- **Transformação**
  - Limpeza e normalização de dados
  - Padronização de formatos
  - Verificações de validação

- **Compressão**
  - Compressão otimizada de PDFs
  - Convenção padronizada de nomes
  - Organização hierárquica de arquivos

### Operações de Banco de Dados

- **Criação do Schema**
  - Criação automatizada de tabelas
  - Otimização de índices
  - Gerenciamento de relacionamentos

- **Análise de Dados**
  - Cálculo de métricas de desempenho
  - Análise de tendências
  - Geração de relatórios
   
## 📋 Dependências

Pacotes principais incluem:

```txt
beautifulsoup4==4.12.2
mysql-connector-python==8.0.33
pandas==2.0.3
pdfplumber==0.10.2
python-dotenv==1.0.0
requests==2.31.0
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

## 📁 Saída

O projeto gera:

1. PDFs baixados em `pdfs/`
2. Dados financeiros processados em `financial_data/`
3. Informações das operadoras em `operators_data/`
4. Logs detalhados de execução em `Terminal`

## 📊 Análise de Dados

Acesse as queries de análise preparadas em `database/import_and_analyze.sql` para:
- Métricas de desempenho das operadoras
- Análise de tendências financeiras
- Cálculos de participação de mercado
- Avaliações de conformidade
