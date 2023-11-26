# Databricks notebook source
print("hello")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "this"

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
display(files)

# COMMAND ----------


