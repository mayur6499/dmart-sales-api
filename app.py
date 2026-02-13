from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("dmart_sales.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        quantity = float(request.form["quantity"])
        sales = float(request.form["sales"])
        discount = float(request.form["discount"])

        features = np.array([[quantity, sales, discount]])
        prediction = model.predict(features)[0]

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
