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
# MAGIC # Databricks Environment
# MAGIC
# MAGIC <!-- ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)  -->
# MAGIC
# MAGIC In this lesson you:<br>
# MAGIC * Use Databricks to: 
# MAGIC   * Create a cluster
# MAGIC   * Run code in a notebook
# MAGIC   * Export notebooks
# MAGIC
# MAGIC
# MAGIC References:
# MAGIC * Databricks documentation on <a href="https://docs.databricks.com/" target="_blank">AWS</a>, <a href="https://docs.microsoft.com/en-us/azure/databricks/" target="_blank">Azure</a>, and <a href="https://docs.gcp.databricks.com/" target="_blank">GCP</a>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ## Create a Cluster
# MAGIC
# MAGIC Before we can run any code, we have to set up a cluster (a cluster is what will execute the code). 
# MAGIC
# MAGIC 1. Click the **Compute** Tab in the left sidebar.
# MAGIC 1. Click the **Create with Personal Compute**.
# MAGIC 1. *(optional)* Edit the name of the cluster.
# MAGIC 1. Configure the following settings:
# MAGIC    * Select **Single node**.
# MAGIC    * Set **Access mode** to **Single user**. Leave **Single user access** as the default (your user id).
# MAGIC    * Set **Databricks runtime version** to **17.3 LTS**.
# MAGIC 1. Click **Create compute**.
# MAGIC
# MAGIC Now we can return to the notebook and attach it to the cluster we just created.
# MAGIC
# MAGIC **NOTE**: In Databricks-provided workspaces, you may not have permission to create clusters.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC
# MAGIC ## Run code
# MAGIC
# MAGIC * Each notebook specifies a default language, in this case **Python**.
# MAGIC * Run the cell below using one of the following options:
# MAGIC   * **CTRL+ENTER** or **CMD+RETURN**
# MAGIC   * **SHIFT+ENTER** or **SHIFT+RETURN** to run the cell and move to the next one
# MAGIC   * Using **Run Cell**, **Run All Above** or **Run All Below** as seen here<br/>
# MAGIC   <!-- <img style="box-shadow: 5px 5px 5px 0px rgba(0,0,0,0.25); border: 1px solid rgba(0,0,0,0.25);" src="https://files.training.databricks.com/images/notebook-cell-run-cmd.png"/> -->
# MAGIC
# MAGIC Feel free to tweak the code below if you like:

# COMMAND ----------

print("I'm running Python!")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### Magic Command: &percnt;md
# MAGIC
# MAGIC Our favorite Magic Command **&percnt;md** allows us to render Markdown in a cell:
# MAGIC * Double click this cell to begin editing it
# MAGIC * Then press the **`Esc`** key to stop editing
# MAGIC
# MAGIC # Title One
# MAGIC ## Title Two
# MAGIC ### Title Three
# MAGIC
# MAGIC This is a test of the emergency broadcast system. This is only a test.
# MAGIC
# MAGIC This is text with a **bold** word in it.
# MAGIC
# MAGIC This is text with an *italicized* word in it.
# MAGIC
# MAGIC This is an ordered list
# MAGIC
# MAGIC 1. one
# MAGIC 2. two
# MAGIC 3. three
# MAGIC
# MAGIC This is an unordered list
# MAGIC
# MAGIC * apples
# MAGIC * peaches
# MAGIC * bananas
# MAGIC
# MAGIC Links/Embedded HTML: <a href="https://www.markdownguide.org/getting-started/" target="_blank">What is Markdown?</a>
# MAGIC
# MAGIC <!-- Images:  
# MAGIC ![Spark Engines](https://files.training.databricks.com/images/Apache-Spark-Logo_TM_200px.png) -->
# MAGIC
# MAGIC And of course, tables:
# MAGIC
# MAGIC | Name  | Age | Breed    |
# MAGIC |-------|-----|--------|
# MAGIC | Buddy   | 2  | Golden Retriever   |
# MAGIC | Bingo  | 10  | Border Collie |
# MAGIC | Momo  | 3  | Lab   |

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ## Learning More
# MAGIC
# MAGIC We like to encourage you to explore the documentation to learn more about the various features of the Databricks Data Intelligence platform and notebooks.
# MAGIC * <a href="https://docs.databricks.com/user-guide/index.html" target="_blank">User Guide</a>
# MAGIC * <a href="https://docs.databricks.com/user-guide/notebooks/index.html" target="_blank">User Guide / Notebooks</a>
# MAGIC * <a href="https://docs.databricks.com/administration-guide/index.html" target="_blank">Administration Guide</a>
# MAGIC * <a href="https://docs.databricks.com/release-notes/index.html" target="_blank">Release Notes</a>
# MAGIC * <a href="https://docs.databricks.com/" target="_blank">And much more!</a>

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2026 Databricks, Inc. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the <a href="https://www.apache.org/" target="_blank">Apache Software Foundation</a>.<br/><br/><a href="https://databricks.com/privacy-policy" target="_blank">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use" target="_blank">Terms of Use</a> | <a href="https://help.databricks.com/" target="_blank">Support</a>
