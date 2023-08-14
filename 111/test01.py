# MAGIC %sql
# MAGIC CREATE WIDGET TEXT ADFParameter DEFAULT ""
def ctbl():
    spark.sql("CREATE TABLE ct.d"
          "("
            "name STRING"
          ")"
          )
ctbl()