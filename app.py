from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = "Acceuil | Anoa'Shopping"
    return render_template("home.html", title=title)

@app.route('/products')
def products():
    title = "Products | Anoa'Shopping"
    return render_template("details.html", title=title)

@app.route('/news')
def news():
    title = "News | Anoa'Shopping"
    return render_template("news.html", title=title)

@app.route('/compte')
def newsletter():
    title = "Newsletter | Anoa'Shopping"
    return render_template("newsletter.html", title=title)

@app.route('/contacts')
def contacts():
    title = "Contacts | Anoa'Shopping"
    return render_template("contacts.html", title=title)