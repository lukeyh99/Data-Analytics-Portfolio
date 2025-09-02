SELECT * FROM orders;
-- Count total rows in Orders
SELECT COUNT(*) AS Total_Orders FROM orders;

-- Distinct customers
SELECT COUNT(DISTINCT `Customer ID`) AS Total_Customers FROM orders;

-- Distinct products
SELECT COUNT(DISTINCT `Product ID`) AS Total_Products FROM orders;
-- Total Sales and Profit
SELECT 
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    ROUND(SUM(Profit)/SUM(Sales)*100, 2) AS Profit_Margin_Percent
FROM orders;

-- Average Order Value (AOV)
SELECT AVG(Sales) AS Avg_Order_Value FROM orders;


-- Monthly Sales Trend
SELECT DATE_FORMAT(`Order Date`, '%Y-%m') AS Month,
       SUM(Sales) AS Monthly_Sales,
       SUM(Profit) AS Monthly_Profit
FROM orders
GROUP BY Month
ORDER BY Month;

-- Yearly Growth
SELECT YEAR(`Order Date`) AS Year,
       SUM(Sales) AS Sales,
       SUM(Profit) AS Profit
FROM orders
GROUP BY Year
ORDER BY Year;

-- Top 10 Customers by Revenue
SELECT `Customer Name`,
       SUM(sales) AS total_spent
FROM orders
GROUP BY `Customer Name`
ORDER BY total_spent DESC
LIMIT 10;


-- Repeat Customers vs One-Time Customers
SELECT 
    CASE WHEN num_orders > 1 THEN 'Repeat' ELSE 'One-Time' END AS Customer_Type,
    COUNT(*) AS Num_Customers
FROM (
    SELECT `Customer ID`, COUNT(`Order ID`) AS num_orders
    FROM orders
    GROUP BY `Customer ID`
) AS customer_orders
GROUP BY Customer_Type;



-- Sales by Region
SELECT Region, 
       SUM(Sales) AS Region_Sales, 
       SUM(Profit) AS Region_Profit
FROM orders
GROUP BY Region
ORDER BY Region_Sales DESC;

-- Top Cities by Sales
SELECT City,
       SUM(Sales) AS Total_Sales
FROM orders
GROUP BY City
ORDER BY Total_Sales DESC
LIMIT 10;

SELECT `Ship Mode`, COUNT(*) AS Num_Orders
FROM orders
GROUP BY `Ship Mode`
ORDER BY Num_Orders DESC;

-- Average Delivery Time
SELECT AVG(DATEDIFF(`Ship Date`, `Order Date`)) AS Avg_Delivery_Days
FROM orders;


