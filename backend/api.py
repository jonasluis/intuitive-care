from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from typing import List
from pydantic import BaseModel

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Operadora(BaseModel):
    registro_ans: str
    cnpj: str
    razao_social: str
    nome_fantasia: str
    modalidade: str
    uf: str

# Carregar os dados das operadoras
import os
import unicodedata
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, 'operators_data', 'Relatorio_cadop.csv')
operators_df = pd.read_csv(csv_path, sep=';', encoding='utf-8')

# Normalizar texto para lidar com problemas de codificação
def normalize_text(text):
    if isinstance(text, str):
        return unicodedata.normalize('NFKD', text)
    return text

# Aplicar normalização às colunas de texto
for col in operators_df.columns:
    if operators_df[col].dtype == 'object':
        operators_df[col] = operators_df[col].apply(normalize_text)

# Imprimir nomes das colunas para depuração
print("Colunas disponíveis:", operators_df.columns.tolist())

@app.get("/operadoras/buscar", response_model=List[Operadora])
async def buscar_operadoras_por_termo(q: str = Query(..., min_length=1)):
    # Converter consulta de busca para minúsculas para pesquisa sem distinção entre maiúsculas e minúsculas
    query = q.lower()
    
    # Pesquisar em colunas relevantes
    # Converter colunas para tipo string antes de aplicar operações de string
    mask = operators_df['Razao_Social'].astype(str).str.lower().str.contains(query, na=False) |\
           operators_df['Nome_Fantasia'].astype(str).str.lower().str.contains(query, na=False) |\
           operators_df['Registro_ANS'].astype(str).str.lower().str.contains(query, na=False) |\
           operators_df['CNPJ'].astype(str).str.lower().str.contains(query, na=False)
    
    results = operators_df[mask].head(50)
    
    # Converter resultados para lista de modelos Operadora
    operators = [
        Operadora(
            registro_ans=str(row['Registro_ANS']),
            cnpj=str(row['CNPJ']),
            razao_social=row['Razao_Social'],
            nome_fantasia=row['Nome_Fantasia'],
            modalidade=row['Modalidade'],
            uf=row['UF']
        )
        for _, row in results.iterrows()
    ]
    
    return operators

@app.get("/buscar", response_model=List[Operadora])
async def buscar_operadoras(nome: str = Query(None)):
    if not nome:
        return []
    
    # Converter consulta de busca para minúsculas para pesquisa sem distinção entre maiúsculas e minúsculas
    query = nome.lower()
    
    # Pesquisar em colunas relevantes
    # Converter colunas para tipo string antes de aplicar operações de string
    mask = operators_df['Razao_Social'].astype(str).str.lower().str.contains(query, na=False) |\
           operators_df['Nome_Fantasia'].astype(str).str.lower().str.contains(query, na=False) |\
           operators_df['Registro_ANS'].astype(str).str.lower().str.contains(query, na=False) |\
           operators_df['CNPJ'].astype(str).str.lower().str.contains(query, na=False)
    
    results = operators_df[mask].head(50)
    
    # Converter resultados para lista de modelos Operadora
    operators = [
        Operadora(
            registro_ans=str(row['Registro_ANS']),
            cnpj=str(row['CNPJ']),
            razao_social=row['Razao_Social'],
            nome_fantasia=row['Nome_Fantasia'],
            modalidade=row['Modalidade'],
            uf=row['UF']
        )
        for _, row in results.iterrows()
    ]
    
    return operators