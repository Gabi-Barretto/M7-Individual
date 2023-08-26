from flask import Flask, request, render_template_string, redirect, session, render_template
import psycopg2
import hashlib
import os

app = Flask(__name__)

def check_login(email, password):
    conn = psycopg2.connect(dbname="todolist", user="user", password="password", host="db", port="5432")
    cursor = conn.cursor()
    cursor.execute("SELECT id_pessoa, senha FROM pessoas WHERE email = %s", (email,))
    user = cursor.fetchone()
    conn.close()

    if user:
        user_id, stored_password = user
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if hashed_password == stored_password:
            return user_id
    return None

@app.route('/', methods=['GET'])
def index():
    return render_template('./login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    user_id = check_login(email, password)

    print(user_id)

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
        return redirect('/login')

    user_id = session['user_id']

    conn = psycopg2.connect(dbname="todolist", user="user", password="password", host="db", port="5432")
    cursor = conn.cursor()
    cursor.execute("SELECT task FROM tasks WHERE user_id = %s", (user_id))
    tasks = [row[0] for row in cursor.fetchall()]
    conn.close()

    return render_template_string("<ul>{% for task in tasks %}<li>{{ task }}</li>{% endfor %}</ul>", tasks=tasks)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
