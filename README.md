# DMart Sales Analysis & Profit Prediction

## Project Overview

This project analyzes DMart retail sales data and builds a machine learning model to predict profit based on sales, quantity, and discount.
It also includes a Flask web application where users can enter values and get predicted profit.

## Business Problem
DMart need to Understand which products and cities generate the most profit
Control discounts to avoid losses

## Dataset
* ### Rows: 5,000
* ### Columns: 10
1. Column	Description
2. Order_ID	Unique order
3. Order_Date	Date of sale
4. Store_ID	Store code
5. City	City
6. Category	Product category
7. Product_Name	Item
8. Quantity	Units sold
9. Sales	Total sales
10. Discount	Discount given
11. Profit	Net profit

## Technology Used:
1. Python
2. Pandas, NumPy
3. Scikit-learn
4. Flask
5. HTML, CSS
6. Render (Deployment)

## Project Workflow:
1.  Data Cleaning & Feature Engineering
2.  Exploratory Data Analysis
3.  Machine Learning Model (Random Forest)
4.  Model Saving (joblib)
5.  Flask Web App
6.  Deployment on Render

## Machine Learning Model:
* Algorithm: Random Forest Regressor
* Features: Quantity, Sales, Discount
* Target: Profit

## Web App
1. Enter Quantity, Sales, Discount
2. Click Predict
3. Get Profit instantly

## Key Insights

* High discounts reduce profit
* Electronics & groceries give higher margins
* Mumbai & Pune are top profit cities

## Github Link:

* https://github.com/mayur6499/dmart-sales-api

## Render Link:
* https://dmart-sales-api.onrender.com