from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from werkzeug.security import generate_password_hash

app = Flask(__name__)

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
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def add_user(username, email, password):
    conn = get_db()
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)
    cursor.execute(
        "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
        (username, email, hashed_password)
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


def get_users():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users


def update_user(id, username, email, password):
    conn = get_db()
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)
    cursor.execute("""
        UPDATE users
        SET username = ?, email = ?, password = ?
        WHERE id = ?
    """, (username, email, hashed_password, id))
    conn.commit()
    conn.close()


def delete_user(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    conn.close()


# =======================
# USER ROUTES
# =======================

@app.route("/users_page")
def users_page():
    users = get_users()
    return render_template("users.html", users=users)


@app.route("/user_page/<int:id>")
def user_page(id):
    user = get_user(id)
    return render_template("user.html", user=user)


@app.route("/profile/<int:id>")
def profile_route(id):
    user = get_user(id)
    return render_template("profile.html", user=user)


@app.route("/add_user", methods=["POST"])
def add_user_route():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    add_user(username, email, password)
    return redirect(url_for("index"))


@app.route("/update_user/<int:id>", methods=["GET", "POST"])
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
def delete_user_route(id):
    delete_user(id)
    return redirect(url_for("index"))


# =======================
# GENERAL PAGES
# =======================

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route("/results")
def results():
    return render_template("results.html")


# =======================
# START APP
# =======================

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
