from flask import Flask, render_template, request, redirect, url_for
import requests
import os
from dotenv import load_dotenv
import psycopg2

# Load environment variables
load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")


def get_db_connection():
    return psycopg2.connect(DATABASE_URL)


@app.route("/")
def index():
    url = "https://api.thedogapi.com/v1/images/search"

    headers = {
        "x-api-key": API_KEY
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        image_url = data[0]["url"]

        # Try to get breed name if available
        dog_name = "Unknown Dog"
        if data[0].get("breeds") and len(data[0]["breeds"]) > 0:
            dog_name = data[0]["breeds"][0].get("name", "Unknown Dog")

        saved = request.args.get("saved") == "1"

        return render_template(
            "index.html",
            image_url=image_url,
            dog_name=dog_name,
            saved=saved
        )

    except Exception as e:
        return f"Error loading dog image: {e}", 500


@app.route("/save", methods=["POST"])
def save():
    image_url = request.form.get("image_url")
    dog_name = request.form.get("dog_name")

    if not image_url:
        return "Missing image URL", 400

    conn = None
    cur = None

    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO favorite_dogs (dog_name, image_url)
            VALUES (%s, %s)
            """,
            (dog_name, image_url)
        )

        conn.commit()

    except Exception as e:
        if conn:
            conn.rollback()
        return f"Database error while saving dog: {e}", 500

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    return redirect(url_for("index", saved=1))


@app.route("/health")
def health():
    try:
        conn = get_db_connection()
        conn.close()
        return {"status": "ok", "database": "connected"}
    except Exception:
        return {"status": "error", "database": "not reachable"}, 500


@app.route("/status")
def status():
    db_status = "unknown"

    try:
        conn = get_db_connection()
        conn.close()
        db_status = "connected"
    except Exception:
        db_status = "error"

    return {
        "service": "Dog API Demo",
        "app": "running",
        "database": db_status
    }


if __name__ == "__main__":
    app.run(debug=True)