from flask import Flask, render_template, request
import requests
import os
import dotenv
import smtplib

dotenv.load_dotenv(".env")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form-entry", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        email_content = f"Name: {data["name"]}\nEmail: {data["email"]}\nPhone: {data["phone"]}\nMessage: {data["message"]}"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()

            connection.login(user=EMAIL, password=PASSWORD)

            connection.sendmail(from_addr=EMAIL,
                                to_addrs=EMAIL,
                                msg=f"Subject: New Message!\n\n{email_content}")
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
