import os
import pandas as pd


# =========================================================
# 1. PROJECT PATHS
# =========================================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

RAW_DATA_PATH = os.path.join(
    PROJECT_ROOT,
    "data",
    "raw"
)

PROCESSED_DATA_PATH = os.path.join(
    PROJECT_ROOT,
    "data",
    "processed"
)

os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)


# =========================================================
# 2. LOAD RAW DATA
# =========================================================

customers = pd.read_csv(
    os.path.join(RAW_DATA_PATH, "customers.csv")
)

products = pd.read_csv(
    os.path.join(RAW_DATA_PATH, "products.csv")
)

orders = pd.read_csv(
    os.path.join(RAW_DATA_PATH, "orders.csv")
)

print("=" * 60)
print("RAW DATA LOADED")
print("=" * 60)

print(f"Customers: {len(customers):,}")
print(f"Products:  {len(products):,}")
print(f"Orders:    {len(orders):,}")


# =========================================================
# 3. CONVERT DATE COLUMNS
# =========================================================

customers["signup_date"] = pd.to_datetime(
    customers["signup_date"],
    errors="coerce"
)

orders["order_date"] = pd.to_datetime(
    orders["order_date"],
    errors="coerce"
)


# =========================================================
# 4. HANDLE MISSING CUSTOMER COUNTRIES
# =========================================================

missing_countries_before = customers["country"].isna().sum()

customers["country"] = customers["country"].fillna(
    "Unknown"
)

missing_countries_after = customers["country"].isna().sum()

print("\n" + "=" * 60)
print("CUSTOMER COUNTRY CLEANING")
print("=" * 60)

print(
    f"Missing countries before: {missing_countries_before}"
)

print(
    f"Missing countries after:  {missing_countries_after}"
)


# =========================================================
# 5. STANDARDIZE PRODUCT CATEGORIES
# =========================================================

print("\n" + "=" * 60)
print("CATEGORY STANDARDIZATION")
print("=" * 60)

print("Categories before:")
print(products["category"].value_counts())

products["category"] = (
    products["category"]
    .str.strip()
    .str.title()
)

print("\nCategories after:")
print(products["category"].value_counts())


# =========================================================
# 6. REMOVE EXACT DUPLICATE ORDERS
# =========================================================

duplicate_orders_before = orders.duplicated().sum()

orders = orders.drop_duplicates()

duplicate_orders_after = orders.duplicated().sum()

print("\n" + "=" * 60)
print("DUPLICATE ORDER CLEANING")
print("=" * 60)

print(
    f"Duplicate rows before: {duplicate_orders_before}"
)

print(
    f"Duplicate rows after:  {duplicate_orders_after}"
)

print(
    f"Orders remaining:      {len(orders):,}"
)


# =========================================================
# 7. HANDLE ANOMALOUS QUANTITIES
# =========================================================

print("\n" + "=" * 60)
print("QUANTITY VALIDATION")
print("=" * 60)

anomalous_quantity_count = (
    orders["quantity"] > 20
).sum()

print(
    f"Orders with quantity > 20: "
    f"{anomalous_quantity_count}"
)

# Business assumption:
# Northstar Retail is a consumer e-commerce business.
# Orders above 20 units are treated as anomalous
# for the standard sales analysis.

orders = orders[
    orders["quantity"] <= 20
].copy()

print(
    f"Orders remaining after quantity filter: "
    f"{len(orders):,}"
)


# =========================================================
# 8. VALIDATE DISCOUNTS
# =========================================================

invalid_discount_count = (
    (orders["discount"] < 0)
    | (orders["discount"] > 1)
).sum()

print("\n" + "=" * 60)
print("DISCOUNT VALIDATION")
print("=" * 60)

print(
    f"Invalid discount records: "
    f"{invalid_discount_count}"
)


# =========================================================
# 9. VALIDATE REFERENTIAL INTEGRITY
# =========================================================

missing_customers = (
    set(orders["customer_id"])
    - set(customers["customer_id"])
)

missing_products = (
    set(orders["product_id"])
    - set(products["product_id"])
)

print("\n" + "=" * 60)
print("REFERENTIAL INTEGRITY")
print("=" * 60)

print(
    f"Missing customer references: "
    f"{len(missing_customers)}"
)

print(
    f"Missing product references: "
    f"{len(missing_products)}"
)


# =========================================================
# 10. CREATE ORDER-LEVEL FINANCIAL METRICS
# =========================================================

orders = orders.merge(
    products[
        [
            "product_id",
            "unit_price",
            "cost"
        ]
    ],
    on="product_id",
    how="left"
)

orders["gross_revenue"] = (
    orders["quantity"]
    * orders["unit_price"]
)

orders["discount_amount"] = (
    orders["gross_revenue"]
    * orders["discount"]
)

orders["net_revenue"] = (
    orders["gross_revenue"]
    - orders["discount_amount"]
)

orders["total_cost"] = (
    orders["quantity"]
    * orders["cost"]
)

orders["profit"] = (
    orders["net_revenue"]
    - orders["total_cost"]
)


# =========================================================
# 11. BASIC FINANCIAL VALIDATION
# =========================================================

print("\n" + "=" * 60)
print("FINANCIAL VALIDATION")
print("=" * 60)

print(
    f"Total gross revenue: "
    f"£{orders['gross_revenue'].sum():,.2f}"
)

print(
    f"Total discounts: "
    f"£{orders['discount_amount'].sum():,.2f}"
)

print(
    f"Total net revenue: "
    f"£{orders['net_revenue'].sum():,.2f}"
)

print(
    f"Total cost: "
    f"£{orders['total_cost'].sum():,.2f}"
)

print(
    f"Total profit: "
    f"£{orders['profit'].sum():,.2f}"
)


# =========================================================
# 12. SAVE PROCESSED DATA
# =========================================================

customers.to_csv(
    os.path.join(
        PROCESSED_DATA_PATH,
        "customers_clean.csv"
    ),
    index=False
)

products.to_csv(
    os.path.join(
        PROCESSED_DATA_PATH,
        "products_clean.csv"
    ),
    index=False
)

orders.to_csv(
    os.path.join(
        PROCESSED_DATA_PATH,
        "orders_clean.csv"
    ),
    index=False
)


# =========================================================
# 13. FINAL SUMMARY
# =========================================================

print("\n" + "=" * 60)
print("CLEANING COMPLETE")
print("=" * 60)

print(
    f"Clean customers: {len(customers):,}"
)

print(
    f"Clean products:  {len(products):,}"
)

print(
    f"Clean orders:    {len(orders):,}"
)

print("\nProcessed files saved to:")

print(PROCESSED_DATA_PATH)