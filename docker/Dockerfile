# Use a imagem oficial do Python com Alpine como base
FROM python:3.13.0a4-alpine3.19

# Defina o diretório de trabalho
WORKDIR /app

# Copie o código-fonte para o contêiner
COPY . /app

# Instale as dependências
RUN apt-get update && apt-get install -y \
    npm \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Instalar as dependências do npm (incluindo o Vue.js)
RUN npm install

# Exponha a porta que a aplicação Flask estará escutando
EXPOSE 5000

# Comando para iniciar a aplicação Flask
CMD ["python", "app.py"]
