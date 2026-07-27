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
# MAGIC # Advanced Pandas Lab
# MAGIC
# MAGIC In this lab, we will answer the question: What regions in the US has the highest average total volume of organic avocado sales in 2018?

# COMMAND ----------

# MAGIC %md
# MAGIC ## REQUIRED - SELECT CLASSIC COMPUTE
# MAGIC Before executing cells in this notebook, please select your classic compute cluster in the lab. Be aware that **Serverless** is enabled by default.
# MAGIC Follow these steps to select the classic compute cluster:
# MAGIC 1. Navigate to the top-right of this notebook and click the drop-down menu to select your cluster. By default, the notebook will use **Serverless**.
# MAGIC 1. If your cluster is available, select it and continue to the next cell. If the cluster is not shown:
# MAGIC     - In the drop-down, select **More**.
# MAGIC     - In the **Attach to an existing compute resource** pop-up, select the first drop-down. You will see a unique cluster name in that drop-down. Please select that cluster.
# MAGIC   **NOTE:** If your cluster has terminated, you might need to restart it in order to select it. To do this:
# MAGIC 1. Right-click on **Compute** in the left navigation pane and select *Open in new tab*.
# MAGIC 1. Find the triangle icon to the right of your compute cluster name and click it.
# MAGIC 1. Wait a few minutes for the cluster to start.
# MAGIC 1. Once the cluster is running, complete the steps above to select your cluster.

# COMMAND ----------

# MAGIC %run "../Includes/Classroom-Setup"

# COMMAND ----------

# MAGIC %md
# MAGIC First, let's import pandas

# COMMAND ----------

import pandas as pd

# COMMAND ----------

# MAGIC %md
# MAGIC ## Read CSV
# MAGIC
# MAGIC To determine the regions with the highest total volume of average organic avocado sales, we will use the [avocado prices](https://www.kaggle.com/datasets/neuromusic/avocado-prices) dataset. 
# MAGIC
# MAGIC We have provided the code to read in the data.

# COMMAND ----------

file_path = f"{DA.paths.datasets}/avocado/avocado.csv".replace("dbfs:", "/dbfs")
df = pd.read_csv(file_path).drop("Unnamed: 0", axis=1) # drop unnamed index column from data

# COMMAND ----------

# MAGIC %md
# MAGIC ## Problem 1: Data Analysis
# MAGIC
# MAGIC Now that you have the DataFrame, you're ready to start doing some analysis. Remember the goal is to determine which regions of the US had the highest average total volume of organic avocado sales in 2018. 
# MAGIC
# MAGIC Filter on the **`type`** and **`year`** to find organic sales in 2018, and assign the result to **`filtered_df`**.

# COMMAND ----------

filtered_df = TODO
filtered_df

# COMMAND ----------

# MAGIC %skip
# MAGIC filtered_df = df[(df["type"] == "organic") & (df["year"] == 2018)]
# MAGIC filtered_df

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC <button onclick="myFunction2()" >Click for Hint</button>
# MAGIC
# MAGIC <div id="myDIV2" style="display: none;">
# MAGIC   Remember to use & for the and operator when creating the boolean array. df[(bool_array) & (bool_array)]
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

assert filtered_df.shape == (648, 13), "There are not the correct number of rows or columns"
assert filtered_df["year"].min() == 2018, "Only look at 2018 data"
assert len(filtered_df[filtered_df["type"] == "conventional"]) == 0, "There should be no rows about non-organic avocado sales"
print("Test passed!")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Problem 2: Find the Regions
# MAGIC
# MAGIC Now, use **`filtered_df`** to determine the top 10 region with the highest average total volume of organic avocado sales in 2018. 
# MAGIC * To do this, create a DataFrame using **`filtered_df`** where each row consists of a **`region`** and the mean **`Total Volume`** of organic avocados for that region. 
# MAGIC * Sort that DataFrame in descending order, and keep the first 10 rows 
# MAGIC * Assign the output to the **`final_df`** variable

# COMMAND ----------

final_df = TODO
final_df

# COMMAND ----------

# MAGIC %skip
# MAGIC final_df = filtered_df.groupby(["region"])[["Total Volume"]].mean().sort_values(["Total Volume"], ascending=False).head(10)
# MAGIC final_df

# COMMAND ----------

testing_df = final_df.reset_index() if final_df.index.name == "region" else final_df
assert type(testing_df) == pd.DataFrame, "final_df should be a DataFrame, make sure it is not a Series. If it is a Series, make sure to use [['Total Volume']] instead of ['Total Volume']"
assert (testing_df.columns == ["region", "Total Volume"]).all(), "The only columns should be region and Total Volume. Make sure to use reset_index and that region is not currently the index column"
assert len(testing_df) == 10, "Only return the top 10 rows"
assert testing_df.iloc[0].values[0] == "TotalUS", "TotalUS should be the on the top row"
assert round(testing_df.iloc[0].values[1], 2) == 1510487.83, "TotalUS should have an average Total Volume of around 1510488"
assert testing_df.iloc[9].values[0] == "LosAngeles", "LosAngeles should be the on the 10th row"
assert round(testing_df.iloc[9].values[1], 2) == 102628.31, "LosAngeles should have an average Total Volume of around 102628"
print("Test passed!")

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2026 Databricks, Inc. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the <a href="https://www.apache.org/" target="_blank">Apache Software Foundation</a>.<br/><br/><a href="https://databricks.com/privacy-policy" target="_blank">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use" target="_blank">Terms of Use</a> | <a href="https://help.databricks.com/" target="_blank">Support</a>
