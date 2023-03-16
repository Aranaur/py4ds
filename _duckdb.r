library(tidyverse)

# DuckDB ---------------------------------------------------------
user_actions <- read_csv("00_data/sql/user_actions.csv")
courier_actions <- read_csv("00_data/sql/courier_actions.csv")
orders <- read_csv("00_data/sql/orders.csv")
users <- read_csv("00_data/sql/users.csv")
couriers <- read_csv("00_data/sql/couriers.csv")
products <- read_csv("00_data/sql/products.csv")

library(DBI)
library(duckdb)
con <- DBI::dbConnect(duckdb::duckdb(), dbdir = ":memory:")
dbWriteTable(con, "user_actions", user_actions)
dbWriteTable(con, "courier_actions", courier_actions)
dbWriteTable(con, "orders", orders)
dbWriteTable(con, "users", users)
dbWriteTable(con, "couriers", couriers)
dbWriteTable(con, "products", products)