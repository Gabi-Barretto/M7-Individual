# Use uma imagem base Python
FROM python:3.8

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código para o diretório de trabalho
COPY . .

# Comando para executar o aplicativo
CMD ["uvicorn", "minha_api:app", "--host", "0.0.0.0", "--port", "80"]
