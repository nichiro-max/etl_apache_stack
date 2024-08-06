from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("ETL Pipeline") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# Read Data from Kafka
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9093") \
    .option("subscribe", "events") \
    .load()

# Extract JSON data from Kafka message value
json_df = kafka_df.selectExpr("CAST(value AS STRING) as json") \
    .selectExpr("from_json(json, 'id STRING, name STRING, timestamp TIMESTAMP') as data") \
    .select("data.*")

# Data Transformation
transformed_df = json_df \
    .withColumn("name", when(col("name").isNull(), "Unknown").otherwise(col("name"))) \
    .withColumn("timestamp", col("timestamp").cast("timestamp"))

# Write Data to Delta Lake (for simplicity, using console output here)
query = transformed_df.writeStream \
    .format("console") \
    .outputMode("append") \
    .start()

query.awaitTermination()
