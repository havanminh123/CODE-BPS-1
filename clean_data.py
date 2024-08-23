import pandas as pd

# Reading CSV files into DataFrames
customer_df = pd.read_csv("CustomerTable.csv")
market_trend_df = pd.read_csv("MarketTrendTable.csv")
product_detail_df = pd.read_csv("ProductDetailTable.csv")
product_group_df = pd.read_csv("ProductGroupTable.csv")
sale_df = pd.read_csv("SaleTable.csv")
website_access_df = pd.read_csv("WebsiteAccessCategoryTable.csv")

# Checking basic information of the data (columns, null values, etc.)
print(customer_df.info())
print(market_trend_df.info())
print(product_detail_df.info())
print(product_group_df.info())
print(sale_df.info())
print(website_access_df.info())

# Handling missing values
# Check for missing values in each column
print(customer_df.isnull().sum())
print(market_trend_df.isnull().sum())

# Drop rows with more than 3 missing values
customer_df = customer_df.dropna(thresh=3)

# Fill missing values in the 'Price' column with the mean price
product_detail_df['Price'].fillna(product_detail_df['Price'].mean(), inplace=True)

# Handling duplicate data
# Check for duplicate rows
print(customer_df.duplicated().sum())

# Remove duplicate rows
customer_df.drop_duplicates(inplace=True)

# Converting data types
# Convert 'RegistrationDate' column to datetime format
customer_df['RegistrationDate'] = pd.to_datetime(customer_df['RegistrationDate'])

# Convert 'Price' column to numeric format
product_detail_df['Price'] = pd.to_numeric(product_detail_df['Price'], errors='coerce')

# Handling invalid data
# Filter out rows with negative values in the 'Price' column
product_detail_df = product_detail_df[product_detail_df['Price'] >= 0]

# Clean up phone numbers by removing non-numeric characters
customer_df['PhoneNumber'] = customer_df['PhoneNumber'].str.replace('[^0-9]', '', regex=True)

# Creating new columns or recalculating existing ones
# Calculate the final sale price after applying the discount
sale_df['FinalPrice'] = sale_df['TotalPrice'] - sale_df['Discount']

# Encoding categorical data
# Convert boolean values to integers (True/False -> 1/0)
product_group_df['IsActive'] = product_group_df['IsActive'].astype(int)

# Saving cleaned and processed data back to CSV files
customer_df.to_csv("Cleaned_CustomerTable.csv", index=False)
market_trend_df.to_csv("Cleaned_MarketTrendTable.csv", index=False)
product_detail_df.to_csv("Cleaned_ProductDetailTable.csv", index=False)
product_group_df.to_csv("Cleaned_ProductGroupTable.csv", index=False)
sale_df.to_csv("Cleaned_SaleTable.csv", index=False)
website_access_df.to_csv("Cleaned_WebsiteAccessCategoryTable.csv", index=False)


