"""
PySpark job to demonstrate basic functionality.
"""
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("LocalGluePySparkJob") \
    .getOrCreate()

data = [("Rehan", 10, 90), ("Shahil", 10, 85), ("Shibran",10 , 80),]
df = spark.createDataFrame(data, ["name", "class", "marks"])

df.show()

spark.stop()
