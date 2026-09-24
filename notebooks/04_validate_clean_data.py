import os
import pandas as pd


# =========================================================
# 1. PROJECT PATH
# =========================================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

PROCESSED_DATA_PATH = os.path.join(
    PROJECT_ROOT,
    "data",
    "processed"
)


# =========================================================
# 2. LOAD CLEAN DATA
# =========================================================

customers = pd.read_csv(
    os.path.join(
        PROCESSED_DATA_PATH,
        "customers_clean.csv"
    )
)

products = pd.read_csv(
    os.path.join(
        PROCESSED_DATA_PATH,
        "products_clean.csv"
    )
)

orders = pd.read_csv(
    os.path.join(
        PROCESSED_DATA_PATH,
        "orders_clean.csv"
    )
)


# =========================================================
# 3. CHECK MISSING VALUES
# =========================================================

print("=" * 60)
print("MISSING VALUE CHECK")
print("=" * 60)

print("\nCustomers:")
print(customers.isna().sum())

print("\nProducts:")
print(products.isna().sum())

print("\nOrders:")
print(orders.isna().sum())


# =========================================================
# 4. CHECK DUPLICATES
# =========================================================

print("\n" + "=" * 60)
print("DUPLICATE CHECK")
print("=" * 60)

print(
    "Duplicate customer rows:",
    customers.duplicated().sum()
)

print(
    "Duplicate product rows:",
    products.duplicated().sum()
)

print(
    "Duplicate order rows:",
    orders.duplicated().sum()
)


# =========================================================
# 5. CHECK UNIQUE IDS
# =========================================================

print("\n" + "=" * 60)
print("UNIQUE ID CHECK")
print("=" * 60)

print(
    "Customer IDs:",
    customers["customer_id"].nunique()
)

print(
    "Product IDs:",
    products["product_id"].nunique()
)

print(
    "Order IDs:",
    orders["order_id"].nunique()
)


# =========================================================
# 6. CHECK CATEGORIES
# =========================================================

print("\n" + "=" * 60)
print("CATEGORY CHECK")
print("=" * 60)

print(
    products["category"].value_counts()
)


# =========================================================
# 7. CHECK QUANTITIES
# =========================================================

print("\n" + "=" * 60)
print("QUANTITY CHECK")
print("=" * 60)

print(
    orders["quantity"].describe()
)

print(
    "\nOrders above 20 units:",
    (orders["quantity"] > 20).sum()
)


# =========================================================
# 8. CHECK DISCOUNTS
# =========================================================

print("\n" + "=" * 60)
print("DISCOUNT CHECK")
print("=" * 60)

print(
    "Minimum discount:",
    orders["discount"].min()
)

print(
    "Maximum discount:",
    orders["discount"].max()
)


# =========================================================
# 9. CHECK REFERENTIAL INTEGRITY
# =========================================================

print("\n" + "=" * 60)
print("REFERENTIAL INTEGRITY CHECK")
print("=" * 60)

missing_customers = (
    set(orders["customer_id"])
    - set(customers["customer_id"])
)

missing_products = (
    set(orders["product_id"])
    - set(products["product_id"])
)

print(
    "Missing customer references:",
    len(missing_customers)
)

print(
    "Missing product references:",
    len(missing_products)
)


# =========================================================
# 10. CHECK FINANCIAL CALCULATIONS
# =========================================================

print("\n" + "=" * 60)
print("FINANCIAL CHECK")
print("=" * 60)

print(
    "Negative net revenue:",
    (orders["net_revenue"] < 0).sum()
)

print(
    "Negative profit:",
    (orders["profit"] < 0).sum()
)

print(
    f"\nTotal revenue: "
    f"£{orders['net_revenue'].sum():,.2f}"
)

print(
    f"Total profit: "
    f"£{orders['profit'].sum():,.2f}"
)


# =========================================================
# 11. FINAL STATUS
# =========================================================

print("\n" + "=" * 60)
print("VALIDATION COMPLETE")
print("=" * 60)