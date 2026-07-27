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
# MAGIC # Control Flow Lab
# MAGIC
# MAGIC <!-- ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)  -->
# MAGIC
# MAGIC In this lab you:<br>
# MAGIC
# MAGIC Apply basic control flow concepts in Python we learned last lesson, including:
# MAGIC
# MAGIC * **`if`** and **`elif`** statements
# MAGIC * More boolean operators
# MAGIC * Type checking

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
# MAGIC ### Food Recommender
# MAGIC
# MAGIC For this lab, write the control flow logic for the following food recommender. Users provide the following input:
# MAGIC
# MAGIC *  **`temperature`**: A float representing the temperature outside (in Fahrenheit)
# MAGIC *  **`sunny`**: A boolean set to **`True`** if it is sunny outside, **`False`** otherwise. 
# MAGIC
# MAGIC Write the system to print the following recommendations:
# MAGIC
# MAGIC * If it is at least 60 degrees outside AND it is sunny, recommend `ice cream`.
# MAGIC * If it is at least 60 degrees outside, but it is not sunny, recommend `dumplings`.
# MAGIC * If it is less than 60 degrees, regardless of the weather, recommend `hot tea`.

# COMMAND ----------

temperature = TODO
sunny = TODO

# COMMAND ----------

# MAGIC %skip
# MAGIC temperature = 72.0
# MAGIC sunny = False
# MAGIC
# MAGIC if temperature >= 60.0 and sunny:
# MAGIC     print("ice cream")
# MAGIC elif temperature >= 60.0 and not sunny:
# MAGIC     print("dumplings")
# MAGIC else:
# MAGIC     print("hot tea")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Try changing the values of **`temperature`** and **`sunny`** and make sure it recommends the proper foods!

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Bonus Exercise 
# MAGIC
# MAGIC For this part of the lab, write the control flow logic for car maintenance. Users provide the following input:
# MAGIC
# MAGIC *  **`km_since_last_change`**: An integer representing the number of kilometers since the last oil change
# MAGIC *  **`oil_change_light`**: A boolean set to **`True`** if the oil change light is on, **`False`** otherwise. 
# MAGIC
# MAGIC Write the system to print the following recommendations:
# MAGIC
# MAGIC * If it is at least 15000 kilometers since last oil change AND the light is on, recommend `oil change`.
# MAGIC * If it is at least 15000 kilometers since last oil change AND the light is off, recommend `waiting`.
# MAGIC * If it is less than 15000 kilometers since last oil change regardless of the light, recommend `waiting`.

# COMMAND ----------

km_since_last_change = TODO
oil_change_light = TODO
## Write your logic here

# COMMAND ----------

# MAGIC %skip
# MAGIC km_since_last_change = 15000
# MAGIC oil_change_light = True
# MAGIC
# MAGIC if km_since_last_change >= 15000 and oil_change_light :
# MAGIC     print("Time for an oil change")
# MAGIC elif km_since_last_change >= 15000 and not oil_change_light:
# MAGIC     print("Wait for the light")
# MAGIC else:
# MAGIC     print("Wait longer")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Bonus Exercise
# MAGIC
# MAGIC A year is considered a leap year if it.
# MAGIC - Is evenly divisible by 4 AND ...
# MAGIC   - Is either evenly divisible by 400 (e.g. 2000 was a leap year) OR not evenly divisible by 100 (e.g. 2100 will not be a leap year).
# MAGIC - How do you know if a number is evenly divisible by another number?
# MAGIC   - Modulo division
# MAGIC     - 2000 % 4 == 0: True
# MAGIC     - 1901 % 4 == 0: False
# MAGIC
# MAGIC Write code to implement the logic described above.
# MAGIC - Name the independent variable __year__.
# MAGIC - Name the dependent variable named __is_leap_year__.
# MAGIC - Test the code for the following years:
# MAGIC   - 1900
# MAGIC   - 1901
# MAGIC   - 1904
# MAGIC   - 2000
# MAGIC
# MAGIC **Hint**: The nested indentation in the instruction suggests that nested logic may be appropriate here.

# COMMAND ----------

dbutils.widgets.text("year", "2022", "Enter Year Here")

# COMMAND ----------

year = TODO
is_leap_year = TODO

# COMMAND ----------

# MAGIC %skip
# MAGIC year = int(dbutils.widgets.get("year"))
# MAGIC is_leap_year = False
# MAGIC if year % 4 == 0:
# MAGIC     if year % 400 == 0 or year % 100 != 0:
# MAGIC         is_leap_year = True

# COMMAND ----------

# Check your work

if year == 1900:
    assert year == 1900 and is_leap_year == False, "Error: 1900 was not a leap year"
elif year == 1901:
    assert year == 1901 and is_leap_year == False, "Error: 1901 was not a leap year"
elif year == 1904:
    assert year == 1904 and is_leap_year == True, "Error: 1904 was a leap year"
elif year == 2000:
    assert year == 2000 and is_leap_year == True, "Error: 2000 was a leap year"

# COMMAND ----------

dbutils.widgets.remove("year")

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2026 Databricks, Inc. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the <a href="https://www.apache.org/" target="_blank">Apache Software Foundation</a>.<br/><br/><a href="https://databricks.com/privacy-policy" target="_blank">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use" target="_blank">Terms of Use</a> | <a href="https://help.databricks.com/" target="_blank">Support</a>
