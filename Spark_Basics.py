from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.master("local[*]").appName("basics").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# load
df = spark.read.csv("sales.csv", header=True, inferSchema=True)
df.printSchema()
df.show()

# new column
df = df.withColumn("revenue", F.col("quantity") * F.col("price"))

# filter
df.filter(F.col("city") == "Graz").show()

# group by
df.groupBy("city").agg(
    F.sum("revenue").alias("total_revenue"),
    F.count("order_id").alias("orders"),
).orderBy(F.desc("total_revenue")).show()

# same thing in SQL
df.createOrReplaceTempView("sales")
spark.sql("""
    SELECT product, SUM(quantity) AS units, ROUND(SUM(quantity * price), 2) AS revenue
    FROM sales
    GROUP BY product
    ORDER BY revenue DESC
""").show()

# back to pandas (only for small results)
pdf = df.toPandas()
pdf.to_csv("sales_out.csv", index=False)

spark.stop()