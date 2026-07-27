# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img
# MAGIC     src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png"
# MAGIC     alt="Databricks Learning"
# MAGIC   >
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # Scaling Pandas with Spark
# MAGIC
# MAGIC
# MAGIC <!-- ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)  -->
# MAGIC
# MAGIC In this lesson you:
# MAGIC - Demonstrate the similarities of the pandas API on Spark API with the pandas API
# MAGIC - Understand the differences in syntax for the same DataFrame operations in pandas API on Spark vs PySpark

# COMMAND ----------

# MAGIC %md
# MAGIC ## REQUIRED - SELECT CLASSIC COMPUTE
# MAGIC Before executing cells in this notebook, please select your classic compute cluster in the lab. Be aware that **Serverless** is enabled by default.
# MAGIC Follow these steps to select the classic compute cluster:
# MAGIC 1. Navigate to the top-right of this notebook and click the drop-down menu to select your cluster. By default, the notebook will use **Serverless**.
# MAGIC 1. If your cluster is available, select it and continue to the next cell. If the cluster is not shown:
# MAGIC     - In the drop-down, select **More**.
# MAGIC     - In the **Attach to an existing compute resource** pop-up, select the first drop-down. You will see a unique cluster name in that drop-down. Please select that cluster.
# MAGIC **NOTE:** If your cluster has terminated, you might need to restart it in order to select it. To do this:
# MAGIC 1. Right-click on **Compute** in the left navigation pane and select *Open in new tab*.
# MAGIC 1. Find the triangle icon to the right of your compute cluster name and click it.
# MAGIC 1. Wait a few minutes for the cluster to start.
# MAGIC 1. Once the cluster is running, complete the steps above to select your cluster.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Recall from the cloud computing lesson the open source technology [Apache Spark](https://spark.apache.org/), which is an open-source data processing engine that manages distributed processing of large data sets. 
# MAGIC
# MAGIC In this course, we have been using Pandas, which is a great library for data analysis, but it only runs on one machine, it is not distributed. Luckily, we can use Spark just like traditional Pandas with the Pandas API on Spark. 
# MAGIC
# MAGIC The pandas API on Spark project makes data scientists more productive when interacting with big data, by implementing the pandas DataFrame API on top of Apache Spark. By unifying the two ecosystems with a familiar API, pandas API on Spark offers a seamless transition between small and large data. 
# MAGIC
# MAGIC See this <a href="https://databricks.com/blog/2021/10/04/pandas-api-on-upcoming-apache-spark-3-2.html" target="_blank">blog post</a> for more information on using Pandas syntax on Spark.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC <!-- <div style="img align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://files.training.databricks.com/images/301/31gb.png" width="900"/>
# MAGIC </div>
# MAGIC
# MAGIC <div style="img align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://files.training.databricks.com/images/301/95gb.png" width="900"/>
# MAGIC </div> -->
# MAGIC
# MAGIC **Pandas** DataFrames are mutable, eagerly evaluated, and maintain row order. They are restricted to a single machine, and are very performant when the data sets are small.
# MAGIC
# MAGIC **Spark** DataFrames are distributed, lazily evaluated, immutable, and do not maintain row order. They are very performant when working at scale.
# MAGIC
# MAGIC **pandas API on Spark** provides the best of both worlds: pandas API with the performance benefits of Spark. However, it is not as fast as implementing your solution natively in Spark, and let's see why below.

# COMMAND ----------

# MAGIC %md
# MAGIC ## InternalFrame
# MAGIC
# MAGIC The InternalFrame holds the current Spark DataFrame and internal immutable metadata.
# MAGIC
# MAGIC It manages mappings from pandas API on Spark column names to Spark column names, as well as from pandas API on Spark index names to Spark column names. 
# MAGIC
# MAGIC If a user calls some API, the pandas API on Spark DataFrame updates the Spark DataFrame and metadata in InternalFrame. It creates or copies the current InternalFrame with the new states, and returns a new pandas API on Spark DataFrame.
# MAGIC
# MAGIC <!-- <div style="img align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://files.training.databricks.com/images/301/InternalFramePs.png" width="900"/>
# MAGIC </div> -->

# COMMAND ----------

# MAGIC %md
# MAGIC ### Read in the dataset
# MAGIC
# MAGIC * PySpark
# MAGIC * pandas
# MAGIC * pandas API on Spark

# COMMAND ----------

# MAGIC %run "./Includes/Classroom-Setup"

# COMMAND ----------

# MAGIC %md
# MAGIC Just like how we can read in data from a CSV file in pandas, we can read in data from a file in spark.

# COMMAND ----------

