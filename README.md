# Retail Order Data Analysis

## **Skills**
- Kaggle API
- Python
- SQL
- Streamlit

---

## **Domain**
**Data Analytics**

---

## **Problem Statement**
### Objective:
To analyze and optimize sales performance by identifying key trends, top-performing products, and growth opportunities using a dataset of sales transactions.

### Goals:
1. Identify products and categories contributing the most to revenue and profit.
2. Analyze year-over-year (YoY) and month-over-month (MoM) sales trends.
3. Highlight subcategories with the highest profit margins to guide decision-making.

---

## **🌐 API Integration**
### Data Extraction:
**Source:** The data is extracted from Kaggle using the Kaggle API.

Steps:
1. Create a Kaggle profile and generate an API token to access the dataset.
2. Fetch the dataset via Python using the Kaggle API to download raw files (usually in CSV format).
3. Handle pagination if the dataset is large (optional, depending on API limitations).

### Tools/Technologies:
- **Python**: requests, kaggle library
- **Kaggle API**: For retrieving the dataset

### Direct Dataset Download Command:
```bash
!kaggle datasets download ankitbansal06/retail-orders -f orders.csv
```

---

## **🧹 Data Cleaning**
### Process:
- **Handling Missing Values**: Replace missing numerical values with defaults like 0 or drop rows with critical missing fields.
- **Renaming Columns**: Standardize column names for clarity and compatibility with SQL databases (e.g., converting `Order ID` to `order_id`).
- **Trimming Spaces**: Remove trailing spaces from text fields.
- **Deriving New Columns**: Calculate discounts, sale prices, and profits.

### Tools/Technologies:
- **Python**: pandas, numpy

---

## **🗄️ SQL Server Integration**
### Steps:
1. Cleaned data is transferred to SQL Server for efficient querying.
2. Create a database and move the dataframe into SQL.

### Tools/Technologies:
- **SQL Server**: To store and query the data

---

## **📊 Data Analysis with SQL**
### Business Insights through SQL Queries:
1. **Top-Selling Products**: Identify products generating the highest revenue based on sale prices.
2. **Monthly Sales Analysis**: Compare YoY sales to identify growth or decline in certain months.
3. **Product Performance**: Use functions like `GROUP BY`, `HAVING`, `ROW_NUMBER()`, and `CASE WHEN` to categorize and rank products by revenue, profit margin, etc.
4. **Regional Sales Analysis**: Query sales data by region to identify high-performing areas.
5. **Discount Analysis**: Identify products with discounts >20% and calculate their impact on sales.

### Example SQL Queries:
1. **Find top 10 highest revenue-generating products**
2. **Find the top 5 cities with the highest profit margins**
3. **Calculate the total discount given for each category**
4. **Find the average sale price per product category**
5. **Find the region with the highest average sale price**
6. **Find the total profit per category**
7. **Identify the top 3 segments with the highest quantity of orders**
8. **Determine the average discount percentage given per region**
9. **Find the product category with the highest total profit**
10. **Calculate the total revenue generated per year**

### SQL Reference:
- Primary key, foreign key, and join operations.
- Query reference: [w3schools SQL](https://www.w3schools.com/sql/)

---

## **📱 Streamlit**
### Steps:
1. **Set Up Your Environment**
   - Install Streamlit.
2. **Connect to the SQL Database**
   - Dynamically query data from the database.
3. **Display Data Using Streamlit**
   - Use tables and charts to display the data.
4. **Show Insights**
   - Visualize insights dynamically.

### Reference:
[Streamlit Documentation](https://docs.streamlit.io/develop/api-reference)



