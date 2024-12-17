import pandas as pd
import sqlalchemy as sa
from sqlalchemy import create_engine, text
import streamlit as st

# MySQL Connection
sql_con = sa.engine.URL.create(
    drivername='mysql+pymysql',
    username="root",
    password="mysql4505",
    host="127.0.0.1",
    database="retail_orders"
)

sql_engine = create_engine(sql_con)

# Streamlit Sidebar with questions
st.sidebar.title("SQL Query Dashboard")
question = st.sidebar.radio(
    "Select a question to view:",
    [
        "1. Top 10 Highest Revenue Generating Products",
        "2. Top 5 Cities with Highest Profit Margins",
        "3. Total Discount Given for Each Category",
        "4. Average Sale Price per Product Category",
        "5. Region with Highest Average Sale Price",
        "6. Total Profit per Category",
        "7. Top 3 Segments with Highest Quantity of Orders",
        "8. Average Discount Percentage per Region",
        "9. Product Category with Highest Total Profit",
        "10. Total Revenue Generated per Year",
        "11. List All Orders with Product Information",
        "12. Total Revenue from Each Product",
        "13. All Products Ordered by Henderson",
        "14. Most Expensive Product Ordered",
        "15. Orders with Product Details and Total Price",
        "16. All Orders with Product Information (LEFT JOIN)",
        "17. Most Expensive Product Ordered (LEFT JOIN)",
        "18. Products with Profit Greater Than 1000 (RIGHT JOIN)",
        "19. All Orders from 2023 and 2024 (UNION)",
        "20. Products in Orders from South Region (CROSS JOIN)"
    ]
)

# Function to execute queries
def execute_query(query):
    df = pd.read_sql_query(query, sql_engine)
    return df

# Display results based on user selection
if question == "1. Top 10 Highest Revenue Generating Products":
    query = '''SELECT 
               Product_Id, 
               Category, 
               Profit  
               FROM retail_orders.retail
               ORDER BY Profit DESC
               LIMIT 10;'''
    
    st.write("SQL Query:")
    st.code(query, language='sql')
    result = execute_query(query)
    st.write("Result:")
    st.dataframe(result)

elif question == "2. Top 5 Cities with Highest Profit Margins":
    query = '''SELECT City, Profit 
               FROM retail_orders.retail 
               ORDER BY Profit DESC 
               LIMIT 5;'''
    
    st.write("SQL Query:")
    st.code(query, language='sql')
    result = execute_query(query)
    st.write("Result:")
    st.dataframe(result)

elif question == "3. Total Discount Given for Each Category":
    query = '''SELECT DISTINCT
               Category, SUM(Discount) AS Total_Discount 
               FROM retail_orders.retail 
               GROUP BY Category;'''
    
    st.write("SQL Query:")
    st.code(query, language='sql')
    result = execute_query(query)
    st.write("Result:")
    st.dataframe(result)

elif question == "4. Average Sale Price per Product Category":
    query = '''SELECT DISTINCT
               Category, AVG(Sales_Price) AS Average_Sale_Price
               FROM retail_orders.retail 
               GROUP BY Category;'''
    
    st.write("SQL Query:")
    st.code(query, language='sql')
    result = execute_query(query)
    st.write("Result:")
    st.dataframe(result)

elif question == "5. Region with Highest Average Sale Price":
    query = '''SELECT DISTINCT
               Region, AVG(Sales_Price) AS Average_Sale_Price
               FROM retail_orders.retail 
               GROUP BY Region 
               ORDER BY Average_Sale_Price DESC;'''
    
    st.write("SQL Query:")
    st.code(query, language='sql')
    result = execute_query(query)
    st.write("Result:")
    st.dataframe(result)

elif question == "6. Total Profit per Category":
    query = '''SELECT DISTINCT
               Category, SUM(Profit) AS Total_Profit
               FROM retail_orders.retail 
               GROUP BY Category;'''
    
    st.write("SQL Query:")
    st.code(query, language='sql')
    result = execute_query(query)
    st.write("Result:")
    st.dataframe(result)

elif question == "7. Top 3 Segments with Highest Quantity of Orders":
    query = '''SELECT DISTINCT
               Segment, MAX(Quantity) AS Highest_Quantity
               FROM retail_orders.retail 
               GROUP BY Segment 
               ORDER BY Highest_Quantity DESC 
               LIMIT 3;'''
    
    st.write("SQL Query:")
    st.code(query, language='sql')
    result = execute_query(query)
    st.write("Result:")
    st.dataframe(result)

elif question == "8. Average Discount Percentage per Region":
    query = '''SELECT DISTINCT
               Region, AVG(Discount_Percent) AS Avg_Discount_Percentage
               FROM retail_orders.retail 
               GROUP BY Region;'''
    
    st.write("SQL Query:")
    st.code(query, language='sql')
    result = execute_query(query)
    st.write("Result:")
    st.dataframe(result)

elif question == "9. Product Category with Highest Total Profit":
    query = '''SELECT DISTINCT
               Sub_Category AS Product, MAX(Profit) AS Total_Profit
               FROM retail_orders.retail 
               GROUP BY Product 
               ORDER BY Total_Profit DESC 
               LIMIT 1;'''
    
    st.write("SQL Query:")
    st.code(query, language='sql')
    result = execute_query(query)
    st.write("Result:")
    st.dataframe(result)

elif question == "10. Total Revenue Generated per Year":
    query = '''SELECT DISTINCT
               YEAR(Order_Date) AS Year, SUM(Profit) AS Total_Revenue
               FROM retail_orders.retail 
               GROUP BY YEAR(Order_Date);'''
    
    st.write("SQL Query:")
    st.code(query, language='sql')
    result = execute_query(query)
    st.write("Result:")
    st.dataframe(result)

