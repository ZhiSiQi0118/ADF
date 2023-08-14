# MAGIC %sql
# MAGIC CREATE WIDGET TEXT ADFParameter DEFAULT ""

# COMMAND ----------
def ctbl():
    spark.sql("CREATE TABLE ct.c"
          "("
            "name STRING"
          ")"
          )