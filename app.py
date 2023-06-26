# import flask from the flask library, along with render_template and request
from flask import Flask, render_template, request

# tells python to create an app from the template. we give the Flask class the name of the current Python file
app = Flask(__name__)


#define default route for index
@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "GET":
        return render_template("index.html")

