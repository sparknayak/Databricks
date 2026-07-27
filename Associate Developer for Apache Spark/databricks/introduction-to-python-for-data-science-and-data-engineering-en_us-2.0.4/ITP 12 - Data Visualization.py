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
# MAGIC # Data Visualization
# MAGIC
# MAGIC <!-- ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)  -->
# MAGIC
# MAGIC In this lesson you:
# MAGIC Explore data visualization of **`pandas`** DataFrames using:
# MAGIC - Databricks built-in plotting
# MAGIC - **`pandas`** plotting methods
# MAGIC - **`seaborn`** plotting functionality
# MAGIC
# MAGIC Let's import **`pandas`** and our Airbnb Dataset

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

# MAGIC %run "./Includes/Classroom-Setup"

# COMMAND ----------

import pandas as pd

# COMMAND ----------

file_path = f"{DA.paths.datasets}/sf-airbnb/sf-airbnb.csv".replace("dbfs:", "/dbfs")
df = pd.read_csv(file_path)
df.head(3)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Built-in Plotting
# MAGIC
# MAGIC Databricks provides built in data visualization tools we can use in a Databricks notebook. 
# MAGIC
# MAGIC In order to use them, we use the built-in **`display()`** function Databricks provides on a pandas DataFrame.

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Plot Options
# MAGIC
# MAGIC In order to create a different type of plot, click the + icon in the result below.
# MAGIC From there we can specify what kind of plot we want on which columns of the DataFrame.
# MAGIC
# MAGIC For example, let's say we wanted to view the average number of bedrooms per neighborhood. 
# MAGIC
# MAGIC To do this:
# MAGIC
# MAGIC 1. Click the **`+`** icon and select Visualization.
# MAGIC 2. Set the visualization type to **Bar**.
# MAGIC 3. For the **X column**, select **`neighborhood`**.
# MAGIC 4. Click Add Column for the **Y column** and select **`bedrooms`**.
# MAGIC 5. Change the aggregate function to **Average**.

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC Note that initially it only will show a preview of the first 1000 rows, but when we click **`apply`** it works on all of them.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Pandas Plotting
# MAGIC
# MAGIC **`pandas`** also provides some plotting functionality. 
# MAGIC
# MAGIC We can create a histogram using the **`hist()`** method on a **`Series`**.
# MAGIC
# MAGIC Let's create a histogram of the number of bedrooms:

# COMMAND ----------

df["bedrooms"].hist()

# COMMAND ----------

# MAGIC %md
# MAGIC We can also specify the number of bins by passing an argument to **`bins`** parameter.

# COMMAND ----------

df["bedrooms"].hist(bins=20)

# COMMAND ----------

# MAGIC %md
# MAGIC We can also create box plots with pandas.
# MAGIC
# MAGIC We use the method **`boxplot([cols])`** on a **`DataFrame`** to create a box plot for each of the specified columns:

# COMMAND ----------

df.boxplot(["bedrooms", "bathrooms"])

# COMMAND ----------

# MAGIC %md
# MAGIC # Seaborn
# MAGIC
# MAGIC [seaborn](https://seaborn.pydata.org/) is a very popular data visualization library that works with pandas DataFrames. 
# MAGIC
# MAGIC It is popular for both being relatively easy to use and for producing nice looking visualizations.
# MAGIC
# MAGIC Let's import **`seaborn`**: it is common practice to use **`sns`** as the alias.

# COMMAND ----------

import seaborn as sns

# COMMAND ----------

# MAGIC %md
# MAGIC ## Scatter plot
# MAGIC
# MAGIC Let's first create a scatter plot. We'll plot **`bedrooms`** cases on the x-axis and **`bathrooms`** on the y-axis. 
# MAGIC
# MAGIC In order to do this, we call **`sns.scatterplot(data=, x=, y=)`**
# MAGIC
# MAGIC We provide a **`DataFrame`** as the data parameter, and the column names we want for the x and y parameters.

# COMMAND ----------

sns.scatterplot(data=df, x="bedrooms", y="bathrooms")

# COMMAND ----------

# MAGIC %md
# MAGIC You might also want to plot a line of best fit for the scatter plot. 
# MAGIC
# MAGIC We can do this by using the same parameters but for the **`regplot()`** function:

# COMMAND ----------

sns.regplot(data=df, x="bedrooms", y="bathrooms")

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2026 Databricks, Inc. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the <a href="https://www.apache.org/" target="_blank">Apache Software Foundation</a>.<br/><br/><a href="https://databricks.com/privacy-policy" target="_blank">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use" target="_blank">Terms of Use</a> | <a href="https://help.databricks.com/" target="_blank">Support</a>
