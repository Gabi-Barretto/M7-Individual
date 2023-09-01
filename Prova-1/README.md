### Introdução

Esta aplicação é composta por um arquivo HTML representando uma tela de cadastro, um arquivo Python que emprega o Fastapi para servir o conteúdo e dois `Dockerfile`. A publicação no docker-hub foi realizada na url: https://hub.docker.com/layers/gabrielabarretto/ponderadasmodulo7/ponderada2/images/sha256-c085a2b9f09f7fe64715929df67e9c3836a5f5fab5cdc7780ddf93b1710e2868?context=repo. A seguir, é apresentado um guia passo a passo para compreender e executar a aplicação. 

### Etapas de Execução

#### 1. Estrutura do Projeto

O projeto tem a seguinte estrutura:

- Uma pasta "templates" contendo os arquivos HTML e CSS.
- Um arquivo `main.py` que contém o código FastAPI.
- Dois `Dockerfile` para criar a imagem Docker.
- Um `docker-compose.yml` para containerizar cada componente da aplicação. (python node e db)
- Um `requirements.txt` que lista as dependências necessárias do python.

#### 2. Código Flask (app.py)

O código em Flask é encarregado de servir o arquivo HTML, gerenciar a comunicação com o banco de dados e autenticar o usuário.

#### 3. Dockerfile e Docker-Compose

O `Dockerfile` fornece instruções para criar a imagem Docker. Ele especifica a imagem base do Python, configura o ambiente, copia os arquivos necessários e instala as dependências, como Flask e psycopg2.

**Código destacável:**

<pre># Use uma imagem base do Python
FROM python:3.8

# Defina o diretório de trabalho
WORKDIR /backend

# Copie os arquivos necessários
COPY . .

# Instale as dependências a partir do arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta que o Fastapi usará
EXPOSE 8000

# Comando para executar o aplicativo
CMD ["python", "main.py"]
</pre>

E:

<pre>FROM node

# Defina o diretório de trabalho
WORKDIR /frontend

# Copie os arquivos necessários
COPY . .

# Instale dependências
RUN npm install

# Comando para executar o aplicativo
CMD ["node", "server.js"]
</pre>


#### 4. Construção do Docker Compose

Os containers e as imagens são definidos da deguinte maneira no compose, segregados pelo seu tipo cada parte da aplicacao tem sua propria imagem e conteiner a partir da definição abaixo:

<pre>version: '3.8'
services:
  web:
    image: gabrielabarretto/ponderadasmodulo7:prova-node
    ports:
      - "3000:3000"
    depends_on:
      - 'db'

  py:
    image: gabrielabarretto/ponderadasmodulo7:prova-python
    depends_on:
      - 'db'

  db:
    image: gabrielabarretto/ponderadasmodulo7:prova-banco</pre>

#### 5. Acessando o conteúdo

Para buildar a imagem, criar e inicar os containers basta utilizar no diretório da aplicação:

<pre>docker compose up</pre>

Depois de iniciar os containers, a tela de login pode ser acessada no navegador em `http://localhost:3000/`.

### Conclusão

Esta aplicação exemplifica uma abordagem contemporânea e eficaz para servir conteúdo web estático usando Fastapi e Docker. O uso do Docker assegura uma execução consistente da aplicação em diferentes ambientes, garantindo a containerização de cada componente. Enquanto isso, o Fastapi proporciona um método ágil e simples de servir o conteúdo HTML. A estrutura organizada do projeto e os arquivos fornecidos tornam a compreensão e execução da aplicação intuitivas, estabelecendo uma excelente base para projetos subsequentes.
