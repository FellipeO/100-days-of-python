from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>")

@app.route("/<number>")
def guessed_number(number):
    answer = random.randint(0,9)
    if int(number) < answer:
        return ("<h1 style='color: red;'>Too low, try again!</h1>"
                "<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>")

    elif int(number) > answer:
        return ("<h1 style='color: red;'>Too high, try again!</h1>"
                "<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>")

    else:
        return ("<h1 style='color: green;'>That's correct!</h1>"
                "<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>")

if __name__ == "__main__":
    app.run()

# def make_bold(function):
#     def wrapper():
#         return f"<b>{function()}</b>"
#     return wrapper
#
# def make_emphasis(function):
#     def wrapper():
#         return f"<em>{function()}</em>"
#     return wrapper
#
# def make_underline(function):
#     def wrapper():
#         return f"<u>{function()}</u>"
#     return wrapper
# @app.route('/')
# def hello_world():
#     return "Hello World"
#
# @app.route('/bye')
# @make_bold
# @make_emphasis
# @make_underline
# def bye():
#     return "Bye"
#
# if __name__ == "__main__":
#     app.run()
