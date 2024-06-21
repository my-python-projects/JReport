# Usar a imagem oficial do Node.js como base
FROM node:14

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar package.json e package-lock.json para o diretório de trabalho
COPY package*.json ./

# Instalar as dependências do projeto
RUN npm install

# Copiar o restante do código da aplicação
COPY . .

# Construir a aplicação para produção
RUN npm run build

# Expor a porta que a aplicação irá rodar
EXPOSE 8080

# Instalar o servidor HTTP para servir a aplicação
RUN npm install -g serve

# Definir o comando para rodar o servidor HTTP
CMD ["serve", "-s", "dist"]
