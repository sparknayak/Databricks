# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "2"
# ///
# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 1**
# MAGIC
# MAGIC A data organization leader is upset about the data analysis team’s reports being different from the data engineering team’s reports. The leader believes the siloed nature of their organization’s data engineering and data analysis architectures is to blame.
# MAGIC
# MAGIC **Which of the following describes how a data lakehouse could alleviate this issue?**
# MAGIC
# MAGIC - **A.** Both teams would autoscale their work as data size evolves  
# MAGIC - **B.** Both teams would use the same source of truth for their work  
# MAGIC - **C.** Both teams would reorganize to report to the same department  
# MAGIC - **D.** Both teams would be able to collaborate on projects in real-time  
# MAGIC - **E.** Both teams would respond more quickly to ad-hoc requests

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 2**
# MAGIC
# MAGIC Which of the following describes a scenario in which a data team will want to utilize cluster pools?
# MAGIC
# MAGIC - **A.** An automated report needs to be refreshed as quickly as possible.
# MAGIC - **B.** An automated report needs to be made reproducible.
# MAGIC - **C.** An automated report needs to be tested to identify errors.
# MAGIC - **D.** An automated report needs to be version-controlled across multiple collaborators.
# MAGIC - **E.** An automated report needs to be runnable by all stakeholders.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 3**
# MAGIC
# MAGIC Which of the following is hosted completely in the control plane of the classic Databricks architecture?
# MAGIC
# MAGIC - **A.** Worker node  
# MAGIC - **B.** JDBC data source  
# MAGIC - **C.** Databricks web application  
# MAGIC - **D.** Databricks Filesystem  
# MAGIC - **E.** Driver node

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 4**
# MAGIC
# MAGIC Which of the following benefits of using the Databricks Lakehouse Platform is provided by Delta Lake?
# MAGIC
# MAGIC - **A.** The ability to manipulate the same data using a variety of languages  
# MAGIC - **B.** The ability to collaborate in real time on a single notebook  
# MAGIC - **C.** The ability to set up alerts for query failures  
# MAGIC - **D.** The ability to support batch and streaming workloads  
# MAGIC - **E.** The ability to distribute complex data operations

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 5**
# MAGIC
# MAGIC Which of the following describes the storage organization of a Delta table?
# MAGIC
# MAGIC - **A.** Delta tables are stored in a single file that contains data, history, metadata, and other attributes.
# MAGIC - **B.** Delta tables store their data in a single file and all metadata in a collection of files in a separate location.
# MAGIC - **C.** Delta tables are stored in a collection of files that contain data, history, metadata, and other attributes.
# MAGIC - **D.** Delta tables are stored in a collection of files that contain only the data stored within the table.
# MAGIC - **E.** Delta tables are stored in a single file that contains only the data stored within the table.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 6**
# MAGIC
# MAGIC Which of the following code blocks will remove the rows where the value in column `age` is greater than 25 from the existing Delta table `my_table` and save the updated table?
# MAGIC
# MAGIC - **A.** `SELECT * FROM my_table WHERE age > 25;`
# MAGIC - **B.** `UPDATE my_table WHERE age > 25;`
# MAGIC - **C.** `DELETE FROM my_table WHERE age > 25;`
# MAGIC - **D.** `UPDATE my_table WHERE age <= 25;`
# MAGIC - **E.** `DELETE FROM my_table WHERE age <= 25;`

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 7**
# MAGIC
# MAGIC A data engineer has realized that they made a mistake when making a daily update to a table. They need to use Delta time travel to restore the table to a version that is 3 days old. However, when the data engineer attempts to time travel to the older version, they are unable to restore the data because the data files have been deleted.
# MAGIC
# MAGIC **Which of the following explains why the data files are no longer present?**
# MAGIC
# MAGIC - **A.** The VACUUM command was run on the table  
# MAGIC - **B.** The TIME TRAVEL command was run on the table  
# MAGIC - **C.** The DELETE HISTORY command was run on the table  
# MAGIC - **D.** The OPTIMIZE command was nun on the table  
# MAGIC - **E.** The HISTORY command was run on the table

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 8**
# MAGIC
# MAGIC Which of the following Git operations must be performed outside of Databricks Repos?
# MAGIC
# MAGIC - **A.** Commit  
# MAGIC - **B.** Pull  
# MAGIC - **C.** Push  
# MAGIC - **D.** Clone  
# MAGIC - **E.** Merge

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 9**
# MAGIC
# MAGIC Which of the following data lakehouse features results in improved data quality over a traditional data lake?
# MAGIC
# MAGIC - **A.** A data lakehouse provides storage solutions for structured and unstructured data.
# MAGIC - **B.** A data lakehouse supports ACID-compliant transactions.
# MAGIC - **C.** A data lakehouse allows the use of SQL queries to examine data.
# MAGIC - **D.** A data lakehouse stores data in open formats.
# MAGIC - **E.** A data lakehouse enables machine learning and artificial Intelligence workloads.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 10**
# MAGIC
# MAGIC A data engineer needs to determine whether to use the built-in Databricks Notebooks versioning or version their project using Databricks Repos.
# MAGIC
# MAGIC **Which of the following is an advantage of using Databricks Repos over the Databricks Notebooks versioning?**
# MAGIC
# MAGIC - **A.** Databricks Repos automatically saves development progress  
# MAGIC - **B.** Databricks Repos supports the use of multiple branches  
# MAGIC - **C.** Databricks Repos allows users to revert to previous versions of a notebook  
# MAGIC - **D.** Databricks Repos provides the ability to comment on specific changes  
# MAGIC - **E.** Databricks Repos is wholly housed within the Databricks Lakehouse Platform

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 11**
# MAGIC
# MAGIC A data engineer has left the organization. The data team needs to transfer ownership of the data engineer’s Delta tables to a new data engineer. The new data engineer is the lead engineer on the data team.
# MAGIC
# MAGIC Assuming the original data engineer no longer has access, which of the following individuals must be the one to transfer ownership of the Delta tables in Data Explorer?
# MAGIC
# MAGIC - **A.** Databricks account representative  
# MAGIC - **B.** This transfer is not possible  
# MAGIC - **C.** Workspace administrator  
# MAGIC - **D.** New lead data engineer  
# MAGIC - **E.** Original data engineer

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 12
# MAGIC
# MAGIC A data analyst has created a Delta table `sales` that is used by the entire data analysis team. They want help from the data engineering team to implement a series of tests to ensure the data is clean. However, the data engineering team uses Python for its tests rather than SQL.
# MAGIC
# MAGIC Which of the following commands could the data engineering team use to access `sales` in PySpark?
# MAGIC
# MAGIC - **A.** SELECT * FROM sales  
# MAGIC - **B.** There is no way to share data between PySpark and SQL.  
# MAGIC - **C.** spark.sql("sales")  
# MAGIC - **D.** spark.delta.table("sales")  
# MAGIC - **E.** spark.table("sales")

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 13
# MAGIC
# MAGIC Which of the following commands will return the location of database `customer360`?
# MAGIC
# MAGIC - **A.** DESCRIBE LOCATION customer360;
# MAGIC - **B.** DROP DATABASE customer360;
# MAGIC - **C.** DESCRIBE DATABASE customer360;
# MAGIC - **D.** ALTER DATABASE customer360 SET DBPROPERTIES ('location' = '/user'};
# MAGIC - **E.** USE DATABASE customer360;

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 14
# MAGIC
# MAGIC A data engineer wants to create a new table containing the names of customers that live in France.  
# MAGIC They have written the following command:  
# MAGIC ![image_1777379614695.png](./image_1777379614695.png "image_1777379614695.png")
# MAGIC
# MAGIC
# MAGIC
# MAGIC A senior data engineer mentions that it is organization policy to include a table property  
# MAGIC indicating that the new table includes personally identifiable information (PII).  
# MAGIC Which of the following lines of code fills in the above blank to successfully complete the task?
# MAGIC
# MAGIC - **A.** There is no way to indicate whether a table contains PII.
# MAGIC - **B.** "COMMENT PII"
# MAGIC - **C.** TBLPROPERTIES PII
# MAGIC - **D.** COMMENT "Contains PII"
# MAGIC - **E.** PII

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 15**
# MAGIC
# MAGIC Which of the following benefits is provided by the array functions from Spark SQL?
# MAGIC
# MAGIC - **A.** An ability to work with data in a variety of types at once  
# MAGIC - **B.** An ability to work with data within certain partitions and windows  
# MAGIC - **C.** An ability to work with time-related data in specified intervals  
# MAGIC - **D.** An ability to work with complex, nested data ingested from JSON files  
# MAGIC - **E.** An ability to work with an array of tables for procedural automation

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 16**
# MAGIC
# MAGIC Which of the following commands can be used to write data into a Delta table while avoiding the writing of duplicate records?
# MAGIC
# MAGIC - **A.** DROP  
# MAGIC - **B.** IGNORE  
# MAGIC - **C.** MERGE  
# MAGIC - **D.** APPEND  
# MAGIC - **E.** INSERT

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 17**
# MAGIC
# MAGIC **A data engineer needs to apply custom logic to string column `city` in table `stores` for a specific use case. In order to apply this custom logic at scale, the data engineer wants to create a SQL user-defined function (UDF).**
# MAGIC
# MAGIC **Which of the following code blocks creates this SQL UDF?**
# MAGIC
# MAGIC - **A.** ![image_1777379255087.png](./image_1777379255087.png "image_1777379255087.png")
# MAGIC
# MAGIC - **B.** ![image_1777379268686.png](./image_1777379268686.png "image_1777379268686.png")
# MAGIC
# MAGIC - **C.** ![image_1777379396381.png](./image_1777379396381.png "image_1777379396381.png")
# MAGIC
# MAGIC - **D.** ![image_1777379281712.png](./image_1777379281712.png "image_1777379281712.png")
# MAGIC
# MAGIC - **E.** ![image_1777379294512.png](./image_1777379294512.png "image_1777379294512.png")

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 18**
# MAGIC
# MAGIC A data analyst has a series of queries in a SQL program. The data analyst wants this program to run every day. They only want the final query in the program to run on Sundays. They ask for help from the data engineering team to complete this task.
# MAGIC
# MAGIC **Which of the following approaches could be used by the data engineering team to complete this task?**
# MAGIC
# MAGIC - **A.** They could submit a feature request with Databricks to add this functionality.
# MAGIC - **B.** They could wrap the queries using PySpark and use Python’s control flow system to determine when to run the final query.
# MAGIC - **C.** They could only run the entire program on Sundays.
# MAGIC - **D.** They could automatically restrict access to the source table in the final query so that it is only accessible on Sundays.
# MAGIC - **E.** They could redesign the data model to separate the data used in the final query into a new table.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 19**
# MAGIC
# MAGIC A data engineer runs a statement every day to copy the previous day’s sales into the table `transactions`. Each day’s sales are in their own file in the location `"/transactions/raw"`.
# MAGIC
# MAGIC Today, the data engineer runs the following command to complete this task:  
# MAGIC ![image_1777378395792.png](./image_1777378395792.png "image_1777378395792.png")  
# MAGIC After running the command today, the data engineer notices that the number of records in table `transactions` has not changed.
# MAGIC
# MAGIC **Which of the following describes why the statement might not have copied any new records into the table?**
# MAGIC
# MAGIC - **A.** The format of the files to be copied were not included with the FORMAT_OPTIONS keyword.
# MAGIC - **B.** The names of the files to be copied were not included with the FILES keyword.
# MAGIC - **C.** The previous day’s file has already been copied into the table.
# MAGIC - **D.** The PARQUET file format does not support COPY INTO.
# MAGIC - **E.** The COPY INTO statement requires the table to be refreshed to view the copied rows.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 20**
# MAGIC
# MAGIC A data engineer needs to create a table in Databricks using data from their organization’s existing SQLite database.  
# MAGIC They run the following command:  
# MAGIC ![image_1777378517671.png](./image_1777378517671.png "image_1777378517671.png")  
# MAGIC Which of the following lines of code fills in the above blank to successfully complete the task?
# MAGIC
# MAGIC - **A.** org.apache.spark.sql.jdbc  
# MAGIC - **B.** autoloader  
# MAGIC - **C.** DELTA  
# MAGIC - **D.** sqlite  
# MAGIC - **E.** org.apache.spark.sql.sqlite

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 21
# MAGIC
# MAGIC A data engineering team has two tables. The first table `march_transactions` is a collection of all retail transactions in the month of March. The second table `april_transactions` is a collection of all retail transactions in the month of April. There are no duplicate records between the tables.
# MAGIC
# MAGIC Which of the following commands should be run to create a new table `all_transactions` that contains all records from `march_transactions` and `april_transactions` without duplicate records?
# MAGIC
# MAGIC - **A.** CREATE TABLE all_transactions AS SELECT * FROM march_transactions INNER JOIN SELECT * FROM april_transactions;
# MAGIC - **B.** CREATE TABLE all_transactions AS SELECT * FROM march_transactions UNION SELECT * FROM april_transactions;
# MAGIC - **C.** CREATE TABLE all_transactions AS SELECT * FROM march_transactions OUTER JOIN SELECT * FROM april_transactions;
# MAGIC - **D.** CREATE TABLE all_transactions AS SELECT * FROM march_transactions INTERSECT SELECT * from april_transactions;
# MAGIC - **E.** CREATE TABLE all_transactions AS SELECT * FROM march_transactions MERGE SELECT * FROM april_transactions;

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC **Question #: 22**
# MAGIC
# MAGIC A data engineer only wants to execute the final block of a Python program if the Python variable `day_of_week` is equal to 1 and the Python variable `review_period` is True.
# MAGIC
# MAGIC Which of the following control flow statements should the data engineer use to begin this conditionally executed code block?
# MAGIC
# MAGIC - **A.** if day_of_week = 1 and review_period:
# MAGIC - **B.** if day_of_week = 1 and review_period = "True":
# MAGIC - **C.** if day_of_week == 1 and review_period == "True":
# MAGIC - **D.** if day_of_week == 1 and review_period:
# MAGIC - **E.** if day_of_week = 1 & review_period: = "True":
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 23**
# MAGIC
# MAGIC A data engineer is attempting to drop a Spark SQL table `my_table`. The data engineer wants to delete all table metadata and data.
# MAGIC
# MAGIC They run the following command:  
# MAGIC `DROP TABLE IF EXISTS my_table`
# MAGIC
# MAGIC While the object no longer appears when they run `SHOW TABLES`, the data files still exist. Which of the following describes why the data files still exist and the metadata files were deleted?
# MAGIC
# MAGIC - **A.** The table’s data was larger than 10 GB  
# MAGIC - **B.** The table’s data was smaller than 10 GB  
# MAGIC - **C.** The table was external  
# MAGIC - **D.** The table did not have a location  
# MAGIC - **E.** The table was managed

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC **Question #: 24**
# MAGIC
# MAGIC A data engineer wants to create a data entity from a couple of tables. The data entity must be used by other data engineers in other sessions. It also must be saved to a physical location.
# MAGIC
# MAGIC Which of the following data entities should the data engineer create?
# MAGIC
# MAGIC - **A.** Database  
# MAGIC - **B.** Function  
# MAGIC - **C.** View  
# MAGIC - **D.** Temporary view  
# MAGIC - **E.** Table  
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC **Question #: 25**
# MAGIC
# MAGIC A data engineer is maintaining a data pipeline. Upon data ingestion, the data engineer notices that the source data is starting to have a lower level of quality. The data engineer would like to automate the process of monitoring the quality level.
# MAGIC
# MAGIC Which of the following tools can the data engineer use to solve this problem?
# MAGIC
# MAGIC - **A.** Unity Catalog  
# MAGIC - **B.** Data Explorer  
# MAGIC - **C.** Delta Lake  
# MAGIC - **D.** Delta Live Tables  
# MAGIC - **E.** Auto Loader  
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 26**
# MAGIC
# MAGIC A Delta Live Table pipeline includes two datasets defined using STREAMING LIVE TABLE. Three datasets are defined against Delta Lake table sources using LIVE TABLE.
# MAGIC The table is configured to run in Production mode using the Continuous Pipeline Mode. Assuming previously unprocessed data exists and all definitions are valid, what is the expected outcome after clicking Start to update the pipeline?
# MAGIC
# MAGIC - **A.** All datasets will be updated at set intervals until the pipeline is shut down. The compute resources will persist to allow for additional testing.
# MAGIC - **B.** All datasets will be updated once and the pipeline will persist without any processing. The compute resources will persist but go unused.
# MAGIC - **C.** All datasets will be updated at set intervals until the pipeline is shut down. The compute resources will be deployed for the update and terminated when the pipeline is stopped.
# MAGIC - **D.** All datasets will be updated once and the pipeline will shut down. The compute resources will be terminated.
# MAGIC - **E.** All datasets will be updated once and the pipeline will shut down. The compute resources will persist to allow for additional testing.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 27
# MAGIC
# MAGIC In order for Structured Streaming to reliably track the exact progress of the processing so that it can handle any kind of failure by restarting and/or reprocessing, which of the following two approaches is used by Spark to record the offset range of the data being processed in each trigger?
# MAGIC
# MAGIC A. Checkpointing and Write-ahead Logs  
# MAGIC B. Structured Streaming cannot record the offset range of the data being processed in each trigger.  
# MAGIC C. Replayable Sources and Idempotent Sinks  
# MAGIC D. Write-ahead Logs and Idempotent Sinks  
# MAGIC E. Checkpointing and Idempotent Sinks  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 28**
# MAGIC
# MAGIC Which of the following describes the relationship between Gold tables and Silver tables?
# MAGIC
# MAGIC - **A.** Gold tables are more likely to contain aggregations than Silver tables.
# MAGIC - **B.** Gold tables are more likely to contain valuable data than Silver tables.
# MAGIC - **C.** Gold tables are more likely to contain a less refined view of data than Silver tables.
# MAGIC - **D.** Gold tables are more likely to contain more data than Silver tables.
# MAGIC - **E.** Gold tables are more likely to contain truthful data than Silver tables.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 29
# MAGIC
# MAGIC Which of the following describes the relationship between Bronze tables and raw data?
# MAGIC
# MAGIC - **A.** Bronze tables contain less data than raw data files.
# MAGIC - **B.** Bronze tables contain more truthful data than raw data.
# MAGIC - **C.** Bronze tables contain aggregates while raw data is unaggregated.
# MAGIC - **D.** Bronze tables contain a less refined view of data than raw data.
# MAGIC - **E.** Bronze tables contain raw data with a schema applied.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 30
# MAGIC
# MAGIC Which of the following tools is used by Auto Loader process data incrementally?
# MAGIC
# MAGIC - **A.** Checkpointing  
# MAGIC - **B.** Spark Structured Streaming  
# MAGIC - **C.** Data Explorer  
# MAGIC - **D.** Unity Catalog  
# MAGIC - **E.** Databricks SQL  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 31
# MAGIC
# MAGIC A data engineer has configured a Structured Streaming job to read from a table, manipulate the data, and then perform a streaming write into a new table.
# MAGIC
# MAGIC The cade block used by the data engineer is below:
# MAGIC
# MAGIC ![image_1777378774026.png](./image_1777378774026.png "image_1777378774026.png")</br>
# MAGIC
# MAGIC If the data engineer only wants the query to execute a micro-batch to process data every 5 seconds, which of the following lines of code should the data engineer use to fill in the blank?
# MAGIC
# MAGIC - **A.** trigger("5 seconds")
# MAGIC - **B.** trigger()
# MAGIC - **C.** trigger(once="5 seconds")
# MAGIC - **D.** trigger(processingTime="5 seconds")
# MAGIC - **E.** trigger(continuous="5 seconds")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 32**
# MAGIC
# MAGIC A dataset has been defined using Delta Live Tables and includes an expectations clause:  
# MAGIC CONSTRAINT valid_timestamp EXPECT (timestamp > '2020-01-01') ON VIOLATION DROP ROW
# MAGIC
# MAGIC What is the expected behavior when a batch of data containing data that violates these constraints is processed?
# MAGIC
# MAGIC - **A.** Records that violate the expectation are dropped from the target dataset and loaded into a quarantine table.
# MAGIC - **B.** Records that violate the expectation are added to the target dataset and flagged as invalid in a field added to the target dataset.
# MAGIC - **C.** Records that violate the expectation are dropped from the target dataset and recorded as invalid in the event log.
# MAGIC - **D.** Records that violate the expectation are added to the target dataset and recorded as invalid in the event log.
# MAGIC - **E.** Records that violate the expectation cause the job to fail.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 33
# MAGIC
# MAGIC Which of the following describes when to use the CREATE STREAMING LIVE TABLE (formerly CREATE INCREMENTAL LIVE TABLE) syntax over the CREATE LIVE TABLE syntax when creating Delta Live Tables (DLT) tables using SQL?
# MAGIC
# MAGIC A.	CREATE STREAMING LIVE TABLE should be used when the subsequent step in the DLT pipeline is static.  
# MAGIC B.	CREATE STREAMING LIVE TABLE should be used when data needs to be processed incrementally.  
# MAGIC C.	CREATE STREAMING LIVE TABLE is redundant for DLT and it does not need to be used.  
# MAGIC D.	CREATE STREAMING LIVE TABLE should be used when data needs to be processed through complicated aggregations.  
# MAGIC E.	CREATE STREAMING LIVE TABLE should be used when the previous step in the DLT pipeline is static.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 34
# MAGIC
# MAGIC A data engineer is designing a data pipeline. The source system generates files in a shared directory that is also used by other processes. As a result, the files should be kept as is and will accumulate in the directory. The data engineer needs to identify which files are new since the previous run in the pipeline, and set up the pipeline to only ingest those new files with each run. Which of the following tools can the data engineer use to solve this problem?
# MAGIC
# MAGIC - A. Unity Catalog  
# MAGIC - B. Delta Lake  
# MAGIC - C. Databricks SQL  
# MAGIC - D. Data Explorer  
# MAGIC - E. Auto Loader

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 35
# MAGIC
# MAGIC Which of the following Structured Streaming queries is performing a hop from a Silver table to a Gold table?
# MAGIC
# MAGIC ![image_1777378954249.png](./image_1777378954249.png "image_1777378954249.png")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 36**
# MAGIC
# MAGIC A data engineer has three tables in a Delta Live Tables (DLT) pipeline. They have configured the pipeline to drop invalid records at each table. They notice that some data is being dropped due to quality concerns at some point in the DLT pipeline. They would like to determine at which table in their pipeline the data is being dropped.
# MAGIC
# MAGIC Which of the following approaches can the data engineer take to identify the table that is dropping the records?
# MAGIC
# MAGIC - **A.** They can set up separate expectations for each table when developing their DLT pipeline.
# MAGIC - **B.** They cannot determine which table is dropping the records.
# MAGIC - **C.** They can set up DLT to notify them via email when records are dropped.
# MAGIC - **D.** They can navigate to the DLT pipeline page, click on each table, and view the data quality statistics.
# MAGIC - **E.** They can navigate to the DLT pipeline page, click on the “Error” button, and review the present errors.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 37**
# MAGIC
# MAGIC A data engineer has a single-task Job that runs each morning before they begin working. After identifying an upstream data issue, they need to set up another task to run a new notebook prior to the original task.
# MAGIC
# MAGIC Which of the following approaches can the data engineer use to set up the new task?
# MAGIC
# MAGIC - **A.** They can clone the existing task in the existing Job and update it to run the new notebook.
# MAGIC - **B.** They can create a new task in the existing Job and then add it as a dependency of the original task.
# MAGIC - **C.** They can create a new task in the existing Job and then add the original task as a dependency of the new task.
# MAGIC - **D.** They can create a new job from scratch and add both tasks to run concurrently.
# MAGIC - **E.** They can clone the existing task to a new Job and then edit it to run the new notebook.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 38**
# MAGIC
# MAGIC
# MAGIC An engineering manager wants to monitor the performance of a recent project using a Databricks SQL query. For the first week following the project’s release, the manager wants the query results to be updated every minute. However, the manager is concerned that the compute resources used for the query will be left running and cost the organization a lot of money beyond the first week of the project’s release.
# MAGIC
# MAGIC Which of the following approaches can the engineering team use to ensure the query does not cost the organization any money beyond the first week of the project’s release?
# MAGIC
# MAGIC - **A.** They can set a limit to the number of DBUs that are consumed by the SQL Endpoint.
# MAGIC - **B.** They can set the query’s refresh schedule to end after a certain number of refreshes.
# MAGIC - **C.** They cannot ensure the query does not cost the organization money beyond the first week of the project’s release.
# MAGIC - **D.** They can set a limit to the number of individuals that are able to manage the query’s refresh schedule.
# MAGIC - **E.** They can set the query’s refresh schedule to end on a certain date in the query scheduler.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 39
# MAGIC
# MAGIC A data analysis team has noticed that their Databricks SQL queries are running too slowly when connected to their always-on SQL endpoint. They claim that this issue is present when many members of the team are running small queries simultaneously. They ask the data engineering team for help. The data engineering team notices that each of the team’s queries uses the same SQL endpoint.
# MAGIC
# MAGIC Which of the following approaches can the data engineering team use to improve the latency of the team’s queries?
# MAGIC
# MAGIC - **A.** They can increase the cluster size of the SQL endpoint.
# MAGIC - **B.** They can increase the maximum bound of the SQL endpoint’s scaling range.
# MAGIC - **C.** They can turn on the Auto Stop feature for the SQL endpoint.
# MAGIC - **D.** They can turn on the Serverless feature for the SQL endpoint.
# MAGIC - **E.** They can turn on the Serverless feature for the SQL endpoint and change the Spot Instance Policy to “Reliability Optimized.”

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC **Question #: 40**
# MAGIC
# MAGIC A data engineer wants to schedule their Databricks SQL dashboard to refresh once per day, but they only want the associated SQL endpoint to be running when it is necessary.
# MAGIC
# MAGIC Which of the following approaches can the data engineer use to minimize the total running time of the SQL endpoint used in the refresh schedule of their dashboard?
# MAGIC
# MAGIC - **A.** They can ensure the dashboard’s SQL endpoint matches each of the queries’ SQL endpoints.
# MAGIC - **B.** They can set up the dashboard’s SQL endpoint to be serverless.
# MAGIC - **C.** They can turn on the Auto Stop feature for the SQL endpoint.
# MAGIC - **D.** They can reduce the cluster size of the SQL endpoint.
# MAGIC - **E.** They can ensure the dashboard’s SQL endpoint is not one of the included query’s SQL endpoint.
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 41**
# MAGIC
# MAGIC A data engineer has been using a Databricks SQL dashboard to monitor the cleanliness of the input data to an ELT job. The ELT job has its Databricks SQL query that returns the number of input records containing unexpected NULL values. The data engineer wants their entire team to be notified via a messaging webhook whenever this value reaches 100.
# MAGIC
# MAGIC Which of the following approaches can the data engineer use to notify their entire team via a messaging webhook whenever the number of NULL values reaches 100?
# MAGIC
# MAGIC - **A.** They can set up an Alert with a custom template.
# MAGIC - **B.** They can set up an Alert with a new email alert destination.
# MAGIC - **C.** They can set up an Alert with a new webhook alert destination.
# MAGIC - **D.** They can set up an Alert with one-time notifications.
# MAGIC - **E.** They can set up an Alert without notifications.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 42**
# MAGIC
# MAGIC A single Job runs two notebooks as two separate tasks. A data engineer has noticed that one of the notebooks is running slowly in the Job’s current run. The data engineer asks a tech lead for help in identifying why this might be the case.
# MAGIC
# MAGIC Which of the following approaches can the tech lead use to identify why the notebook is running slowly as part of the Job?
# MAGIC
# MAGIC - **A.** They can navigate to the Runs tab in the Jobs UI to immediately review the processing notebook.
# MAGIC - **B.** They can navigate to the Tasks tab in the Jobs UI and click on the active run to review the processing notebook.
# MAGIC - **C.** They can navigate to the Runs tab in the Jobs UI and click on the active run to review the processing notebook.
# MAGIC - **D.** There is no way to determine why a Job task is running slowly.
# MAGIC - **E.** They can navigate to the Tasks tab in the Jobs UI to immediately review the processing notebook.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 43**
# MAGIC
# MAGIC A data engineer has a Job with multiple tasks that runs nightly. Each of the tasks runs slowly because the clusters take a long time to start.
# MAGIC
# MAGIC Which of the following actions can the data engineer perform to improve the start up time for the clusters used for the Job?
# MAGIC
# MAGIC - **A.** They can use endpoints available in Databricks SQL  
# MAGIC - **B.** They can use jobs clusters instead of all-purpose clusters  
# MAGIC - **C.** They can configure the clusters to be single-node  
# MAGIC - **D.** They can use clusters that are from a cluster pool  
# MAGIC - **E.** They can configure the clusters to autoscale for larger data sizes  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 44
# MAGIC
# MAGIC A new data engineering team team. has been assigned to an ELT project. The new data engineering team will need full privileges on the database customers to fully manage the project.
# MAGIC
# MAGIC Which of the following commands can be used to grant full permissions on the database to the new data engineering team?
# MAGIC
# MAGIC - **A.** GRANT USAGE ON DATABASE customers TO team;
# MAGIC - **B.** GRANT ALL PRIVILEGES ON DATABASE team TO customers;
# MAGIC - **C.** GRANT SELECT PRIVILEGES ON DATABASE customers TO teams;
# MAGIC - **D.** GRANT SELECT CREATE MODIFY USAGE PRIVILEGES ON DATABASE customers TO team;
# MAGIC - **E.** GRANT ALL PRIVILEGES ON DATABASE customers TO team;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 45**
# MAGIC
# MAGIC A new data engineering team has been assigned to work on a project. The team will need access to database customers in order to see what tables already exist. The team has its own group team.
# MAGIC
# MAGIC Which of the following commands can be used to grant the necessary permission on the entire database to the new team?
# MAGIC
# MAGIC - **A.** GRANT VIEW ON CATALOG customers TO team;
# MAGIC - **B.** GRANT CREATE ON DATABASE customers TO team;
# MAGIC - **C.** GRANT USAGE ON CATALOG team TO customers;
# MAGIC - **D.** GRANT CREATE ON DATABASE team TO customers;
# MAGIC - **E.** GRANT USAGE ON DATABASE customers TO team;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 46**
# MAGIC
# MAGIC A data engineer is running code in a Databricks Repo that is cloned from a central Git repository. A colleague of the data engineer informs them that changes have been made and synced to the central Git repository. The data engineer now needs to sync their Databricks Repo to get the changes from the central Git repository.
# MAGIC
# MAGIC Which of the following Git operations does the data engineer need to run to accomplish this task?
# MAGIC
# MAGIC - **A.** Merge  
# MAGIC - **B.** Push  
# MAGIC - **C.** Pull  
# MAGIC - **D.** Commit  
# MAGIC - **E.** Clone  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 47**
# MAGIC
# MAGIC Which of the following is a benefit of the Databricks Lakehouse Platform embracing open source technologies?
# MAGIC
# MAGIC - **A.** Cloud-specific integrations  
# MAGIC - **B.** Simplified governance  
# MAGIC - **C.** Ability to scale storage  
# MAGIC - **D.** Ability to scale workloads  
# MAGIC - **E.** Avoiding vendor lock-in  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 48**
# MAGIC
# MAGIC A data engineer needs to use a Delta table as part of a data pipeline, but they do not know if they have the appropriate permissions.
# MAGIC
# MAGIC In which of the following locations can the data engineer review their permissions on the table?
# MAGIC
# MAGIC - **A.** Databricks Filesystem  
# MAGIC - **B.** Jobs  
# MAGIC - **C.** Dashboards  
# MAGIC - **D.** Repos  
# MAGIC - **E.** Data Explorer  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 49
# MAGIC
# MAGIC Which of the following describes a scenario in which a data engineer will want to use a single-node cluster?
# MAGIC
# MAGIC - **A.** When they are working interactively with a small amount of data  
# MAGIC - **B.** When they are running automated reports to be refreshed as quickly as possible  
# MAGIC - **C.** When they are working with SQL within Databricks SQL  
# MAGIC - **D.** When they are concerned about the ability to automatically scale with larger data  
# MAGIC - **E.** When they are manually running reports with a large amount of data

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 50**
# MAGIC
# MAGIC A data engineer has been given a new record of data:
# MAGIC
# MAGIC id STRING = 'a1'  
# MAGIC rank INTEGER = 6  
# MAGIC rating FLOAT = 9.4
# MAGIC
# MAGIC Which of the following SQL commands can be used to append the new record to an existing Delta table `my_table`?
# MAGIC
# MAGIC - **A.** INSERT INTO my_table VALUES ('a1', 6, 9.4)
# MAGIC - **B.** my_table UNION VALUES ('a1', 6, 9.4)
# MAGIC - **C.** INSERT VALUES ( 'a1' , 6, 9.4) INTO my_table
# MAGIC - **D.** UPDATE my_table VALUES ('a1', 6, 9.4)
# MAGIC - **E.** UPDATE VALUES ('a1', 6, 9.4) my_table
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 51**
# MAGIC
# MAGIC A data engineer has realized that the data files associated with a Delta table are incredibly small. They want to compact the small files to form larger files to improve performance.
# MAGIC
# MAGIC Which of the following keywords can be used to compact the small files?
# MAGIC
# MAGIC - **A.** REDUCE  
# MAGIC - **B.** OPTIMIZE  
# MAGIC - **C.** COMPACTION  
# MAGIC - **D.** REPARTITION  
# MAGIC - **E.** VACUUM  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 52
# MAGIC
# MAGIC In which of the following file formats is data from Delta Lake tables primarily stored?
# MAGIC
# MAGIC - **A.** Delta  
# MAGIC - **B.** CSV  
# MAGIC - **C.** Parquet  
# MAGIC - **D.** JSON  
# MAGIC - **E.** A proprietary, optimized format specific to Databricks  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 53**
# MAGIC
# MAGIC Which of the following is stored in the Databricks customer's cloud account?
# MAGIC
# MAGIC - **A.** Databricks web application  
# MAGIC - **B.** Cluster management metadata  
# MAGIC - **C.** Repos  
# MAGIC - **D.** Data  
# MAGIC - **E.** Notebooks  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 54**
# MAGIC
# MAGIC Which of the following can be used to simplify and unify siloed data architectures that are specialized for specific use cases?
# MAGIC
# MAGIC - **A.** None of these  
# MAGIC - **B.** Data lake  
# MAGIC - **C.** Data warehouse  
# MAGIC - **D.** All of these  
# MAGIC - **E.** Data lakehouse  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC **Question #: 55**
# MAGIC
# MAGIC **A data architect has determined that a table of the following format is necessary:**
# MAGIC
# MAGIC ![image_1777379419208.png](./image_1777379419208.png "image_1777379419208.png")  
# MAGIC **Which of the following code blocks uses SQL DDL commands to create an empty Delta table in the above format regardless of whether a table already exists with this name?**
# MAGIC
# MAGIC - **A.**  
# MAGIC   ![image_1777379590423.png](./image_1777379590423.png "image_1777379590423.png")
# MAGIC
# MAGIC - **B.**  
# MAGIC   ![image_1777379603146.png](./image_1777379603146.png "image_1777379603146.png")
# MAGIC
# MAGIC - **C.**  
# MAGIC   ![image_1777379620246.png](./image_1777379620246.png "image_1777379620246.png")
# MAGIC
# MAGIC - **D.**  
# MAGIC   ![image_1777379648723.png](./image_1777379648723.png "image_1777379648723.png")
# MAGIC
# MAGIC - **E.**  
# MAGIC   ![image_1777379660592.png](./image_1777379660592.png "image_1777379660592.png")
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 56**
# MAGIC
# MAGIC A data engineer has a Python notebook in Databricks, but they need to use SQL to accomplish a specific task within a cell. They still want all of the other cells to use Python without making any changes to those cells.
# MAGIC
# MAGIC Which of the following describes how the data engineer can use SQL within a cell of their Python notebook?
# MAGIC
# MAGIC - **A.** It is not possible to use SQL in a Python notebook  
# MAGIC - **B.** They can attach the cell to a SQL endpoint rather than a Databricks cluster  
# MAGIC - **C.** They can simply write SQL syntax in the cell  
# MAGIC - **D.** They can add %sql to the first line of the cell  
# MAGIC - **E.** They can change the default language of the notebook to SQL  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 57**
# MAGIC
# MAGIC Which of the following SQL keywords can be used to convert a table from a long format to a wide format?
# MAGIC
# MAGIC - **A.** TRANSFORM  
# MAGIC - **B.** PIVOT  
# MAGIC - **C.** SUM  
# MAGIC - **D.** CONVERT  
# MAGIC - **E.** WHERE  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 58
# MAGIC
# MAGIC Which of the following describes a benefit of creating an external table from Parquet rather than CSV when using a CREATE TABLE AS SELECT statement?
# MAGIC
# MAGIC - **A.** Parquet files can be partitioned  
# MAGIC - **B.** CREATE TABLE AS SELECT statements cannot be used on files  
# MAGIC - **C.** Parquet files have a well-defined schema  
# MAGIC - **D.** Parquet files have the ability to be optimized  
# MAGIC - **E.** Parquet files will become Delta tables  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 59**
# MAGIC
# MAGIC A data engineer wants to create a relational object by pulling data from two tables. The relational object does not need to be used by other data engineers in other sessions. In order to save on storage costs, the data engineer wants to avoid copying and storing physical data.
# MAGIC
# MAGIC Which of the following relational objects should the data engineer create?
# MAGIC
# MAGIC - **A.** Spark SQL Table  
# MAGIC - **B.** View  
# MAGIC - **C.** Database  
# MAGIC - **D.** Temporary view  
# MAGIC - **E.** Delta Table  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 60
# MAGIC
# MAGIC A data analyst has developed a query that runs against Delta table. They want help from the data engineering team to implement a series of tests to ensure the data returned by the query is clean. However, the data engineering team uses Python for its tests rather than SQL.
# MAGIC
# MAGIC Which of the following operations could the data engineering team use to run the query and operate with the results in PySpark?
# MAGIC
# MAGIC - **A.** SELECT * FROM sales  
# MAGIC - **B.** spark.delta.table  
# MAGIC - **C.** spark.sql  
# MAGIC - **D.** There is no way to share data between PySpark and SQL.  
# MAGIC - **E.** spark.table  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 61**
# MAGIC
# MAGIC Which of the following commands will return the number of null values in the member_id column?
# MAGIC
# MAGIC - **A.** SELECT count(member_id) FROM my_table;
# MAGIC - **B.** SELECT count(member_id) - count_null(member_id) FROM my_table;
# MAGIC - **C.** SELECT count_if(member_id IS NULL) FROM my_table;
# MAGIC - **D.** SELECT null(member_id) FROM my_table;
# MAGIC - **E.** SELECT count_null(member_id) FROM my_table;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 62**
# MAGIC
# MAGIC **A data engineer needs to apply custom logic to identify employees with more than 5 years of experience in array column `employees` in table `stores`. The custom logic should create a new column `exp_employees` that is an array of all of the employees with more than 5 years of experience for each row. In order to apply this custom logic at scale, the data engineer wants to use the FILTER higher-order function.**
# MAGIC
# MAGIC **Which of the following code blocks successfully completes this task?**
# MAGIC
# MAGIC - **A.**  
# MAGIC   ![image_1777380181347.png](./image_1777380181347.png "image_1777380181347.png")
# MAGIC
# MAGIC - **B.**  
# MAGIC   ![image_1777380207926.png](./image_1777380207926.png "image_1777380207926.png")
# MAGIC
# MAGIC - **C.**  
# MAGIC   ![image_1777380219499.png](./image_1777380219499.png "image_1777380219499.png")
# MAGIC
# MAGIC - **D.**  
# MAGIC   ![image_1777380230623.png](./image_1777380230623.png "image_1777380230623.png")
# MAGIC
# MAGIC - **E.**  
# MAGIC   ![image_1777380243533.png](./image_1777380243533.png "image_1777380243533.png")
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 63
# MAGIC
# MAGIC A data engineer has a Python variable table_name that they would like to use in a SQL query. They want to construct a Python code block that will run the query using table_name.
# MAGIC
# MAGIC They have the following incomplete code block:
# MAGIC
# MAGIC     (f"SELECT customer_id, spend FROM {table_name}")
# MAGIC
# MAGIC Which of the following can be used to fill in the blank to successfully complete the task?
# MAGIC
# MAGIC - **A.** spark.delta.sql  
# MAGIC - **B.** spark.delta.table  
# MAGIC - **C.** spark.table  
# MAGIC - **D.** dbutils.sql  
# MAGIC - **E.** spark.sql  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 64**
# MAGIC
# MAGIC A data engineer has created a new database using the following command:  
# MAGIC `CREATE DATABASE IF NOT EXISTS customer360;`
# MAGIC
# MAGIC In which of the following locations will the customer360 database be located?
# MAGIC
# MAGIC - **A.** dbfs:/user/hive/database/customer360  
# MAGIC - **B.** dbfs:/user/hive/warehouse  
# MAGIC - **C.** dbfs:/user/hive/customer360  
# MAGIC - **D.** More information is needed to determine the correct response  
# MAGIC - **E.** dbfs:/user/hive/database  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 65**
# MAGIC
# MAGIC A data engineer is attempting to drop a Spark SQL table `my_table` and runs the following command:
# MAGIC
# MAGIC
# MAGIC DROP TABLE IF EXISTS my_table;
# MAGIC
# MAGIC
# MAGIC After running this command, the engineer notices that the data files and metadata files have been deleted from the file system.
# MAGIC
# MAGIC Which of the following describes why all of these files were deleted?
# MAGIC
# MAGIC - **A.** The table was managed  
# MAGIC - **B.** The table's data was smaller than 10 GB  
# MAGIC - **C.** The table's data was larger than 10 GB  
# MAGIC - **D.** The table was external  
# MAGIC - **E.** The table did not have a location  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 66
# MAGIC A data engineer that is new to using Python needs to create a Python function to add two integers together and return the sum?
# MAGIC
# MAGIC Which of the following code blocks can the data engineer use to complete this task? 
# MAGIC ![image_1777380347521.png](./image_1777380347521.png "image_1777380347521.png")
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC
# MAGIC **Question #: 67**
# MAGIC
# MAGIC In which of the following scenarios should a data engineer use the MERGE INTO command instead of the INSERT INTO command?
# MAGIC
# MAGIC **A.** When the location of the data needs to be changed  
# MAGIC **B.** When the target table is an external table  
# MAGIC **C.** When the source table can be deleted  
# MAGIC **D.** When the target table cannot contain duplicate records  
# MAGIC **E.** When the source is not a Delta table  
# MAGIC
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC **Question #: 68**
# MAGIC
# MAGIC **A data engineer is working with two tables. Each of these tables is displayed below in its entirety.**
# MAGIC
# MAGIC ![image_1777380376819.png](./image_1777380376819.png "image_1777380376819.png")  
# MAGIC ![image_1777380409624.png](./image_1777380409624.png "image_1777380409624.png")  
# MAGIC
# MAGIC **The data engineer runs the following query to join these tables together:**
# MAGIC
# MAGIC ![image_1777380429714.png](./image_1777380429714.png "image_1777380429714.png")
# MAGIC
# MAGIC - **A.**  
# MAGIC   ![image_1777380453222.png](./image_1777380453222.png "image_1777380453222.png")
# MAGIC
# MAGIC - **B.**  
# MAGIC   ![image_1777380468807.png](./image_1777380468807.png "image_1777380468807.png")
# MAGIC
# MAGIC - **C.**  
# MAGIC   ![image_1777380482474.png](./image_1777380482474.png "image_1777380482474.png")
# MAGIC
# MAGIC - **D.**  
# MAGIC   ![image_1777380503972.png](./image_1777380503972.png "image_1777380503972.png")
# MAGIC
# MAGIC - **E.**  
# MAGIC   ![image_1777380520952.png](./image_1777380520952.png "image_1777380520952.png")
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 69
# MAGIC
# MAGIC A data engineer needs to create a table in Databricks using data from a CSV file at location /path/to/csv.
# MAGIC
# MAGIC They run the following command:
# MAGIC
# MAGIC ![image_1777380530249.png](./image_1777380530249.png "image_1777380530249.png")  
# MAGIC Which of the following lines of code fills in the above blank to successfully complete the task?
# MAGIC
# MAGIC - **A.** None of these lines of code are needed to successfully complete the task  
# MAGIC - **B.** USING CSV  
# MAGIC - **C.** FROM CSV  
# MAGIC - **D.** USING DELTA  
# MAGIC - **E.** FROM "path/to/csv"

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 70**
# MAGIC
# MAGIC A data engineer has configured a Structured Streaming job to read from a table, manipulate the data, and then perform a streaming write into a new table.
# MAGIC
# MAGIC The code block used by the data engineer is below:  
# MAGIC ![image_1777380609904.png](./image_1777380609904.png "image_1777380609904.png")  
# MAGIC
# MAGIC If the data engineer only wants the query to process all of the available data in as many batches as required, which of the following lines of code should the data engineer use to fill in the blank?
# MAGIC
# MAGIC - **A.** processingTime(1)
# MAGIC - **B.** trigger(availableNow=True)
# MAGIC - **C.** trigger(parallelBatch=True)
# MAGIC - **D.** trigger(processingTime="once")
# MAGIC - **E.** trigger(continuous="once")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 71**
# MAGIC
# MAGIC A data engineer has developed a data pipeline to ingest data from a JSON source using Auto Loader, but the engineer has not provided any type inference or schema hints in their pipeline. Upon reviewing the data, the data engineer has noticed that all of the columns in the target table are of the string type despite some of the fields only including float or boolean values.
# MAGIC
# MAGIC Which of the following describes why Auto Loader inferred all of the columns to be of the string type?
# MAGIC
# MAGIC - **A.** There was a type mismatch between the specific schema and the inferred schema  
# MAGIC - **B.** JSON data is a text-based format  
# MAGIC - **C.** Auto Loader only works with string data  
# MAGIC - **D.** All of the fields had at least one null value  
# MAGIC - **E.** Auto Loader cannot infer the schema of ingested

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 72
# MAGIC
# MAGIC A Delta Live Table pipeline includes two datasets defined using STREAMING LIVE TABLE. Three datasets are defined against Delta Lake table sources using LIVE TABLE.
# MAGIC
# MAGIC The table is configured to run in Development mode using the Continuous Pipeline Mode.
# MAGIC
# MAGIC Assuming previously unprocessed data exists and all definitions are valid, what is the expected outcome after clicking Start to update the pipeline?
# MAGIC
# MAGIC - **A.** All datasets will be updated once and the pipeline will shut down. The compute resources will be terminated.
# MAGIC - **B.** All datasets will be updated at set intervals until the pipeline is shut down. The compute resources will persist until the pipeline is shut down.
# MAGIC - **C.** All datasets will be updated once and the pipeline will persist without any processing. The compute resources will persist but go unused.
# MAGIC - **D.** All datasets will be updated once and the pipeline will shut down. The compute resources will persist to allow for additional testing.
# MAGIC - **E.** All datasets will be updated at set intervals until the pipeline is shut down. The compute resources will persist to allow for additional testing.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 73**
# MAGIC
# MAGIC Which of the following data workloads will utilize a Gold table as its source?
# MAGIC
# MAGIC - **A.** A job that enriches data by parsing its timestamps into a human-readable format  
# MAGIC - **B.** A job that aggregates uncleaned data to create standard summary statistics  
# MAGIC - **C.** A job that cleans data by removing malformatted records  
# MAGIC - **D.** A job that queries aggregated data designed to feed into a dashboard  
# MAGIC - **E.** A job that ingests raw data from a streaming source into the Lakehouse

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC **Question #: 74**
# MAGIC
# MAGIC Which of the following must be specified when creating a new Delta Live Tables pipeline?
# MAGIC
# MAGIC - **A.** A key-value pair configuration  
# MAGIC - **B.** The preferred DBU/hour cost  
# MAGIC - **C.** A path to cloud storage location for the written data  
# MAGIC - **D.** A location of a target database for the written data  
# MAGIC - **E.** At least one notebook library to be executed  
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 75**
# MAGIC
# MAGIC A data engineer has joined an existing project and they see the following query in the project repository:
# MAGIC
# MAGIC
# MAGIC CREATE STREAMING LIVE TABLE loyal_customers AS 
# MAGIC SELECT customer_id
# MAGIC FROM STREAM(LIVE.customers)
# MAGIC WHERE loyalty_level = 'high';
# MAGIC
# MAGIC
# MAGIC Which of the following describes why the STREAM function is included in the query?
# MAGIC
# MAGIC - **A.** The STREAM function is not needed and will cause an error.
# MAGIC - **B.** The table being created is a live table.
# MAGIC - **C.** The customers table is a streaming live table.
# MAGIC - **D.** The customers table is a reference to a Structured Streaming query on a PySpark DataFrame.
# MAGIC - **E.** The data in the customers table has been updated since its last run.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 76
# MAGIC
# MAGIC Which of the following describes the type of workloads that are always compatible with Auto Loader?
# MAGIC
# MAGIC - **A.** Streaming workloads  
# MAGIC - **B.** Machine learning workloads  
# MAGIC - **C.** Serverless workloads  
# MAGIC - **D.** Batch workloads  
# MAGIC - **E.** Dashboard workloads

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 77**
# MAGIC
# MAGIC A data engineer and data analyst are working together on a data pipeline. The data engineer is working on the raw, bronze, and silver layers of the pipeline using Python, and the data analyst is working on the gold layer of the pipeline using SQL. The raw source of the pipeline is a streaming input. They now want to migrate their pipeline to use Delta Live Tables.
# MAGIC
# MAGIC Which of the following changes will need to be made to the pipeline when migrating to Delta Live Tables?
# MAGIC
# MAGIC - **A.** None of these changes will need to be made  
# MAGIC - **B.** The pipeline will need to stop using the medallion-based multi-hop architecture  
# MAGIC - **C.** The pipeline will need to be written entirely in SQL  
# MAGIC - **D.** The pipeline will need to use a batch source in place of a streaming source  
# MAGIC - **E.** The pipeline will need to be written entirely in Python  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 78
# MAGIC
# MAGIC A data engineer is using the following code block as part of a batch ingestion pipeline to read from a composable table:
# MAGIC
# MAGIC ![image_1777381324150.png](./image_1777381324150.png "image_1777381324150.png")  
# MAGIC Which of the following changes needs to be made so this code block will work when the transactions table is a stream source?
# MAGIC
# MAGIC - **A.** Replace predict with a stream-friendly prediction function  
# MAGIC - **B.** Replace schema(schema) with option ("maxFilesPerTrigger", 1)  
# MAGIC - **C.** Replace "transactions" with the path to the location of the Delta table  
# MAGIC - **D.** Replace format("delta") with format("stream")  
# MAGIC - **E.** Replace spark.read with spark.readStream

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 79**
# MAGIC
# MAGIC **Which of the following queries is performing a streaming hop from raw data to a Bronze table?**
# MAGIC
# MAGIC A.  
# MAGIC ![image_1777465867943.png](./image_1777465867943.png "image_1777465867943.png")
# MAGIC
# MAGIC B.  
# MAGIC ![image_1777465890337.png](./image_1777465890337.png "image_1777465890337.png")
# MAGIC
# MAGIC C.  
# MAGIC ![image_1777465904373.png](./image_1777465904373.png "image_1777465904373.png")
# MAGIC
# MAGIC D.  
# MAGIC ![image_1777465934622.png](./image_1777465934622.png "image_1777465934622.png")
# MAGIC
# MAGIC E.  
# MAGIC ![image_1777465951973.png](./image_1777465951973.png "image_1777465951973.png")

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 80
# MAGIC
# MAGIC A dataset has been defined using Delta Live Tables and includes an expectations clause:
# MAGIC
# MAGIC CONSTRAINT valid_timestamp EXPECT (timestamp > '2020-01-01') ON VIOLATION FAIL UPDATE
# MAGIC
# MAGIC What is the expected behavior when a batch of data containing data that violates these constraints is processed?
# MAGIC
# MAGIC A. Records that violate the expectation are dropped from the target dataset and recorded as invalid in the event log.  
# MAGIC B. Records that violate the expectation cause the job to fail.  
# MAGIC C. Records that violate the expectation are dropped from the target dataset and loaded into a quarantine table.  
# MAGIC D. Records that violate the expectation are added to the target dataset and recorded as invalid in the event log.  
# MAGIC E. Records that violate the expectation are added to the target dataset and flagged as invalid in a field added to the target dataset.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 81
# MAGIC
# MAGIC Which of the following statements regarding the relationship between Silver tables and Bronze tables is always true?
# MAGIC
# MAGIC - **A.** Silver tables contain a less refined, less clean view of data than Bronze data.
# MAGIC - **B.** Silver tables contain aggregates while Bronze data is unaggregated.
# MAGIC - **C.** Silver tables contain more data than Bronze tables.
# MAGIC - **D.** Silver tables contain a more refined and cleaner view of data than Bronze tables.
# MAGIC - **E.** Silver tables contain less data than Bronze tables.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 82**
# MAGIC
# MAGIC A data engineering team has noticed that their Databricks SQL queries are running too slowly when they are submitted to a non-running SQL endpoint. The data engineering team wants this issue to be resolved.
# MAGIC
# MAGIC **Which of the following approaches can the team use to reduce the time it takes to return results in this scenario?**
# MAGIC
# MAGIC - **A.** They can turn on the Serverless feature for the SQL endpoint and change the Spot Instance Policy to "Reliability Optimized."
# MAGIC - **B.** They can turn on the Auto Stop feature for the SQL endpoint.
# MAGIC - **C.** They can increase the cluster size of the SQL endpoint.
# MAGIC - **D.** They can turn on the Serverless feature for the SQL endpoint.
# MAGIC - **E.** They can increase the maximum bound of the SQL endpoint's scaling range.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 83
# MAGIC
# MAGIC A data engineer has a Job that has a complex run schedule, and they want to transfer that schedule to other Jobs.  
# MAGIC Rather than manually selecting each value in the scheduling form in Databricks, which of the following tools can the data engineer use to represent and submit the schedule programmatically?
# MAGIC
# MAGIC - **A.** pyspark.sql.types.DateType  
# MAGIC - **B.** datetime  
# MAGIC - **C.** pyspark.sql.types.TimestampType  
# MAGIC - **D.** Cron syntax  
# MAGIC - **E.** There is no way to represent and submit this information programmatically

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 84
# MAGIC
# MAGIC Which of the following approaches should be used to send the Databricks Job owner an email in the case that the Job fails?
# MAGIC
# MAGIC - **A.** Manually programming in an alert system in each cell of the Notebook  
# MAGIC - **B.** Setting up an Alert in the Job page  
# MAGIC - **C.** Setting up an Alert in the Notebook  
# MAGIC - **D.** There is no way to notify the Job owner in the case of Job failure  
# MAGIC - **E.** MLflow Model Registry Webhooks

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 85
# MAGIC
# MAGIC An engineering manager uses a Databricks SQL query to monitor ingestion latency for each data source. The manager checks the results of the query every day, but they are manually rerunning the query each day and waiting for the results.
# MAGIC
# MAGIC Which of the following approaches can the manager use to ensure the results of the query are updated each day?
# MAGIC
# MAGIC - **A.** They can schedule the query to refresh every 1 day from the SQL endpoint's page in Databricks SQL.
# MAGIC - **B.** They can schedule the query to refresh every 12 hours from the SQL endpoint's page in Databricks SQL.
# MAGIC - **C.** They can schedule the query to refresh every 1 day from the query's page in Databricks SQL.
# MAGIC - **D.** They can schedule the query to run every 1 day from the Jobs UI.
# MAGIC - **E.** They can schedule the query to run every 12 hours from the Jobs UI.
# MAGIC
# MAGIC Correct Answer: **C**

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 86
# MAGIC
# MAGIC In which of the following scenarios should a data engineer select a Task in the Depends On field of a new Databricks Job Task?
# MAGIC
# MAGIC - **A.** When another task needs to be replaced by the new task  
# MAGIC - **B.** When another task needs to fail before the new task begins  
# MAGIC - **C.** When another task has the same dependency libraries as the new task  
# MAGIC - **D.** When another task needs to use as little compute resources as possible  
# MAGIC - **E.** When another task needs to successfully complete before the new task begins

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 87
# MAGIC
# MAGIC A data engineer has been using a Databricks SQL dashboard to monitor the cleanliness of the input data to a data analytics dashboard for a retail use case. The job has a Databricks SQL query that returns the number of store-level records where sales is equal to zero. The data engineer wants their entire team to be notified via a messaging webhook whenever this value is greater than 0.
# MAGIC
# MAGIC Which of the following approaches can the data engineer use to notify their entire team via a messaging webhook whenever the number of stores with $0 in sales is greater than zero?
# MAGIC
# MAGIC - **A.** They can set up an Alert with a custom template.
# MAGIC - **B.** They can set up an Alert with a new email alert destination.
# MAGIC - **C.** They can set up an Alert with one-time notifications.
# MAGIC - **D.** They can set up an Alert with a new webhook alert destination.
# MAGIC - **E.** They can set up an Alert without

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 88
# MAGIC
# MAGIC A data engineer wants to schedule their Databricks SQL dashboard to refresh every hour, but they only want the associated SQL endpoint to be running when it is necessary. The dashboard has multiple queries on multiple datasets associated with it. The data that feeds the dashboard is automatically processed using a Databricks Job.
# MAGIC
# MAGIC Which of the following approaches can the data engineer use to minimize the total running time of the SQL endpoint used in the refresh schedule of their dashboard?
# MAGIC
# MAGIC - **A.** They can turn on the Auto Stop feature for the SQL endpoint.
# MAGIC - **B.** They can ensure the dashboard's SQL endpoint is not one of the included query's SQL endpoint.
# MAGIC - **C.** They can reduce the cluster size of the SQL endpoint.
# MAGIC - **D.** They can ensure the dashboard's SQL endpoint matches each of the queries' SQL endpoints.
# MAGIC - **E.** They can set up the dashboard's SQL endpoint to be serverless.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 89
# MAGIC
# MAGIC A data engineer needs access to a table new_table, but they do not have the correct permissions. They can ask the table owner for permission, but they do not know who the table owner is.
# MAGIC
# MAGIC Which of the following approaches can be used to identify the owner of new_table?
# MAGIC
# MAGIC - **A.** Review the Permissions tab in the table's page in Data Explorer  
# MAGIC - **B.** All of these options can be used to identify the owner of the table  
# MAGIC - **C.** Review the Owner field in the table's page in Data Explorer  
# MAGIC - **D.** Review the Owner field in the table's page in the cloud storage solution  
# MAGIC - **E.** There is no way to identify the owner of the

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 90
# MAGIC A new data engineering team team has been assigned to an ELT project. The new data engineering team will need full privileges on the table sales to fully manage the project.
# MAGIC
# MAGIC **Which of the following commands can be used to grant full permissions on the database to the new data engineering team?**
# MAGIC
# MAGIC - **A.** GRANT ALL PRIVILEGES ON TABLE sales TO team;
# MAGIC - **B.** GRANT SELECT CREATE MODIFY ON TABLE sales TO team;
# MAGIC - **C.** GRANT SELECT ON TABLE sales TO team;
# MAGIC - **D.** GRANT USAGE ON TABLE sales TO team;
# MAGIC - **E.** GRANT ALL PRIVILEGES ON TABLE team TO sales;

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 91
# MAGIC
# MAGIC Which data lakehouse feature results in improved data quality over a traditional data lake?
# MAGIC
# MAGIC - **A.** A data lakehouse stores data in open formats.
# MAGIC - **B.** A data lakehouse allows the use of SQL queries to examine data.
# MAGIC - **C.** A data lakehouse provides storage solutions for structured and unstructured data.
# MAGIC - **D.** A data lakehouse supports ACID-compliant transactions.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 92
# MAGIC
# MAGIC In which scenario will a data team want to utilize cluster pools?
# MAGIC
# MAGIC - **A.** An automated report needs to be version-controlled across multiple collaborators.
# MAGIC - **B.** An automated report needs to be runnable by all stakeholders.
# MAGIC - **C.** An automated report needs to be refreshed as quickly as possible.
# MAGIC - **D.** An automated report needs to be made reproducible.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 93
# MAGIC
# MAGIC
# MAGIC **What is hosted completely in the control plane of the classic Databricks architecture?**
# MAGIC
# MAGIC - **A.** Worker node  
# MAGIC - **B.** Databricks web application  
# MAGIC - **C.** Driver node  
# MAGIC - **D.** Databricks Filesystem

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 94**
# MAGIC
# MAGIC A data engineer needs to determine whether to use the built-in Databricks Notebooks versioning or version their project using Databricks Repos.
# MAGIC
# MAGIC **What is an advantage of using Databricks Repos over the Databricks Notebooks versioning?**
# MAGIC
# MAGIC - **A.** Databricks Repos allows users to revert to previous versions of a notebook  
# MAGIC - **B.** Databricks Repos is wholly housed within the Databricks Data Intelligence Platform  
# MAGIC - **C.** Databricks Repos provides the ability to comment on specific changes  
# MAGIC - **D.** Databricks Repos supports the use of multiple branches

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 95**
# MAGIC
# MAGIC What is a benefit of the Databricks Lakehouse Architecture embracing open source technologies?
# MAGIC
# MAGIC - **A.** Avoiding vendor lock-in  
# MAGIC - **B.** Simplified governance  
# MAGIC - **C.** Ability to scale workloads  
# MAGIC - **D.** Cloud-specific integrations

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 96
# MAGIC
# MAGIC A data engineer needs to use a Delta table as part of a data pipeline, but they do not know if they have the appropriate permissions.
# MAGIC
# MAGIC In which location can the data engineer review their permissions on the table?
# MAGIC
# MAGIC - **A.** Jobs  
# MAGIC - **B.** Dashboards  
# MAGIC - **C.** Catalog Explorer  
# MAGIC - **D.** Repos

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 97
# MAGIC
# MAGIC A data engineer is running code in a Databricks Repo that is cloned from a central Git repository. A colleague of the data engineer informs them that changes have been made and synced to the central Git repository. The data engineer now needs to sync their Databricks Repo to get the changes from the central Git repository.
# MAGIC
# MAGIC Which Git operation does the data engineer need to run to accomplish this task?
# MAGIC
# MAGIC - **A.** Clone  
# MAGIC - **B.** Pull  
# MAGIC - **C.** Merge  
# MAGIC - **D.** Push

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 98
# MAGIC
# MAGIC Which file format is used for storing Delta Lake Table?
# MAGIC
# MAGIC - **A.** CSV  
# MAGIC - **B.** Parquet  
# MAGIC - **C.** JSON  
# MAGIC - **D.** Delta

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 99
# MAGIC
# MAGIC A data architect has determined that a table of the following format is necessary:
# MAGIC
# MAGIC ![image_1777466877971.png](./image_1777466877971.png "image_1777466877971.png")  
# MAGIC <br>
# MAGIC
# MAGIC Which code block is used by SQL DDL command to create an empty Delta table in the above format regardless of whether a table already exists with this name?
# MAGIC
# MAGIC A.  
# MAGIC CREATE OR REPLACE TABLE table_name ( employeeId STRING, startDate DATE, avgRating FLOAT )
# MAGIC
# MAGIC B.  
# MAGIC CREATE OR REPLACE TABLE table_name WITH COLUMNS ( employeeId STRING, startDate DATE, avgRating FLOAT ) USING DELTA
# MAGIC
# MAGIC C.  
# MAGIC CREATE TABLE IF NOT EXISTS table_name ( employeeId STRING, startDate DATE, avgRating FLOAT )
# MAGIC
# MAGIC D.  
# MAGIC CREATE TABLE table_name AS SELECT employeeId STRING, startDate DATE, avgRating FLOAT

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 100
# MAGIC
# MAGIC A data engineer has been given a new record of data:
# MAGIC
# MAGIC id STRING = 'a1'  
# MAGIC rank INTEGER = 6  
# MAGIC rating FLOAT = 9.4
# MAGIC
# MAGIC Which SQL commands can be used to append the new record to an existing Delta table `my_table`?
# MAGIC
# MAGIC - **A.** `INSERT INTO my_table VALUES ('a1', 6, 9.4)`
# MAGIC - **B.** `INSERT VALUES ('a1', 6, 9.4) INTO my_table`
# MAGIC - **C.** `UPDATE my_table VALUES ('a1', 6, 9.4)`
# MAGIC - **D.** `UPDATE VALUES ('a1', 6, 9.4) my_table`

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 101
# MAGIC
# MAGIC A data engineer has realized that the data files associated with a Delta table are incredibly small. They want to compact the small files to form larger files to improve performance.
# MAGIC
# MAGIC Which keyword can be used to compact the small files?
# MAGIC
# MAGIC - **A.** OPTIMIZE  
# MAGIC - **B.** VACUUM  
# MAGIC - **C.** COMPACTION  
# MAGIC - **D.** REPARTITION

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 102
# MAGIC
# MAGIC A data engineer wants to create a data entity from a couple of tables. The data entity must be used by other data engineers in other sessions. It also must be saved to a physical location.
# MAGIC
# MAGIC Which of the following data entities should the data engineer create?
# MAGIC
# MAGIC - **A.** Table  
# MAGIC - **B.** Function  
# MAGIC - **C.** View  
# MAGIC - **D.** Temporary view

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 103**
# MAGIC
# MAGIC A data engineer runs a statement every day to copy the previous day’s sales into the table `transactions`. Each day’s sales are in their own file in the location `"/transactions/raw"`.
# MAGIC
# MAGIC Today, the data engineer runs the following command to complete this task:
# MAGIC
# MAGIC ![image_1777467018449.png](./image_1777467018449.png "image_1777467018449.png")  
# MAGIC <br>
# MAGIC
# MAGIC After running the command today, the data engineer notices that the number of records in table `transactions` has not changed.
# MAGIC
# MAGIC **What explains why the statement might not have copied any new records into the table?**
# MAGIC
# MAGIC - **A.** The format of the files to be copied were not included with the FORMAT_OPTIONS keyword.
# MAGIC - **B.** The COPY INTO statement requires the table to be refreshed to view the copied rows.
# MAGIC - **C.** The previous day’s file has already been copied into the table.
# MAGIC - **D.** The PARQUET file format does not support COPY INTO.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 104
# MAGIC
# MAGIC Which command can be used to write data into a Delta table while avoiding the writing of duplicate records?
# MAGIC
# MAGIC - **A.** DROP  
# MAGIC - **B.** INSERT  
# MAGIC - **C.** MERGE  
# MAGIC - **D.** APPEND

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 105
# MAGIC
# MAGIC A data analyst has created a Delta table `sales` that is used by the entire data analysis team. They want help from the data engineering team to implement a series of tests to ensure the data is clean. However, the data engineering team uses Python for its tests rather than SQL.
# MAGIC
# MAGIC Which command could the data engineering team use to access `sales` in PySpark?
# MAGIC
# MAGIC - **A.** SELECT * FROM sales  
# MAGIC - **B.** spark.table("sales")  
# MAGIC - **C.** spark.sql("sales")  
# MAGIC - **D.** spark.delta.table("sales")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 106
# MAGIC
# MAGIC A data engineer has created a new database using the following command:  
# MAGIC CREATE DATABASE IF NOT EXISTS customer360;
# MAGIC
# MAGIC In which location will the customer360 database be located?
# MAGIC
# MAGIC - **A.** dbfs:/user/hive/database/customer360  
# MAGIC - **B.** dbfs:/user/hive/warehouse  
# MAGIC - **C.** dbfs:/user/hive/customer360  
# MAGIC - **D.** dbfs:/user/hive/database

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC **Question #: 107**
# MAGIC
# MAGIC A data engineer is attempting to drop a Spark SQL table `my_table` and runs the following command:
# MAGIC
# MAGIC
# MAGIC DROP TABLE IF EXISTS my_table;
# MAGIC
# MAGIC
# MAGIC After running this command, the engineer notices that the data files and metadata files have been deleted from the file system.
# MAGIC
# MAGIC **What is the reason behind the deletion of all these files?**
# MAGIC
# MAGIC - **A.** The table was managed  
# MAGIC - **B.** The table's data was smaller than 10 GB  
# MAGIC - **C.** The table did not have a location  
# MAGIC - **D.** The table was external  
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 108
# MAGIC
# MAGIC A data engineer needs to create a table in Databricks using data from a CSV file at location /path/to/csv.
# MAGIC
# MAGIC They run the following command:
# MAGIC
# MAGIC ![image_1777467132012.png](./image_1777467132012.png "image_1777467132012.png")  
# MAGIC <br>
# MAGIC
# MAGIC Which of the following lines of code fills in the above blank to successfully complete the task?
# MAGIC
# MAGIC - **A.** FROM "path/to/csv"  
# MAGIC - **B.** USING CSV  
# MAGIC - **C.** FROM CSV  
# MAGIC - **D.** USING DELTA

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 109
# MAGIC
# MAGIC What is a benefit of creating an external table from Parquet rather than CSV when using a CREATE TABLE AS SELECT statement?
# MAGIC
# MAGIC - **A.** Parquet files can be partitioned  
# MAGIC - **B.** Parquet files will become Delta tables  
# MAGIC - **C.** Parquet files have a well-defined schema  
# MAGIC - **D.** Parquet files have the ability to be optimized

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 110
# MAGIC
# MAGIC Which SQL keyword can be used to convert a table from a long format to a wide format?
# MAGIC
# MAGIC - **A.** TRANSFORM  
# MAGIC - **B.** PIVOT  
# MAGIC - **C.** SUM  
# MAGIC - **D.** CONVERT

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 111
# MAGIC
# MAGIC A data engineer has a Python variable table_name that they would like to use in a SQL query. They want to construct a Python code block that will run the query using table_name.
# MAGIC
# MAGIC They have the following incomplete code block:
# MAGIC
# MAGIC     (f"SELECT customer_id, spend FROM {table_name}")
# MAGIC
# MAGIC What can be used to fill in the blank to successfully complete the task?
# MAGIC
# MAGIC - **A.** spark.delta.sql  
# MAGIC - **B.** spark.sql  
# MAGIC - **C.** spark.table  
# MAGIC - **D.** dbutils.sql

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 112**
# MAGIC
# MAGIC A data engineer is working with two tables. Each of these tables is displayed below in its entirety.
# MAGIC
# MAGIC ![image_1777467259733.png](./image_1777467259733.png "image_1777467259733.png")</br>
# MAGIC
# MAGIC The data engineer runs the following query to join these tables together:
# MAGIC
# MAGIC ![image_1777467387578.png](./image_1777467387578.png "image_1777467387578.png")
# MAGIC
# MAGIC **A.**  
# MAGIC ![image_1777467433665.png](./image_1777467433665.png "image_1777467433665.png")
# MAGIC
# MAGIC **B.**  
# MAGIC ![image_1777467445261.png](./image_1777467445261.png "image_1777467445261.png")
# MAGIC
# MAGIC **C.**  
# MAGIC ![image_1777467457208.png](./image_1777467457208.png "image_1777467457208.png")
# MAGIC
# MAGIC **D.**  
# MAGIC ![image_1777467483788.png](./image_1777467483788.png "image_1777467483788.png")

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 113**  
# MAGIC
# MAGIC **A data engineer needs to apply custom logic to identify employees with more than 5 years of experience in array column employees in table stores. The custom logic should create a new column exp_employees that is an array of all of the employees with more than 5 years of experience for each row. In order to apply this custom logic at scale, the data engineer wants to use the FILTER higher-order function.**
# MAGIC
# MAGIC **Which code block successfully completes this task?**<br>
# MAGIC A. ![image_1777521876738.png](./image_1777521876738.png "image_1777521876738.png")
# MAGIC
# MAGIC B. ![image_1777521890699.png](./image_1777521890699.png "image_1777521890699.png")
# MAGIC
# MAGIC C. ![image_1777521903067.png](./image_1777521903067.png "image_1777521903067.png")
# MAGIC
# MAGIC D. ![image_1777521917592.png](./image_1777521917592.png "image_1777521917592.png")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 114
# MAGIC
# MAGIC A data engineer that is new to using Python needs to create a Python function to add two integers together and return the sum?
# MAGIC
# MAGIC Which code block can the data engineer use to complete this task?
# MAGIC
# MAGIC ![image_1777467441889.png](./image_1777467441889.png "image_1777467441889.png")</br>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 115**
# MAGIC
# MAGIC A data engineer has configured a Structured Streaming job to read from a table, manipulate the data, and then perform a streaming write into a new table.
# MAGIC
# MAGIC The code block used by the data engineer is below:
# MAGIC
# MAGIC ![image_1777467503417.png](./image_1777467503417.png "image_1777467503417.png")</br>
# MAGIC
# MAGIC **Which line of code should the data engineer use to fill in the blank if the data engineer only wants the query to execute a micro-batch to process data every 5 seconds?**
# MAGIC
# MAGIC - **A.** trigger("5 seconds")
# MAGIC - **B.** trigger(continuous="5 seconds")
# MAGIC - **C.** trigger(once="5 seconds")
# MAGIC - **D.** trigger(processingTime="5 seconds") 
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 116**
# MAGIC
# MAGIC A data engineer is maintaining a data pipeline. Upon data ingestion, the data engineer notices that the source data is starting to have a lower level of quality. The data engineer would like to automate the process of monitoring the quality level.
# MAGIC
# MAGIC Which of the following tools can the data engineer use to solve this problem?
# MAGIC
# MAGIC - **A.** Auto Loader  
# MAGIC - **B.** Unity Catalog  
# MAGIC - **C.** Delta Lake  
# MAGIC - **D.** Delta Live Tables  

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 117
# MAGIC
# MAGIC A data engineer has three tables in a Delta Live Tables (DLT) pipeline. They have configured the pipeline to drop invalid records at each table. They notice that some data is being dropped due to quality concerns at some point in the DLT pipeline. They would like to determine at which table in their pipeline the data is being dropped.
# MAGIC
# MAGIC Which approach can the data engineer take to identify the table that is dropping the records?
# MAGIC
# MAGIC - **A.** They can set up separate expectations for each table when developing their DLT pipeline.
# MAGIC - **B.** They can navigate to the DLT pipeline page, click on the “Error” button, and review the present errors.
# MAGIC - **C.** They can set up DLT to notify them via email when records are dropped.
# MAGIC - **D.** They can navigate to the DLT pipeline page, click on each table, and view the data quality statistics.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 118
# MAGIC
# MAGIC What is used by Spark to record the offset range of the data being processed in each trigger in order for Structured Streaming to reliably track the exact progress of the processing so that it can handle any kind of failure by restarting and/or reprocessing?
# MAGIC
# MAGIC - **A.** Checkpointing and Write-ahead Logs  
# MAGIC - **B.** Replayable Sources and Idempotent Sinks  
# MAGIC - **C.** Write-ahead Logs and Idempotent Sinks  
# MAGIC - **D.** Checkpointing and Idempotent Sinks

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 119
# MAGIC
# MAGIC What describes the relationship between Gold tables and Silver tables?
# MAGIC
# MAGIC - **A.** Gold tables are more likely to contain aggregations than Silver tables.
# MAGIC - **B.** Gold tables are more likely to contain valuable data than Silver tables.
# MAGIC - **C.** Gold tables are more likely to contain a less refined view of data than Silver tables.
# MAGIC - **D.** Gold tables are more likely to contain truthful data than Silver tables.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 120
# MAGIC
# MAGIC What describes when to use the CREATE STREAMING LIVE TABLE (formerly CREATE INCREMENTAL LIVE TABLE) syntax over the CREATE LIVE TABLE syntax when creating Delta Live Tables (DLT) tables using SQL?
# MAGIC
# MAGIC - **A.** CREATE STREAMING LIVE TABLE should be used when the subsequent step in the DLT pipeline is static.
# MAGIC - **B.** CREATE STREAMING LIVE TABLE should be used when data needs to be processed incrementally.
# MAGIC - **C.** CREATE STREAMING LIVE TABLE should be used when data needs to be processed through complicated aggregations.
# MAGIC - **D.** CREATE STREAMING LIVE TABLE should be used when the previous step in the DLT pipeline is static.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 121
# MAGIC
# MAGIC A Delta Live Table pipeline includes two datasets defined using STREAMING LIVE TABLE. Three datasets are defined against Delta Lake table sources using LIVE TABLE.
# MAGIC
# MAGIC The table is configured to run in Production mode using the Continuous Pipeline Mode.
# MAGIC
# MAGIC What is the expected outcome after clicking Start to update the pipeline assuming previously unprocessed data exists and all definitions are valid?
# MAGIC
# MAGIC - **A.** All datasets will be updated at set intervals until the pipeline is shut down. The compute resources will persist to allow for additional testing.
# MAGIC - **B.** All datasets will be updated once and the pipeline will shut down. The compute resources will persist to allow for additional testing.
# MAGIC - **C.** All datasets will be updated at set intervals until the pipeline is shut down. The compute resources will be deployed for the update and terminated when the pipeline is stopped.
# MAGIC - **D.** All datasets will be updated once and the pipeline will shut down. The compute resources will be terminated.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 122**
# MAGIC
# MAGIC Which type of workloads are compatible with Auto Loader?
# MAGIC
# MAGIC - **A.** Streaming workloads  
# MAGIC - **B.** Machine learning workloads  
# MAGIC - **C.** Serverless workloads  
# MAGIC - **D.** Batch workloads

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 123
# MAGIC
# MAGIC A data engineer has developed a data pipeline to ingest data from a JSON source using Auto Loader, but the engineer has not provided any type inference or schema hints in their pipeline. Upon reviewing the data, the data engineer has noticed that all of the columns in the target table are of the string type despite some of the fields only including float or boolean values.
# MAGIC
# MAGIC Why has Auto Loader inferred all of the columns to be of the string type?
# MAGIC
# MAGIC - A. Auto Loader cannot infer the schema of ingested data  
# MAGIC - B. JSON data is a text-based format  
# MAGIC - C. Auto Loader only works with string data  
# MAGIC - D. All of the fields had at least one null value

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 124
# MAGIC
# MAGIC Which statement regarding the relationship between Silver tables and Bronze tables is always true?
# MAGIC
# MAGIC - **A.** Silver tables contain a less refined, less clean view of data than Bronze data.
# MAGIC - **B.** Silver tables contain aggregates while Bronze data is unaggregated.
# MAGIC - **C.** Silver tables contain more data than Bronze tables.
# MAGIC - **D.** Silver tables contain less data than Bronze tables.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 125
# MAGIC
# MAGIC Which query is performing a streaming hop from raw data to a Bronze table?
# MAGIC
# MAGIC ![image_1777522282241.png](./image_1777522282241.png "image_1777522282241.png")

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 126
# MAGIC
# MAGIC A dataset has been defined using Delta Live Tables and includes an expectations clause:
# MAGIC
# MAGIC
# MAGIC CONSTRAINT valid_timestamp EXPECT (timestamp > '2020-01-01') ON VIOLATION DROP ROW
# MAGIC
# MAGIC
# MAGIC What is the expected behavior when a batch of data containing data that violates these constraints is processed?
# MAGIC
# MAGIC - **A.** Records that violate the expectation cause the job to fail.
# MAGIC - **B.** Records that violate the expectation are added to the target dataset and flagged as invalid in a field added to the target dataset.
# MAGIC - **C.** Records that violate the expectation are dropped from the target dataset and recorded as invalid in the event log.
# MAGIC - **D.** Records that violate the expectation are added to the target dataset and recorded as invalid in the event log.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 127
# MAGIC
# MAGIC A data engineer has a Job with multiple tasks that runs nightly. Each of the tasks runs slowly because the clusters take a long time to start.
# MAGIC
# MAGIC Which action can the data engineer perform to improve the start up time for the clusters used for the Job?
# MAGIC
# MAGIC - **A.** They can use endpoints available in Databricks SQL  
# MAGIC - **B.** They can use jobs clusters instead of all-purpose clusters  
# MAGIC - **C.** They can configure the clusters to autoscale for larger data sizes  
# MAGIC - **D.** They can use clusters that are from a cluster pool  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 128
# MAGIC
# MAGIC A data engineer has a single-task Job that runs each morning before they begin working. After identifying an upstream data issue, they need to set up another task to run a new notebook prior to the original task.
# MAGIC
# MAGIC Which approach can the data engineer use to set up the new task?
# MAGIC
# MAGIC - **A.** They can clone the existing task in the existing Job and update it to run the new notebook.
# MAGIC - **B.** They can create a new task in the existing Job and then add it as a dependency of the original task.
# MAGIC - **C.** They can create a new task in the existing Job and then add the original task as a dependency of the new task.
# MAGIC - **D.** They can create a new job from scratch and add both tasks to run concurrently.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 129
# MAGIC
# MAGIC A single Job runs two notebooks as two separate tasks. A data engineer has noticed that one of the notebooks is running slowly in the Job’s current run. The data engineer asks a tech lead for help in identifying why this might be the case.
# MAGIC
# MAGIC Which approach can the tech lead use to identify why the notebook is running slowly as part of the Job?
# MAGIC
# MAGIC - **A.** They can navigate to the Runs tab in the Jobs UI to immediately review the processing notebook.
# MAGIC - **B.** They can navigate to the Tasks tab in the Jobs UI and click on the active run to review the processing notebook.
# MAGIC - **C.** They can navigate to the Runs tab in the Jobs UI and click on the active run to review the processing notebook.
# MAGIC - **D.** They can navigate to the Tasks tab in the Jobs UI to immediately review the processing notebook.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 130
# MAGIC
# MAGIC A data analysis team has noticed that their Databricks SQL queries are running too slowly when connected to their always-on SQL endpoint. They claim that this issue is present when many members of the team are running small queries simultaneously. They ask the data engineering team for help. The data engineering team notices that each of the team’s queries uses the same SQL endpoint.
# MAGIC
# MAGIC Which approach can the data engineering team use to improve the latency of the team’s queries?
# MAGIC
# MAGIC - **A.** They can increase the cluster size of the SQL endpoint.
# MAGIC - **B.** They can increase the maximum bound of the SQL endpoint’s scaling range.
# MAGIC - **C.** They can turn on the Auto Stop feature for the SQL endpoint.
# MAGIC - **D.** They can turn on the Serverless feature for the SQL endpoint.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 131
# MAGIC
# MAGIC A data engineer has been using a Databricks SQL dashboard to monitor the cleanliness of the input data to an ELT job. The ELT job has its Databricks SQL query that returns the number of input records containing unexpected NULL values. The data engineer wants their entire team to be notified via a messaging webhook whenever this value reaches 100.
# MAGIC
# MAGIC Which approach can the data engineer use to notify their entire team via a messaging webhook whenever the number of NULL values reaches 100?
# MAGIC
# MAGIC - A. They can set up an Alert with a custom template.
# MAGIC - B. They can set up an Alert with a new email alert destination.
# MAGIC - C. They can set up an Alert with a new webhook alert destination.
# MAGIC - D. They can set up an Alert with one-time notifications.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 132
# MAGIC
# MAGIC A data engineer wants to schedule their Databricks SQL dashboard to refresh once per day, but they only want the associated SQL endpoint to be running when it is necessary.
# MAGIC
# MAGIC Which approach can the data engineer use to minimize the total running time of the SQL endpoint used in the refresh schedule of their dashboard?
# MAGIC
# MAGIC - **A.** They can ensure the dashboard’s SQL endpoint matches each of the queries’ SQL endpoints.
# MAGIC - **B.** They can set up the dashboard’s SQL endpoint to be serverless.
# MAGIC - **C.** They can turn on the Auto Stop feature for the SQL endpoint.
# MAGIC - **D.** They can ensure the dashboard’s SQL endpoint is not one of the included query’s SQL.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 133
# MAGIC
# MAGIC An engineering manager wants to monitor the performance of a recent project using a Databricks SQL query. For the first week following the project’s release, the manager wants the query results to be updated every minute. However, the manager is concerned that the compute resources used for the query will be left running and cost the organization a lot of money beyond the first week of the project’s release.
# MAGIC
# MAGIC Which approach can the engineering team use to ensure the query does not cost the organization any money beyond the first week of the project’s release?
# MAGIC
# MAGIC - A. They can set a limit to the number of DBUs that are consumed by the SQL Endpoint.
# MAGIC - B. They can set the query’s refresh schedule to end after a certain number of refreshes.
# MAGIC - C. They can set the query’s refresh schedule to end on a certain date in the query scheduler.
# MAGIC - D. They can set a limit to the number of individuals that are able to manage the query’s refresh schedule.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 134
# MAGIC
# MAGIC A new data engineering team has been assigned to work on a project. The team will need access to database customers in order to see what tables already exist. The team has its own group team.
# MAGIC
# MAGIC Which command can be used to grant the necessary permission on the entire database to the new team?
# MAGIC
# MAGIC A. GRANT VIEW ON CATALOG customers TO team;  
# MAGIC B. GRANT CREATE ON DATABASE customers TO team;  
# MAGIC C. GRANT USAGE ON CATALOG team TO customers;  
# MAGIC D. GRANT USAGE ON DATABASE customers TO team;

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 135
# MAGIC
# MAGIC A new data engineering team team has been assigned to an ELT project. The new data engineering team will need full privileges on the table sales to fully manage the project.
# MAGIC
# MAGIC Which command can be used to grant full permissions on the database to the new data engineering team?
# MAGIC
# MAGIC - **A.** GRANT ALL PRIVILEGES ON TABLE sales TO team;
# MAGIC - **B.** GRANT SELECT CREATE MODIFY ON TABLE sales TO team;
# MAGIC - **C.** GRANT SELECT ON TABLE sales TO team;
# MAGIC - **D.** GRANT ALL PRIVILEGES ON TABLE team TO sales;

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 136**
# MAGIC
# MAGIC Differentiate between all-purpose clusters and jobs clusters.
# MAGIC
# MAGIC A data engineering team has created a python notebook to load data from cloud storage, this job has been tested and now needs to be scheduled in production.
# MAGIC
# MAGIC **Which would be the best cluster to be used in this case?**
# MAGIC
# MAGIC - **A.** All purpose cluster  
# MAGIC - **B.** Any Unity Catalog-enabled cluster  
# MAGIC - **C.** Jobs Cluster  
# MAGIC - **D.** Serverless SQL warehouse  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 137
# MAGIC
# MAGIC Identify how the count_if function and the count where x is null can be used
# MAGIC
# MAGIC Consider a table random_values with below data.
# MAGIC
# MAGIC What would be the output of below query?
# MAGIC
# MAGIC
# MAGIC select count_if(col > 1) as count_a, count(*) as count_b, count(col1) as count_c from random_values
# MAGIC
# MAGIC
# MAGIC | col1 |
# MAGIC |------|
# MAGIC | 0    |
# MAGIC | 1    |
# MAGIC | 2    |
# MAGIC | NULL |
# MAGIC | NULL |
# MAGIC | 3    |
# MAGIC
# MAGIC A. 3 6 5  
# MAGIC B. 4 6 5  
# MAGIC C. 3 6 6  
# MAGIC D. 4 6 6

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 138
# MAGIC
# MAGIC Which two components function in the DB platform architecture’s control plane? (Choose two.)
# MAGIC
# MAGIC - A. Virtual Machines  
# MAGIC - B. Compute Orchestration  
# MAGIC - C. Serverless Compute  
# MAGIC - D. Compute  
# MAGIC - E. Unity Catalog

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 139
# MAGIC
# MAGIC In a healthcare provider organization using Delta Lake to store electronic health records (EHRs), a data analyst needs to analyze a snapshot of the patient_records table from two weeks ago before some recent data corrections were applied.
# MAGIC
# MAGIC What approach should the Data Engineer take to allow the analyst to query that specific prior version?
# MAGIC
# MAGIC - **A.** Truncate the table to remove all data, then reload the data from two weeks ago into the truncated table for the analyst to query.
# MAGIC - **B.** Identify the version number corresponding to two weeks ago from the Delta transaction log, share that version number with the analyst to query using VERSION AS OF syntax, or export that version to a new Delta table for the analyst to query.
# MAGIC - **C.** Restore the table to the version from two weeks ago using the RESTORE command, and have the analyst query the restored table.
# MAGIC - **D.** Use the VACUUM command to remove all versions of the table older than two weeks, then the analyst can query the remaining version.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 140
# MAGIC
# MAGIC What can be used to simplify and unify siloed data architectures that are specialized for specific use cases?
# MAGIC
# MAGIC - A. Delta Lake  
# MAGIC - B. Data lake  
# MAGIC - C. Data warehouse  
# MAGIC - D. Data lakehouse

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 141
# MAGIC
# MAGIC A data engineer has configured a Structured Streaming job to read from a table, manipulate the data, and then perform a streaming write into a new table.
# MAGIC
# MAGIC The code block used by the data engineer is below:
# MAGIC
# MAGIC ![image_1777522610752.png](./image_1777522610752.png "image_1777522610752.png")  
# MAGIC The data engineer only wants the query to process all of the available data in as many batches as required.
# MAGIC
# MAGIC Which line of code should the data engineer use to fill in the blank?
# MAGIC
# MAGIC - A. trigger(availableNow=True)
# MAGIC - B. trigger(processingTime= “once”)
# MAGIC - C. trigger(continuous= “once”)
# MAGIC - D. trigger(once=True)

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 142
# MAGIC
# MAGIC Data engineer and data analysts are working together on a data pipeline. The data engineer is working on the raw, bronze, and silver layers of the pipeline using Python, and the data analyst is working on the gold layer of the pipeline using SQL. The raw source of the pipeline is a streaming input. They now want to migrate their pipeline to use Delta Live Tables.
# MAGIC
# MAGIC Which of the following changes will need to be made to the pipeline when migrating to Delta Live Tables?
# MAGIC
# MAGIC - **A.** The pipeline can have different notebook sources in SQL & Python  
# MAGIC - **B.** The pipeline will need to be written entirely in SQL  
# MAGIC - **C.** The pipeline will need to use a batch source in place of a streaming source  
# MAGIC - **D.** The pipeline will need to be written entirely in Python

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 143
# MAGIC
# MAGIC Identify a scenario to use an external table.
# MAGIC
# MAGIC A Data Engineer needs to create a parquet bronze table and wants to ensure that it gets stored in a specific path in an external location.
# MAGIC
# MAGIC Which table can be created in this scenario?
# MAGIC
# MAGIC - **A.** An external table where the location is pointing to specific path in external location.
# MAGIC - **B.** An external table where the schema has managed location pointing to specific path in external location.
# MAGIC - **C.** A managed table where the catalog has managed location pointing to specific path in external location.
# MAGIC - **D.** A managed table where the location is pointing to specific path in external location.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 144
# MAGIC
# MAGIC Identify the impact of ON VIOLATION DROP ROW and ON VIOLATION FAIL UPDATE for a constraint violation.
# MAGIC
# MAGIC A data engineer has created an ETL pipeline using Delta Live table to manage their company travel reimbursement detail. They want to ensure that if the location details have not been provided by the employee, the pipeline needs to be terminated.
# MAGIC
# MAGIC How can the scenario be implemented?
# MAGIC
# MAGIC - **A.** CONSTRAINT valid_location EXPECT (location = NULL)
# MAGIC - **B.** CONSTRAINT valid_location EXPECT (location != NULL) ON VIOLATION FAIL UPDATE
# MAGIC - **C.** CONSTRAINT valid_location EXPECT (location != NULL) ON DROP ROW
# MAGIC - **D.** CONSTRAINT valid_location EXPECT (location != NULL) ON VIOLATION FAIL

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 145
# MAGIC
# MAGIC Which two conditions are applicable for governance in Databricks Unity Catalog? (Choose two.)
# MAGIC
# MAGIC - **A.** You can have more than 1 metastore within a databricks account console but only 1 per region.
# MAGIC - **B.** Both catalog and schema must have a managed location in Unity Catalog provided metastore is not associated with a location
# MAGIC - **C.** You can have multiple catalogs within metastore and 1 catalog can be associated with multiple metastore
# MAGIC - **D.** If catalog is not associated with location, it’s mandatory to associate schema with managed locations
# MAGIC - **E.** If metastore is not associated with location, it’s mandatory to associate catalog with managed locations

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 146
# MAGIC
# MAGIC A data engineer needs to access the view created by the sales team, using a shared cluster. The data engineer has been provided usage permissions on the catalog and schema. In order to access the view created by sales team.
# MAGIC
# MAGIC What are the minimum permissions the data engineer would require in addition?
# MAGIC
# MAGIC - **A.** Needs SELECT permission on the VIEW and the underlying TABLE.
# MAGIC - **B.** Needs SELECT permission only on the VIEW
# MAGIC - **C.** Needs ALL PRIVILEGES on the VIEW
# MAGIC - **D.** Needs ALL PRIVILEGES at the SCHEMA level

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 147**
# MAGIC
# MAGIC **Which method should a Data Engineer apply to ensure Workflows are being triggered on schedule?**
# MAGIC
# MAGIC - A. Scheduled Workflows require an always-running cluster, which is more expensive but reduces processing latency.
# MAGIC - B. Scheduled Workflows process data as it arrives at configured sources.
# MAGIC - C. Scheduled Workflows can reduce resource consumption and expense since the cluster runs only long enough to execute the pipeline.
# MAGIC - D. Scheduled Workflows run continuously until manually stopped.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 148
# MAGIC
# MAGIC The Delta transaction log for the ‘students’ tables is shown using the ‘DESCRIBE HISTORY students’ command. A Data Engineer needs to query the table as it existed before the UPDATE operation listed in the log.
# MAGIC
# MAGIC Which command should the Data Engineer use to achieve this? (Choose two.)
# MAGIC
# MAGIC ![image_1777522803783.png](./image_1777522803783.png "image_1777522803783.png")
# MAGIC
# MAGIC - A. SELECT * FROM students@v4  
# MAGIC - B. SELECT * FROM students TIMESTAMP AS OF ‘2024-04-22T 14:32:47.000+00:00’  
# MAGIC - C. SELECT * FROM students FROM HISTORY VERSION AS OF 3  
# MAGIC - D. SELECT * FROM students VERSION AS OF 5  
# MAGIC - E. SELECT * FROM students TIMESTAMP AS OF ‘2024-04-22T 14:32:58.000+00:00’

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 149
# MAGIC
# MAGIC An engineering manager uses a Databricks SQL query to monitor ingestion latency for each data source. The manager checks the results of the query every day, but they are manually rerunning the query each day and waiting for the results.
# MAGIC
# MAGIC Which of the following approaches can the manager use to ensure the results of the query are updated each day?
# MAGIC
# MAGIC - A. They can schedule the query to refresh every 1 day from the SQL endpoint's page in Databricks SQL.
# MAGIC - B. They can schedule the query to refresh every 12 hours from the SQL endpoint's page in Databricks SQL.
# MAGIC - C. They can schedule the query to refresh every 1 day from the query's page in Databricks SQL.
# MAGIC - D. They can schedule the query to run every 12 hours from the Jobs UI.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 150
# MAGIC
# MAGIC A data engineer needs to apply custom logic to string column city in table stores for a specific use case. In order to apply this custom logic at scale, the data engineer wants to create a SQL user-defined function (UDF).
# MAGIC
# MAGIC Which of the following code blocks creates this SQL UDF?
# MAGIC
# MAGIC ![image_1777522897337.png](./image_1777522897337.png "image_1777522897337.png")

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 151
# MAGIC
# MAGIC A data engineer has realized that they made a mistake when making a daily update to a table. They need to use Delta time travel to restore the table to a version that is 3 days old. However, when the data engineer attempts to time travel to the older version, they are unable to restore the data because the data files have been deleted.
# MAGIC
# MAGIC Which of the following explains why the data files are no longer present?
# MAGIC
# MAGIC - A. The VACUUM command was run on the table  
# MAGIC - B. The TIME TRAVEL command was run on the table  
# MAGIC - C. The DELETE HISTORY command was run on the table  
# MAGIC - D. The OPTIMIZE command was nun on the table

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 152**
# MAGIC
# MAGIC **Which of the following describes the relationship between Bronze tables and raw data?**
# MAGIC
# MAGIC A. Bronze tables contain less data than raw data files.<br>
# MAGIC B. Bronze tables contain more truthful data than raw data.<br>
# MAGIC C. Bronze tables contain raw data with a schema applied.
# MAGIC <br>
# MAGIC D. Bronze tables contain a less refined view of data than raw data.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 153**
# MAGIC
# MAGIC **A data engineer only wants to execute the final block of a Python program if the Python variable day_of_week is equal to 1 and the Python variable review_period is True.**
# MAGIC
# MAGIC **Which of the following control flow statements should the data engineer use to begin this conditionally executed code block?**
# MAGIC
# MAGIC A. if day_of_week = 1 and review_period:  
# MAGIC B. if day_of_week = 1 and review_period = "True":  
# MAGIC C. if day_of_week = 1 & review_period: = "True":  
# MAGIC D. if day_of_week == 1 and review_period:

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 154**
# MAGIC
# MAGIC **Which of the following must be specified when creating a new Delta Live Tables pipeline?**
# MAGIC
# MAGIC A. A key-value pair configuration  
# MAGIC B. At least one notebook library to be executed  
# MAGIC C. A path to cloud storage location for the written data  
# MAGIC D. A location of a target database for the written data

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 155**
# MAGIC
# MAGIC **In which of the following scenarios should a data engineer select a Task in the Depends On field of a new Databricks Job Task?**
# MAGIC
# MAGIC A. When another task needs to be replaced by the new task  
# MAGIC B. When another task needs to successfully complete before the new task begins  
# MAGIC C. When another task has the same dependency libraries as the new task  
# MAGIC D. When another task needs to use as little compute resources as possible

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 156**  
# MAGIC A data engineering team has two tables. The first table `march_transactions` is a collection of all retail transactions in the month of March. The second table `april_transactions` is a collection of all retail transactions in the month of April. There are no duplicate records between the tables.
# MAGIC
# MAGIC Which of the following commands should be run to create a new table `all_transactions` that contains all records from `march_transactions` and `april_transactions` without duplicate records?
# MAGIC
# MAGIC A. `CREATE TABLE all_transactions AS SELECT * FROM march_transactions INNER JOIN SELECT * FROM april_transactions;`  
# MAGIC B. `CREATE TABLE all_transactions AS SELECT * FROM march_transactions UNION SELECT * FROM april_transactions;`  
# MAGIC C. `CREATE TABLE all_transactions AS SELECT * FROM march_transactions OUTER JOIN SELECT * FROM april_transactions;`  
# MAGIC D. `CREATE TABLE all_transactions AS SELECT * FROM march_transactions INTERSECT SELECT * from april_transactions;`

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 157**  
# MAGIC **How can Git operations must be performed outside of Databricks Repos?**  
# MAGIC **A.** Commit  
# MAGIC **B.** Pull  
# MAGIC **C.** Merge  
# MAGIC **D.** Clone

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 159**
# MAGIC **Which Structured Streaming query is performing a hop from a Silver table to a Gold table?**<br>
# MAGIC A. 
# MAGIC ![image_1777522154949.png](./image_1777522154949.png "image_1777522154949.png")
# MAGIC
# MAGIC B. 
# MAGIC ![image_1777522168560.png](./image_1777522168560.png "image_1777522168560.png")
# MAGIC
# MAGIC C. 
# MAGIC ![image_1777522185248.png](./image_1777522185248.png "image_1777522185248.png")
# MAGIC
# MAGIC D. 
# MAGIC ![image_1777522198375.png](./image_1777522198375.png "image_1777522198375.png")

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 160**
# MAGIC
# MAGIC **A data organization leader is upset about the data analysis team’s reports being different from the data engineering team’s reports. The leader believes the siloed nature of their organization’s data engineering and data analysis architectures is to blame.**
# MAGIC
# MAGIC **Which of the following describes how a data lakehouse could alleviate this issue?**
# MAGIC
# MAGIC **A.** Both teams would respond more quickly to ad-hoc requests  
# MAGIC **B.** Both teams would use the same source of truth for their work  
# MAGIC **C.** Both teams would reorganize to report to the same department  
# MAGIC **D.** Both teams would be able to collaborate on projects in real-time

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 161**
# MAGIC
# MAGIC **A data analyst has developed a query that runs against Delta table. They want help from the data engineering team to implement a series of tests to ensure the data returned by the query is clean. However, the data engineering team uses Python for its tests rather than SQL.**
# MAGIC
# MAGIC **Which of the following operations could the data engineering team use to run the query and operate with the results in PySpark?**
# MAGIC
# MAGIC A. SELECT * FROM sales  
# MAGIC B. spark.delta.table  
# MAGIC C. spark.sql  
# MAGIC D. spark.table

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 162**
# MAGIC
# MAGIC **A data engineer has a Job that has a complex run schedule, and they want to transfer that schedule to other Jobs.**
# MAGIC
# MAGIC **Rather than manually selecting each value in the scheduling form in Databricks, which of the following tools can the data engineer use to represent and submit the schedule programmatically?**
# MAGIC
# MAGIC A. pyspark.sql.types.DateType  
# MAGIC B. datetime  
# MAGIC C. pyspark.sql.types.TimestampType  
# MAGIC D. Cron syntax

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 163**
# MAGIC
# MAGIC **A data engineer and data analyst are working together on a data pipeline. The data engineer is working on the raw, bronze, and silver layers of the pipeline using Python, and the data analyst is working on the gold layer of the pipeline using SQL. The raw source of the pipeline is a streaming input. They now want to migrate their pipeline to use Delta Live Tables.**
# MAGIC
# MAGIC **Which of the following changes will need to be made to the pipeline when migrating to Delta Live Tables?**
# MAGIC
# MAGIC **A.** The pipeline will need to be written entirely in Python  
# MAGIC **B.** The pipeline will need to stop using the medallion-based multi-hop architecture  
# MAGIC **C.** The pipeline will need to be written entirely in SQL  
# MAGIC **D.** The pipeline can have different notebook sources in SQL & Python.  

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 164**
# MAGIC
# MAGIC **A data engineer needs access to a table `new_table`, but they do not have the correct permissions. They can ask the table owner for permission, but they do not know who the table owner is.**
# MAGIC
# MAGIC **Which of the following approaches can be used to identify the owner of `new_table`?**
# MAGIC
# MAGIC **A.** Review the Permissions tab in the table's page in Data Explorer  
# MAGIC **B.** There is no way to identify the owner of the table  
# MAGIC **C.** Review the Owner field in the table's page in Data Explorer  
# MAGIC **D.** Review the Owner field in the table's page in the cloud storage solution

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 165**
# MAGIC
# MAGIC **A data engineer needs to create a table in Databricks using data from their organization's existing SQLite database.**
# MAGIC
# MAGIC They run the following command: 
# MAGIC ```SQL
# MAGIC CREATE TABLE jdbc_customer360 USING <blank>
# MAGIC OPTIONS (
# MAGIC   url "jdbc.sqlite://customers.db", 
# MAGIC   dbtable "customer360"
# MAGIC )
# MAGIC ```
# MAGIC **Which of the following lines of code fills in the above blank to successfully complete the task?**
# MAGIC
# MAGIC - **A.** org.apache.spark.sql.jdbc  
# MAGIC - **B.** autoloader  
# MAGIC - **C.** org.apache.spark.sql.sqlite  
# MAGIC - **D.** sqlite

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 166**  
# MAGIC **In which of the following scenarios should a data engineer use the MERGE INTO command instead of the INSERT INTO command?**
# MAGIC
# MAGIC **A.** When the location of the data needs to be changed  
# MAGIC **B.** When the target table is an external table  
# MAGIC **C.** When the source is not a Delta table  
# MAGIC **D.** When the target table cannot contain duplicate records

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 167**<br>
# MAGIC **A data engineer is designing a data pipeline. The source system generates files in a shared directory that is also used by other processes. As a result, the files should be kept as is and will accumulate in the directory. The data engineer needs to identify which files are new since the previous run in the pipeline, and set up the pipeline to only ingest those new files with each run.**
# MAGIC
# MAGIC **Which of the following tools can the data engineer use to solve this problem?**<br>
# MAGIC A. Unity Catalog <br>
# MAGIC B. Delta Lake<br>
# MAGIC C. Databricks SQL<br>
# MAGIC D. Auto Loader 
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 168**
# MAGIC
# MAGIC **What is stored in the Databricks customer’s cloud account?**
# MAGIC
# MAGIC **A.** Databricks web application  
# MAGIC **B.** Cluster management metadata  
# MAGIC **C.** Notebooks  
# MAGIC **D.** Data

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #: 169**
# MAGIC
# MAGIC **A data engineer wants to create a relational object by pulling data from two tables. The relational object does not need to be used by other data engineers in other sessions. In order to save on storage costs, the data engineer wants to avoid copying and storing physical data.**
# MAGIC
# MAGIC **Which of the following relational objects should the data engineer create?**
# MAGIC
# MAGIC **A.** Spark SQL Table  
# MAGIC **B.** View  
# MAGIC **C.** Delta Table  
# MAGIC **D.** Temporary view

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 170**
# MAGIC
# MAGIC **Which of the following commands will return the number of null values in the member_id column?**
# MAGIC
# MAGIC A. SELECT count(member_id) FROM my_table;  
# MAGIC B. SELECT count(member_id) - count_null(member_id) FROM my_table;  
# MAGIC C. SELECT count_if(member_id IS NULL) FROM my_table;  
# MAGIC D. SELECT null(member_id) FROM my_table;

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #: 171**
# MAGIC
# MAGIC **Which tool is used by Auto Loader to process data incrementally?**
# MAGIC
# MAGIC **A.** Checkpointing  
# MAGIC **B.** Spark Structured Streaming  
# MAGIC **C.** Databricks SQL  
# MAGIC **D.** Unity Catalog

