import json

from flask import Flask
from flask import render_template
import requests


app = Flask(__name__)


def get_posts():
    with open("posts/posts_2021.json") as file:
        contents = json.load(file)
        return contents


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/blog')
def get_blog():
    return render_template('blog.html', posts=get_posts())


if __name__ == "__main__":
    app.run(debug=True)
