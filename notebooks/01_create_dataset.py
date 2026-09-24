import os
import random
from datetime import datetime

import numpy as np
import pandas as pd
from faker import Faker


# ---------------------------------------------------------
# 1. PROJECT SETTINGS
# ---------------------------------------------------------

SEED = 42

random.seed(SEED)
np.random.seed(SEED)

fake = Faker("en_GB")
Faker.seed(SEED)

# Project root = folder containing "data", "notebooks", etc.
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

RAW_DATA_PATH = os.path.join(PROJECT_ROOT, "data", "raw")

os.makedirs(RAW_DATA_PATH, exist_ok=True)


# ---------------------------------------------------------
# 2. BASIC SETTINGS
# ---------------------------------------------------------

NUM_CUSTOMERS = 2000
NUM_PRODUCTS = 100
NUM_ORDERS = 40000

START_DATE = pd.Timestamp("2024-01-01")
END_DATE = pd.Timestamp("2025-12-31")


# ---------------------------------------------------------
# 3. CREATE CUSTOMERS
# ---------------------------------------------------------

print("Creating customers...")

customers = []

countries = [
    "United Kingdom",
    "Ireland",
    "Germany",
    "France",
    "Netherlands",
]

for i in range(1, NUM_CUSTOMERS + 1):

    signup_date = fake.date_between(
        start_date=START_DATE.date(),
        end_date=END_DATE.date(),
    )

    customers.append(
        {
            "customer_id": f"C{i:05d}",
            "customer_name": fake.name(),
            "country": random.choices(
                countries,
                weights=[70, 8, 8, 7, 7],
                k=1,
            )[0],
            "signup_date": signup_date,
        }
    )

customers_df = pd.DataFrame(customers)


# ---------------------------------------------------------
# 4. CREATE PRODUCTS
# ---------------------------------------------------------

print("Creating products...")

categories = {
    "Electronics": [
        "Laptop",
        "Monitor",
        "Keyboard",
        "Mouse",
        "Headphones",
        "Webcam",
    ],
    "Furniture": [
        "Office Chair",
        "Desk",
        "Bookshelf",
        "Standing Desk",
    ],
    "Home": [
        "Coffee Machine",
        "Air Purifier",
        "Desk Lamp",
        "Vacuum Cleaner",
    ],
    "Accessories": [
        "USB Cable",
        "Laptop Bag",
        "Phone Stand",
        "Power Bank",
    ],
}

products = []

product_number = 1

# Create exactly NUM_PRODUCTS products
category_names = list(categories.keys())

for i in range(NUM_PRODUCTS):

    category = random.choice(category_names)

    product_name = random.choice(categories[category])

    unit_price = round(
        np.random.uniform(15, 1200),
        2,
    )

    cost = round(
        unit_price * np.random.uniform(0.45, 0.75),
        2,
    )

    products.append(
        {
            "product_id": f"P{product_number:04d}",
            "product_name": product_name,
            "category": category,
            "unit_price": unit_price,
            "cost": cost,
        }
    )

    product_number += 1

products_df = pd.DataFrame(products)


# ---------------------------------------------------------
# 5. CREATE ORDERS
# ---------------------------------------------------------

print("Creating orders...")

customer_ids = customers_df["customer_id"].tolist()
product_ids = products_df["product_id"].tolist()

orders = []

for i in range(1, NUM_ORDERS + 1):

    order_date = pd.Timestamp(
        np.random.randint(
            START_DATE.value // 10**9,
            END_DATE.value // 10**9,
        ),
        unit="s",
    )

    customer_id = random.choice(customer_ids)
    product_id = random.choice(product_ids)

    quantity = random.choices(
        [1, 2, 3, 4, 5],
        weights=[55, 25, 12, 6, 2],
        k=1,
    )[0]

    discount = random.choices(
        [0, 0.05, 0.10, 0.15, 0.20],
        weights=[50, 20, 15, 10, 5],
        k=1,
    )[0]

    orders.append(
        {
            "order_id": f"O{i:06d}",
            "customer_id": customer_id,
            "product_id": product_id,
            "order_date": order_date,
            "quantity": quantity,
            "discount": discount,
        }
    )

orders_df = pd.DataFrame(orders)


# ---------------------------------------------------------
# 6. ADD REALISTIC DATA QUALITY PROBLEMS
# ---------------------------------------------------------

print("Introducing data quality issues...")

# Duplicate some orders
duplicate_rows = orders_df.sample(
    n=100,
    random_state=SEED,
)

orders_df = pd.concat(
    [orders_df, duplicate_rows],
    ignore_index=True,
)

# Missing customer country values
missing_country_indices = customers_df.sample(
    n=30,
    random_state=SEED,
).index

customers_df.loc[
    missing_country_indices,
    "country"
] = np.nan

# Inconsistent category names
category_indices = products_df.sample(
    n=10,
    random_state=SEED,
).index

products_df.loc[
    category_indices,
    "category"
] = products_df.loc[
    category_indices,
    "category"
].str.upper()

# Add a few suspicious quantities
suspicious_indices = orders_df.sample(
    n=10,
    random_state=SEED,
).index

orders_df.loc[
    suspicious_indices,
    "quantity"
] = 99


# ---------------------------------------------------------
# 7. SAVE RAW DATA
# ---------------------------------------------------------

print("Saving files...")

customers_file = os.path.join(
    RAW_DATA_PATH,
    "customers.csv",
)

products_file = os.path.join(
    RAW_DATA_PATH,
    "products.csv",
)

orders_file = os.path.join(
    RAW_DATA_PATH,
    "orders.csv",
)

customers_df.to_csv(
    customers_file,
    index=False,
)

products_df.to_csv(
    products_file,
    index=False,
)

orders_df.to_csv(
    orders_file,
    index=False,
)


# ---------------------------------------------------------
# 8. SUMMARY
# ---------------------------------------------------------

print("\nDataset creation completed.")

print(f"Customers: {len(customers_df):,}")
print(f"Products: {len(products_df):,}")
print(f"Orders: {len(orders_df):,}")

print("\nFiles created:")

print(customers_file)
print(products_file)
print(orders_file)