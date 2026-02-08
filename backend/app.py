from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add-user", methods=["POST"])
def add_user():
    username = request.form["username"]
    password = request.form["password"]

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, password)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return "User inserted successfully ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
