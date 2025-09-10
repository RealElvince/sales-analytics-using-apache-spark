from pyspark.sql import SparkSession

def create_spark_session(app_name="Sales KPI"):
    spark = SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()
    return spark