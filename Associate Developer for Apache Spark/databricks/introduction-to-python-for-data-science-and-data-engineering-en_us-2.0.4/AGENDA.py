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
# MAGIC # Introduction to Python for Data Science & Data Engineering
# MAGIC This course is intended for complete beginners to Python, providing the basics of programmatically interacting with data. The course begins with a basic introduction to programming expressions, variables, and data types. It then progresses into conditional and control statements, followed by an introduction to methods and functions. You will learn the basics of data structures, classes, and various string and utility functions. Lastly, you will gain experience using the Pandas library for data analysis and visualization, as well as the fundamentals of cloud computing. Throughout the course, you will gain hands-on practice through lab exercises, with additional resources to deepen your knowledge of programming after the class.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Prerequisites
# MAGIC The content was developed for participants with these skills/knowledge/abilities: 
# MAGIC - General familiarity with one or more programming languages
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC ## Course Agenda
# MAGIC  Lessons | Description |
# MAGIC |-------|-------------|
# MAGIC  **Introductions & Setup**     | *Registration, courseware & introductions*|
# MAGIC  **[Databricks Environment]($./ITP 00 - Databricks Environment)** | *Overview of the Databricks environment and course content* | 
# MAGIC  **[Data Types and Variables]($./ITP 01 - Data Types and Variables) & [Lab]($./Labs/ITP 01L - Data Types and Variables Lab)**  |  *Built-in data types, variable assignment statements, related functions* | 
# MAGIC  **[Control Flow]($./ITP 02 - Control Flow) & [Lab]($./Labs/ITP 02L - Control Flow Lab)**    | *Control flow of python programs using conditional statements* |
# MAGIC  **[Functions]($./ITP 03 - Functions) & [Lab]($./Labs/ITP 03L - Functions Lab)** | *Write and use functions to reuse and parameterize code* |
# MAGIC  **[Collection Types and Methods]($./ITP 04 - Collection Types and Methods) & [Lab]($./Labs/ITP 04L - Collection Types and Methods Lab)**      | *Advanced data types and methods*|
# MAGIC  **[Loops]($./ITP 05 - Loops) & [Lab]($./Labs/ITP 05L - Loops Lab)**| *More control flow statements with for-loops* |
# MAGIC  **[Exceptions]($./ITP 06 - Exceptions)**| *Assert statements and exception handling*  |
# MAGIC  **[Classes]($./ITP 07 - Classes) & [Lab]($./Labs/ITP 07L - Classes Lab)** | *Classes and custom data types* |
# MAGIC  **[Cloud Computing 101]($./ITP 08 - Cloud Computing 101)**| *Overview of cloud computing and how Databricks fits in*  |
# MAGIC  **[Libraries]($./ITP 09 - Libraries)**  | *Libraries, PyPI, and how use them* |
# MAGIC  **[Pandas Overview]($./ITP 10 - Pandas Overview) & [Lab]($./Labs/ITP 10L - Pandas Overview Lab)**    | *Industry standard library for data manipulation* |
# MAGIC  **[Advanced Pandas]($./ITP 11 - Advanced Pandas) & [Lab]($./Labs/ITP 11L - Advanced Pandas Lab)** |  *More advanced Pandas functionality*|
# MAGIC  **[Data Visualization]($./ITP 12 - Data Visualization) & [Lab]($./Labs/ITP 12L - Data Visualization Lab)**      | *Visualizing data with Databricks, Pandas, and Seaborn*|
# MAGIC  **[Scaling Pandas with Spark]($./ITP 13 - Scaling Pandas with Spark)**  | *Write Pandas code that leverages Spark under the hood*|
# MAGIC  **[Additional Resources]($./ITP 14 - Additional Resources)**  | *Explore additional resources for continuing your python and data science journey* |
# MAGIC
# MAGIC ---
# MAGIC ### Requirements
# MAGIC
# MAGIC Please review the following requirements before starting the lesson:
# MAGIC
# MAGIC * To run demo and lab notebooks, you need to use the following Databricks runtime: **`17.3.x-scala2.13`**

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2026 Databricks, Inc. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the <a href="https://www.apache.org/" target="_blank">Apache Software Foundation</a>.<br/><br/><a href="https://databricks.com/privacy-policy" target="_blank">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use" target="_blank">Terms of Use</a> | <a href="https://help.databricks.com/" target="_blank">Support</a>
