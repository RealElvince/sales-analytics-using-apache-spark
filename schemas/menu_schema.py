from pyspark.sql.types import StructType, StructField, StringType, IntegerType

menu_schema = StructType([
    StructField("product_id", IntegerType(), True),
    StructField("product_name", StringType(), True)])