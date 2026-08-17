from flask import Flask, render_template
from post import Post
import requests

post_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
post_response.raise_for_status()
posts = post_response.json()
posts_list = []
for post in posts:
    item = Post(post["id"], post["title"], post["subtitle"], post["body"])
    posts_list.append(item)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=posts_list)

@app.route('/post/<int:index>')
def get_post(index):
    render_post = None
    for thing in posts_list:
        if thing.id == index:
            render_post = thing
    return render_template("post.html", post=render_post)



if __name__ == "__main__":
    app.run(debug=True)
