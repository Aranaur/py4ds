library(tidyverse)
library(vroom)
library(DBI)
library(duckdb)

# read_csv ---------------------------------------------------------

user_actions <- vroom("00_data/sql/user_actions.csv", col_types = list(
    user_id = col_integer(),
    order_id = col_integer(),
    action = col_character(),
    time = col_datetime("%d/%m/%y %H:%M")
))

courier_actions <- vroom("00_data/sql/courier_actions.csv", col_types = list(
    courier_id = col_integer(),
    order_id = col_integer(),
    action = col_character(),
    time = col_datetime("%d/%m/%y %H:%M")
))

orders <- vroom("00_data/sql/orders.csv", col_types = list(
    order_id = col_integer(),
    creation_time = col_datetime("%d/%m/%y %H:%M"),
    product_ids = col_character()
))

users <- read_csv("00_data/sql/users.csv", col_types = list(
    user_id = col_integer(),
    birth_date = col_date('%d/%m/%y'),
    sex = col_character()
))

couriers <- read_csv("00_data/sql/couriers.csv", col_types = list(
    courier_id = col_integer(),
    birth_date = col_date('%d/%m/%y'),
    sex = col_character()
))

products <- read_csv("00_data/sql/products.csv", col_types = list(
    product_id = col_integer(),
    name = col_character(),
    price = col_double()
))

# DuckDB ---------------------------------------------------------
con <- DBI::dbConnect(duckdb::duckdb(), dbdir = ":memory:")
dbWriteTable(con, "user_actions", user_actions)
dbWriteTable(con, "courier_actions", courier_actions)
dbWriteTable(con, "orders", orders)
dbWriteTable(con, "users", users)
dbWriteTable(con, "couriers", couriers)
dbWriteTable(con, "products", products)

res <- dbGetQuery(con, "SELECT * FROM couriers")
print(res)
