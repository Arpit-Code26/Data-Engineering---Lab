"""
Mini Project: Retail Sales Data Lifecycle
Covers Capture → Storage → Processing → Analysis → Visualization
"""

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. DATA CAPTURE & STORAGE
# -------------------------------
# Data captured from transactions and stored in sales.csv
print("Loading data from sales.csv...")
df = pd.read_csv("sales.csv")

# -------------------------------
# 2. DATA PROCESSING / CLEANING
# -------------------------------
print("\n--- Data Cleaning ---")
print("Checking for missing values:")
print(df.isnull().sum())

# Handle missing values if any (fill with 0 for Quantity, 0 for Price)
df["Quantity"].fillna(0, inplace=True)
df["Price"].fillna(0, inplace=True)

# Calculate Total amount for each transaction
df["Total"] = df["Quantity"] * df["Price"]

print("Data after cleaning and adding Total column:")
print(df.head())

# -------------------------------
# 3. DATA ANALYSIS
# -------------------------------
print("\n--- Data Analysis ---")
total_sales = df["Total"].sum()
print(f"Total Sales Revenue: ₹{total_sales}")

best_product = df.groupby("Product")["Total"].sum().idxmax()
print(f"Best-Selling Product: {best_product}")

customer_spending = df.groupby("Customer")["Total"].sum().sort_values(ascending=False)
print("\nCustomer Spending:")
print(customer_spending)

# -------------------------------
# 4. DATA VISUALIZATION
# -------------------------------
print("\n--- Generating Visualizations ---")

# Product-wise sales bar chart
product_sales = df.groupby("Product")["Total"].sum()
product_sales.plot(kind="bar", title="Sales by Product", ylabel="Revenue (₹)", xlabel="Product", color="skyblue")
plt.show()

# Customer spending pie chart
customer_spending.plot(kind="pie", autopct='%1.1f%%', title="Customer Contribution to Revenue")
plt.ylabel("")  # Hide y-label for better look
plt.show()

print("\nPipeline Completed Successfully ✅")
