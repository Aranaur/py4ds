import pandas as pd
from IPython.display import display
import duckdb
import sqlalchemy

# read_csv ---------------------------------------------------------

user_actions = pd.read_csv("00_data/sql/user_actions.csv", parse_dates=['time'])
courier_actions = pd.read_csv("00_data/sql/courier_actions.csv", parse_dates=['time'])
orders = pd.read_csv("00_data/sql/orders.csv", parse_dates=['creation_time'])
users = pd.read_csv("00_data/sql/users.csv", parse_dates=['birth_date'])
couriers = pd.read_csv("00_data/sql/couriers.csv", parse_dates=['birth_date'])
products = pd.read_csv("00_data/sql/products.csv")

# connect to DuckDB in-memory database
con = sqlalchemy.create_engine('duckdb:////path/to/duck.db')

# data Ingestion to DuckDB
user_actions.to_sql("user_actions", con)
courier_actions.to_sql("courier_actions", con)
orders.to_sql("orders", con)
users.to_sql("users", con)
couriers.to_sql("couriers", con)
products.to_sql("products", con)

