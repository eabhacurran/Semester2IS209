from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

saved_dogs = []

@app.route("/")
def index():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()

    dog_image = data["message"]
    dog_name = "Unknown Dog"

    return render_template(
        "index.html",
        dog_image=dog_image,
        dog_name=dog_name,
        saved_dogs=saved_dogs
    )


@app.route("/save", methods=["POST"])
def save():
    dog_image = request.form.get("dog_image")
    dog_name = request.form.get("dog_name")

    if dog_image:
        saved_dogs.append({
            "name": dog_name,
            "image": dog_image
        })

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)