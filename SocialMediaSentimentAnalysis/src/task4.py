# As per Task 1 write the python script for task4
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, size, split

# Initialize Spark Session
spark = SparkSession.builder.appName("HashtagTrends").getOrCreate()

# Load posts data
posts_df = spark.read.option("header", True).csv("input/posts.csv")

# Average Number of Hashtags per Post
avg_hashtags = posts_df \
    .withColumn("hashtag_count", size(split(col("Hashtags"), ","))) \
    .agg({"hashtag_count": "avg"})

avg_hashtags.coalesce(1).write.mode("overwrite").csv("outputs/avg_hashtags_per_post.csv", header=True)