import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
customer_df = pd.read_csv("Cleaned_CustomerTable.csv")
market_trend_df = pd.read_csv("Cleaned_MarketTrendTable.csv")
product_detail_df = pd.read_csv("Cleaned_ProductDetailTable.csv")
product_group_df = pd.read_csv("Cleaned_ProductGroupTable.csv")
sale_df = pd.read_csv("Cleaned_SaleTable.csv")
website_access_df = pd.read_csv("Cleaned_WebsiteAccessCategoryTable.csv")

# 1. Distribution of Product Prices
# This histogram visualizes the distribution of product prices.
plt.figure(figsize=(10, 6))
plt.hist(product_detail_df['Price'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Product Prices')
plt.xlabel('Price')
plt.ylabel('Number of Products')
plt.show()


# 2. Revenue by Payment Method
# This pie chart illustrates the distribution of total revenue by payment method.
plt.figure(figsize=(10, 6))
sale_df.groupby('PaymentMethod')['FinalPrice'].sum().plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'orange', 'pink'])
plt.title('Revenue by Payment Method')
plt.ylabel('')  # Remove y-label to enhance the appearance of the pie chart
plt.show()




plt.figure(figsize=(10, 8))
correlation_matrix = product_detail_df[['Price', 'StockQuantity', 'Rating']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Product Features')
plt.show()


plt.figure(figsize=(12, 6))
website_access_counts = website_access_df['PageVisited'].value_counts()
website_access_counts.plot(kind='bar', color='teal')
plt.title('Number of Website Accesses by Page')
plt.xlabel('Page Visited')
plt.ylabel('Number of Accesses')
plt.show()



