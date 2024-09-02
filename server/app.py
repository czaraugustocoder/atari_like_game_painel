from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/labirinto")
def labirinto():
    return render_template("labirinto.html")