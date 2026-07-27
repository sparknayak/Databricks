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
# MAGIC # Data Visualization Lab
# MAGIC
# MAGIC Let's import **`pandas`** and **`seaborn`**, then load the avocado dataset to perform data visualizations/analyses.

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

# MAGIC %run "../Includes/Classroom-Setup"

# COMMAND ----------

import pandas as pd
import seaborn as sns

# Set seaborn plot size to be easier to read
sns.set(rc = {"figure.figsize": (15,8)})

# COMMAND ----------

file_path = f"{DA.paths.datasets}/avocado/avocado.csv".replace("dbfs:", "/dbfs")
# Dropping incorrect index column.
df = pd.read_csv(file_path).drop("Unnamed: 0", axis=1) 
df

# COMMAND ----------

# MAGIC %md
# MAGIC ## Problem 1: Databricks Plotting
# MAGIC
# MAGIC Using the built-in plotting feature in Databricks to plot the average **`Total Volume`** per **`year`**.
# MAGIC
# MAGIC Remember to use **`display(df)`** to access built-in plotting.

# COMMAND ----------

display(TODO)

# COMMAND ----------

# MAGIC %skip
# MAGIC display(df)

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC
# MAGIC <button onclick="myFunction2()" >Click for Hint</button>
# MAGIC
# MAGIC <div id="myDIV2" style="display: none;">
# MAGIC   Select the bar chart, Plot Options, set the aggregate function to average, and put year as key and Total Volume as value. 
# MAGIC </div>
# MAGIC <script>
# MAGIC function myFunction2() {
# MAGIC   var x = document.getElementById("myDIV2");
# MAGIC   if (x.style.display === "none") {
# MAGIC     x.style.display = "block";
# MAGIC   } else {
# MAGIC     x.style.display = "none";
# MAGIC   }
# MAGIC }
# MAGIC </script>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Problem 2: `pandas` plotting
# MAGIC
# MAGIC Create a histogram of the **`AveragePrice`** of avocados using the pandas **`.hist()`** method.

# COMMAND ----------

df(TODO)

# COMMAND ----------

# MAGIC %skip
# MAGIC df["AveragePrice"].hist()

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC <button onclick="myFunction2()" >Click for Hint</button>
# MAGIC
# MAGIC <div id="myDIV2" style="display: none;">
# MAGIC   Select the column to make a Series. Then call .hist() on the Series for the column.
# MAGIC </div>
# MAGIC <script>
# MAGIC function myFunction2() {
# MAGIC   var x = document.getElementById("myDIV2");
# MAGIC   if (x.style.display === "none") {
# MAGIC     x.style.display = "block";
# MAGIC   } else {
# MAGIC     x.style.display = "none";
# MAGIC   }
# MAGIC }
# MAGIC </script>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Datetime
# MAGIC
# MAGIC Unfortunately, our **`Date`** column is represented as an object type, when we want it to be a **`datetime`** type so we can do operations based on time (e.g. plot in chronological order instead of lexicographical order).  
# MAGIC
# MAGIC Luckily, `pandas` provides a function called [to_datetime()](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html?highlight=to_datetime#pandas.to_datetime) that takes in a Series and converts the type to **`datetime`**.

# COMMAND ----------

# Notice the dtype of Date
df.dtypes

# COMMAND ----------

df["Date"] = pd.to_datetime(df["Date"])
df.dtypes

# COMMAND ----------

# MAGIC %md
# MAGIC ## Problem 3: `seaborn` plotting
# MAGIC
# MAGIC Using **`seaborn`**, which is aliased as **`sns`** from above, create a scatter plot for the Total Volume of organic avocado sales over time for all of the US (e.g. filter on **`region`** for the **`TotalUS`** region & on **`type`** for just **`organic`**). Select **`Date`** as the x-axis.

# COMMAND ----------

plot_df = TODO

# COMMAND ----------

# MAGIC %skip
# MAGIC plot_df = df[(df["region"] == "TotalUS") & (df["type"] == "organic")]
# MAGIC sns.scatterplot(data=plot_df, x="Date", y="Total Volume")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC <button onclick="myFunction2()" >Click for Hint</button>
# MAGIC
# MAGIC <div id="myDIV2" style="display: none;">
# MAGIC   Recall the seaborn plot function looks like this: sns.scatterplot(data=, x=, y=). Create a filtered DataFrame to pass to this with the region and type we want.
# MAGIC </div>
# MAGIC <script>
# MAGIC function myFunction2() {
# MAGIC   var x = document.getElementById("myDIV2");
# MAGIC   if (x.style.display === "none") {
# MAGIC     x.style.display = "block";
# MAGIC   } else {
# MAGIC     x.style.display = "none";
# MAGIC   }
# MAGIC }
# MAGIC </script>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Problem 4: What about conventional avocados?
# MAGIC
# MAGIC Create the same scatter plot except with conventional avocados instead of organic ones. What differences do you notice between the two? Notice the axis scales.

# COMMAND ----------

d = TODO

# COMMAND ----------

# MAGIC %skip
# MAGIC d = df[(df["region"] == "TotalUS") & (df["type"] == "conventional")]
# MAGIC sns.scatterplot(data=d, x="Date", y="Total Volume")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC <button onclick="myFunction2()" >Click for Hint</button>
# MAGIC
# MAGIC <div id="myDIV2" style="display: none;">
# MAGIC   Use the same code as before but make sure to filter with df["type"] == "conventional" this time
# MAGIC </div>
# MAGIC <script>
# MAGIC function myFunction2() {
# MAGIC   var x = document.getElementById("myDIV2");
# MAGIC   if (x.style.display === "none") {
# MAGIC     x.style.display = "block";
# MAGIC   } else {
# MAGIC     x.style.display = "none";
# MAGIC   }
# MAGIC }
# MAGIC </script>

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2026 Databricks, Inc. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the <a href="https://www.apache.org/" target="_blank">Apache Software Foundation</a>.<br/><br/><a href="https://databricks.com/privacy-policy" target="_blank">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use" target="_blank">Terms of Use</a> | <a href="https://help.databricks.com/" target="_blank">Support</a>
