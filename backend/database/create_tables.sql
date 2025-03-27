-- Create database for ANS healthcare operator data
CREATE DATABASE IF NOT EXISTS ans_data;
USE ans_data;

-- Create table for healthcare operators
CREATE TABLE IF NOT EXISTS healthcare_operators (
    registro_ans VARCHAR(20) PRIMARY KEY,
    cnpj VARCHAR(14),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),
    cep VARCHAR(8),
    ddd VARCHAR(2),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    email VARCHAR(100),
    representante VARCHAR(255),
    cargo_representante VARCHAR(100),
    data_registro_ans DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create table for financial statements
CREATE TABLE IF NOT EXISTS financial_statements (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    registro_ans VARCHAR(20),
    data_relatorio DATE,
    trimestre INT,
    ano INT,
    receita_total DECIMAL(15,2),
    despesa_total DECIMAL(15,2),
    resultado DECIMAL(15,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (registro_ans) REFERENCES healthcare_operators(registro_ans)
);

-- Create indexes for better query performance
CREATE INDEX idx_operator_cnpj ON healthcare_operators(cnpj);
CREATE INDEX idx_operator_razao_social ON healthcare_operators(razao_social);
CREATE INDEX idx_financial_date ON financial_statements(data_relatorio);
CREATE INDEX idx_financial_year_quarter ON financial_statements(ano, trimestre);