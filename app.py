from flask import Flask, render_template, url_for

app = Flask(__name__)

DB_PATH = "database/users.db"

# DB
def init_db():
    ...

def get_users():
    ...

def get_user(id):
    ...

def add_user():
    ...

def update_user(form_fields):
    ...

def delete_user(id):
    ...

# ROUTES
@app.route('/')
def index():
    return render_template('home.html')

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
    app.run(debug = True)
