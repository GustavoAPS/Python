from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('to_do_list.html')
