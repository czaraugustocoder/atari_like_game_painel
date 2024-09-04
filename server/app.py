from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']
        return "Your name is "+name
    return render_template("register.html")

@app.route("/labirinto")
def labirinto():
    return render_template("labirinto.html")