elif question == "11. List All Orders with Product Information":
    query = '''SELECT o.Order_Id, o.Order_Date, o.Ship_Mode, o.Segment, o.Country,
                      p.Product_Id, p.Category, p.Sales_Price, p.Quantity
               FROM retail_orders.Orders o 
               INNER JOIN retail_orders.Product p 
               ON o.Order_Id = p.Order_Id;'''
    
    st.write("SQL Query:")
    st.code(query, language='sql')
    result = execute_query(query)
    st.write("Result:")
    st.dataframe(result)

elif question == "12. Total Revenue from Each Product":
    query = '''SELECT 
               P.Product_Entry_Id, P.Product_Id, SUM(Sales_Price * Quantity) AS total_revenue
               FROM retail_orders.Product p 
               INNER JOIN retail_orders.Orders o 
               ON o.Order_Id = p.Order_Id
               GROUP BY p.Product_Entry_Id, p.Product_Id;'''
    
    st.write("SQL Query:")
    st.code(query, language='sql')
    result = execute_query(query)
    st.write("Result:")
    st.dataframe(result)

elif question == "13. All Products Ordered by Henderson":
    query = '''SELECT  
               P.Product_Id,
               P.Category,
               P.Sales_Price,
               o.City
               FROM retail_orders.Orders o 
               INNER JOIN retail_orders.Product P
               ON o.Order_Id = p.Order_Id
               WHERE o.City = 'Henderson';'''
    
    st.write("SQL Query:")
    st.code(query, language='sql')
    result = execute_query(query)
    st.write("Result:")
    st.dataframe(result)

elif question == "14. Most Expensive Product Ordered":
    query = '''SELECT  
               P.Product_Id,
               P.Sales_Price,
               o.Order_Date
               FROM retail_orders.Orders o 
               INNER JOIN retail_orders.Product P
               ON o.Order_Id = p.Order_Id
               ORDER BY P.Sales_Price DESC
               LIMIT 1;'''
    
    st.write("SQL Query:")
    st.code(query, language='sql')
    result = execute_query(query)
    st.write("Result:")
    st.dataframe(result)

elif question == "15. Orders with Product Details and Total Price":
    query = '''SELECT  
               o.Order_Id,
               o.Order_Date,
               o.Ship_Mode,
               p.Sales_Price,
               p.Quantity,
               (p.Sales_Price * p.Quantity) AS total_price
               FROM retail_orders.Orders o 
               INNER JOIN retail_orders.Product P
               ON o.Order_Id = p.Order_Id;'''
    
    st.write("SQL Query:")
    st.code(query, language='sql')
    result = execute_query(query)
    st.write("Result:")
    st.dataframe(result)

elif question == "16. All Orders with Product Information (Using LEFT JOIN)":
    query = '''SELECT  
               o.Order_Id, 
               o.Order_Date, 
               o.Ship_Mode, 
               o.Segment, 
               o.Country, 
               p.Product_Id, 
               p.Category, 
               p.Sales_Price, 
               p.Quantity
               FROM retail_orders.Orders o 
               LEFT JOIN retail_orders.Product P
               ON o.Order_Id = p.Order_Id;'''
    
    st.write("SQL Query:")
    st.code(query, language='sql')
    result = execute_query(query)
    st.write("Result:")
    st.dataframe(result)

elif question == "17. Most Expensive Product Ordered (Using LEFT JOIN)":
    query = '''SELECT  
               p.Product_Id, 
               p.Sales_Price,
               o.Order_Date 
               FROM retail_orders.Orders o 
               LEFT JOIN retail_orders.Product P
               ON o.Order_Id = p.Order_Id
               ORDER BY p.Sales_Price DESC 
               LIMIT 1;'''
    
    st.write("SQL Query:")
    st.code(query, language='sql')
    result = execute_query(query)
    st.write("Result:")
    st.dataframe(result)

elif question == "18. Products with Profit Greater Than 1000 (Using RIGHT JOIN)":
    query = '''SELECT  
               p.Product_Id, 
               p.Sales_Price
               FROM retail_orders.Orders o 
               RIGHT JOIN retail_orders.Product P
               ON o.Order_Id = p.Order_Id
               WHERE p.Profit > 1000;'''
    
    st.write("SQL Query:")
    st.code(query, language='sql')
    result = execute_query(query)
    st.write("Result:")
    st.dataframe(result)

elif question == "19. All Orders from 2023 and 2024 (UNION)":
    query = '''SELECT Order_Id, Order_Date 
               FROM retail_orders.Orders 
               WHERE YEAR(Order_Date) = 2023
               UNION 
               SELECT Order_Id, Order_Date 
               FROM retail_orders.Orders 
               WHERE YEAR(Order_Date) = 2024;'''
    
    st.write("SQL Query:")
    st.code(query, language='sql')
    result = execute_query(query)
    st.write("Result:")
    st.dataframe(result)

elif question == "20. Products in Orders from South Region (CROSS JOIN)":
    query = '''SELECT  
               P.Product_Id,
               P.Category,
               P.Sales_Price
               FROM retail_orders.Orders o 
               CROSS JOIN retail_orders.Product P
               WHERE o.Region = "South" AND o.Order_Id = p.Order_Id;'''
    
    st.write("SQL Query:")
    st.code(query, language='sql')
    result = execute_query(query)
    st.write("Result:")
    st.dataframe(result)


