from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_word():
    title = "Acceuil | J'apprend Flask"
    return render_template("home.html", title=title)

@app.route('/details')
def details():
    title = "Details | J'apprend Flask"
    return render_template("details.html", title=title)