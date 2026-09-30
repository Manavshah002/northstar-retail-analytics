\# Northstar Retail Analytics



\## End-to-End Sales \& Profitability Analytics



Northstar Retail Analytics is an end-to-end retail analytics project designed to transform raw transactional data into reliable business reporting and decision-support insights.



The project covers the complete analytics workflow:



\*\*Data Quality Audit → Python Data Preparation → SQL Server → Business Analysis → Power BI → Executive Insights\*\*



The solution analyses sales performance, profitability, products, customers, countries and discount behaviour across a two-year retail dataset.


\## Business Problem



Retail businesses often have sales data spread across transactional records, customer information and product data. Without a unified reporting solution, it can be difficult to understand overall performance, identify profitable products and customers, and evaluate the impact of discounts.



This project addresses that problem by creating a validated analytical dataset and an interactive reporting solution that brings key commercial metrics into one place.



\## Objectives



The project aims to:



\- Monitor revenue, profit and order performance over time

\- Identify high-performing and profitable product categories

\- Identify top-performing products by revenue and profit

\- Analyse customer revenue and order frequency

\- Compare performance across countries

\- Examine the relationship between discount levels and observed profit margins

\- Provide an executive-level Power BI dashboard for business monitoring and analysis

## Dataset



The project uses a synthetic retail dataset covering January 2024 to December 2025.



| Dataset | Records |

|---|---:|

| Customers | 2,000 |

| Products | 100 |

| Orders after cleaning | 39,990 |



The dataset contains customer, product and transactional order information.



\### Data Quality Issues Identified



The raw data was audited before analysis. The following issues were identified:



\- 100 duplicate order rows

\- 30 missing customer country values

\- Inconsistent category capitalization

\- 10 suspicious quantity values



\### Data Cleaning



The data preparation process included:



\- Removing exact duplicate order rows

\- Filling missing customer countries with `Unknown`

\- Standardizing product category values

\- Handling anomalous order quantities

\- Validating customer and product references

\- Validating discount values and dates

\- Calculating revenue, discount, cost and profit metrics



The cleaned dataset was validated before being loaded into SQL Server and used for business analysis.

## Technical Approach



The project follows a layered analytics workflow.



```text

Raw CSV Data

&#x20;    ↓

Python Data Quality Audit

&#x20;    ↓

Python Data Cleaning \& Validation

&#x20;    ↓

SQL Server Database

&#x20;    ↓

SQL Business Analysis

&#x20;    ↓

SQL Reporting View

&#x20;    ↓

Power BI Data Model \& DAX

&#x20;    ↓

Interactive Dashboard

&#x20;    ↓

Executive Insights

## Key Business Insights



The analysis produced the following observations from the cleaned synthetic dataset.



\### Overall Performance



\- Total revenue: \*\*£38.95M\*\*

\- Total profit: \*\*£14.58M\*\*

\- Overall profit margin: \*\*37.43%\*\*

\- Total orders: \*\*39,990\*\*

\- Total units sold: \*\*70,248\*\*



\### Year-over-Year Performance



Performance remained relatively stable between 2024 and 2025.



| Metric | 2024 | 2025 | Change |

|---|---:|---:|---:|

| Orders | 20,044 | 19,946 | -0.49% |

| Units | 35,161 | 35,087 | -0.21% |

| Revenue | £19.43M | £19.53M | +0.49% |

| Profit | £7.28M | £7.30M | +0.25% |

| Average Order Value | £969.32 | £978.90 | +0.99% |



Revenue and profit increased slightly despite a small reduction in order volume.



\### Category Performance



Accessories generated the highest revenue among the four product categories at approximately \*\*£10.39M\*\* and also had the highest observed profit margin at approximately \*\*39.13%\*\*.



Electronics had the lowest observed category profit margin at approximately \*\*35.98%\*\*.



\### Customer Order Frequency



Customers with \*\*21+ orders\*\* generated approximately \*\*£20.88M\*\*, representing around \*\*53.6% of total revenue\*\*.



Customers with \*\*11–20 orders\*\* generated approximately \*\*£17.85M\*\*.



This highlights the importance of understanding customer purchase frequency alongside total customer revenue.



\### Discount and Profitability



Observed profit margin decreased as discount levels increased:



| Discount Band | Observed Profit Margin |

|---|---:|

| 0% | 40.63% |

| 1–5% | 37.43% |

| 6–10% | 33.77% |

| 11–15% | 30.27% |

| 16–20% | 25.64% |



This is an observed relationship in the synthetic dataset and should not be interpreted as evidence that discounts directly cause lower profitability.



These findings are intended to demonstrate how transactional data can be converted into commercially relevant observations for decision-making.

## Power BI Dashboard



The Power BI report contains three interactive pages designed for different levels of business analysis.



\### Executive Overview



Provides a high-level view of revenue, profit, orders and category performance.








\### Product \& Profitability



Examines product-level revenue, profit margins and discount behaviour.



!\[Product \& Profitability](images/product\_profitability.png)



\### Customer \& Market



Analyses customer revenue, order frequency and geographic performance.



!\[Customer \& Market](images/customer\_market.png)

## Tools \& Technologies



| Area | Technology |

|---|---|

| Programming | Python |

| Data Preparation | Pandas, NumPy |

| Database | SQL Server |

| Analytics | SQL |

| Business Intelligence | Power BI |

| Data Modelling | Star Schema / Relational Modelling |

| Calculations | DAX |

| Version Control | Git |

| Documentation | Markdown |



\### Key Skills Demonstrated



\- Data quality auditing

\- Data cleaning and validation

\- Relational database design

\- SQL business analysis

\- Data modelling

\- KPI development

\- Power BI dashboard development

\- DAX measures and calculated columns

\- Customer segmentation

\- Profitability analysis

\- Business-focused data storytelling

\- End-to-end analytics workflow

## Assumptions \& Limitations



This project uses synthetic retail data created for portfolio and demonstration purposes.



The following assumptions were made during the analysis:



\- Missing customer country values were replaced with `Unknown`.

\- Product categories were standardized for consistent reporting.

\- Exact duplicate order rows were removed.

\- Quantity values above 20 were treated as anomalous based on a consumer-retail assumption and excluded during cleaning.

\- Discount values were expected to fall between 0% and 20%.

\- Revenue and profit calculations were based on the available order quantity, selling price, discount and product cost fields.

\- The relationship between discount levels and profit margin is observational and does not establish causation.

\- Customer order-frequency segments were calculated from the available transaction history.

\- The dataset does not represent an actual company's commercial performance.



Because the data is synthetic, the financial figures and business findings should be treated as demonstrations of the analytical workflow rather than real-world business results.

## How to Reproduce the Project



\### 1. Clone the Repository



```bash

git clone <your-github-repository-url>

cd "freelance data analytics"

2. Create a Python Environment
python -m venv .venv
.venv\\Scripts\\activate

3. Install Dependencies
pip install pandas numpy

4. Generate the Dataset
python notebooks/01\_create\_dataset.py

5. Run the Data Quality Audit
python notebooks/02\_data\_quality\_audit.py

6. Clean the Data
python notebooks/03\_clean\_data.py

7. Validate the Data
python notebooks/04\_validate\_clean\_data.py

8. Load Data into SQL server
sql/01\_schema.sql

sql/02\_data\_validation.sql

sql/03\_business\_analysis.sql

sql/04\_reporting\_view.sql

9. Open the Power BI Report
powerbi/NorthstarRetail.pbix



