
### Introdução

A aplicação é composta por um arquivo HTML que representa um currículo, arquivos CSS para estilização, um arquivo Python que usa FastAPI para servir o conteúdo, e um `Dockerfile` para empacotar tudo em uma imagem Docker. A seguir, descrevemos o passo a passo para entender e executar esta aplicação.

### Etapas de Execução

#### 1. Estrutura do Projeto

A estrutura do projeto inclui uma pasta "curriculo" contendo o arquivo HTML e os arquivos CSS, um arquivo `main.py` com o código FastAPI, um `Dockerfile` para construir a imagem Docker, e um `requirements.txt` com as dependências necessárias.

#### 2. Código FastAPI (main.py)

O código FastAPI é responsável por servir o arquivo HTML. Ele pode ser configurado para servir também os arquivos estáticos, como CSS.

#### 3. Dockerfile

O `Dockerfile` contém as instruções para construir a imagem Docker. Ele define a imagem base do Python, configura o ambiente, copia os arquivos necessários e instala as dependências.

**Código destacável:**

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>Dockerfile</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-Dockerfile">
# Imagem base
FROM python:3.9

# Diretório dentro da imagem que vamos trabalhar
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY . /code

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
</code></div></div></pre>

#### 4. Construindo a Imagem Docker

A imagem Docker é construída usando o comando:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">docker build -t nome-da-imagem .
</code></div></div></pre>

#### 5. Executando o Contêiner Docker

O contêiner é executado a partir da imagem construída com o comando:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">docker run -p 8000:80 nome-da-imagem
</code></div></div></pre>

#### 6. Acessando o Currículo

Após executar o contêiner, o currículo pode ser acessado através do navegador em `http://localhost:8000/`.

### Conclusão

Esta aplicação demonstra uma abordagem moderna e eficiente para servir conteúdo web estático usando FastAPI e Docker. A utilização do Docker garante que a aplicação seja executada de maneira consistente em diferentes ambientes, enquanto o FastAPI oferece uma maneira simples e rápida de servir o conteúdo HTML. A estrutura do projeto e os arquivos fornecidos facilitam a compreensão e a execução da aplicação, tornando-a uma excelente base para projetos futuros.
