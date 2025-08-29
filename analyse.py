# analyze.py
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("sales_data.csv")

# Show data
print("📊 Sales Data:\n", df)

# Convert DateTime to proper datetime
df["DateTime"] = pd.to_datetime(df["DateTime"])

# Total revenue
df["Revenue"] = df["Quantity"] * df["Price"]
print("\n💰 Total Revenue:", df["Revenue"].sum())

# 1. Revenue by Product
product_revenue = df.groupby("ProductName")["Revenue"].sum()
print("\nRevenue by Product:\n", product_revenue)

# Plot revenue by product
product_revenue.plot(kind="bar", title="Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

# 2. Sales by Payment Method
payment_counts = df["PaymentMethod"].value_counts()
print("\nPayment Method Counts:\n", payment_counts)

payment_counts.plot(kind="pie", autopct="%1.1f%%", title="Payment Method Distribution")
plt.ylabel("")
plt.show()

# 3. Daily Sales Trend
daily_sales = df.groupby(df["DateTime"].dt.date)["Revenue"].sum()
print("\nDaily Sales:\n", daily_sales)

daily_sales.plot(kind="line", marker="o", title="Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.show()
