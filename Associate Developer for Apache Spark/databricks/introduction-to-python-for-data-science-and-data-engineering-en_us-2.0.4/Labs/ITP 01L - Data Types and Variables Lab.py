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
# MAGIC # Data Types and Variables Lab
# MAGIC
# MAGIC ## Exercise:
# MAGIC * Define a variable **`num_chocolate`** and set it equal to the number of chocolate bars you would like to eat. These should be whole numbers (e.g. integer).
# MAGIC * Define a variable **`name`** and set it equal to your name.
# MAGIC * Define the string **`chocolate_string`** as follows: "**`name`** would like to eat **`num_chocolate`** bars of chocolate" using f-string formatting
# MAGIC * Print the string  **`chocolate_string`**

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

name = TODO
num_chocolate = TODO
chocolate_string = TODO

print(TODO)

# COMMAND ----------

# MAGIC %skip
# MAGIC name = "James"
# MAGIC num_chocolate = 10
# MAGIC chocolate_string = f"{name} would like to eat {num_chocolate} bars of chocolate"
# MAGIC
# MAGIC print(chocolate_string)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Check your work:**
# MAGIC
# MAGIC For labs, we will have **Check your work** cells like the following after most questions. After you complete a question, run the cell to make sure you did it correctly. 
# MAGIC
# MAGIC You do not have to know how to use the **assert** statements we use below. 
# MAGIC
# MAGIC If you are curious, if the boolean expression after the assert statement does not evaluate to True, then the code stops and raises an error.

# COMMAND ----------

assert type(name) == str, "Name should be a string"
assert type(num_chocolate) == int, "You have to eat the entire chocolate bar! No floats allowed"
assert chocolate_string == f"{name} would like to eat {num_chocolate} bars of chocolate", "Did you mistype something?"
print("Test passed!")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Bonus Exercise:
# MAGIC * Define a variable **`num_students`** and set it equal to the number of students in the class.
# MAGIC * Define a variable **`num_days`** and set it equal to the number of class days.
# MAGIC * Define a variable **`class_name`** and set it equal to the name of this class.
# MAGIC
# MAGIC * Define the string **`class_information`**  as follows: "There are **`num_students`** * **`num_days`** student days in the **`class_name`**" using f-string formatting.  Make sure to print the product of students and days.
# MAGIC * Print the string  **`class_information`**

# COMMAND ----------

num_students = TODO
num_days = TODO
class_name = TODO
course_information = TODO

print(TODO)

# COMMAND ----------

# MAGIC %skip
# MAGIC num_students = 16
# MAGIC num_days = 2
# MAGIC class_name = "introduction-to-python-for-data-science-and-data-engineering"
# MAGIC course_information = f"There are {num_students * num_days} student days in the {class_name}"
# MAGIC
# MAGIC print(course_information)

# COMMAND ----------

assert type(class_name) == str, "Name should be a string"
assert type(num_students) == int, "Use an integer"
assert course_information == f"There are {num_students * num_days} student days in the {class_name}"

print("Test passed!")

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2026 Databricks, Inc. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the <a href="https://www.apache.org/" target="_blank">Apache Software Foundation</a>.<br/><br/><a href="https://databricks.com/privacy-policy" target="_blank">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use" target="_blank">Terms of Use</a> | <a href="https://help.databricks.com/" target="_blank">Support</a>
