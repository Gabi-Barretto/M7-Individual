
### Introdução

A aplicação é composta por um arquivo Python que usa FastAPI para servir o conteúdo, e um `Dockerfile` para empacotar tudo em uma imagem Docker com as bibliotecas devidamente instalandas. A seguir, descrevemos o passo a passo para entender e executar esta aplicação. 

Segue o **colab** da aplicação, com o tratamento dos dados e o modelo escolhido com justificativa: https://colab.research.google.com/drive/1IOmiQLkVzXF1L2f1TmKfwJZx1VBsz7v_?usp=sharing

Segue o **repositório no dockerhub** onde esta a imagem para execução: https://hub.docker.com/repository/docker/gabrielabarretto/ponderadasmodulo7/tags?page=1&ordering=last_updated

Bibliotecas utilizadas na imagem:

```python
pycaret
fastapi
uvicorn
pydantic
```

# Aplicação de Previsão com FastAPI, Pydantic e Uvicorn

Esta aplicação é construída com FastAPI e utiliza Pydantic para a criação de modelos e Uvicorn como servidor ASGI. A aplicação apresenta uma interface Swagger para facilitar a interação com a API, permitindo que os usuários façam previsões com base nas informações fornecidas através de requisições POST.

## Destaques do Código

1. **FastAPI**: Um moderno framework web de alta performance para construir APIs com Python.
2. **Pydantic**: Usado para a definição de modelos de dados e validação de dados.
3. **Uvicorn**: Um servidor ASGI leve e de alta performance, que serve como a base para executar a aplicação.

## Códigos Importantes

**API:**
```python
# Load trained Pipeline
model = load_model("minha_api")

# Create input/output pydantic models
input_model = create_model("minha_api_input", Gender=(int, ...), Age=(int, ...), Annual_Income=(int, ...))
output_model = create_model("minha_api_output", prediction=(int, ...))


# Define predict function
@app.post("/predict", response_model=output_model)
def predict(data: input_model):
    data = pd.DataFrame([data.dict()])
    predictions = round(predict_model(model, data=data))
    return {"prediction": predictions["prediction_label"].iloc[0]}
```

**Dockerfile:**
```python
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
CMD ["uvicorn", "minha_api:app", "--host", "0.0.0.0", "--port", "8000"]

```

## Passos para Execução

### Pré-requisitos

- Docker instalado em seu sistema.

### Passo a Passo

1. **Puxe a Imagem Docker**: Primeiro, você precisa puxar a imagem Docker do Docker Hub usando o seguinte comando:

   ```sh
   docker pull gabrielabarretto/ponderadasmodulo7:ponderada3
   ```

2. **Executar a Imagem Docker**: Após puxar a imagem, você pode executá-la usando o comando `docker run`. Certifique-se de substituir `<PORTA>` pelo número da porta em que deseja que a aplicação seja hospedada (por exemplo, 8000):

   ```sh
   docker run -p <PORTA>:80 gabrielabarretto/ponderadasmodulo7:ponderada3
   ```

3. **Acessar a Interface Swagger**: Uma vez que a aplicação está rodando, você pode acessar a interface Swagger através do navegador, visitando:

   ```
   http://localhost:<PORTA>/docs
   ```

4. **Utilizar a API**: Agora, você pode usar a API para fazer previsões. Use a interface Swagger para enviar requisições POST com as informações necessárias e viáveis para obter previsões.

## Conclusão e próximos passos

A aplicação até aqui está praticamente completa de facil usabilidade e logo será deployada na AWS contando com o serviço ECR ou EC2. O repositorio ECR já está pronto para deploy em: https://us-east-2.console.aws.amazon.com/ecr/repositories/public/316550699607/ponderada3?region=us-east-2, esperando apenas alguns ajustes que serão estudados na próxima aula.
