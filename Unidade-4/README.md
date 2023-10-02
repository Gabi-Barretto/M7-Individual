# Streamlit e AWS

## Descrição

O arquivo `streamlit_app.py` é o aplicativo Streamlit que contém o código para carregar dados de um bucket S3, criar gráficos com esses dados, e implementar uma seção de logins. Abaixo está um resumo das funcionalidades principais do arquivo:

email: admin@admin.com

senha: admin123

1. **Carregar Dados do S3**: A função `load_data_from_s3` carrega dados de um bucket S3 usando credenciais AWS fornecidas. O conjunto de dados `Mall_Customers.csv` é carregado do bucket chamado `ponderada4`.

2. **Visualizações de Dados**: Funções para criar e exibir gráficos de dispersão que mostram as relações entre idade e renda anual (`plot_age_vs_income`) e entre renda anual e pontuação de gastos (`plot_income_vs_score`).

3. **Predição utilizando modelo e variáveis**: Função (`predict`) que realiza predição através da conexão comoutra instacia com a api configurada.

4. **Seção de Login**: Uma simples implementação de login, onde um email e uma s4enha são inseridos e verificados para autenticação. A senha é criptografada usando SHA256.

5. **Estado de Sessão**: O código **tenta** implementar um tipo de gerenciamento de estado de sessão para o aplicativo Streamlit. 

Logo, visamos:

- Carregar dados de clientes de um arquivo CSV hospedado em um bucket S3 da AWS. O arquivo contém informações como idade, renda anual e pontuação de gastos dos clientes.
- Visualizar relações entre diferentes atributos dos clientes através de gráficos de dispersão, como a relação entre idade e renda anual, e entre renda anual e pontuação de gastos.
- Prover uma seção de login simples para acessar funcionalidades administrativas ou protegidas do aplicativo.

O aplicativo é encapsulado em um contêiner Docker para facilitar o deployment e a execução em diferentes ambientes, incluindo uma instância EC2 da AWS.

### Precauções de Segurança
Certifique-se de não expor credenciais AWS ou qualquer outra informação sensível no código. Considere usar variáveis de ambiente ou serviços de gerenciamento de segredos para lidar com credenciais de forma segura.

## Passos Realizados

### Pré-Requisitos

- Python
- Docker
- AWS CLI 

### Docker

1. **Construa a Imagem Docker**: Navegue até o diretório contendo o `Dockerfile` e construa a imagem Docker.

    ```bash
    docker build -t ponderada4 .
    ```

2. **Colando imagem no DockerHub**:

    ```bash
    docker tag ponderada4:latest gabrielabarretto/ponderadasmodulo7:ponderada4

    docker push gabrielabarretto/ponderadasmodulo7:ponderada4
    ```

## Deploy na AWS

### Pré-Requisitos

- Uma conta AWS
- Um bucket S3 configurado
- Uma instância EC2 configurada

### Passos realizados para o Deploy e utilizar da aplicação.

1. **Enviar os Dados para o S3**: Faça upload dos dados necessários para o bucket S3.

2. **Configurar as Instâncias EC2**: Inicie e configure duas instância EC2 na AWS, uma para o back e predição e ourta com o front e S3.

3. **Deploy do Docker na EC2**: Faça deploy das imagens Docker em sua devida instância EC2. (Apenas dar um pull do DockerHub)

4. **Acessar o Aplicativo**: Acesse o aplicativo Streamlit através do endereço IP público da instância EC2 e aproveite da aplicação.
