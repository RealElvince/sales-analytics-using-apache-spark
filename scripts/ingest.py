from utils import create_spark_session
from schemas import order_schema


spark = create_spark_session("sales kpi")

# Read the orders data
orders_df = spark.read.format("csv") \
    .option("header", "true") \
    .schema(order_schema) \
    .load("data/sales.csv")

orders_df.show(truncate=False)