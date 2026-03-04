from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")


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


if __name__ == "__main__":
    app.run(debug=True)