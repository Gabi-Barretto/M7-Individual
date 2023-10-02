import streamlit as st
import pandas as pd
import hashlib
import matplotlib.pyplot as plt
import boto3
from io import StringIO

def load_data_from_s3(bucket_name, file_key):
    s3 = boto3.client('s3', aws_access_key_id='AKIAUTM7ELJLZUKUDQYQ', aws_secret_access_key='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', region_name='us-east-2')
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    data = obj['Body'].read().decode('utf-8')
    return pd.read_csv(StringIO(data))

# Replace the next line with your bucket name and file key
data = load_data_from_s3('ponderada4', 'Mall_Customers.csv')

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

if __name__ == '__main__':
    main()
