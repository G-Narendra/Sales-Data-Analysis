import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from statsmodels.tsa.arima.model import ARIMA

# Load the data
df = pd.read_csv('Sales Data.csv')

# Inspect the data
print(df.head())
print(df.info())

# Data Cleaning
# Remove rows with NaN values
df = df.dropna()

# Convert columns to appropriate data types
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'])
df['Price Each'] = pd.to_numeric(df['Price Each'])

# Feature Engineering
# Extract month from 'Order Date'
df['Month'] = df['Order Date'].dt.month

# Extract hour from 'Order Date'
df['Hour'] = df['Order Date'].dt.hour

# Extract city from 'Purchase Address'
df['City'] = df['Purchase Address'].apply(lambda x: x.split(',')[1].strip())

# Calculate Sales
df['Sales'] = df['Quantity Ordered'] * df['Price Each']

# Exploratory Data Analysis (EDA)
# Monthly Sales
monthly_sales = df.groupby('Month')['Sales'].sum()
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='bar')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()

# Sales by City
city_sales = df.groupby('City')['Sales'].sum()
plt.figure(figsize=(10, 6))
city_sales.plot(kind='bar')
plt.title('Sales by City')
plt.xlabel('City')
plt.ylabel('Sales')
plt.show()

# Sales by Hour
hourly_sales = df.groupby('Hour')['Sales'].sum()
plt.figure(figsize=(10, 6))
hourly_sales.plot(kind='bar')
plt.title('Sales by Hour')
plt.xlabel('Hour')
plt.ylabel('Sales')
plt.show()

# Sales Forecasting
# Resample the data by month for forecasting
df.set_index('Order Date', inplace=True)
monthly_sales_ts = df['Sales'].resample('M').sum()

# Plot the time series
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales_ts)
plt.title('Monthly Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# Use ARIMA for forecasting
model = ARIMA(monthly_sales_ts, order=(1, 1, 1)) # (p,d,q) parameters
fit = model.fit()
forecast = fit.forecast(steps=12)

# Plot the forecast
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales_ts, label='Observed')
plt.plot(forecast, label='Forecast', linestyle='--')
plt.title('Sales Forecast')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.show()

# Print the forecasted values
print(forecast)

# Save the forecasted values to a CSV file
forecast.to_csv('sales_forecast.csv', header=True)
