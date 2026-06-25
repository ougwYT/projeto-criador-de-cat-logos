# 🚀 Projeto Criador de Catálogos Comerciais

> Sistema completo para geração automática de catálogos HTML e PDF a partir de listagens de produtos.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-green)
![PDFPlumber](https://img.shields.io/badge/PDFPlumber-PDF%20Parsing-yellow)
![Playwright](https://img.shields.io/badge/Playwright-PDF%20Generation-orange)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Deploy-black)
![Status](https://img.shields.io/badge/Status-Active-success)

## 🔗 Links

🌐 Demo Online: https://ougwyt.github.io/projeto-criador-de-cat-logos/

📦 Repositório: https://github.com/ougwYT/projeto-criador-de-cat-logos



## 🚀 Como Utilizar

Adicione os arquivos de entrada nas pastas correspondentes e execute:

```bash
python gerar_catalogo.py
```

O sistema executará automaticamente:

1. Extração dos produtos
2. Categorização automática
3. Associação das imagens
4. Geração do QR Code
5. Geração do HTML
6. Geração do PDF

```
```


## 📖 Sobre o Projeto

Este projeto foi desenvolvido para automatizar a criação de catálogos comerciais da **Senna Fix**.

Antes do sistema, a atualização dos catálogos era realizada manualmente, exigindo:

* Organização dos produtos
* Associação de imagens
* Criação das páginas
* Geração de PDF
* Atualização do catálogo online

Com este projeto, todo o processo passou a ser automatizado.

---

# ⭐ Destaques

- Automação completa do processo de geração de catálogos
- Projeto aplicado em um caso real de negócio
- Integração entre PDF, CSV, HTML e GitHub Pages
- Geração de catálogo web e PDF a partir da mesma base de dados
- Publicação online automatizada

## 🎯 Resultado

📦 Mais de 400 produtos processados automaticamente

🖼️ Centenas de imagens associadas automaticamente

⚡ Geração automática de catálogo HTML

📄 Geração automática de catálogo PDF

🌐 Publicação online via GitHub Pages

📱 Layout responsivo para Desktop, Tablet e Mobile

🔄 Pipeline completa executada por um único comando


---

# 📸 Screenshots

## 🏠 Página Inicial

A página inicial apresenta a identidade visual da empresa, estatísticas do catálogo, QR Code para contato e acesso rápido às categorias.

![Página Inicial](docs/assets/screenshots/home.png)

---

## 🛠️ Catálogo de Produtos

Os produtos são organizados automaticamente por categoria, exibindo imagem, código e preço de forma responsiva para desktop, tablet e dispositivos móveis.

![Catálogo](docs/assets/screenshots/categoria.png)


# 🛠 Tecnologias Utilizadas

| Tecnologia      | Utilização            |
| --------------- | --------------------- |
| 🐍 Python       | Backend do projeto    |
| 📊 Pandas       | Manipulação dos dados |
| 📄 PDFPlumber   | Leitura dos PDFs      |
| 🎭 Playwright   | Geração do PDF final  |
| 🌐 HTML5        | Estrutura do catálogo |
| 🎨 CSS3         | Estilização           |
| 🐙 Git          | Versionamento         |
| 🚀 GitHub Pages | Hospedagem            |

---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/ougwYT/projeto-criador-de-cat-logos.git
cd projeto-criador-de-cat-logos
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Instale os navegadores do Playwright:

```bash
python -m playwright install
```

## 📂 Estrutura do Projeto

```
projeto-criador-de-catalogos/

├── config/
│   └── categorias.json
│
├── dados/
│   └── .gitkeep
│
├── docs/
│   ├── assets/
│   ├── imagens_nomeadas_corretamente/
│   └── style.css
│
├── entrada/
│   ├── grupos/
│   └── .gitkeep
│
├── scripts/
│   ├── extrair_pdf.py
│   ├── categorizar_por_grupo.py
│   ├── produtos_com_imagens.py
│   ├── gerar_qrcode.py
│   ├── gerar_html.py
│   └── gerar_pdf.py
│
├── gerar_catalogo.py
├── requirements.txt
├── README.md
└── .gitignore
```


---

# ⚙️ Fluxo de Funcionamento

## 1️⃣ Extração dos Produtos

Leitura automática da listagem fornecida pela empresa.

```python
with pdfplumber.open(PDF_PATH) as pdf:
    for pagina in pdf.pages:
        texto = pagina.extract_text()
```

Resultado:

```text
381 produtos encontrados.
```

---

## 2️⃣ Tratamento dos Dados

Conversão dos registros para DataFrame.

```python
df = pd.DataFrame(produtos)
```

Exemplo:

```text
Código | Produto | Preço
205    | MAX DUCHA 5500W | 8.99
```

---

## 3️⃣ Categorização Automática

Os produtos são classificados utilizando grupos definidos pela empresa.

```python
df["categoria"] = categoria_encontrada
```

Categorias:

* ⚡ Elétrica
* 🔧 Ferramentas
* 🚿 Hidráulica
* 🏠 Utilidades

---

## 4️⃣ Associação das Imagens

Busca automática das imagens correspondentes.

```python
imagem_encontrada = encontrar_imagem(produto)
```

Resultado:

```text
277 imagens associadas automaticamente
```

---

## 5️⃣ Geração do Catálogo HTML

Criação dinâmica dos cards.

```python
def build_card(row):
```

Exemplo gerado:

```html
<article class="card">
    <img src="produto.jpg">
    <h2>Produto</h2>
</article>
```

---

## 6️⃣ Geração do PDF

Conversão automática usando Playwright.

```python
page.pdf(
    path=PDF_PATH,
    format="A4"
)
```

---

## 7️⃣ Publicação Online

Hospedagem gratuita utilizando GitHub Pages.

🌎 Site publicado:

https://ougwyt.github.io/projeto-criador-de-cat-logos/

---

# 📈 Desafios Resolvidos

### ✔ Múltiplos formatos de PDF

Durante o desenvolvimento foi identificado que diferentes versões do sistema geravam PDFs com estruturas distintas.

Para resolver o problema foram implementados múltiplos padrões de Expressões Regulares (Regex), permitindo que o sistema interpretasse corretamente diferentes formatos de listagem.

### ✔ Associação de centenas de imagens

Mais de 400 imagens foram processadas e relacionadas aos produtos.

---

### ✔ Organização automática por categoria

O catálogo é gerado automaticamente com páginas específicas para cada grupo de produtos.

---

# 🚀 Próximas Melhorias

### 📱 Experiência do Usuário

* ✅ Layout Desktop
* ✅ Layout Tablet
* ✅ Layout Mobile
* ☐ Otimização para telas ultrawide
* ☐ Melhorias de acessibilidade

### 🔍 Busca e Navegação

* ☐ Busca por nome do produto
* ☐ Busca por código
* ☐ Destaque visual dos resultados encontrados
* ☐ Pesquisa em tempo real

### 🗂️ Filtros Inteligentes

* ☐ Filtro por categoria
* ☐ Filtro por faixa de preço
* ☐ Filtro por disponibilidade
* ☐ Combinação de múltiplos filtros

### 📊 Relatórios e Exportação

* ☐ Exportação para Excel (.xlsx)
* ☐ Exportação para CSV
* ☐ Relatórios por categoria
* ☐ Relatório de produtos sem imagem

### 🖼️ Tratamento de Imagens

* ☐ Compressão automática
* ☐ Padronização de resolução
* ☐ Conversão automática de formatos
* ☐ Validação de qualidade das imagens

### ⚙️ Painel Administrativo

* ☐ Cadastro de produtos
* ☐ Edição de preços
* ☐ Gerenciamento de categorias
* ☐ Upload de imagens
* ☐ Publicação automática do catálogo

### 🌐 Plataforma Web

* ☐ Progressive Web App (PWA)
* ☐ Modo Offline
* ☐ Instalação em dispositivos móveis
* ☐ Cache inteligente

### 🤖 Automação e IA

* ☐ Associação automática de imagens por IA
* ☐ Sugestão automática de categorias
* ☐ Correção de descrições
* ☐ Geração automática de textos promocionais

### 🔒 Infraestrutura

* ☐ GitHub Actions para deploy automático
* ☐ Testes automatizados
* ☐ Monitoramento de erros
* ☐ Backup automático

# 📊 Métricas do Projeto

| Indicador | Quantidade |
|------------|------------|
| Produtos processados | 380+ |
| Imagens catalogadas | 400+ |
| Categorias | 5 |
| Scripts Python | 5 |
| Tecnologias utilizadas | 8+ |

# 💡 Aprendizados

Durante o desenvolvimento foram praticados:

* Manipulação de arquivos PDF
* Processamento de dados
* Expressões Regulares
* Automação com Python
* HTML e CSS
* Git e GitHub
* Deploy com GitHub Pages

---

# 👨‍💻 Autor

## Miguel Ferreira Sena

🐍 Desenvolvedor Python

💻 Automação de Processos

📊 Manipulação e Tratamento de Dados

🌐 Desenvolvimento Web

🔗 GitHub:
https://github.com/ougwYT

⭐ Se gostou do projeto, deixe uma estrela no repositório.
