# **📊 Sales Data Analysis & Forecasting**

*A comprehensive analysis and forecasting of sales data using machine learning.*

## 🌟 **Overview**
This project analyzes and forecasts sales using a dataset containing **185,950 transactions**. It explores **sales trends, customer behavior, and forecasting future sales** using statistical models.

## 📊 **Dataset Overview**
The dataset contains **various sales attributes**, including:
- **Order ID** – Unique identifier for each order.
- **Product** – Name of the product sold.
- **Quantity Ordered** – Number of items per order.
- **Price Each** – Unit price of the product.
- **Order Date** – Date and time of the transaction.
- **Purchase Address** – Location of the purchase.
- **Month & Hour** – Extracted from the order date.
- **Sales** – Computed as `Quantity Ordered × Price Each`.
- **City** – Extracted from the purchase address.

## 🎯 **Project Workflow**
✅ **Data Cleaning** – Handling missing values, type conversions, and duplicate removal.  
✅ **Feature Engineering** – Extracting meaningful features like month, hour, and city.  
✅ **Exploratory Data Analysis (EDA)** – Visualizing sales trends across time, location, and products.  
✅ **Sales Forecasting** – Using the **ARIMA** model to predict future sales.  

## 🛠️ **Tech Stack**
🔹 **Programming Language:** Python  
🔹 **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Statsmodels (ARIMA)  
🔹 **Model Type:** Time Series Forecasting (ARIMA)  
🔹 **Development Environment:** Jupyter Notebook / Python Script  

## 📂 **Project Structure**
```
Sales-Data-Analysis/
├── sales_analysis.py          # Python script with analysis & forecasting
├── Sales Data.csv             # Dataset used for training/testing
├── sales_forecast.csv         # Forecasted sales data
├── sales_data_intro.txt       # Dataset overview
├── sales_data_report.txt      # Detailed project report
├── Visualizations/            # Sales insights and plots
│   ├── monthly sales.png
│   ├── sales by city.png
│   ├── sales by hour.png
│   ├── sales forecast.png
├── requirements.txt           # Dependencies for the project
├── README.md                  # Project documentation
```

## 🚀 **Installation & Setup**
1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/G-Narendra/Sales-Data-Analysis.git
cd Sales-Data-Analysis
```
2️⃣ **Install Dependencies**  
```sh
pip install -r requirements.txt
```
3️⃣ **Run the Analysis**  
```sh
python sales_analysis.py
```

## 📈 **Key Insights & Forecasting**
### **Exploratory Data Analysis (EDA)**
- **Monthly Sales Trends** – Identifies peak sales periods.
- **Sales by City** – Highlights the most profitable locations.
- **Sales by Hour** – Finds optimal sales hours for targeted marketing.

### **Sales Forecasting Results (ARIMA Model)**
| Month        | Forecasted Sales ($) |
|-------------|--------------------|
| February 2020 | 2,908,670 |
| March 2020    | 336,821 |
| April 2020    | 2,617,652 |
| May 2020      | 594,909 |
| June 2020     | 2,388,767 |
| July 2020     | 797,894 |
| August 2020   | 2,208,752 |
| September 2020 | 957,540 |
| October 2020  | 2,067,170 |
| November 2020 | 1,083,101 |
| December 2020 | 1,955,817 |
| January 2021  | 1,181,854 |

## 📉 **Conclusion**
This project provides a **data-driven approach** to understanding sales trends and forecasting future performance. The **ARIMA model** effectively predicts sales, offering valuable insights for **business decision-making and strategy planning**.

## 🤝 **Contributions**
💡 Open to improvements! Feel free to:
1. Fork the repo  
2. Create a new branch (`feature-branch`)  
3. Make changes & submit a PR  



## 📩 **Connect with Me**
📧 **Email:** [narendragandikota2540@gmail.com](mailto:narendragandikota2540@gmail.com)  
🌐 **Portfolio:** [G-Narendra Portfolio](https://g-narendra-portfolio.vercel.app/)  
💼 **LinkedIn:** [G-Narendra](https://linkedin.com/in/g-narendra/)  
👨‍💻 **GitHub:** [G-Narendra](https://github.com/G-Narendra)  

⭐ **If you find this project useful, drop a star!** 🚀

