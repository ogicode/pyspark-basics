# Spark Basics

In this project I explore PySpark with a small sales dataset.<br>
I plan to use it on more complex projects in the future for unstructured data,<br>
while for structured I plan to use Airflow+dbt.

## What it does

`Spark_Basics.py` runs Spark locally:

1. Loads `Sales.csv` (order_id, date, city, product, quantity, price)
2. Adds `revenue = quantity * price`
3. Filters orders from Graz
4. Groups revenue and order count by city
5. Runs the same kind of aggregation in Spark SQL (revenue per product)
6. Converts the result to pandas and saves it as `sales_out.csv`

`test_spark.py` is a quick check that Spark starts and prints its version.

## Requirements

- Python 3.10+
- Java 17 or 21 (Spark runs on the JVM)

## Run

```bash
pip install -r requirements.txt
python test_spark.py
python Spark_Basics.py
```

## Stack

PySpark 4.2, Spark SQL, pandas