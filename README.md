📊 Vendor Sales Performance – End-to-End Data Analysis Project

Author: Anand Pathak

📌 Project Overview

This project focuses on analyzing vendor-level sales performance using an end-to-end data analytics approach. The objective is to understand purchasing behavior, inventory movement, pricing strategies, and profitability trends across vendors.

The analysis was carried out using Python and SQLite for data processing and querying, while Power BI was used to build interactive dashboards and extract actionable business insights.

🛠️ Tools & Technologies Used

Python – Data cleaning, transformation, and analysis

SQLite – Querying and managing relational data

Power BI – Data visualization and dashboard creation

Pandas, NumPy – Statistical analysis and feature engineering

📂 Dataset

The dataset contains vendor-wise purchase, sales, pricing, inventory, and logistics information.

🔗 Dataset Link (Google Drive):
👉 https://drive.google.com/drive/folders/1oRjBD8TWxLk90Mio-lKtIOCWIqPfMcgW?usp=drive_link

🔎 Exploratory Data Analysis (EDA)

During the EDA phase, all relevant tables were reviewed and consolidated to identify key variables and relationships. This step helped in understanding data distributions, detecting anomalies, and validating data quality before proceeding to advanced analysis.

The analysis focused on:

Sales and purchase quantities

Pricing and cost structures

Profitability and margins

Inventory movement and stock turnover

📈 Correlation Analysis – Key Insights
1. Purchase Price vs Sales & Profit

Purchase price shows a very weak correlation with both total sales dollars (–0.012) and gross profit (–0.016).
This indicates that changes in purchase price do not have a significant direct impact on overall revenue or profitability.

2. Purchase Quantity vs Sales Quantity

There is a very strong positive correlation (0.999) between total purchase quantity and total sales quantity.
This confirms efficient inventory movement, where most of the purchased stock is successfully sold.

3. Profit Margin vs Sales Price

A moderate negative correlation (–0.179) exists between profit margin and total sales price.
As selling prices increase, profit margins tend to decline, possibly due to competitive pricing pressures or higher associated costs.

4. Stock Turnover vs Profitability

Stock turnover shows weak negative correlations with gross profit (–0.038) and profit margin (–0.055).
This suggests that faster inventory turnover does not necessarily lead to higher profitability and may be driven by lower-margin or discounted sales.

📊 Summary Statistics – Key Findings
Negative and Zero Values

Gross Profit: A minimum value of –52,002.78 indicates that certain products or transactions resulted in losses, likely due to high procurement costs, aggressive discounting, or selling below cost.

Profit Margin: The presence of negative infinity (–∞) values highlights cases where revenue was zero or lower than costs, indicating unprofitable sales.

Sales Quantity and Sales Amount: Minimum values of 0 suggest that some items were purchased but never sold, pointing to slow-moving or obsolete inventory.

Outliers and High Variability

Purchase Price & Selling Price: Maximum values (5,681.81 and 7,499.99) are significantly higher than their averages (24.39 and 35.64), indicating the presence of premium or high-value products.

Freight Cost: A wide range from 0.09 to 257,032.07 reflects large variability in logistics expenses, possibly due to bulk shipments, long-distance transportation, or inefficiencies.

Stock Turnover: Values ranging from 0 to 274.5 show that while some products sell rapidly, others remain in inventory for extended periods. Turnover values greater than 1 suggest sales fulfilled from previously held stock.

🧠 Business Insights
Bulk Purchasing Advantage

Vendors placing large-volume orders achieve the lowest unit purchase price (~$10.78 per unit).
There is an approximate 72% reduction in per-unit cost when comparing bulk purchases to small orders.
This highlights the effectiveness of bulk pricing strategies in driving higher overall sales and improving cost efficiency when inventory is managed properly.

Sales Volume vs Profitability

Vendors with lower sales volumes tend to have higher profit margins (40–43%).

Vendors with higher sales volumes operate at lower margins (around 31%).

This indicates that higher sales do not always translate to higher per-unit profitability.

Recommendations:

High-sales vendors can improve profitability by optimizing pricing, reducing costs, or offering bundled deals instead of relying solely on volume.

Low-sales vendors, while profitable per unit, should focus on increasing sales volume through better marketing, competitive pricing, or expanded distribution.

📌 Conclusion
This project demonstrates how combining Python, SQLite, and Power BI can deliver meaningful insights into vendor performance, pricing strategies, and inventory efficiency. The findings can help businesses optimize procurement, improve profitability, and make data-driven decisions.
