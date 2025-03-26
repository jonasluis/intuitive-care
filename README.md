# 📌 Soluções do Teste Técnico

Este repositório contém soluções para um teste técnico, divididas em quatro branches separadas. Cada branch corresponde a uma implementação específica.

## 🌳 Estrutura de Branches

- `main` - Branch principal com documentação base
- `teste-01` - Implementação de Web Scraping
- `teste-02` - Transformação de Dados
- `teste-03` - Banco de Dados
- `teste-04` - API

## 🔧 Tecnologias Utilizadas

O projeto foi desenvolvido utilizando **Python**, devido à sua eficiência em manipulação de dados e web scraping. As principais bibliotecas utilizadas são:

- **Web Scraping:** `requests`, `BeautifulSoup`
- **Manipulação de PDFs:** `PyPDF2`, `pdfplumber`
- **Transformação de Dados:** `pandas`
- **Compactação de Arquivos:** `zipfile`
- **Banco de Dados:** `MySQL`

---

## 📂 Detalhamento das Soluções

### 1️⃣ Web Scraping (Python)

**Objetivo:** Baixar os anexos I e II da página da ANS e compactá-los.

#### 📌 Passos:
1. Acessar o site da ANS e identificar os links dos PDFs.
2. Baixar os arquivos utilizando `requests` e `BeautifulSoup`.
3. Compactar os arquivos em um `.zip`.

---

### 2️⃣ Transformação de Dados (Python)

**Objetivo:** Extrair os dados do Anexo I, salvar em CSV e compactar.

#### 📌 Passos:
1. Extrair tabelas do PDF utilizando `pdfplumber`.
2. Salvar os dados estruturados em um arquivo CSV com `pandas`.
3. Substituir abreviações nas colunas OD e AMB pelas descrições completas.
4. Compactar o CSV utilizando `zipfile`.

---

## ⚙️ Configuração do Git

1. **Clone o Repositório**
```bash
git clone git@github.com:jonasluis/intuitive-care.git
cd intuitive-care
```

2. **Atualize as Referências Remotas**
```bash
git fetch --all
```

3. **Visualize Todas as Branches**
```bash
git branch -a
```

4. **Configure as Branches Locais**
```bash
git checkout -b teste-01 origin/teste-01
git checkout -b teste-02 origin/teste-02
git checkout -b teste-03 origin/teste-03
git checkout -b teste-04 origin/teste-04
```

5. **Verificar as Branches Locais**
```bash
git branch
```

---

## 📬 Contato

Agradeço a oportunidade de realizar este teste técnico. 

📞 Telefone: 21 964655190
🔗 LinkedIn: linkedin.com/in/jonasluisds/
📧 E-mail: jonasluis66@gmail.com

---

🔗 **Autor:** Jonas Luis

