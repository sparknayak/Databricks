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
# MAGIC # Functions Lab
# MAGIC
# MAGIC <!-- ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)  -->
# MAGIC
# MAGIC In this lab you:<br>
# MAGIC
# MAGIC Apply concepts learned in the last lesson, which include:
# MAGIC * Defining and using functions to reuse code
# MAGIC * Calling the **`help()`** function to learn about functions.

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
# MAGIC #### Problem 1: Even vs. Odd
# MAGIC
# MAGIC One integer operator that's very useful we have not yet seen is [modulo](https://www.w3schools.com/python/python_operators.asp), which uses the symbol **`%`**. Modulo returns the remainder of the division of two integers.
# MAGIC
# MAGIC For example, **`12 % 7`** is **`5`**, because 12 divided by 7 is 1 with remainder 5. 
# MAGIC
# MAGIC Using modulo, write a function called **`even_or_odd(num)`** that accepts an integer **`num`** and will return **`even`** if it is even, **`odd`** otherwise. Remember, all even numbers will have modulo 0 because they are divisible by 2.  
# MAGIC
# MAGIC **Hint:** Make sure to use **`return`** rather than **`print`** in the function, so it passes the test cases below.

# COMMAND ----------

12 % 7

# COMMAND ----------

def even_or_odd(num):
    # <FILL-IN>

# COMMAND ----------

# MAGIC %skip
# MAGIC def even_or_odd(num):
# MAGIC     if num % 2 == 0:
# MAGIC         return "even"
# MAGIC     else:
# MAGIC         return "odd"

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Check your work:**

# COMMAND ----------

assert even_or_odd(2) == "even", "2 is an even number"
assert even_or_odd(42) == "even", "42 is an even number"
assert even_or_odd(1) == "odd", "1 is an odd number"
assert even_or_odd(327) == "odd", "327 is an odd number"
print("Test passed!")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Problem 2: Fizz Buzz
# MAGIC
# MAGIC Now that you've built the basic foundations of identifying even vs odd numbers, you're ready to extend that idea to tackle one of the most common programming interview questions: Fizz Buzz.
# MAGIC
# MAGIC Write a function  called **`fizz_buzz`** that takes in an integer and performs the following:
# MAGIC
# MAGIC * If the input is not an integer at all (remember we can pass in the wrong type, even when we shouldn't), return **`"Wrong type"`**
# MAGIC * For a given integer input, if it is divisible by 5 but not 3 return **`"Fizz"`**.
# MAGIC * If it is divisible by 3 but not 5 return **`"Buzz"`**.
# MAGIC * If it is divisible by both 3 and 5 return **`"FizzBuzz"`**.
# MAGIC * If it is divisible by neither 3 nor 5, return the number itself.
# MAGIC
# MAGIC
# MAGIC **Hint:** You will want to use an **`elif`** statement and **`%`**. 
# MAGIC
# MAGIC Be careful the order in which you check for each of these conditions. For example, you should check if the input is integer before you check if it is divisible by something.

# COMMAND ----------

def fizz_buzz(num):
    # <FILL-IN>

# COMMAND ----------

# MAGIC %skip
# MAGIC def fizz_buzz(num):
# MAGIC     if type(num) != int:
# MAGIC         return "Wrong type"
# MAGIC     elif num % 5 == 0 and num % 3 == 0:
# MAGIC         return "FizzBuzz"
# MAGIC     elif num % 5 == 0:
# MAGIC         return "Fizz"
# MAGIC     elif num % 3 == 0:
# MAGIC         return "Buzz"
# MAGIC     else:
# MAGIC         return num

# COMMAND ----------

# MAGIC %md
# MAGIC **Check your work:**

# COMMAND ----------

assert fizz_buzz(15) == "FizzBuzz", "15 is divisible by both 5 and 3. Should return 'FizzBuzz'"
assert fizz_buzz(30) == "FizzBuzz", "30 is divisible by both 5 and 3. Should return 'FizzBuzz'"
assert fizz_buzz(5) == "Fizz", "5 is divisible by 5. Should return 'Fizz'"
assert fizz_buzz(25) == "Fizz", "25 is divisible by 5. Should return 'Fizz'"
assert fizz_buzz(3) == "Buzz", "3 is divisible by 3. Should return 'Buzz'"
assert fizz_buzz(81) == "Buzz", "81 is divisible by 3. Should return 'Buzz'"
assert fizz_buzz(23) == 23, "23 is not divisible by 3 or 5. Should return 23"
assert fizz_buzz(23.0) == "Wrong type", "Input is not an integer. Should return `Wrong type'"
assert fizz_buzz(True) == "Wrong type", "Input is not an integer. Should return `Wrong type'"
print("Test passed!")

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
# MAGIC Write code to implement the logic described above as a function.
# MAGIC - Name the function __is_leap_year__.
# MAGIC - Define the function to receive a single parameter named __year__.
# MAGIC - Define the function to return a boolean value:
# MAGIC   - True if the value of the parameter __year__ is a leap year.
# MAGIC   - False if the value of the parameter __year__ is a not leap year.
# MAGIC - Test the code for the following years:
# MAGIC   - 1900
# MAGIC   - 1901
# MAGIC   - 1904
# MAGIC   - 2000
# MAGIC
# MAGIC **Hint**: The nested indentation in the instruction suggests that nested logic may be appropriate here.

# COMMAND ----------

def is_leap_year(year):
    # <FILL-IN>

# COMMAND ----------

# MAGIC %skip
# MAGIC def is_leap_year(year):
# MAGIC     leap_year = False
# MAGIC     if year % 4 == 0:
# MAGIC         if year % 400 == 0 or year % 100 != 0:
# MAGIC             leap_year = True
# MAGIC     return leap_year

# COMMAND ----------

assert is_leap_year(1900) == False, "1900 was a leap year"
assert is_leap_year(1901) == False, "1901 was not a leap year"
assert is_leap_year(1904) == True, "1904 was a leap year"
assert is_leap_year(2000) == True, "2000 was a leap year"
print("All tests passed")

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2026 Databricks, Inc. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the <a href="https://www.apache.org/" target="_blank">Apache Software Foundation</a>.<br/><br/><a href="https://databricks.com/privacy-policy" target="_blank">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use" target="_blank">Terms of Use</a> | <a href="https://help.databricks.com/" target="_blank">Support</a>
