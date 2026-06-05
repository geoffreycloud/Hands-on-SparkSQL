# As per Task 1 write the python script for task2
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder.appName("HashtagTrends").getOrCreate()

# Load posts data
posts_df = spark.read.option("header", True).csv("input/posts.csv")

# Top 10 Most Active Users
top_users = posts_df.groupBy("UserID") \
    .count() \
    .orderBy(col("count").desc()) \
    .limit(10)

top_users.coalesce(1).write.mode("overwrite").csv("outputs/top_users.csv", header=True)