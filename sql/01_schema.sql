/*
Northstar Retail Analytics
Database Schema

Database: NorthstarRetail
Platform: Microsoft SQL Server

Purpose:
Define the relational structure used for retail sales analysis.
*/

USE NorthstarRetail;
GO


/* =========================================================
   Customers
   ========================================================= */

CREATE TABLE dbo.Customers
(
    customer_id   VARCHAR(10)  NOT NULL,
    customer_name VARCHAR(100) NOT NULL,
    country       VARCHAR(50)  NOT NULL,
    signup_date   DATE         NOT NULL,

    CONSTRAINT PK_Customers
        PRIMARY KEY (customer_id)
);
GO


/* =========================================================
   Products
   ========================================================= */

CREATE TABLE dbo.Products
(
    product_id   VARCHAR(10)   NOT NULL,
    product_name VARCHAR(100)  NOT NULL,
    category     VARCHAR(50)   NOT NULL,
    unit_price   DECIMAL(12,2) NOT NULL,
    cost         DECIMAL(12,2) NOT NULL,

    CONSTRAINT PK_Products
        PRIMARY KEY (product_id)
);
GO


/* =========================================================
   Orders
   ========================================================= */

CREATE TABLE dbo.Orders
(
    order_id          VARCHAR(10)   NOT NULL,
    customer_id       VARCHAR(10)   NOT NULL,
    product_id        VARCHAR(10)   NOT NULL,
    order_date        DATETIME2     NOT NULL,
    quantity          INT           NOT NULL,
    discount          DECIMAL(5,4)  NOT NULL,
    unit_price        DECIMAL(12,2) NOT NULL,
    cost              DECIMAL(12,2) NOT NULL,
    gross_revenue     DECIMAL(14,2) NOT NULL,
    discount_amount   DECIMAL(14,2) NOT NULL,
    net_revenue       DECIMAL(14,2) NOT NULL,
    total_cost        DECIMAL(14,2) NOT NULL,
    profit            DECIMAL(14,2) NOT NULL,

    CONSTRAINT PK_Orders
        PRIMARY KEY (order_id),

    CONSTRAINT FK_Orders_Customers
        FOREIGN KEY (customer_id)
        REFERENCES dbo.Customers(customer_id),

    CONSTRAINT FK_Orders_Products
        FOREIGN KEY (product_id)
        REFERENCES dbo.Products(product_id)
);
GO