from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from typing import List, Optional
from pydantic import BaseModel, validator
import os
import unicodedata
import math

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
    nome_fantasia: Optional[str] = None  # Make this field optional
    modalidade: str
    uf: str

    @validator('nome_fantasia', pre=True)
    def handle_nan(cls, v):
        if pd.isna(v):  # Handle NaN values
            return None
        return v

# Carregar os dados das operadoras
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, 'backend/operators_data', 'Relatorio_cadop.csv')
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
    query = q.lower()
    
    mask = (
        operators_df['Razao_Social'].astype(str).str.lower().str.contains(query, na=False) |
        operators_df['Nome_Fantasia'].astype(str).str.lower().str.contains(query, na=False) |
        operators_df['Registro_ANS'].astype(str).str.lower().str.contains(query, na=False) |
        operators_df['CNPJ'].astype(str).str.lower().str.contains(query, na=False)
    )
    
    results = operators_df[mask].head(50)

    if results.empty:
        raise HTTPException(status_code=404, detail="Nenhuma operadora encontrada")
    
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
    
    query = nome.lower()
    
    mask = (
        operators_df['Razao_Social'].astype(str).str.lower().str.contains(query, na=False) |
        operators_df['Nome_Fantasia'].astype(str).str.lower().str.contains(query, na=False) |
        operators_df['Registro_ANS'].astype(str).str.lower().str.contains(query, na=False) |
        operators_df['CNPJ'].astype(str).str.lower().str.contains(query, na=False)
    )
    
    results = operators_df[mask].head(50)
    
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