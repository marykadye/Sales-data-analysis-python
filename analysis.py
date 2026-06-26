import pandas as pd

# Load dataset
data = pd.read_csv("sales_data.csv")

# Create Total column
data["Total"] = data["Quantity"] * data["Price"]

# Show data
print("Sales Data:")
print(data)

# Total sales
total_sales = data["Total"].sum()
print("\nTotal Sales:", total_sales)

# Best selling product
best_product = data.groupby("Product")["Total"].sum().idxmax()
print("Best Selling Product:", best_product)

# Sales by product
print("\nSales by Product:")
print(data.groupby("Product")["Total"].sum())
