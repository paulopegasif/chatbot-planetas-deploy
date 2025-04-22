"""---"""
import os

from flask import Flask, render_template, request, session, redirect, url_for, Response
from dotenv import load_dotenv
import google.generativeai as genai

from dados.dados import carregar_conhecimento_em_texto

# Carrega variáveis de ambiente
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configura a API do Gemini
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

# Flask App
app = Flask(__name__)
app.secret_key = "chave_super_secreta"

# Carrega base de conhecimento da planilha
base_conhecimento: str = carregar_conhecimento_em_texto()

# Mensagem inicial com contexto
mensagem_inicial: str = f"""
Você é um assistente que responde perguntas sobre planetas do Sistema Solar.
Use apenas as informações abaixo:

{base_conhecimento}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if "chat_history" not in session:
        # Inicia histórico com mensagem base de conhecimento
        session["chat_history"] = [
            {
                "role": "user",
                "parts": [mensagem_inicial]
            }
        ]

    resposta: str = ""
    if request.method == "POST":
        pergunta = request.form.get("pergunta")
        if pergunta:
            # Adiciona a pergunta ao histórico
            session["chat_history"].append(
                {
                    "role": "user",
                    "parts": [pergunta]
                }
            )

            # Inicia conversa com histórico atual
            chat = model.start_chat(history=session["chat_history"])

            # Envia mensagem e obtém resposta
            resposta_modelo: genai.GenerativeModel = chat.send_message(pergunta)
            resposta: str = resposta_modelo.text

            # Salva a resposta no histórico
            session["chat_history"].append(
                {
                    "role": "model",
                    "parts": [resposta]
                }
            )

    # Remove mensagem inicial da exibição (opcional)
    historico_visivel: list[str] = session["chat_history"][1:]
    print(historico_visivel)

    return render_template("index.html", historico=historico_visivel)

@app.route("/resetar", methods=["POST"])
def resetar() -> Response:
    """
    resetar Reseta o historico de chamadas, e retorna a pagina index.

    Returns:
        _type_: Response
    """    
    session.pop("chat_history", None)
    return redirect(url_for("index"))

# Executa o app
if __name__ == "__main__":
    app.run(debug=True)
