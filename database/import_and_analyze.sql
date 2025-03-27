LOAD DATA INFILE 'path_to_csv/operators.csv'
INTO TABLE healthcare_operators
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@registro_ans, @cnpj, @razao_social, @nome_fantasia, @modalidade, @logradouro, 
 @numero, @complemento, @bairro, @cidade, @uf, @cep, @ddd, @telefone, @fax, 
 @email, @representante, @cargo_representante, @data_registro)
SET
    registro_ans = @registro_ans,
    cnpj = @cnpj,
    razao_social = @razao_social,
    nome_fantasia = @nome_fantasia,
    modalidade = @modalidade,
    logradouro = @logradouro,
    numero = @numero,
    complemento = @complemento,
    bairro = @bairro,
    cidade = @cidade,
    uf = @uf,
    cep = @cep,
    ddd = @ddd,
    telefone = @telefone,
    fax = @fax,
    email = @email,
    representante = @representante,
    cargo_representante = @cargo_representante,
    data_registro_ans = STR_TO_DATE(@data_registro, '%Y-%m-%d');

LOAD DATA INFILE 'path_to_csv/financial_statement.csv'
INTO TABLE financial_statements
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@registro_ans, @data_relatorio, @trimestre, @ano, @receita, @despesa)
SET
    registro_ans = @registro_ans,
    data_relatorio = STR_TO_DATE(@data_relatorio, '%Y-%m-%d'),
    trimestre = @trimestre,
    ano = @ano,
    receita_total = REPLACE(@receita, ',', '.'),
    despesa_total = REPLACE(@despesa, ',', '.'),
    resultado = REPLACE(@receita, ',', '.') - REPLACE(@despesa, ',', '.');

-- Query to get top 10 operators with highest medical-hospital expenses in the last quarter
SELECT 
    ho.razao_social,
    ho.registro_ans,
    fs.trimestre,
    fs.ano,
    fs.eventos_conhecidos_medico_hospitalar as despesa_medico_hospitalar
FROM financial_statements fs
JOIN healthcare_operators ho ON fs.registro_ans = ho.registro_ans
WHERE (fs.ano, fs.trimestre) = (
    SELECT ano, trimestre
    FROM financial_statements
    ORDER BY ano DESC, trimestre DESC
    LIMIT 1
)
ORDER BY fs.eventos_conhecidos_medico_hospitalar DESC
LIMIT 10;

-- Query to get top 10 operators with highest medical-hospital expenses in the last year
SELECT 
    ho.razao_social,
    ho.registro_ans,
    SUM(fs.eventos_conhecidos_medico_hospitalar) as despesa_medico_hospitalar_anual
FROM financial_statements fs
JOIN healthcare_operators ho ON fs.registro_ans = ho.registro_ans
WHERE fs.ano = (SELECT MAX(ano) FROM financial_statements)
GROUP BY ho.razao_social, ho.registro_ans
ORDER BY despesa_medico_hospitalar_anual DESC
LIMIT 10;