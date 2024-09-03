from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def register():
    return render_template("register.html")

@app.route("/labirinto")
def labirinto():
    return render_template("labirinto.html")