/*
Northstar Retail Analytics
Database Validation Checks

Purpose:
Validate row counts, uniqueness, referential integrity,
and basic numerical data quality after loading the dataset.
*/

USE NorthstarRetail;
GO


/* =========================================================
   1. Row Counts
   ========================================================= */

SELECT
    'Customers' AS TableName,
    COUNT(*) AS TotalRows
FROM dbo.Customers

UNION ALL

SELECT
    'Products',
    COUNT(*)
FROM dbo.Products

UNION ALL

SELECT
    'Orders',
    COUNT(*)
FROM dbo.Orders;
GO


/* =========================================================
   2. Order Uniqueness
   ========================================================= */

SELECT
    COUNT(*) AS TotalOrders,
    COUNT(DISTINCT order_id) AS UniqueOrders
FROM dbo.Orders;
GO


/* =========================================================
   3. Customer and Product Coverage
   ========================================================= */

SELECT
    COUNT(DISTINCT customer_id) AS UniqueCustomers,
    COUNT(DISTINCT product_id) AS UniqueProducts
FROM dbo.Orders;
GO


/* =========================================================
   4. Referential Integrity
   ========================================================= */

SELECT
    COUNT(*) AS InvalidCustomerReferences
FROM dbo.Orders o
LEFT JOIN dbo.Customers c
    ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
GO


SELECT
    COUNT(*) AS InvalidProductReferences
FROM dbo.Orders o
LEFT JOIN dbo.Products p
    ON o.product_id = p.product_id
WHERE p.product_id IS NULL;
GO


/* =========================================================
   5. Quantity Validation
   ========================================================= */

SELECT
    SUM(quantity) AS TotalUnits,
    AVG(CAST(quantity AS DECIMAL(10,2))) AS AvgQuantity,
    MIN(quantity) AS MinQuantity,
    MAX(quantity) AS MaxQuantity
FROM dbo.Orders;
GO


/* =========================================================
   6. Discount Validation
   ========================================================= */

SELECT
    MIN(discount) AS MinDiscount,
    MAX(discount) AS MaxDiscount
FROM dbo.Orders;
GO


/* =========================================================
   7. Financial Validation
   ========================================================= */

SELECT
    SUM(net_revenue) AS TotalRevenue,
    SUM(profit) AS TotalProfit,
    SUM(profit) / NULLIF(SUM(net_revenue), 0) AS ProfitMargin
FROM dbo.Orders;
GO


/* =========================================================
   8. Negative Financial Values
   ========================================================= */

SELECT
    COUNT(*) AS NegativeRevenueRows
FROM dbo.Orders
WHERE net_revenue < 0;


SELECT
    COUNT(*) AS NegativeProfitRows
FROM dbo.Orders
WHERE profit < 0;
GO


/* =========================================================
   9. Date Range
   ========================================================= */

SELECT
    MIN(order_date) AS FirstOrderDate,
    MAX(order_date) AS LastOrderDate
FROM dbo.Orders;
GO