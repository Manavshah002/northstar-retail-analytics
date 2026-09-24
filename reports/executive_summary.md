\# Northstar Retail Analytics

\## Executive Summary



\### Project Overview



Northstar Retail is an online consumer-products business selling

Electronics, Furniture, Home and Accessories.



The objective of this project was to build an end-to-end analytics

solution that transforms transactional data into reliable business

reporting and decision-support insights.



The solution combines Python, SQL Server and Power BI.



\---



\## Dataset



The final validated dataset contains:



\- 2,000 customers

\- 100 products

\- 39,990 orders

\- 70,248 units sold

\- Order period: January 2024 to December 2025



\---



\## Data Quality



The initial dataset was audited before analysis.



Key issues identified included:



\- 100 duplicate order rows

\- 30 missing customer country values

\- Inconsistent category capitalisation

\- 10 suspicious quantity values



The data was cleaned and validated before being used for reporting.



Validation confirmed:



\- No duplicate rows remained

\- No missing values remained in the cleaned customer/product/order data

\- No invalid customer references

\- No invalid product references

\- No negative revenue values

\- No negative profit values



\---



\## Overall Performance



Across the validated dataset:



\- Total Revenue: £38.95M

\- Total Profit: £14.58M

\- Profit Margin: approximately 37.4%

\- Total Orders: 39,990

\- Units Sold: 70,248



\---



\## Year-over-Year Performance



\### 2024



\- Orders: 20,044

\- Units Sold: 35,161

\- Revenue: £19.43M

\- Profit: £7.28M

\- Average Order Value: £969.32



\### 2025



\- Orders: 19,946

\- Units Sold: 35,087

\- Revenue: £19.53M

\- Profit: £7.30M

\- Average Order Value: £978.90



Compared with 2024, 2025 showed:



\- Revenue increase of approximately 0.49%

\- Orders decrease of approximately 0.49%

\- Units decrease of approximately 0.21%

\- Profit increase of approximately 0.25%

\- Average Order Value increase of approximately 0.99%



This indicates that revenue and profit were broadly stable year-over-year,

with a small increase in average order value.



\---



\## Category Performance



The four product categories were:



\- Accessories

\- Furniture

\- Home

\- Electronics



Accessories generated the highest observed revenue and profit margin

among the four categories.



Category-level profit margins ranged from approximately 36.0% to 39.1%.



\---



\## Product Performance



Product-level analysis identified substantial differences in revenue,

profit and profit margin across individual products.



The dashboard highlights:



\- Top products by revenue

\- Top products by profit

\- Top products by profit margin



This allows management to distinguish between products that generate

high sales volume and products that generate strong profitability.



\---



\## Customer Performance



Customer analysis examined:



\- Revenue by country

\- Top customers by revenue

\- Customer order frequency

\- Revenue contribution by order-frequency segment



The largest customer order-frequency groups were:



\- 11–20 orders

\- 21+ orders



The 21+ order segment generated approximately £20.88M in revenue,

representing approximately 53.6% of total revenue.



\---



\## Discount and Profitability



Observed profit margins decreased across higher discount bands.



| Discount Band | Observed Profit Margin |

|---|---:|

| 0% | 40.6% |

| 1–5% | 37.4% |

| 6–10% | 33.8% |

| 11–15% | 30.3% |

| 16–20% | 25.6% |



Higher discount bands were associated with lower observed profit margins

in this dataset.



This is an observed relationship and does not establish that discounts

caused the lower margins.



Further analysis would be required to evaluate causality.



\---



\## Business Questions Supported



The solution allows management to answer questions such as:



\- How much revenue and profit are we generating?

\- How is performance changing over time?

\- Which categories generate the most revenue and profit?

\- Which products are the strongest contributors to profit?

\- Which customers generate the most revenue?

\- How frequently are customers ordering?

\- How does profitability vary across discount levels?

\- Which countries contribute the most revenue?



\---



\## Technical Solution



\### Data Processing



Python was used for:



\- Data generation

\- Data-quality auditing

\- Data cleaning

\- Validation

\- Feature calculations



\### Database



SQL Server was used for:



\- Relational data storage

\- Data validation

\- Business analysis

\- Reporting-layer preparation



\### Business Intelligence



Power BI was used to create:



\- Executive KPIs

\- Revenue trends

\- Category analysis

\- Product profitability analysis

\- Customer analysis

\- Discount analysis

\- Interactive reporting



\---



\## Deliverables



The project produces:



1\. Cleaned analytical datasets

2\. SQL database schema

3\. SQL validation queries

4\. SQL business analysis queries

5\. SQL reporting view

6\. Power BI dashboard

7\. Executive summary



\---



\## Important Assumptions



This project uses a synthetic retail dataset.



Quantity values above 20 were treated as anomalous based on an assumed

consumer-retail business rule and excluded from standard analysis.



Customer countries with missing values were retained and represented as

`Unknown` rather than removing the associated customers.



Historical order pricing is based on the price and cost values contained

in the order dataset.



\---



\## Conclusion



The project demonstrates an end-to-end analytics workflow:



Raw Data → Data Quality Audit → Cleaning → Validation → SQL Analysis →

Reporting Layer → Power BI Dashboard → Business Insights

