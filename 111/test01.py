# MAGIC %sql
# MAGIC CREATE WIDGET TEXT ADFParameter DEFAULT ""

# COMMAND ----------
import pyspark
from pyspark.sql import SparkSession
def test():
 spark.sql("CREATE DATABASE IF NOT EXISTS ct1")