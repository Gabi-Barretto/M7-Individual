
import streamlit as st
import pandas as pd
import hashlib

# Load CSV data
data = pd.read_csv('./dataset/Mall_Customers.csv')

def main():
    st.title('Aplicação com Streamlit e Autenticação')
    
    menu = ['Login', 'Dashboard']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Login':
        st.subheader('Login Section')
        # TODO: Implement login functionality
    elif choice == 'Dashboard':
        st.subheader('Dashboard')
        # TODO: Plot charts using the CSV data

if __name__ == '__main__':
    main()

def login():
    st.subheader('Login Section')

    email = st.text_input('Email')
    password = st.text_input('Password', type='password')
    
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    if email == 'admin@admin.com' and hashed_pw == hashlib.sha256('admin'.encode()).hexdigest():
        return True
    return False

def main():
    st.title('Aplicação com Streamlit e Autenticação')
    
    menu = ['Login', 'Dashboard']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Login':
        if login():
            st.success('Logged in successfully.')
            st.write('Redirecting to dashboard...')
            # TODO: Implement redirection
        else:
            st.warning('Incorrect email or password')
    elif choice == 'Dashboard':
        st.subheader('Dashboard')
        # TODO: Plot charts using the CSV data

if __name__ == '__main__':
    main()

import matplotlib.pyplot as plt

def plot_data():
    st.subheader('Scatter Plot - Age vs Annual Income')
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Age'], data['Annual Income (k$)'], alpha=0.6, edgecolors='w', linewidth=0.5)
    plt.title('Age vs Annual Income')
    plt.xlabel('Age')
    plt.ylabel('Annual Income (k$)')
    st.pyplot()

def main():
    st.title('Aplicação com Streamlit e Autenticação')
    
    menu = ['Login', 'Dashboard']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Login':
        if login():
            st.success('Logged in successfully.')
            st.write('Redirecting to dashboard...')
            # Redirecting to Dashboard
            choice = 'Dashboard'
        else:
            st.warning('Incorrect email or password')
    if choice == 'Dashboard':
        plot_data()

if __name__ == '__main__':
    main()
