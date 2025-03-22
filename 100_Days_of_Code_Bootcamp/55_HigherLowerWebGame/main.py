from flask import Flask
from random import randint

correct_number = randint(0, 9)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1>Search the doggo between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route("/<int:guess>")
def try_guess(guess):
    if guess == correct_number:
        return '<h1>YOU FOUND THE DOGGOOO</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif guess < correct_number:
        return '<h1>The doggo is Higher</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h1>The doggo is </h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
