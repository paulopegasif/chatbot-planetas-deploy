# 🪐 Chatbot dos Planetas com Gemini API + Flask

Um mini chatbot com interface web que responde perguntas sobre planetas do Sistema Solar, com base em dados de uma planilha. Ele utiliza a API gratuita do Gemini (Google) para gerar respostas com linguagem natural e mantém o histórico de conversa entre usuário e assistente.

## 🚀 Funcionalidades

- Respostas automáticas com base em uma planilha `.xlsx`
- Integração com o modelo **Gemini Flash 2.5 (Google Generative AI)**
- Histórico de conversa com contexto
- Interface web simples com Flask
- Reset do chat a qualquer momento

## 📁 Estrutura do Projeto

```bash
chatbot-planetas/
    ├── app.py
    ├── dados.py
    ├── planetas.xlsx
    ├── templates/
    │   └── index.html
    ├── .env
    ├── requirements.txt
    └── README.md
```

## 📦 Instalação

### Procedimentos

#### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/chatbot-planetas.git
cd chatbot-planetas
```

#### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

#### 3. Instale as dependências

**Com UV (recomendado):**

```bash
uv add .
```

**Ou com o PIP:**

```bash
pip install .
```

#### 4. Configure sua chave de API

**Crie um arquivo `.env` com o seguinte conteúdo:**

```env
GOOGLE_API_KEY=sua_chave_da_gemini_api
```

_Você pode obter a chave em:_
🔗 <https://makersuite.google.com/app/apikey>

## 📄 Estrutura da Planilha (`planetas.xlsx`)

| Planeta | Descrição
|---------|---------
| Mercúrio | É o planeta mais próximo do Sol.
| Vênus | Muito quente devido ao efeito estufa.
| Terra | Nosso planeta, com água e vida conhecida.
| Marte | Conhecido como o planeta vermelho.
| ... | ...

## ▶️ Como Rodar

**Usando a ferramenta UV:**

```bash
uv run app.py
```

**Ou:**

```bash
python app.py # Windows
python3 app.py # Linux/MAC
```

## 🧠 Tecnologias Usadas

- Flask
- Google Generative AI (Gemini)
- Pandas
- dotenv
- UV (opcional)
