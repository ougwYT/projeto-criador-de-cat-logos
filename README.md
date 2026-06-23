# 🚀 Projeto Criador de Catálogos Comerciais

> Sistema completo para geração automática de catálogos HTML e PDF a partir de listagens de produtos.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-green?logo=pandas)
![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-black?logo=github)
![Playwright](https://img.shields.io/badge/Playwright-PDF-red)
![Status](https://img.shields.io/badge/Status-Concluído-success)

---

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

## 🎯 Resultado

✅ 380+ produtos processados automaticamente

✅ Catálogo Web responsivo

✅ Catálogo PDF pronto para impressão

✅ Organização automática por categorias

✅ Associação automática de imagens

✅ Publicação online via GitHub Pages

---

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

# 📂 Estrutura do Projeto

```text
projeto-criador-de-catalogos/

├── docs/
│   ├── index.html
│   ├── style.css
│   ├── catalogo_sennafix.pdf
│   ├── assets/
│   └── imagens_nomeadas_corretamente/
│
├── scripts/
│   ├── extrair_pdf.py
│   ├── categorizar_por_grupo.py
│   ├── produtos_com_imagens.py
│   ├── gerar_html.py
│   └── gerar_pdf.py
│
├── dados/
│   ├── produtos.csv
│   ├── produtos_com_imagem.csv
│   └── produtos_raw.csv
│
└── entrada/
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

### ✔ Extração de PDFs com formatos diferentes

Foi necessário criar múltiplas expressões regulares:

```python
padrao_1 = re.compile(...)
padrao_2 = re.compile(...)
padrao_3 = re.compile(...)
```

---

### ✔ Associação de centenas de imagens

Mais de 400 imagens foram processadas e relacionadas aos produtos.

---

### ✔ Organização automática por categoria

O catálogo é gerado automaticamente com páginas específicas para cada grupo de produtos.

---

# 🚀 Próximas Melhorias

O projeto está funcional e em produção, mas ainda existem diversas evoluções planejadas para torná-lo mais completo, escalável e amigável para usuários e administradores.

### 📱 Responsividade Avançada

* ✅ Desktop
* ✅ Tablet
* ✅ Mobile
* 🔄 Otimização para telas ultrawide
* 🔄 Ajustes específicos para dispositivos abaixo de 400px

### 🔍 Busca e Navegação

* ☐ Busca por nome do produto
* ☐ Busca por código
* ☐ Busca por categoria
* ☐ Destaque visual dos resultados encontrados

### 🗂️ Filtros Inteligentes

* ☐ Filtro por categoria
* ☐ Filtro por faixa de preço
* ☐ Filtro por disponibilidade
* ☐ Combinação de múltiplos filtros

### 📊 Exportação de Dados

* ☐ Exportação para Excel (.xlsx)
* ☐ Exportação para CSV
* ☐ Relatórios por categoria
* ☐ Relatórios de produtos sem imagem

### 🖼️ Processamento de Imagens

* ☐ Compressão automática
* ☐ Redimensionamento inteligente
* ☐ Conversão automática de formatos
* ☐ Validação de qualidade das imagens

### ⚙️ Painel Administrativo

* ☐ Cadastro de produtos
* ☐ Edição de preços
* ☐ Gerenciamento de categorias
* ☐ Upload de imagens
* ☐ Controle de catálogo publicado

### 📄 Geração de Catálogos

* ☐ Múltiplos modelos de layout
* ☐ Personalização de cores
* ☐ Catálogos por categoria
* ☐ Catálogos promocionais automáticos

### 🌐 Plataforma Web

* ☐ Progressive Web App (PWA)
* ☐ Modo offline
* ☐ Instalação em dispositivos móveis
* ☐ Cache inteligente

### 🤖 Automação e IA

* ☐ Associação automática de imagens por IA
* ☐ Correção automática de descrições
* ☐ Sugestão de categorias
* ☐ Geração automática de textos promocionais

### 🔒 Infraestrutura

* ☐ Deploy automatizado via GitHub Actions
* ☐ Testes automatizados
* ☐ Monitoramento de erros
* ☐ Backup automático dos catálogos



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

🐍 Python Developer

🔗 GitHub:
https://github.com/ougwYT

📫 Em busca de oportunidades para desenvolvimento Python, automação de processos e análise de dados.

---

⭐ Se gostou do projeto, deixe uma estrela no repositório.
