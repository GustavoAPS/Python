from flask import Flask, jsonify, render_template, request
import database_manager
import json


dataManager = database_manager.DatabaseManager()
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    # print(dataManager.get_random_cafe())
    return json.dumps(dataManager.get_random_cafe())


@app.route("/all")
def get_all_cafes():
    # print(dataManager.get_random_cafe())
    return dataManager.get_all_cafes()


#/search?loc=Peckham   --THis is an example of what should be done
@app.route("/search/<string:loc>")
def search_for_cafe(loc):
    return "nothing"


if __name__ == '__main__':
    app.run(debug=True)
