import streamlit as st
import pandas as pd
import hashlib
import requests
import matplotlib.pyplot as plt
import boto3
from io import StringIO

data = pd.read_csv('./dataset/Mall_Customers.csv')

def plot_age_vs_income():
    st.subheader('Scatter Plot - Age vs Annual Income')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(data['Age'], data['Annual Income (k$)'], alpha=0.6, edgecolors='w', linewidth=0.5)
    ax.set_title('Age vs Annual Income')
    ax.set_xlabel('Age')
    ax.set_ylabel('Annual Income (k$)')
    st.pyplot(fig)

def plot_income_vs_score():
    st.subheader('Scatter Plot - Annual Income vs Spending Score')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(data['Annual Income (k$)'], data['Spending Score (1-100)'], alpha=0.6, edgecolors='w', linewidth=0.5)
    ax.set_title('Annual Income vs Spending Score')
    ax.set_xlabel('Annual Income (k$)')
    ax.set_ylabel('Spending Score (1-100)')
    st.pyplot(fig)

def login():
    st.subheader('Login Section')
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')
    
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    if email == 'admin@admin.com' and hashed_pw == hashlib.sha256('admin'.encode()).hexdigest():
        return True
    return False

# Creating a simple session state using a class (a trick to simulate session management in Streamlit)
class SessionState:
    def __init__(self):
        self.is_authenticated = False

# Function to get the session state
def get_session_state():
    if not hasattr(st, '_session_state'):
        st._session_state = SessionState()
    return st._session_state

def main():
    session_state = get_session_state()
    
    st.title('Aplicação com Streamlit e Autenticação')
    menu = ['Login', 'Dashboard']
    choice = st.sidebar.selectbox('Menu', menu, key="main_menu_choice")
    
    if choice == 'Login':
        if login():
            st.success('Logged in successfully.')
            st.write('Redirecting to dashboard...')
            session_state.is_authenticated = True
            choice = 'Dashboard'
        else:
            st.warning('Incorrect email or password')
    
    if choice == 'Dashboard':
        if session_state.is_authenticated:
            plot_age_vs_income()
            plot_income_vs_score()
        else:
            st.warning('Please login to access the dashboard.')
            choice = 'Login'

    if choice == 'API Request':  # Adicionado um novo bloco de código para lidar com solicitações API
        st.subheader('API Request Section')
        
        # Criar campos de entrada para Idade, Sexo e Renda Anual
        age = st.number_input('Enter Age', min_value=0)
        gender = st.selectbox('Select Gender', ['Male', 'Female'])
        annual_income = st.number_input('Enter Annual Income', min_value=0)
        
        # Quando o botão 'Submit' é pressionado, enviar uma solicitação POST para a API
        if st.button('Submit'):
            # Formatar os dados de entrada
            data = {
                'Age': int(age),
                'Gender': 1 if gender == 'Male' else 0,
                'Annual_Income': int(annual_income)
            }
            
            # Enviar uma solicitação POST para a API e obter a resposta
            response = requests.post('http://44.201.203.246:5000/predict', json=data)
            
            # Exibir a resposta da API no frontend
            if response.status_code == 200:
                st.success(f'Response from API: {response.json()}')
            else:
                st.error(f'Error: {response.status_code}')

if __name__ == '__main__':
    main()
