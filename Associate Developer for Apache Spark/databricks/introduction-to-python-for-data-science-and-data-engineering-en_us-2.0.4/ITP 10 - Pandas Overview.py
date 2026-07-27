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
# MAGIC # Pandas Overview
# MAGIC
# MAGIC **<a href="https://pandas.pydata.org/pandas-docs/stable/reference/index.html" target="_blank">Pandas</a>** is a popular Python library among data scientists with high performing, easy-to-use data structures and data analysis tools.
# MAGIC
# MAGIC <!-- ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)  -->
# MAGIC
# MAGIC In this lesson you:
# MAGIC * Explain what **`pandas`** is and why it's so popular
# MAGIC * Create and manipulate **`pandas`** **`DataFrame`** and **`Series`**
# MAGIC * Perform operations on **`pandas`** objects
# MAGIC
# MAGIC First, let us import **`pandas`** with the alias **`pd`** so we can refer to the library without having to type **`pandas`** out each time. **`pandas`** is pre-installed on Databricks.
# MAGIC

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

import pandas as pd

# COMMAND ----------

# MAGIC %md
# MAGIC #### Why `pandas`?
# MAGIC
# MAGIC * More and more, data is leading decision making.
# MAGIC * Excel is great but what if...
# MAGIC   - You want to automate your analysis so it re-runs on new data each day?
# MAGIC   - You want to build a code base to share with your colleagues?
# MAGIC   - You want more robust analyses to feed a business decision?
# MAGIC   - You want to do machine learning?
# MAGIC * **`pandas`** is one of the core libraries used by data analysts and data scientists in Python.

# COMMAND ----------

# MAGIC %md
# MAGIC ## `DataFrame`
# MAGIC
# MAGIC We have seen how different data types provide different kinds of data and functionality. 
# MAGIC
# MAGIC **`pandas` is a library that provides data types and functions that allows us to do rigorous, programmatic data analysis.** 
# MAGIC - The core **`pandas`** data type is called a **`DataFrame`**.
# MAGIC
# MAGIC A [**DataFrame**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) is a two dimensional table of named rows and columns, similar to a SQL table. 
# MAGIC
# MAGIC - The **`DataFrame`** class has a **`data`** attribute for the data in the table that we have to define when we instantiate a **`DataFrame`** object.
# MAGIC
# MAGIC Let's say we want to make the following table into a **`DataFrame`**:
# MAGIC
# MAGIC | Name    | Age | Job|
# MAGIC | ----------- | ----------- | ----------- | 
# MAGIC | John   | 30    | Journalist |
# MAGIC | Mary    | 30       | Programmer |
# MAGIC | Abe     | 40       | Chef |
# MAGIC
# MAGIC One way to do this is to create a list of lists where each list in the list represents a row of data:

# COMMAND ----------

data = [["John", 30, "Journalist"], ["Mary", 30, "Programmer"], ["Abe", 40, "Chef"]]

df = pd.DataFrame(data=data)
df

# COMMAND ----------

# MAGIC %md
# MAGIC As you can see, we have a list of lists called **"data"** where each inner list represents a row of data with three elements specifying a name, age, and job title. We then instantiate a **`DataFrame`** based on that data.
# MAGIC
# MAGIC Recall that we create an object of a custom class like **`object = Class()`**. Since **`DataFrame`** is defined in **`pandas`** we use **`pd.DataFrame()`**.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Adding Column Names
# MAGIC
# MAGIC The 0, 1, 2 column names above are default values. To specify the column names we want, **`DataFrame`** has another attribute: **`columns`**

# COMMAND ----------

cols = ["Name", "Age", "Job"]
df = pd.DataFrame(data=data, columns=cols)
df

# COMMAND ----------

# MAGIC %md
# MAGIC ## `Series`
# MAGIC
# MAGIC The other main data type that **`pandas`** provides is the [**Series**](https://pandas.pydata.org/docs/reference/api/pandas.Series.html).
# MAGIC
# MAGIC A **`Series`** is just one column of the **`DataFrame`**.
# MAGIC
# MAGIC We can select a **`Series`** in two ways:
# MAGIC
# MAGIC 1. **`df["column_name"]`**
# MAGIC 2. **`df.column_name`**
# MAGIC
# MAGIC Let's select the **`Age`** column below:

# COMMAND ----------

df["Age"]

# COMMAND ----------

df.Age

# COMMAND ----------

