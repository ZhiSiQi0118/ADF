# MAGIC %sql
# MAGIC CREATE WIDGET TEXT ADFParameter DEFAULT ""

# COMMAND ----------
def ctbl(a):
    spark.sql("CREATE TABLE ct.a"
          "("
            "name STRING"
          ")"
          )