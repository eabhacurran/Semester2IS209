from flask import Flask, render_template, request, redirect, jsonify
import requests
import os
from dotenv import load_dotenv
import psycopg2

# load environment variables
load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")


# connect to PostgreSQL
def get_db_connection():
    return psycopg2.connect(DATABASE_URL)


# homepage - get random dog
@app.route("/")
def index():
    url = "https://api.thedogapi.com/v1/images/search"

    headers = {
        "x-api-key": API_KEY
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    image_url = data[0]["url"]

    return render_template("index.html", image_url=image_url)


# save dog image URL to database
@app.route("/save", methods=["POST"])
def save():
    image_url = request.form["image_url"]

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO favorite_dogs (image_url) VALUES (%s)",
        (image_url,)
    )

    conn.commit()

    cur.close()
    conn.close()

    return redirect("/")


# health check endpoint
@app.route("/health")
def health():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({"status": "ok", "database": "connected"}), 200
    except Exception as e:
        return jsonify({"status": "error", "database": "not reachable"}), 500


# status endpoint (diagnostics)
@app.route("/status")
def status():
    db_status = "unknown"

    try:
        conn = get_db_connection()
        conn.close()
        db_status = "connected"
    except Exception as e:
        db_status = "error"

    return jsonify({
        "service": "Dog API Demo",
        "app": "running",
        "database": db_status
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)