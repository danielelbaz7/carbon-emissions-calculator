from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='http://localhost:3000')

@app.route("/")
def index():
    return "Hello World!"

@app.route("/about")
def about():
    return render_template('about.html')