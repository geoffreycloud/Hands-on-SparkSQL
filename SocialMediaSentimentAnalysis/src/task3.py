# As per Task 1 write the python script for task3
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

# Initialize Spark Session
spark = SparkSession.builder.appName("HashtagTrends").getOrCreate()

# Load posts data
posts_df = spark.read.option("header", True).csv("input/posts.csv")

posts_per_day = posts_df \
    .withColumn("post_date", to_date(col("Timestamp"))) \
    .groupBy("post_date") \
    .count() \
    .orderBy("post_date")

posts_per_day.coalesce(1).write.mode("overwrite").csv("outputs/posts_per_day.csv", header=True)