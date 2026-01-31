from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = "1234567890" #will be changed later

DB_PATH = "database/users.db"


# =======================
# DATABASE HELPERS
# =======================

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            middlename TEXT,
            lastname TEXT NOT NULL,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def add_user(username, firstname, middlename, lastname, email, password):
    conn = get_db()
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)
    cursor.execute(
        "INSERT INTO users (username, firstname, middlename, lastname, email, password) VALUES (?, ?, ?, ?, ?, ?)",
        (username, firstname, middlename, lastname, email, hashed_password)
    )
    conn.commit()
    conn.close()


def get_user(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
    user = cursor.fetchone()
    conn.close()
    return user


def get_user_by_email(email):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user


def get_users():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users


def update_user(id, username, firstname, middlename, lastname, email, password):
    conn = get_db()
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)
    cursor.execute("""
        UPDATE users
        SET username = ?, firstname = ?, middlename = ?, lastname = ?, email = ?, password = ?
        WHERE id = ?
    """, (username, firstname, middlename, lastname, email, hashed_password, id))
    conn.commit()
    conn.close()


def delete_user(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    conn.close()


# =======================
# AUTH DECORATOR
# =======================

def login_required(route_func):
    @wraps(route_func)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return route_func(*args, **kwargs)
    return wrapper


# =======================
# AUTH ROUTES
# =======================

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = get_user_by_email(email)

        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            return redirect(url_for("profile_route", id=user["id"]))

        return render_template("login.html", error="Invalid email or password")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        add_user(username, email, password)
        return redirect(url_for("login"))

    return render_template("register.html")


# =======================
# PROTECTED USER ROUTES
# =======================

@app.route("/profile/<int:id>")
@login_required
def profile_route(id):
    user = get_user(id)
    return render_template("profile.html", user=user)


@app.route("/users_page")
@login_required
def users_page():
    users = get_users()
    return render_template("users.html", users=users)


@app.route("/update_user/<int:id>", methods=["GET", "POST"])
@login_required
def update_user_route(id):
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        update_user(id, username, email, password)
        return redirect(url_for("profile_route", id=id))

    user = get_user(id)
    return render_template("update_user.html", user=user)


@app.route("/delete_user/<int:id>", methods=["POST"])
@login_required
def delete_user_route(id):
    delete_user(id)
    return redirect(url_for("users_page"))


# =======================
# GENERAL ROUTES
# =======================

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/upload")
@login_required
def upload():
    return render_template("upload.html")


@app.route("/results")
@login_required
def results():
    return render_template("results.html")


# =======================
# START APP
# =======================

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
