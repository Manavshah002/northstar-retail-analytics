/*
Northstar Retail Analytics
Reporting View

Purpose:
Create a business-ready reporting layer combining
orders, customers, and products for Power BI analysis.
*/

USE NorthstarRetail;
GO


/* =========================================================
   Retail Sales Reporting View
   ========================================================= */

CREATE OR ALTER VIEW dbo.vw_RetailSales
AS
SELECT
    o.order_id,
    o.order_date,
    CAST(o.order_date AS DATE) AS OrderDate,

    YEAR(o.order_date) AS OrderYear,
    MONTH(o.order_date) AS OrderMonth,
    DATENAME(MONTH, o.order_date) AS OrderMonthName,

    c.customer_id,
    c.customer_name,
    c.country,

    p.product_id,
    p.product_name,
    p.category,

    o.quantity,
    o.discount,
    o.unit_price,
    o.cost,

    o.gross_revenue,
    o.discount_amount,
    o.net_revenue,
    o.total_cost,
    o.profit,

    CASE
        WHEN o.net_revenue = 0 THEN 0
        ELSE o.profit / o.net_revenue * 100
    END AS ProfitMargin

FROM dbo.Orders o

INNER JOIN dbo.Customers c
    ON o.customer_id = c.customer_id

INNER JOIN dbo.Products p
    ON o.product_id = p.product_id;
GO


/* =========================================================
   Reporting View Validation
   ========================================================= */

SELECT
    COUNT(*) AS TotalRows,
    COUNT(DISTINCT order_id) AS UniqueOrders,
    SUM(net_revenue) AS TotalRevenue,
    SUM(profit) AS TotalProfit
FROM dbo.vw_RetailSales;
GO