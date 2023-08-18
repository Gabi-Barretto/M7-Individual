from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

def get_tasks():
    conn = psycopg2.connect(dbname="todolist", user="user", password="password", host="db")
    cursor = conn.cursor()
    cursor.execute("SELECT task FROM tasks")
    tasks = [row[0] for row in cursor.fetchall()]
    conn.close()
    return tasks

@app.route('/')
def index():
    tasks = get_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    conn = psycopg2.connect(dbname="todolist", user="user", password="password", host="db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