# COMMAND ----------

# MAGIC %md
# MAGIC Question #: 172
# MAGIC
# MAGIC Which of the following benefits is provided by the array functions from Spark SQL?
# MAGIC
# MAGIC **A.** An ability to work with data in a variety of types at once  
# MAGIC **B.** An ability to work with data within certain partitions and windows  
# MAGIC **C.** An ability to work with time-related data in specified intervals  
# MAGIC **D.** An ability to work with complex, nested data ingested from JSON files

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #: 173
# MAGIC
# MAGIC A data engineer is working with two tables. Each of these tables is displayed below in its entirety.
# MAGIC
# MAGIC **sales**
# MAGIC
# MAGIC | customer_id | spend  | units |
# MAGIC |-------------|--------|-------|
# MAGIC | a1          | 28.94  | 7     |
# MAGIC | a3          | 874.12 | 23    |
# MAGIC | a4          | 8.99   | 1     |
# MAGIC
# MAGIC **Favorite_stores**
# MAGIC
# MAGIC | customer_id | store_id |
# MAGIC |-------------|----------|
# MAGIC | a1          | s1       |
# MAGIC | a2          | s1       |
# MAGIC | a4          | s2       |
# MAGIC
# MAGIC The data engineer runs the following query to join these tables together:
# MAGIC
# MAGIC
# MAGIC SELECT
# MAGIC   sales.customer_id,
# MAGIC   sales.spend,
# MAGIC   favorite_stores.store_id
# MAGIC FROM sales
# MAGIC LEFT JOIN favorite_stores
# MAGIC ON sales.customer_id = favorite_stores.customer_id;
# MAGIC
# MAGIC
# MAGIC Which of the following will be returned by the above query?
# MAGIC
# MAGIC **A.**
# MAGIC | customer_id | spend  | store_id |
# MAGIC |-------------|--------|----------|
# MAGIC | a1          | 28.94  | s1       |
# MAGIC | a4          | 8.99   | s2       |
# MAGIC
# MAGIC **B.**
# MAGIC | customer_id | spend  | store_id |
# MAGIC |-------------|--------|----------|
# MAGIC | a1          | 28.94  | s1       |
# MAGIC | a2          | NULL   | s1       |
# MAGIC | a4          | 8.99   | s2       |
# MAGIC
# MAGIC **C.**
# MAGIC | customer_id | spend  | store_id |
# MAGIC |-------------|--------|----------|
# MAGIC | a1          | 28.94  | s1       |
# MAGIC | a3          | 874.12 | NULL     |
# MAGIC | a4          | 8.99   | s2       |
# MAGIC
# MAGIC **D.**
# MAGIC | customer_id | spend  | store_id |
# MAGIC |-------------|--------|----------|
# MAGIC | a1          | 28.94  | s1       |
# MAGIC | a2          | NULL   | s1       |
# MAGIC | a3          | 874.12 | NULL     |
# MAGIC | a4          | 8.99   | s2       |

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
