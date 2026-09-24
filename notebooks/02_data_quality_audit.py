import os
import pandas as pd


# ---------------------------------------------------------
# 1. FILE PATHS
# ---------------------------------------------------------

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

RAW_DATA_PATH = os.path.join(
    PROJECT_ROOT,
    "data",
    "raw"
)


# ---------------------------------------------------------
# 2. LOAD DATA
# ---------------------------------------------------------

customers = pd.read_csv(
    os.path.join(RAW_DATA_PATH, "customers.csv")
)

products = pd.read_csv(
    os.path.join(RAW_DATA_PATH, "products.csv")
)

orders = pd.read_csv(
    os.path.join(RAW_DATA_PATH, "orders.csv")
)


# ---------------------------------------------------------
# 3. BASIC DATASET INFORMATION
# ---------------------------------------------------------

print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print(f"Customers: {customers.shape[0]:,} rows, {customers.shape[1]} columns")
print(f"Products:  {products.shape[0]:,} rows, {products.shape[1]} columns")
print(f"Orders:    {orders.shape[0]:,} rows, {orders.shape[1]} columns")


# ---------------------------------------------------------
# 4. COLUMN INFORMATION
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("CUSTOMER COLUMNS")
print("=" * 60)

print(customers.dtypes)


print("\n" + "=" * 60)
print("PRODUCT COLUMNS")
print("=" * 60)

print(products.dtypes)


print("\n" + "=" * 60)
print("ORDER COLUMNS")
print("=" * 60)

print(orders.dtypes)


# ---------------------------------------------------------
# 5. MISSING VALUES
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

print("\nCustomers:")
print(customers.isnull().sum())

print("\nProducts:")
print(products.isnull().sum())

print("\nOrders:")
print(orders.isnull().sum())


# ---------------------------------------------------------
# 6. DUPLICATE RECORDS
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("DUPLICATE RECORDS")
print("=" * 60)

print(
    f"Duplicate customer rows: "
    f"{customers.duplicated().sum():,}"
)

print(
    f"Duplicate product rows: "
    f"{products.duplicated().sum():,}"
)

print(
    f"Duplicate order rows: "
    f"{orders.duplicated().sum():,}"
)


# ---------------------------------------------------------
# 7. UNIQUE IDENTIFIERS
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("UNIQUE IDENTIFIER CHECK")
print("=" * 60)

print(
    f"Customer IDs: {customers['customer_id'].nunique():,} "
    f"unique out of {len(customers):,}"
)

print(
    f"Product IDs: {products['product_id'].nunique():,} "
    f"unique out of {len(products):,}"
)

print(
    f"Order IDs: {orders['order_id'].nunique():,} "
    f"unique out of {len(orders):,}"
)


# ---------------------------------------------------------
# 8. CATEGORY CONSISTENCY
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("PRODUCT CATEGORIES")
print("=" * 60)

print(
    products["category"]
    .value_counts(dropna=False)
)


# ---------------------------------------------------------
# 9. NUMERIC RANGE CHECKS
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("NUMERIC DATA CHECKS")
print("=" * 60)

print("\nQuantity statistics:")

print(
    orders["quantity"].describe()
)

print("\nDiscount statistics:")

print(
    orders["discount"].describe()
)

print("\nProduct price statistics:")

print(
    products["unit_price"].describe()
)


# ---------------------------------------------------------
# 10. SUSPICIOUS QUANTITIES
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("SUSPICIOUS ORDER QUANTITIES")
print("=" * 60)

suspicious_orders = orders[
    (orders["quantity"] <= 0)
    | (orders["quantity"] > 20)
]

print(
    f"Suspicious quantity records: "
    f"{len(suspicious_orders):,}"
)

print(suspicious_orders.head(20))


# ---------------------------------------------------------
# 11. INVALID DISCOUNTS
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("DISCOUNT CHECK")
print("=" * 60)

invalid_discounts = orders[
    (orders["discount"] < 0)
    | (orders["discount"] > 1)
]

print(
    f"Invalid discount records: "
    f"{len(invalid_discounts):,}"
)


# ---------------------------------------------------------
# 12. REFERENTIAL INTEGRITY
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("REFERENTIAL INTEGRITY")
print("=" * 60)

missing_customer_ids = (
    set(orders["customer_id"])
    - set(customers["customer_id"])
)

missing_product_ids = (
    set(orders["product_id"])
    - set(products["product_id"])
)

print(
    f"Orders referencing missing customers: "
    f"{len(missing_customer_ids):,}"
)

print(
    f"Orders referencing missing products: "
    f"{len(missing_product_ids):,}"
)


# ---------------------------------------------------------
# 13. DATE RANGE
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("DATE RANGE")
print("=" * 60)

orders["order_date"] = pd.to_datetime(
    orders["order_date"],
    errors="coerce"
)

print(
    f"Earliest order: {orders['order_date'].min()}"
)

print(
    f"Latest order:   {orders['order_date'].max()}"
)

print(
    f"Invalid dates:  {orders['order_date'].isna().sum():,}"
)


# ---------------------------------------------------------
# 14. FINAL MESSAGE
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("AUDIT COMPLETE")
print("=" * 60)