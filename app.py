from crypt import methods
from flask import Flask, render_template, request
import spreadsheet

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

@app.route("/result", methods=["POST"])
def result():
    
    cheese = request.form["cheese"]
    butter = request.form["butter"]
    salt = request.form["salt"]
    ketchup = request.form["ketchup"]
    item = [cheese,butter,salt,ketchup]
    
    order_id = spreadsheet.main(item)
    return render_template("result.html", order_id = order_id)