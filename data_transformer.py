class PdfDataTransformer:
    def __init__(self, pdf_path, output_csv, output_zip):
        self.pdf_path = pdf_path
        self.output_csv = output_csv
        self.output_zip = output_zip
        self.abreviacoes = {
            "OD": "Ordem de Serviço",
            "AMB": "Ambulatorial"
        }

    def extrair_tabela_pdf(self):
        """Extrai os dados da tabela do PDF."""
        dados = []
        with pdfplumber.open(self.pdf_path) as pdf:
            for page in pdf.pages:
                tabelas = page.extract_table()
                if tabelas:
                    for row in tabelas:
                        dados.append(row)
        return dados

    def transformar_dados(self):
        """Transforma os dados e salva como CSV."""
        dados_extraidos = self.extrair_tabela_pdf()
        df = pd.DataFrame(dados_extraidos)
        df = df.dropna().reset_index(drop=True)
        df = df.replace(self.abreviacoes)
        df.to_csv(self.output_csv, index=False, encoding="utf-8")
        print(f"CSV salvo como: {self.output_csv}")