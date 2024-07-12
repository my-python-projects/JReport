# Use a imagem oficial do Python com Alpine como base
FROM python:3.9-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o código da aplicação
COPY . .

# Instalar dependências de sistema necessárias para construir lxml
RUN apt-get update && apt-get install -y \
    libxml2-dev \
    libxslt-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar o arquivo de requisitos e instalar as dependências
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Expor a porta que a aplicação irá rodar
EXPOSE 5000

# Definir o comando para rodar a aplicação
CMD ["python", "app.py"]
