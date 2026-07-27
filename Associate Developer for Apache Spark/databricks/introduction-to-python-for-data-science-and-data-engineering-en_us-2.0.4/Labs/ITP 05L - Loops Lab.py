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
# MAGIC
# MAGIC # Loops Lab
# MAGIC
# MAGIC <!-- ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)  -->
# MAGIC
# MAGIC In this lab you:<br>
# MAGIC
# MAGIC Apply concepts learned in the last lesson, including:
# MAGIC - Utilizing for-loops to handle more advanced control flow
# MAGIC - Using list comprehension to filter lists

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
# MAGIC ## Exercise: Bart Simpson in Detention
# MAGIC
# MAGIC <img src="https://preview.redd.it/386z0p2eh5v21.jpg?auto=webp&s=383ef3536776dc3a34515e6cfd9979f363570a05" width="40%" height="20%">
# MAGIC
# MAGIC Bart Simpson got detention again... He needs to write **`I will not let my dog eat my homework`** 50 times. Of course, Bart is lazy, and needs your help to automate this in Python. 
# MAGIC
# MAGIC Write a function called **`detention_helper()`** that takes in **`detention_message`** and **`num_lines`** representing the message Bart needs to write and the number of times he needs to write it respectively. 
# MAGIC
# MAGIC Your function should print out **`detention_message`** **`num_lines`** times, but each line of **`detention_message`** should be numbered. 
# MAGIC
# MAGIC For example, if **`detention_message`** is `I will not let my dog eat my homework`, and **`num_lines`** is 50, the function should print
# MAGIC
# MAGIC `1. I will not let my dog eat my homework`
# MAGIC
# MAGIC `2. I will not let my dog eat my homework`
# MAGIC
# MAGIC `3. I will not let my dog eat my homework`
# MAGIC
# MAGIC `.
# MAGIC .
# MAGIC .`
# MAGIC
# MAGIC `50. I will not let my dog eat my homework`
# MAGIC
# MAGIC
# MAGIC Here, we are parameterizing the **`detention_message`** and **`num_lines`** in case he gets detention again.
# MAGIC
# MAGIC **Hint:** Recall the **`range()`** function, but make sure to start counting at 1, not 0. f-string formatting will also be helpful.

# COMMAND ----------

def detention_helper(detention_message, num_lines):
    <FILL_IN>

# COMMAND ----------

# MAGIC %skip
# MAGIC def detention_helper(detention_message, num_lines):
# MAGIC     for i in range(num_lines):
# MAGIC         print(f"{i+1}. {detention_message}")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Call your function below with the correct inputs for Bart's current detention and make sure you can see "I will not let my dog eat my homework" printed out 50 times, with the lines numbered, as shown in the problem description.

# COMMAND ----------

detention_helper(FILL_IN, FILL_IN)

# COMMAND ----------

# MAGIC %skip
# MAGIC detention_helper("I will not let my dog eat my homework", 50)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ##Bonus Exercise
# MAGIC Rewrite the for loop above as a while-loop

# COMMAND ----------

def detention_helper(detention_message, num_lines):
    <FILL_IN>

# COMMAND ----------

# MAGIC %skip
# MAGIC def detention_helper(detention_message, num_lines):
# MAGIC     i=0
# MAGIC     while i < num_lines:
# MAGIC         i += 1
# MAGIC         print(f"{i}. {detention_message}")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Call your function below with the correct inputs for Bart's current detention and make sure you can see "I will do my python homework" printed out 25 times, with the lines numbered, as shown in the problem description.

# COMMAND ----------

detention_helper(FILL_IN, FILL_IN)

# COMMAND ----------

# MAGIC %skip
# MAGIC detention_helper("I will do my python homework", 25)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Bonus Exercise
# MAGIC
# MAGIC Below is the code used to display a table of cities and their respective temperatures and humidities from a previous notebook.
# MAGIC
# MAGIC Modify the code to use lists and loops instead of repetitive variables.

# COMMAND ----------

city_list = TODO

# COMMAND ----------

# MAGIC %skip
# MAGIC city_list = ["San Francisco", "Paris", "Mumbai"]
# MAGIC temperature_list = [58, 75, 81]
# MAGIC humidity_list = [.85, .5, .88]
# MAGIC
# MAGIC print(f"{'City':15} {'Temperature':15} {'Humidity':15}")
# MAGIC i = 0
# MAGIC while (i < len(city_list)):
# MAGIC     print(f"{city_list[i]:15} {temperature_list[i]:11} {humidity_list[i]:12.2f}")
# MAGIC     i = i + 1

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Bonus Exercise
# MAGIC
# MAGIC Write a function named `item_count` that accepts a list of values and returns a dictionary with a count of the number of times each unique value appeared in the list
# MAGIC - For example, `item_count(['a', 'b', 'a'])` should return the dictionary `{'a': 2, 'b': 1}`

# COMMAND ----------

def item_count(<FILL IN>):  
   <FILL IN>

# COMMAND ----------

# MAGIC %skip
# MAGIC def item_count(input_list):
# MAGIC     output_dict = {}  # Initialize an empty dictionary
# MAGIC   
# MAGIC     for item in input_list:
# MAGIC         if item not in output_dict:
# MAGIC             # Create an element for the item with an initial count of 1
# MAGIC             output_dict[item] = 1
# MAGIC         else:
# MAGIC             # Add 1 to the current count for the item
# MAGIC             output_dict[item] += 1
# MAGIC       
# MAGIC     return output_dict

# COMMAND ----------

assert item_count(['a', 'b', 'a']) == {'a': 2, 'b': 1}, "There should be 2 occurrences of the letter 'a' and one occurrence of the letter 'b'"

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2026 Databricks, Inc. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the <a href="https://www.apache.org/" target="_blank">Apache Software Foundation</a>.<br/><br/><a href="https://databricks.com/privacy-policy" target="_blank">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use" target="_blank">Terms of Use</a> | <a href="https://help.databricks.com/" target="_blank">Support</a>
