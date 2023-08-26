from flask import Flask, request, render_template_string, redirect, session, render_template, url_for
import psycopg2
import hashlib
import os
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

app.secret_key = os.urandom(24)

def check_login(email, password):
    try:
        conn = psycopg2.connect(dbname="todolist", user="user", password="password", host="db", port="5432")
    except Exception as e:
        logging.debug(f"Erro ao conectar ao banco de dados: {e}")
        return None

    cursor = conn.cursor()
    cursor.execute("SELECT id_pessoa, senha FROM pessoas WHERE email = %s", (email,))
    user = cursor.fetchone()

    logging.debug(f"Usuário encontrado: {user}")

    conn.close()

    if user:
        user_id, stored_password = user
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        hashed_password_2 = hashlib.sha256(stored_password.encode()).hexdigest()
        logging.debug(f"Senha fornecida (hash): {hashed_password}")
        logging.debug(f"Senha armazenada (hash): {hashed_password_2}")
        if hashed_password == hashed_password_2:
            return user_id
        
    return None

@app.route('/', methods=['GET'])
def index():
    if 'user_id' in session or 'token' in session:
        return redirect('/todo')
    
    return render_template('./login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    user_id = check_login(email, password)

    logging.debug(f"ID do usuário: {user_id}")

    if user_id:
        token = hashlib.sha256(os.urandom(24)).hexdigest()
        session['user_id'] = user_id
        session['token'] = token
        return redirect('/todo')
    else:
        return "Login falhou!"


@app.route('/todo')
def todo_list():
    if 'user_id' not in session or 'token' not in session:
        return redirect('/')

    user_id = session['user_id']

    logging.debug(f"ID do usuário: {user_id}")

    conn = psycopg2.connect(dbname="todolist", user="user", password="password", host="db", port="5432")
    cursor = conn.cursor()
    cursor.execute("SELECT task_description FROM tasks WHERE id_pessoa = %s", (user_id,))
    tasks = [row[0] for row in cursor.fetchall()]
    conn.close()

    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    if 'user_id' not in session or 'token' not in session:
        return redirect('/')

    user_id = session['user_id']
    new_task = request.form['task']

    conn = psycopg2.connect(dbname="todolist", user="user", password="password", host="db", port="5432")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task_description, id_pessoa) VALUES (%s, %s)", (new_task, user_id))
    conn.commit()
    conn.close()

    return redirect(url_for('todo_list'))  # Redireciona de volta para a lista de tarefas após adicionar uma nova tarefa

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('token', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
