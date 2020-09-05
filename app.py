from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = "Acceuil | Anoa"
    return render_template("home.html", title=title)

@app.route('/products')
def products():
    title = "Products | Anoa"
    return render_template("details.html", title=title)

@app.route('/news')
def news():
    title = "News | Anoa"
    return render_template("news.html", title=title)

@app.route('/newsletter')
def newsletter():
    title = "Newsletter | Anoa"
    return render_template("newsletter.html", title=title)

@app.route('/contacts')
def contacts():
    title = "Contacts | Anoa"
    return render_template("contacts.html", title=title)