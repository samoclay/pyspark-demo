from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("LocalGluePySparkJob") \
    .getOrCreate()

data = [("Alice", 30), ("Bob", 40)]
df = spark.createDataFrame(data, ["name", "age"])

df.show()

spark.stop()
