# Usando uma imagem base do Python
FROM python:3.9-slim

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando os arquivos do projeto para dentro do container
COPY . /app

# Instalando as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expondo a porta que o Flask vai rodar
EXPOSE 5000

# Comando para rodar a aplicação Flask
CMD ["python", "app.py"]
