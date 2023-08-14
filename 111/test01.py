# MAGIC %sql
# MAGIC CREATE WIDGET TEXT ADFParameter DEFAULT ""

from pyspark.sql import SparkSession
#from pyspark.context import SparkContex
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
#sc = SparkContext.getOrCreate()
def ctbl():
    spark.sql("CREATE TABLE ct.f"
          "("
            "name STRING"
          ")"
          )