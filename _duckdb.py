import pandas as pd
import duckdb

# read_csv ---------------------------------------------------------

user_actions = pd.read_csv("00_data/sql/user_actions.csv", parse_dates=['time'])

courier_actions = pd.read_csv("00_data/sql/courier_actions.csv", parse_dates=['time'])

orders = pd.read_csv("00_data/sql/orders.csv", parse_dates=['creation_time'])

users = pd.read_csv("00_data/sql/users.csv", parse_dates=['birth_date'])

couriers = pd.read_csv("00_data/sql/couriers.csv", parse_dates=['birth_date'])

products = pd.read_csv("00_data/sql/products.csv")

# DuckDB ---------------------------------------------------------

# connect to DuckDB in-memory database
con = duckdb.connect(':memory:')

# write pandas dataframes to DuckDB
duckdb.sql("CREATE TABLE user_actions AS SELECT * FROM user_actions")
duckdb.sql("CREATE TABLE courier_actions AS SELECT * FROM courier_actions")
duckdb.sql("CREATE TABLE orders AS SELECT * FROM orders")
duckdb.sql("CREATE TABLE users AS SELECT * FROM users")
duckdb.sql("CREATE TABLE couriers AS SELECT * FROM couriers")
duckdb.sql("CREATE TABLE products AS SELECT * FROM products")

# user_actions.to_sql('user_actions', conn)
# courier_actions.to_sql('courier_actions', conn)
# orders.to_sql('orders', conn)
# users.to_sql('users', conn)
# couriers.to_sql('couriers', conn)
# products.to_sql('products', conn)

# run a query
# df = conn.execute("SELECT * FROM user_actions").fetchdf()
# print(df)