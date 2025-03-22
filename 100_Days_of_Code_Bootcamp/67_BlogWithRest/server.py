from flask import Flask
from flask import render_template
from flask import request
import database_manager
import json


app = Flask(__name__)
database = database_manager.DatabaseManager()


def get_posts():
    with open("posts/posts_2021.json") as file:
        contents = json.load(file)
        return contents


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html', posts=database.get_all_posts())


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post', methods=["GET"])
def post():

    print(request.args.get("post_id"))
    all_posts = database.get_all_posts()
    new_post = all_posts[int(request.args.get("post_id")) - 1]
    return render_template('post.html', post=new_post)


@app.route('/create-post', methods=["POST", "GET"])
def create_post():

    if request.method == "POST":
        title = request.form['title']
        sub_title = request.form['subtitle']
        text = request.form['text']
        database.create_new_post(post_title=title, post_sub_title=sub_title, post_text=text)
        print(f"{title} {sub_title} {text}")
        return render_template('index.html', posts=database.get_all_posts())

    if request.method == "GET":
        return render_template('make-post.html')


@app.route('/edit-post', methods=["POST", "GET"])
def edit_post():

    if request.method == "POST":
        title = request.form['title']
        sub_title = request.form['subtitle']
        text = request.form['text']
        database.create_new_post(post_title=title, post_sub_title=sub_title, post_text=text)
        print(f"{title} {sub_title} {text}")
        return render_template('index.html', posts=database.get_all_posts())

    if request.method == "GET":
        return render_template('make-post.html')


@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        print(f"{name} {email} {phone} {message}")
        return f"Message sent"

    return render_template('contact.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form['username']
        password = request.form['password']
        return f"<h1>name: {name}password: {password}</h1>"
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
