# Use uma imagem base do Python
FROM python:3.8

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos necessários
COPY . /app

# Instale as dependências a partir do arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta que o Flask usará
EXPOSE 5000

# Comando para executar o aplicativo
CMD ["python", "app.py"]
