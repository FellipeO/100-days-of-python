from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
posts = response.json()

@app.route("/")
def home():
    return render_template("index.html", posts=posts)

@app.route("/post/<int:index>")
def get_post(index):
    render_post = None
    for post in posts:
        if post["id"] == index:
            render_post = post
    return render_template("post.html", post=render_post)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run()