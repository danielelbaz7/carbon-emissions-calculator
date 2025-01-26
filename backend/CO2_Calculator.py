from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import API_Management

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)