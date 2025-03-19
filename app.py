from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Function to insert data into SQL
def insert_data(date, product_name, quantity, price):
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sales_data (date, product_name, quantity, price) VALUES (?, ?, ?, ?)",
                   (date, product_name, quantity, price))
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    date = request.form["date"]
    product_name = request.form["product_name"]
    quantity = int(request.form["quantity"])
    price = float(request.form["price"])
    insert_data(date, product_name, quantity, price)
    return "Data saved successfully!"

if __name__ == "__main__":
    app.run(debug=True)
