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
# MAGIC # Exceptions
# MAGIC
# MAGIC <!-- ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)  -->
# MAGIC
# MAGIC In this lesson you:
# MAGIC
# MAGIC - Explore errors and exceptions
# MAGIC - Review assert statements
# MAGIC - Employ try-catch for exception handling

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
# MAGIC ### Syntax Errors
# MAGIC
# MAGIC In Python, there are mainly two different kinds of errors: Syntax Errors and Exceptions. Syntax Errors are errors that are thrown because code was typed incorrectly and Python does not know how to interpret it. 
# MAGIC
# MAGIC The example below illustrates a Syntax Error.

# COMMAND ----------

# if print("Hello World") # This is not correct Python code, so it throws a Syntax Error

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Exceptions
# MAGIC
# MAGIC If we have properly formatted code that Python knows how to run, we might still encounter errors as the code is executed. Errors that arise like this as the code is executed are known as Exceptions. They indicate that, while Python understood what we were trying to do, there is a problem.
# MAGIC
# MAGIC The example below illustrates an Exception.

# COMMAND ----------

# 1 / 0

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC This time we observed a **`ZeroDivisionError`** exception, indicating that we tried to divide by zero, which is not defined. There are different exceptions provided by Python that indicate different problems, a full list of the built-in ones can be found [here](https://docs.python.org/3/library/exceptions.html#bltin-exceptions).

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Exception Handling
# MAGIC
# MAGIC Syntax Errors will always cause our programs to exit and fail, but we can handle exceptions in Python. This allows us to program what happens in the case that Python encounters an exception or specific exceptions when trying to run a code block. To handle exceptions in Python we use a **`try`** statement. 
# MAGIC
# MAGIC We write a **`try`** statement like this:
# MAGIC
# MAGIC ```
# MAGIC try:
# MAGIC     code block
# MAGIC except:
# MAGIC     code block
# MAGIC
# MAGIC ```
# MAGIC
# MAGIC When Python encounters a **`try`** statement, it will first try to run the code in the **`try`** code block. If it encounters an exception, instead of exiting and erroring like we have seen, it will instead run the code block under **`except`**.

# COMMAND ----------

try:
    1/0 # Throws an exception
except:
    print("Exception Handled")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC In this last example, we run the **`except`** block if we encounter any exception in the **`try`** block. If we want to only handle a certain exception we can write the exception after the **`except`** keyword like this:
# MAGIC
# MAGIC ```
# MAGIC try:
# MAGIC     code block
# MAGIC except ExceptionName:
# MAGIC     code block
# MAGIC
# MAGIC ```

# COMMAND ----------

try:
    1/0 # Throws a ZeroDivisionError exception
except ZeroDivisionError:
    print("Exception Handled")

# COMMAND ----------

# try:
#     print(undefined_variable) # Throws a Name Error exception
# except ZeroDivisionError:
#     print("Exception Handled")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC If we want to handle multiple specific exceptions we can write a sequence of exceptions separated by commas inside parentheses. 
# MAGIC
# MAGIC Try commenting out one of the exception throwing lines below at a time, and notice that both exceptions are handled.

# COMMAND ----------

try:
    1/0 # Throws a ZeroDivisionError exception
    print(undefined_variable) # Throws a Name Error exception
except (ZeroDivisionError, NameError):
    print("Exception Handled")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC This now handles both the ZeroDivisionError and NameError exceptions.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Assertion Error
# MAGIC
# MAGIC One very useful exception is called an **`AssertionError`**. We can raise **`AssertionErrors`** using **`assert`** statements like this:
# MAGIC
# MAGIC ```
# MAGIC assert boolean expression, optional message
# MAGIC ```
# MAGIC
# MAGIC When Python executes this statement, it evaluates the boolean expression first. If it is **`True`**, Python does nothing and moves on. If it is **`False`**, then it throws an AssertionError with the optional message, if provided.

# COMMAND ----------

assert 1 == 1

# COMMAND ----------

# assert 1 == 2, "That is not true"

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2026 Databricks, Inc. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the <a href="https://www.apache.org/" target="_blank">Apache Software Foundation</a>.<br/><br/><a href="https://databricks.com/privacy-policy" target="_blank">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use" target="_blank">Terms of Use</a> | <a href="https://help.databricks.com/" target="_blank">Support</a>
