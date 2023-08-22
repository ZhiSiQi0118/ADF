# MAGIC %sql
# MAGIC CREATE WIDGET TEXT ADFParameter DEFAULT ""

from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
def ctbl():
    spark.sql("CREATE TABLE ct.l"
          "("
            "name STRING"
          ")"
          )