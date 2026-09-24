/*
Northstar Retail Analytics
Business Analysis

Purpose:
Answer key commercial questions using the validated retail dataset.
*/


USE NorthstarRetail;
GO


/* =========================================================
   1. Monthly Revenue and Profit Trend
   ========================================================= */

SELECT
    YEAR(order_date) AS OrderYear,
    MONTH(order_date) AS OrderMonth,
    SUM(net_revenue) AS Revenue,
    SUM(profit) AS Profit,
    SUM(quantity) AS UnitsSold,
    COUNT(DISTINCT order_id) AS Orders
FROM dbo.Orders
GROUP BY
    YEAR(order_date),
    MONTH(order_date)
ORDER BY
    OrderYear,
    OrderMonth;
GO


/* =========================================================
   2. Annual Performance
   ========================================================= */

SELECT
    YEAR(order_date) AS OrderYear,
    COUNT(DISTINCT order_id) AS Orders,
    SUM(quantity) AS UnitsSold,
    SUM(net_revenue) AS Revenue,
    SUM(profit) AS Profit,
    SUM(net_revenue) /
        NULLIF(COUNT(DISTINCT order_id), 0) AS AverageOrderValue
FROM dbo.Orders
GROUP BY YEAR(order_date)
ORDER BY OrderYear;
GO


/* =========================================================
   3. Category Performance
   ========================================================= */

SELECT
    p.category AS Category,
    COUNT(DISTINCT o.order_id) AS Orders,
    SUM(o.quantity) AS UnitsSold,
    SUM(o.net_revenue) AS Revenue,
    SUM(o.profit) AS Profit,
    SUM(o.profit) /
        NULLIF(SUM(o.net_revenue), 0) * 100 AS ProfitMargin
FROM dbo.Orders o
INNER JOIN dbo.Products p
    ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY Revenue DESC;
GO


/* =========================================================
   4. Top 20 Products by Revenue
   ========================================================= */

SELECT TOP 20
    p.product_id,
    p.product_name,
    p.category,
    SUM(o.net_revenue) AS Revenue,
    SUM(o.profit) AS Profit,
    SUM(o.profit) /
        NULLIF(SUM(o.net_revenue), 0) * 100 AS ProfitMargin
FROM dbo.Orders o
INNER JOIN dbo.Products p
    ON o.product_id = p.product_id
GROUP BY
    p.product_id,
    p.product_name,
    p.category
ORDER BY Revenue DESC;
GO


/* =========================================================
   5. Top 20 Products by Profit
   ========================================================= */

SELECT TOP 20
    p.product_id,
    p.product_name,
    p.category,
    SUM(o.net_revenue) AS Revenue,
    SUM(o.profit) AS Profit,
    SUM(o.profit) /
        NULLIF(SUM(o.net_revenue), 0) * 100 AS ProfitMargin
FROM dbo.Orders o
INNER JOIN dbo.Products p
    ON o.product_id = p.product_id
GROUP BY
    p.product_id,
    p.product_name,
    p.category
ORDER BY Profit DESC;
GO


/* =========================================================
   6. Top 20 Customers by Revenue
   ========================================================= */

SELECT TOP 20
    c.customer_id,
    c.customer_name,
    c.country,
    COUNT(DISTINCT o.order_id) AS Orders,
    SUM(o.quantity) AS Units,
    SUM(o.net_revenue) AS Revenue,
    SUM(o.profit) AS Profit,
    SUM(o.profit) /
        NULLIF(SUM(o.net_revenue), 0) * 100 AS ProfitMargin
FROM dbo.Orders o
INNER JOIN dbo.Customers c
    ON o.customer_id = c.customer_id
GROUP BY
    c.customer_id,
    c.customer_name,
    c.country
ORDER BY Revenue DESC;
GO


/* =========================================================
   7. Revenue by Country
   ========================================================= */

SELECT
    c.country,
    COUNT(DISTINCT o.order_id) AS Orders,
    SUM(o.quantity) AS UnitsSold,
    SUM(o.net_revenue) AS Revenue,
    SUM(o.profit) AS Profit,
    SUM(o.profit) /
        NULLIF(SUM(o.net_revenue), 0) * 100 AS ProfitMargin
FROM dbo.Orders o
INNER JOIN dbo.Customers c
    ON o.customer_id = c.customer_id
GROUP BY c.country
ORDER BY Revenue DESC;
GO


/* =========================================================
   8. Discount vs Profitability
   ========================================================= */

WITH DiscountAnalysis AS
(
    SELECT
        CASE
            WHEN discount = 0 THEN '0%'
            WHEN discount <= 0.05 THEN '1-5%'
            WHEN discount <= 0.10 THEN '6-10%'
            WHEN discount <= 0.15 THEN '11-15%'
            ELSE '16-20%'
        END AS DiscountBand,
        CASE
            WHEN discount = 0 THEN 1
            WHEN discount <= 0.05 THEN 2
            WHEN discount <= 0.10 THEN 3
            WHEN discount <= 0.15 THEN 4
            ELSE 5
        END AS DiscountBandSort,
        order_id,
        quantity,
        net_revenue,
        profit
    FROM dbo.Orders
)

SELECT
    DiscountBand,
    COUNT(DISTINCT order_id) AS Orders,
    SUM(quantity) AS UnitsSold,
    SUM(net_revenue) AS Revenue,
    SUM(profit) AS Profit,
    SUM(profit) /
        NULLIF(SUM(net_revenue), 0) * 100 AS ProfitMargin
FROM DiscountAnalysis
GROUP BY
    DiscountBand,
    DiscountBandSort
ORDER BY DiscountBandSort;
GO