# Streamlit e AWS

## Descrição

O arquivo `streamlit_app.py` é o aplicativo Streamlit que contém o código para carregar dados de um bucket S3, criar gráficos com esses dados, e implementar uma seção de login. Abaixo está um resumo das funcionalidades principais do arquivo:

1. **Carregar Dados do S3**: A função `load_data_from_s3` carrega dados de um bucket S3 usando credenciais AWS fornecidas (nota: você deve considerar remover ou ocultar as credenciais do código). O conjunto de dados `Mall_Customers.csv` é carregado do bucket chamado `ponderada4`.

2. **Visualizações de Dados**: Funções para criar e exibir gráficos de dispersão que mostram as relações entre idade e renda anual (`plot_age_vs_income`) e entre renda anual e pontuação de gastos (`plot_income_vs_score`).

3. **Seção de Login**: Uma simples implementação de login, onde um email e uma senha são inseridos e verificados para autenticação. A senha é criptografada usando SHA256.

4. **Estado de Sessão**: O código **tenta** implementar um tipo de gerenciamento de estado de sessão para o aplicativo Streamlit. 

Logo, visamos:

- Carregar dados de clientes de um arquivo CSV hospedado em um bucket S3 da AWS. O arquivo contém informações como idade, renda anual e pontuação de gastos dos clientes.
- Visualizar relações entre diferentes atributos dos clientes através de gráficos de dispersão, como a relação entre idade e renda anual, e entre renda anual e pontuação de gastos.
- Prover uma seção de login simples para acessar funcionalidades administrativas ou protegidas do aplicativo.

O aplicativo é encapsulado em um contêiner Docker para facilitar o deployment e a execução em diferentes ambientes, incluindo uma instância EC2 da AWS.

### Precauções de Segurança
Certifique-se de não expor credenciais AWS ou qualquer outra informação sensível no código. Considere usar variáveis de ambiente ou serviços de gerenciamento de segredos para lidar com credenciais de forma segura.

## Configuração do Ambiente

### Pré-Requisitos

- Python
- Docker
- AWS CLI (para deploy no EC2 e interação com o S3)

### Configuração Local

1. **Instale as Dependências**: Instale as dependências listadas em `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

2. **Execute o Aplicativo Streamlit Localmente**: Execute o aplicativo Streamlit em seu ambiente local.

    ```bash
    streamlit run streamlit_app.py
    ```

### Docker

1. **Construa a Imagem Docker**: Navegue até o diretório contendo o `Dockerfile` e construa a imagem Docker.

    ```bash
    docker build -t nome-da-imagem .
    ```

2. **Execute o Contêiner Docker**: Inicie um contêiner usando a imagem criada.

    ```bash
    docker run -p 8501:8501 nome-da-imagem
    ```

## Deploy na AWS

### Pré-Requisitos

- Uma conta AWS
- Um bucket S3 configurado
- Uma instância EC2 configurada

### Passos para o Deploy

1. **Envie os Dados para o S3**: Faça upload dos dados necessários para o bucket S3.

2. **Configure a Instância EC2**: Inicie e configure uma instância EC2 na AWS.

3. **Deploy do Docker na EC2**: Faça deploy da imagem Docker na instância EC2.

4. **Acesse o Aplicativo**: Acesse o aplicativo Streamlit através do endereço IP público da instância EC2.
