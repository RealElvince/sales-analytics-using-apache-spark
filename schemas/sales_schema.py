from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, DateType

order_schema = StructType([
    StructField("product_id", IntegerType(), True),
    StructField("customer_id", StringType(), True),
    StructField("order_date", DateType(), True),
    StructField("location", StringType(), True),
    StructField("source_order", StringType(), True),
])
