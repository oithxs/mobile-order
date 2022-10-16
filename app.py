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

@app.route("/confirm", methods=["POST"]) 
def confirm():
    
    salt = int(request.form["salt"])
    ketchup = int(request.form["ketchup"])
    cheese = int(request.form["cheese"])
    butter = int(request.form["butter"])
    sum_num = salt + ketchup + cheese + butter
    sum_price = 200*sum_num
    return render_template("confirm.html", salt = salt, ketchup = ketchup, cheese = cheese, butter = butter, sum_num = sum_num, sum_price = sum_price)

@app.route("/result", methods=["POST"])
def result():
    
    cheese = int(request.form["cheese"])
    butter = int(request.form["butter"])
    salt = int(request.form["salt"])
    ketchup = int(request.form["ketchup"])
    num = cheese + butter + salt + ketchup
    if num <= 0:
        return render_template("result.html", order_id= "1つ以上アイテムを注文してください")
    else:
        item = [cheese,butter,salt,ketchup]

        order_id = spreadsheet.main(item)
        return render_template("result.html", order_id = order_id)