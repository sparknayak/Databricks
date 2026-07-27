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
# MAGIC
# MAGIC # Libraries
# MAGIC <!-- ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)  -->
# MAGIC
# MAGIC In this lesson you:
# MAGIC - Explore the Databricks **%run** feature
# MAGIC - Introduce libraries and PyPI

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
# MAGIC
# MAGIC ### %run
# MAGIC
# MAGIC So far, we have been running individual cells in a single notebook or using **Run All** in the notebook toolbar to run all of the executable command cells in sequence from top to bottom.
# MAGIC
# MAGIC Databricks also supports the **%run** magic command to allow one notebook to run all of the executable command cells in a *different* notebook.
# MAGIC
# MAGIC When we do this, we also get access to that other notebook's state, which means all of the classes, functions, and variables defined in that notebook.
# MAGIC
# MAGIC The **%run** magic command must appear at the top of a command cell, followed by the path to the other notebook. You can *not* have any Python code in the command cell before or after the **%run** magic command

# COMMAND ----------

# MAGIC %run ./Includes/run_example

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC The example notebook defines the function **`greet()`**, which takes in a name and returns a greeting. Since we now have access to that notebook's state, we can use **`greet()`** even though it was not defined in the notebook. This is a useful way to define & test helper functions without cluttering up your main notebook.

# COMMAND ----------

greet("Bob")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### PyPI and Python Libraries
# MAGIC
# MAGIC This idea of storing collections of useful definitions in libraries to access in different files extends beyond the Databricks Environment. In fact, when Python is installed on a system it usually includes a useful collection of utilities called the [Python Standard Library](https://docs.python.org/3/library/). Furthermore, developers can share any libraries they create with the Python community by uploading them online. 
# MAGIC
# MAGIC <a href="https://pypi.org/" target="_blank">PyPI</a>, which stands for the Python Package Index, is the central repository where developers upload and share their libraries, and where users can download them. It contains thousands of libraries for a wide variety of uses. Some of them have become the industry standard for certain use cases and help standardize code in an industry. 
# MAGIC
# MAGIC
# MAGIC By default, Python does not have access to these libraries. Before you can import a library to use in your program, you must first install it from PyPI on your system.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC #### pip
# MAGIC
# MAGIC pip is the tool most often used to actually download a library from PyPI. It is usually included in your Python installation. 
# MAGIC
# MAGIC In a command line or terminal, simply type **`pip install package_name`**. If we wanted to install **`numpy`**, a popular library, for example, we would write **`pip install numpy`**.
# MAGIC
# MAGIC The Databricks environment is a little different. Rather than typing **`pip install package_name`** into a terminal, we would write **`%pip install package_name`** into a cell. The Databricks cell is expecting Python code, and **`%pip`** tells it to expect a pip command instead.
# MAGIC
# MAGIC **Note:** In Databricks, this type of command will restart the Python terminal, so it's best to use it at the top of a notebook to not lose the results of code ran before.

# COMMAND ----------

# MAGIC %pip --help

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC The following code cell will restart the Python interpreter, which means you will have to re-run the `./Includes/run_example` notebook to have access to `greet()`.

# COMMAND ----------

# MAGIC %pip install numpy

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Let's say we wanted a function to take the square root of a number. Python doesn't have this built-in but <a href="https://numpy.org/doc/stable/" target="_blank">numpy</a> does.
# MAGIC
# MAGIC Fortunately, our Databricks environment comes with several useful libraries preinstalled, including **`numpy`**. For more information, you can refer to the <a href="https://docs.databricks.com/en/release-notes/runtime/index.html" target="_blank">Databricks Runtime Release Notes</a>. So, for now, we will only have to import the one we want.
# MAGIC
# MAGIC The first step is to tell Python that we want to use the features defined by **`numpy`** by *importing* it. The simplest way to import a library installed on your system is to use the **`import`** statement as shown below:

# COMMAND ----------

import numpy

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC Now to access functions defined in the **`numpy`** library once imported, you write **`numpy.function_name(arguments)`**.
# MAGIC
# MAGIC Let's see this for the square root function which is defined in numpy as **`sqrt(arguments)`**.

# COMMAND ----------

numpy.sqrt(4.0)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC We can create an alias when importing the library as well.

# COMMAND ----------

import numpy as np

np.sqrt(4.0)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC We can also import specific functions from libraries.

# COMMAND ----------

from numpy import sqrt

sqrt(4.0)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC #### `help()`
# MAGIC
# MAGIC Recall the **`help()`** function that displays documentation for the item passed into it. We can use **`help()`** both on a library and anything defined in that library.

# COMMAND ----------

help(np)

# COMMAND ----------

help(np.sqrt)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC Note that while creating a library is outside the scope of this introductory course, all of the functions and classes they define are defined in the same way we have seen.

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2026 Databricks, Inc. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the <a href="https://www.apache.org/" target="_blank">Apache Software Foundation</a>.<br/><br/><a href="https://databricks.com/privacy-policy" target="_blank">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use" target="_blank">Terms of Use</a> | <a href="https://help.databricks.com/" target="_blank">Support</a>
