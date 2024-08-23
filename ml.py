import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Đọc dữ liệu từ các file CSV
customer_df = pd.read_csv('CustomerTable.csv')
market_trend_df = pd.read_csv('MarketTrendTable.csv')
product_detail_df = pd.read_csv('ProductDetailTable.csv')
product_group_df = pd.read_csv('ProductGroupTable.csv')
sale_df = pd.read_csv('SaleTable.csv')
website_access_df = pd.read_csv('WebsiteAccessCategoryTable.csv')

# Xem xét dữ liệu và xử lý thiếu sót
print(product_detail_df.head())
product_detail_df.dropna(subset=['Price', 'Rating', 'StockQuantity'], inplace=True)

# Chọn đặc trưng và biến mục tiêu
X = product_detail_df[['Rating', 'StockQuantity']]
y = product_detail_df['Price']

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)



# Khởi tạo mô hình Linear Regression
model = LinearRegression()

# Huấn luyện mô hình trên tập huấn luyện
model.fit(X_train, y_train)


# Dự đoán giá trị trên tập kiểm tra
y_pred = model.predict(X_test)

# Tính toán các chỉ số đánh giá mô hình
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')


plt.figure(figsize=(10, 6))
plt.scatter(X_test['Rating'], y_test, color='blue', label='Actual Prices')
plt.scatter(X_test['Rating'], y_pred, color='red', label='Predicted Prices')
plt.xlabel('Rating')
plt.ylabel('Price')
plt.title('Actual vs Predicted Prices by Rating')
plt.legend()
plt.show()




fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot actual data points
ax.scatter(X_test['Rating'], X_test['StockQuantity'], y_test, color='blue', label='Actual Prices')

# Plot predicted data points
ax.scatter(X_test['Rating'], X_test['StockQuantity'], y_pred, color='red', label='Predicted Prices')

ax.set_xlabel('Rating')
ax.set_ylabel('Stock Quantity')
ax.set_zlabel('Price')
plt.title('Actual vs Predicted Prices (3D)')
plt.legend()
plt.show()


residuals = y_test - y_pred

plt.figure(figsize=(10, 6))
sns.histplot(residuals, kde=True, color='purple')
plt.title('Distribution of Residuals')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.show()
