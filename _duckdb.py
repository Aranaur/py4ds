# import duckdb
# import pandas as pd
# from datetime import datetime

# dateparse = lambda x: datetime.strptime(x, '%d/%m/%y %H:%M')

# user_actions = pd.read_csv("00_data/sql/user_actions.csv", parse_dates=['time'], date_parser=dateparse)
# courier_actions = pd.read_csv("00_data/sql/courier_actions.csv")
# orders = pd.read_csv("00_data/sql/orders.csv")
# users = pd.read_csv("00_data/sql/users.csv")
# couriers =- pd.read_csv("00_data/sql/couriers.csv")
# products = pd.read_csv("00_data/sql/products.csv")

# con = duckdb.connect(database=':memory:')

# duckdb.sql("CREATE TABLE my_table AS SELECT * FROM my_df")
# courier_actions.to_sql("courier_actions", con)
# orders.to_sql("orders", con)
# users.to_sql("users", con)
# couriers.to_sql("couriers", con)
# products.to_sql("products", con)

# user_actions.dtypes