# MAGIC %md
# MAGIC Here we see two approaches:
# MAGIC * indexing (normally associated with lists), and 
# MAGIC * attribute reference
# MAGIC
# MAGIC These operations have implementations in DataFrames to simplify searching and matching of columns. It is preferred to use **`df["column_name"]`** to access a column, because the **`df.column_name`** notation does not work well when there are spaces in the column names.

# COMMAND ----------

# MAGIC %md
# MAGIC ## dtypes
# MAGIC
# MAGIC If you look at the **`Series`** object above you can see **`dtype: int64`**. 
# MAGIC
# MAGIC In **`pandas`** *dtypes*, which is an abbreviation for data types, refers to the type of the values in the column. 
# MAGIC
# MAGIC We will next look at some of the methods and functionality that **`DataFrame`** and **`Series`** provide, but much like how object types determine what you can do with them, the [**dtype**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html) of a column determines what functionality we can do with it.
# MAGIC
# MAGIC For example, we can take the average of a numeric column, but not a non-numeric one. 
# MAGIC
# MAGIC The **`dtypes`** of columns are specific to **`pandas`**, but the most common ones are very similar to the built-in Python types:
# MAGIC
# MAGIC 1. **`object`** is just text, which is similar to strings
# MAGIC 2. **`int64`** are integers
# MAGIC 3. **`float64`** are float
# MAGIC 4. **`bool`** are boolean
# MAGIC
# MAGIC
# MAGIC We can view the **`dtypes`** of every column in our **`DataFrame`** by accessing its **`dtypes`** attribute:

# COMMAND ----------

# MAGIC %md
# MAGIC ## `Series` Operations
# MAGIC
# MAGIC We can use operations on **`Series`** of a certain dtype that are similar to the operations we can do with the dtype's similar built-in counterpart. 
# MAGIC
# MAGIC These operations act element-wise. 
# MAGIC
# MAGIC For example, we can add **`int64`** **`Series`** similarly to how we can add integer values in Python.

# COMMAND ----------

df["Age"] + df["Age"]

# COMMAND ----------

# MAGIC %md
# MAGIC We can use all basic integer operations here:

# COMMAND ----------

df["Age"] * 3 - 1

# COMMAND ----------

# MAGIC %md
# MAGIC #### Selecting a value from a **`Series`**
# MAGIC
# MAGIC Sometimes we will want to pull out a value in a **`Series`**. We can index into a **`Series`** similar to how we index into a list to pull out values:

# COMMAND ----------

df["Age"][0]

# COMMAND ----------

# MAGIC %md
# MAGIC ## Selecting a Subset of Columns
# MAGIC
# MAGIC We have seen how to select a given column as a **`Series`**.
# MAGIC
# MAGIC We can also select a subset of columns as a **`DataFrame`**.
# MAGIC
# MAGIC We can select a subset of columns like this:
# MAGIC
# MAGIC **`df[[col_1, col_2, col_3, ...]]`**
# MAGIC
# MAGIC Let's select only the Name and Age columns:

# COMMAND ----------

df[["Name", "Age"]]

# COMMAND ----------

# MAGIC %md
# MAGIC ## Mutability of DataFrame objects
# MAGIC
# MAGIC When performing operations that modify a DataFrame, a new object is returned by default, leaving the original intact. Consider the following operation.

# COMMAND ----------

df.drop("Age", axis=1)

# COMMAND ----------

# MAGIC %md
# MAGIC Here, we're dropping the **`Age`** column and displaying the result. This result is a new object that is promptly forgotten since we haven't stored it in a variable for later use, using a pattern like **`new_df = df.drop(...)`**.
# MAGIC
# MAGIC The following proves the original DataFrame **`df`** has not been modified.

# COMMAND ----------

df

# COMMAND ----------

# MAGIC %md
# MAGIC This behavior is generally desirable since it makes coding and maintaining complex pipelines easier. However, sometimes it's convenient to modify the DataFrame in place, which can be done using the **`inplace`** parameter as follows.

# COMMAND ----------

df.drop("Age", axis=1, inplace=True)

# COMMAND ----------

# MAGIC %md
# MAGIC In this instance, no new object has been returned. Let's demonstrate that the result has been applied to the original DataFrame.

# COMMAND ----------

df

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2026 Databricks, Inc. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the <a href="https://www.apache.org/" target="_blank">Apache Software Foundation</a>.<br/><br/><a href="https://databricks.com/privacy-policy" target="_blank">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use" target="_blank">Terms of Use</a> | <a href="https://help.databricks.com/" target="_blank">Support</a>