spark_df = spark.read.csv(f"{DA.paths.datasets}/sf-airbnb/sf-airbnb.csv", header="true", inferSchema="true", multiLine="true", escape='"')
display(spark_df)

# COMMAND ----------

# MAGIC %md
# MAGIC Read in CSV with pandas

# COMMAND ----------

import pandas as pd

pandas_df = pd.read_csv(f"{DA.paths.datasets}/sf-airbnb/sf-airbnb.csv".replace("dbfs:", "/dbfs"))
pandas_df.head()

# COMMAND ----------

# MAGIC %md
# MAGIC Read in CSV with pandas API on Spark. You'll notice pandas API on Spark generates an index column for you, like in pandas.

# COMMAND ----------

import pyspark.pandas as ps

df = ps.read_csv(f"{DA.paths.datasets}/sf-airbnb/sf-airbnb.csv", inferSchema="true", multiLine="true", escape='"')
df.head()

# COMMAND ----------

# MAGIC %md
# MAGIC ### <a href="https://koalas.readthedocs.io/en/latest/user_guide/options.html#default-index-type" target="_blank">Index Types</a>
# MAGIC
# MAGIC ![](https://files.training.databricks.com/images/301/koalas_index.png)
# MAGIC
# MAGIC Our recommended rule of thumb for choosing is as follows:
# MAGIC * If your data is small, or if you're running workloads on a single-node cluster, then use **sequence**.
# MAGIC * For larger datasets or multi-node cluster processing, try **distributed**.
# MAGIC * If workloads are not working correctly or not delivering expected results, then use **distributed-sequence** for best compatibility while sacrificing some performance.

# COMMAND ----------

ps.set_option("compute.default_index_type", "distributed-sequence")
df_dist_sequence = ps.read_csv(f"{DA.paths.datasets}/sf-airbnb/sf-airbnb.csv", inferSchema="true", multiLine="true", escape='"')
df_dist_sequence.head()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Converting to pandas API on Spark DataFrame to/from Spark DataFrame

# COMMAND ----------

# MAGIC %md
# MAGIC Creating a pandas API on Spark DataFrame from PySpark DataFrame

# COMMAND ----------

df = ps.DataFrame(spark_df)
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC Alternative way of creating a pandas API on Spark DataFrame from PySpark DataFrame

# COMMAND ----------

df = spark_df.pandas_api()
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC Go from a pandas API on Spark DataFrame to a Spark DataFrame

# COMMAND ----------

display(df.to_spark())

# COMMAND ----------

# MAGIC %md
# MAGIC ### Value Counts

# COMMAND ----------

# MAGIC %md
# MAGIC Get value counts of the different property types with PySpark

# COMMAND ----------

display(spark_df.groupby("property_type").count().orderBy("count", ascending=False))

# COMMAND ----------

# MAGIC %md
# MAGIC Get value counts of the different property types with pandas API on Spark

# COMMAND ----------

df["property_type"].value_counts()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Visualizations
# MAGIC
# MAGIC Based on the type of visualization, the pandas API on Spark has optimized ways to execute the plotting.
# MAGIC <!-- <br><br>
# MAGIC
# MAGIC ![](https://files.training.databricks.com/images/301/ps_plotting.png) -->

# COMMAND ----------

df["bedrooms"].hist(bins=20)

# COMMAND ----------

# MAGIC %md
# MAGIC ### SQL on pandas API on Spark DataFrames

# COMMAND ----------

ps.sql("SELECT distinct(property_type) FROM {df}", df=df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interesting Facts
# MAGIC
# MAGIC * With pandas API on Spark you can read from Delta Tables and read in a directory of files
# MAGIC * If you use apply on a pandas API on Spark DF and that DF is <1000 (by default), pandas API on Spark will use pandas as a shortcut - this can be adjusted using **`compute.shortcut_limit`**
# MAGIC * When you create bar plots, the top n rows are only used - this can be adjusted using **`plotting.max_rows`**
# MAGIC * How to utilize **`.apply`** <a href="https://koalas.readthedocs.io/en/latest/reference/api/databricks.koalas.DataFrame.apply.html#databricks.koalas.DataFrame.apply" target="_blank">docs</a> with its use of return type hints similar to pandas UDFs
# MAGIC * How to check the execution plan, as well as caching a pandas API on Spark DF (which aren't immediately intuitive)
# MAGIC * Koalas are marsupials whose max speed is 30 kph (20 mph)

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2026 Databricks, Inc. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the <a href="https://www.apache.org/" target="_blank">Apache Software Foundation</a>.<br/><br/><a href="https://databricks.com/privacy-policy" target="_blank">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use" target="_blank">Terms of Use</a> | <a href="https://help.databricks.com/" target="_blank">Support</a>
