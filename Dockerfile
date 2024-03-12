# Use a imagem oficial do Python com Alpine como base
FROM python:3.13.0a4-alpine3.19

# Defina o diretório de trabalho
WORKDIR /app

# Instale as dependências
RUN apk --no-cache add gcc musl-dev libffi-dev libressl-dev
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copie o código-fonte para o contêiner
COPY . .

# Exponha a porta que a aplicação Flask estará escutando
EXPOSE 5000

# Comando para iniciar a aplicação Flask
CMD ["python", "app.py"]
