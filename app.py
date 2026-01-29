from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DB_PATH = "database/users.db"


# DB
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def add_user(username, email, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(' INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
    conn.commit()
    conn.close()
    
# get one user
def get_user(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (id,))
    user = cursor.fetchone()
    conn.close()
    return user

# get all users
def get_users():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM users ''')
    users = cursor.fetchall()
    conn.close()
    return users

def update_user(id, username, email, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE users 
    SET username = ?, email = ?, password = ?, 
    WHERE id = ? ''', (username, email, password, id,))
    conn.commit()
    conn.close()

def delete_user(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (id,))
    conn.commit()
    conn.close()


# ROUTES
@app.route('/')
def index():
    return render_template('home.html')

# MANAGING USER
# all users
@app.route('/users_page', methods = ['GET'])
def users_route():
    users = get_users()
    return render_template('users.html', users = users)

# single user
@app.route('/user_page', methods = ['GET'])
def users_route(id):
    user = get_user(id)
    return render_template('users.html', user = user)


@app.route('/profile', methods = ['GET'])
def profile_route(id):
    user = get_user(id)
    return render_template('profile.html', user = user)

@app.route('/add_user', methods = ['POST'])
def add_user_route():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    add_user(username, email, password)
    return redirect(url_for('home'))

@app.route('/delete_user/<int:id>', methods = ['GET'])    
def delete_user_route(id):
    delete_user(id)
    return redirect(url_for('home'))


@app.route('/update_user', methods = ['GET', 'POST'])
def update_user_route(id):
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        update_user(id, username, email, password)
        return redirect(url_for('home'))
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (id,))
    user = user.fetchone()
    conn.close()
    return redirect(url_for('profile', user = user))



# MANAGING GENERAL PAGE ROUTES
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == "__main__":
    init_db()
    app.run(debug = True)
