### Introdução

Esta aplicação é composta por um arquivo HTML representando uma tela de login, após autenticado, o usuário tem acesso a uma "todo list" que será carregada com base nos dados salvos em um banco de dados postgreSQL que foi trabalhado via adminer. Além disso, inclui arquivos CSS para estilização, um arquivo Python que emprega o Flask para servir o conteúdo e um `Dockerfile` que empacota tudo em uma imagem Docker. Vale ressaltar que a aplicação conta com um autenticador para que nao seja possivel acessar a página sem login ou autenticação do mesmo, cotnando com hashlib sha256 para sua execução. A publicação no docker-hub foi realizada na url: https://hub.docker.com/layers/gabrielabarretto/ponderadasmodulo7/ponderada2/images/sha256-c085a2b9f09f7fe64715929df67e9c3836a5f5fab5cdc7780ddf93b1710e2868?context=repo. A seguir, é apresentado um guia passo a passo para compreender e executar a aplicação. 

### Etapas de Execução

#### 1. Estrutura do Projeto

O projeto tem a seguinte estrutura:

- Uma pasta "templates" contendo os arquivos HTML e CSS.
- Um arquivo `app.py` que contém o código Flask.
- Um `Dockerfile` para criar a imagem Docker.
- Um `docker-compose.yml` para containerizar cada componente da aplicação.
- Um `requirements.txt` que lista as dependências necessárias.

#### 2. Código Flask (app.py)

O código em Flask é encarregado de servir o arquivo HTML, gerenciar a comunicação com o banco de dados e autenticar o usuário.

#### 3. Dockerfile e Docker-Compose

O `Dockerfile` fornece instruções para criar a imagem Docker. Ele especifica a imagem base do Python, configura o ambiente, copia os arquivos necessários e instala as dependências, como Flask e psycopg2.

**Código destacável:**

<pre># Use uma imagem base do Python
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
CMD ["python", "app.py"]</pre>

#### 4. Construção da Imagem Docker

Os containers e as imagens são construídos usando o seguinte comando:

<pre>version: '3.8'
services:
  web:
    image: my-flask-app
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db
  db:
    image: postgres:13
    environment:
      POSTGRES_DB: todolist
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    ports:
      - "5432:5432"
      
  adminer:
    image: adminer
    restart: always
    ports:
      - 8080:8080
    depends_on:
      - db
    container_name: adminer</pre>

#### 5. Acessando o conteúdo

Para buildar a imagem, criar e inicar os containers basta utilizar:

<pre>docker compose up</pre>

Depois de iniciar os containers, a tela de login pode ser acessada no navegador em `http://localhost:5000/`.

### Conclusão

Esta aplicação exemplifica uma abordagem contemporânea e eficaz para servir conteúdo web estático usando Flask e Docker. O uso do Docker assegura uma execução consistente da aplicação em diferentes ambientes, garantindo a containerização de cada componente. Enquanto isso, o Flask proporciona um método ágil e simples de servir o conteúdo HTML. A estrutura organizada do projeto e os arquivos fornecidos tornam a compreensão e execução da aplicação intuitivas, estabelecendo uma excelente base para projetos subsequentes.
