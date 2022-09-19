from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/confirm")
def confirm():
    return render_template("confirm.html")

@app.route("/result")
def result():
    return render_template("result.html")