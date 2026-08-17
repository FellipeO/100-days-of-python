from flask import Flask, render_template
from datetime import date
import requests

app = Flask(__name__)
agify_endpoint = "https://api.agify.io"
genderize_endpoint = "https://api.genderize.io"
blog_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"

@app.route("/")
def home():
    current_year = date.today().year
    return render_template("index.html", year=current_year)

@app.route("/guess/<name>")
def guess(name):
    parameters = {"name":name}
    response = requests.get(agify_endpoint, parameters)
    response.raise_for_status()
    guess_age = response.json()["age"]
    response = requests.get(genderize_endpoint, parameters)
    response.raise_for_status()
    guess_gender = response.json()["gender"]
    return render_template("guess.html", name=name, age=guess_age, gender=guess_gender)

@app.route("/blog")
def get_blog():
    response = requests.get(blog_endpoint)
    response.raise_for_status()
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run()