# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "2"
# ///
# MAGIC %md
# MAGIC **Question #:1**
# MAGIC
# MAGIC **Which SQL code snippet will correctly demonstrate a Data Definition Language (DDL) operation used to create a table?**
# MAGIC
# MAGIC A. CREATE TABLE employees ( id INT,
# MAGIC    name STRING
# MAGIC    );
# MAGIC
# MAGIC B. DROP TABLE employees;
# MAGIC
# MAGIC C. ALTER TABLE employees ADD COLUMN salary DECIMAL(10,2);
# MAGIC
# MAGIC D. INSERT INTO employees (id, name) VALUES (1 'Alice');

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:2**
# MAGIC
# MAGIC **What are the transformations typically included in building the Bronze layer?**
# MAGIC
# MAGIC A. Include columns Load date/time, process ID  
# MAGIC B. Business rules and transformations  
# MAGIC C. Perform extensive data cleansing  
# MAGIC D. Aggregate data from multiple

# COMMAND ----------

# MAGIC %md
# MAGIC    
# MAGIC **Question #:3**
# MAGIC
# MAGIC **A global retail company sells products across multiple categories (e.g., Electronics, Clothing) and regions (e.g., North, South, East, West). The sales team has provided the data engineer with a PySpark dataframe named sales_df as below and the team wants the data engineer to analyze the sales data to help them make strategic decisions. sales_df.** 
# MAGIC
# MAGIC ![image_1777376367427.png](./image_1777376367427.png "image_1777376367427.png")
# MAGIC
# MAGIC **Calculate the total sales amount for each product category and store the results in a new dataframe called category_sales.**
# MAGIC
# MAGIC **What will generate the expected result of category_sales?**
# MAGIC
# MAGIC ![image_1777376477759.png](./image_1777376477759.png "image_1777376477759.png")
# MAGIC
# MAGIC A. category_sales = sales_df.groupBy("category").agg(sum("sales_amount").alias("total_sales_amount"))  
# MAGIC B. category_sales = sales_df.sum("sales_amount").groupBy("category").alias("total_sales_amount"))  
# MAGIC C. category_sales = sales_df.agg(sum("sales_amount").groupBy("category").alias("total_sales_amount"))  
# MAGIC D. category_sales = sales_df.groupBy("region").agg(sum("sales_amount").alias("total_sales_amount"))

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #:4**
# MAGIC
# MAGIC **A company sells products across multiple categories (e.g., Electronics, Clothing) and regions. The sales team has provided you with a PySpark dataframe named sales_df as below, and the team wants the data engineer to analyze the sales data to help make strategic decisions.**
# MAGIC
# MAGIC ![image_1777376604852.png](./image_1777376604852.png "image_1777376604852.png")
# MAGIC
# MAGIC **Calculate the total sales amount for each region and store the results in a new dataframe called region_sales.**
# MAGIC
# MAGIC Given the expected result:
# MAGIC
# MAGIC ![image_1777376624732.png](./image_1777376624732.png "image_1777376624732.png")
# MAGIC
# MAGIC **Which code will generate the expected result?**
# MAGIC
# MAGIC A. region_sales = sales_df.groupBy("category").sum("sales_amount").alias("total_sales_amount")  
# MAGIC B. region_sales = sales_df.groupBy("region").agg(sum("sales_amount").alias("total_sales_amount"))  
# MAGIC C. region_sales sales_df.sum("sales_amount").groupBy("region").alias("total_sales_amount")  
# MAGIC D. region_sales = sales_df.agg(sum("sales_amount").groupBy("region").alias("total_sales_amount"))

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:5**
# MAGIC
# MAGIC **A data engineering team is using Kafka to capture event data and then ingest it into Databricks. The team wants to be able to see these historical events. Medallion architecture is already in place. The team wants to be mindful of costs.**
# MAGIC
# MAGIC **Where should this historical event data be stored?**
# MAGIC
# MAGIC A. Gold  
# MAGIC B. Silver  
# MAGIC C. Bronze  
# MAGIC D. Raw layer

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #:6**
# MAGIC
# MAGIC **Which two items are characteristics of the Gold Layer? (Choose two.)**
# MAGIC
# MAGIC A. Historical lineage  
# MAGIC B. Raw Data  
# MAGIC C. Normalised  
# MAGIC D. De-normalised  
# MAGIC E. Read-optimized

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:7**
# MAGIC
# MAGIC **A data engineer team has decided to implement a new data platform on Databricks and is currently deciding how to store each kind of data on each data layer.**
# MAGIC
# MAGIC **What is the appropriate layer and data pairing for medallion architecture?**
# MAGIC
# MAGIC A. Silver Layer - Raw data from deposit account application  
# MAGIC B. Bronze Layer - Summary of cash deposit amount for each country and city  
# MAGIC C. Silver Layer - Cleansed master customer data  
# MAGIC D. Gold Layer - Deduplicated money transfer

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:8**
# MAGIC
# MAGIC **A data engineer has been provided a PySpark DataFrame named df with columns product and revenue. The data engineer needs to compute complex aggregations to determine each product's total revenue, average revenue, and transaction count**.
# MAGIC
# MAGIC **Which code snippet should the data engineer use?**
# MAGIC
# MAGIC A. ```from pyspark.sql import functions as F
# MAGIC  aggregated_df = df.groupBy("product").agg(F.sum("revenue").alias("total_revenue"), F.avg("revenue").alias("avg_revenue"), F.count("*").alias("transaction_count"))```
# MAGIC
# MAGIC B. ```aggregated_df = df.groupBy("product").agg( "sum(revenue)", "avg(revenue)", "count(revenue)" )```
# MAGIC
# MAGIC C. ```from pyspark.sql import functions as F aggregated_df = df.select("product", "revenue").groupBy("product").agg(F.sum("revenue"), F.mean("revenue"))```
# MAGIC
# MAGIC D. ```aggregated_df = df.groupBy("product").agg({"revenue": "sum", "revenue": "avg", "revenue": "count"})```

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:9**
# MAGIC
# MAGIC **A data engineer is developing an ETL process based on Spark SQL. The execution fails. The data engineer checks the Spark UI and can see the ERRORS as follows: `"java.lang.OutofMemoryError: Java heap space"`**
# MAGIC
# MAGIC **Which two corrective actions should the data engineer perform to resolve this issue? (Choose two.)**
# MAGIC
# MAGIC A. Narrow the filters in order to collect less data in the query  
# MAGIC B. Upsize the worker nodes and activate autoshuffle partitions  
# MAGIC C. Upsize the driver node and deactivate autoshuffle partitions  
# MAGIC D. Cache the dataset in order to boost the query performance  
# MAGIC E. Fix the shuffle partitions to 50 to ensure the allocation

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:10**
# MAGIC
# MAGIC **A data engineer is working in a Python notebook on Databricks to process data, but notices that the output is not as expected. The data engineer wants to investigate the issue by stepping through the code and checking the values of certain variables during execution.**
# MAGIC
# MAGIC **Which tool should the data engineer use to inspect the code execution and variables in real-time?**
# MAGIC
# MAGIC A. Cluster Logs  
# MAGIC B. Job Execution Dashboard  
# MAGIC C. Python Notebook Interactive Debugger  
# MAGIC D. SQL Analytics

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:11**
# MAGIC
# MAGIC **A data engineer is writing a script that is meant to ingest new data from cloud storage. In the event of the Schema change, the ingestion should fail. It should fail until the changes downstream source can be found and verified as intended changes.**
# MAGIC
# MAGIC **Which command will meet the requirements?**
# MAGIC
# MAGIC A. failonNewColumns  
# MAGIC B. none  
# MAGIC C. rescue  
# MAGIC D. addNewColumns

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:12**
# MAGIC
# MAGIC **A data engineer needs to ingest from both streaming and batch sources for a firm that relies on highly accurate data. Occasionally, some of the data picked up by the sensors that provide a streaming input are outside the expected parameters. If this occurs, the data must be dropped, but the stream should not fail.**
# MAGIC
# MAGIC **Which feature of Delta Live Tables meets this requirement?**
# MAGIC
# MAGIC A. Change Data Capture  
# MAGIC B. Error Handling  
# MAGIC C. Monitoring  
# MAGIC D. Expectations

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:13**
# MAGIC
# MAGIC **A data engineer has inherited a Databricks pipeline from a previous team. The pipeline is missing SLAs and costs more than the allotted budget. On analysis, it is noted that the cluster is not being fully utilized, and the dataset is getting skewed.**
# MAGIC
# MAGIC **How should the data engineer resolve this issue?**
# MAGIC
# MAGIC A. Use coalesce() on the dataset to merge partitions and reduce skew.  
# MAGIC B. Increase the number of executors for the job.  
# MAGIC C. Repartition the dataset to have it be more optimally spread across all nodes.  
# MAGIC D. Increase the executor memory for the job.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #:14**
# MAGIC
# MAGIC **A data engineer streams customer orders into a Kafka topic (`orders_topic`) and is currently writing the ingestion script of a DLT pipeline. The data engineer needs to ingest the data from Kafka brokers to DLT using Databricks.**
# MAGIC
# MAGIC **What is the correct code for ingesting the data?**
# MAGIC
# MAGIC A.
# MAGIC ```python
# MAGIC import dlt
# MAGIC
# MAGIC @dlt.table(
# MAGIC     name = "orders_raw",
# MAGIC )
# MAGIC def orders_raw():
# MAGIC     return (
# MAGIC         spark.readStream
# MAGIC             .format("kafka")
# MAGIC             .option("kafka.bootstrap.servers", "broker:9092")
# MAGIC             .option("subscribe", "orders_topic")
# MAGIC             .option("startingOffsets", "earliest")
# MAGIC             .load()
# MAGIC     )
# MAGIC ```
# MAGIC
# MAGIC B.
# MAGIC ```python
# MAGIC import dlt
# MAGIC
# MAGIC @dlt.table(
# MAGIC     name = "orders_raw",
# MAGIC )
# MAGIC def orders_raw():
# MAGIC     return (
# MAGIC         spark.readStream
# MAGIC             .format("cloudFiles")
# MAGIC             .option("cloudFiles.format", "json")
# MAGIC             .option("cloudFiles.schemaLocation", "/schema/location")
# MAGIC             .load("kafka://broker:9092/orders_topic")
# MAGIC     )
# MAGIC ```
# MAGIC
# MAGIC C.
# MAGIC ```sql
# MAGIC CREATE LIVE TABLE orders_raw AS
# MAGIC SELECT CAST(value AS STRING) AS json_data
# MAGIC FROM STREAM kafka.`broker:9092/orders_topic`;
# MAGIC ```
# MAGIC
# MAGIC D.
# MAGIC ```sql
# MAGIC CREATE STREAMING LIVE TABLE orders_raw AS
# MAGIC SELECT
# MAGIC     value:order_id AS order_id,
# MAGIC     value:customer_id AS customer_id,
# MAGIC     value:amount AS amount,
# MAGIC     value:order_status AS order_status,
# MAGIC     value:order_timestamp AS order_timestamp
# MAGIC FROM cloud_files("kafka://broker:9092/orders_topic", "json");
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:15**
# MAGIC
# MAGIC **A data engineer has developed an ETL that produce a Delta managed table with liquid clustering feature activated as output. Several consumers are having issues regarding time delay when reading this table.**
# MAGIC
# MAGIC **How could the Data Engineer be sure about the OPTIMIZE command has been executed explicitly?**
# MAGIC
# MAGIC A. Check the system table system.storage.predictive_optimization operations_history  
# MAGIC B. Use SHOW TABLES EXTENDED to check the partitions columns used  
# MAGIC C. Use DESCRIBE DETAIL table to see the file size and number of files for the table  
# MAGIC D. Use DESCRIBE HISTORY table to check if exists any OPTIMIZE operation

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:16**
# MAGIC
# MAGIC **A data engineer is working on a Databricks project that utilizes cloud storage. The data engineer wants to load several JSON files from containers on a storage account as soon as the file arrives within the storage account.**
# MAGIC
# MAGIC **Which syntax should the data engineer follow to first load the files into a dataframe and check that it is working as expected using Python?**
# MAGIC
# MAGIC A. `df = spark.read.json ("input/path")`  
# MAGIC B. `df = spark.readstream.format("cloud").option ("json").load("/input/path")`  
# MAGIC C. `df = spark.readStream.format("json".load("input/path")`  
# MAGIC D. `df = spark.readStream.format("cloudFiles").option ("cloudFiles.format", "json").load("/input/path")`

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #:17**
# MAGIC
# MAGIC **A data engineer is processing ingested streaming tables and needs to filter out NULL values in the order_datetime column from the raw streaming table orders_raw and store the results in a new table orders_valid using DLT.**
# MAGIC
# MAGIC **Which code snippet should the data engineer use?**
# MAGIC
# MAGIC A.
# MAGIC ```SQL
# MAGIC CREATE OR REFRESH STREAMING TABLE orders_valid(
# MAGIC   CONSTRAINT valid_date
# MAGIC   EXPECT (order_datetime IS NOT NULL) ON VIOLATION DROP ROW
# MAGIC )
# MAGIC AS SELECT * FROM STREAM orders_raw;
# MAGIC ```
# MAGIC
# MAGIC B.
# MAGIC ```SQL
# MAGIC CREATE OR REFRESH STREAMING TABLE orders_valid (
# MAGIC   CONSTRAINT valid_date EXPECT (order_datetime IS NOT NULL) ON VIOLATION DROP ROW
# MAGIC )
# MAGIC AS SELECT * FROM orders_raw;
# MAGIC ```
# MAGIC
# MAGIC C.
# MAGIC ```SQL
# MAGIC CREATE OR REFRESH STREAMING TABLE orders_valid AS
# MAGIC SELECT *
# MAGIC FROM STREAM(orders_raw)
# MAGIC WHERE order_datetime IS NOT NULL;
# MAGIC ```
# MAGIC
# MAGIC D.
# MAGIC ```SQL
# MAGIC CREATE OR REPLACE STREAMING TABLE orders_valid (
# MAGIC   FILTER (order_datetime IS NOT NULL)
# MAGIC )
# MAGIC AS SELECT * FROM STREAM(orders_raw);
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #:18**
# MAGIC
# MAGIC **What is the functionality of AutoLoader in Databricks?**
# MAGIC
# MAGIC A. Auto Loader automatically ingests and processes new files from cloud storage, handling both batch and streaming data with support for schema evolution.  
# MAGIC B. Auto Loader automatically ingests and processes new files from cloud storage, handling batch and streaming data with no support for schema evolution.  
# MAGIC C. Auto Loader automatically ingests and processes new files from cloud storage, handling only streaming data with no support for schema evolution.  
# MAGIC D. Auto Loader automatically ingests and processes new files from cloud storage, handling batch data with support for schema evolution.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:19**
# MAGIC
# MAGIC **A data engineer is using the Databricks OPTIMIZE command on a Delta table. What happens when OPTIMIZE is run twice on the same table with the same data?**
# MAGIC
# MAGIC A. It has no effect because it is idempotent.  
# MAGIC B. It changes the number of tuples per file significantly.  
# MAGIC C. It further reduces file sizes by re-clustering the data.  
# MAGIC D. It triggers a full liquid clustering

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:20**
# MAGIC
# MAGIC **A data engineer is inspecting an ETL pipeline based on a Pyspark job that consistently encounters performance bottlenecks. Based on developer feedback, the data engineer assumes the job is low on compute resources. To pinpoint the issue, the data engineer observes the Spark UI and finds out the job has a high CPU time vs Task time.**
# MAGIC
# MAGIC **Which course of action should the data engineer take?**
# MAGIC
# MAGIC A. High CPU time vs Task time means an under-utilized cluster. The data engineer may need to repartition data to spread the jobs more evenly throughout the cluster.  
# MAGIC B. High CPU time vs Task time means efficient use of cluster and no change needed  
# MAGIC C. High CPU time vs Task time means a CPU over-utilized job. The data engineer may need to consider executor and core tuning or resizing the cluster  
# MAGIC D. High CPU time vs Task time means over-utilized memory and the need to increase parallelism

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:21**
# MAGIC
# MAGIC A data engineer needs to parse only png files in a directory that contains files with different suffixes.
# MAGIC
# MAGIC Which code should the data engineer use to achieve this task?
# MAGIC
# MAGIC A. 
# MAGIC ```python
# MAGIC df = spark.readStream.format("cloudFiles") \
# MAGIC     .option("cloudFiles.format", "binaryFile") \
# MAGIC     .append("/*.png")
# MAGIC ```
# MAGIC
# MAGIC B. 
# MAGIC ```python
# MAGIC df = spark.readstream.format("cloudFiles") \
# MAGIC     .option("cloudFiles.format", "binaryFile") \
# MAGIC     .option("pathGlobfilter", "*.png") \
# MAGIC     .load(<base-path>)
# MAGIC ```
# MAGIC
# MAGIC C. 
# MAGIC ```python
# MAGIC df = spark.readStream.format("cloudFiles") \
# MAGIC     .option("cloudFiles.format", "binaryFile") \
# MAGIC     .option("pathGlobfilter", "*.png") \
# MAGIC     .append()
# MAGIC ```
# MAGIC
# MAGIC D. 
# MAGIC ```python
# MAGIC df = spark.readstream.format("cloudFiles") \
# MAGIC     .option("cloudFiles.format", "binaryFile") \
# MAGIC     .load("/*.png")
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:22**
# MAGIC
# MAGIC **A data engineer has inherited a Databricks pipeline from a previous team. The pipeline is missing its SLAs, and an initial investigation has identified memory spills in Spark. These increased runtimes are also driving up costs. The data engineer needs to reduce the runtime without significantly increasing costs.**
# MAGIC
# MAGIC **What should the data engineer do first to address this issue?**
# MAGIC
# MAGIC A. Tweak the "spark.sql.shuffle.partitions" configuration.  
# MAGIC B. Enable autoscaling in the cluster to match the requirements  
# MAGIC C. Use a photon enabled execution engine.  
# MAGIC D. Ensure the cluster uses memory optimized node

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:23**
# MAGIC
# MAGIC **A data engineer is facing performance bottlenecks in an e-commerce transactions Delta table. The table is a managed Unity Catalog table, and it uses partitioning and Z-ordering in its data layout scheme. The predictive optimization for Unity Catalog tables is also enabled. The table has a frequently changing query filter, and the data engineer does not observe a benefit of the Data Layout or the Predictive Optimization.**
# MAGIC
# MAGIC **How should the data engineer fix the data layout bottlenecks?**
# MAGIC
# MAGIC A. Re-write the Data Layout with Liquid Clustering and cluster by the Z-Ordered columns.  
# MAGIC B. Enable Delta Caching so that query results can be read through caches.  
# MAGIC C. Tweak the Z-Order columns and run OPTIMIZE manually.  
# MAGIC D. Switch the Data layout from Partition+Z-Ordering to Automatic Liquid Clustering.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:24**
# MAGIC
# MAGIC **A data engineer needs to optimize the data layout and query performance for an e-commerce transactions Delta table. The table is partitioned by "purchase_date" (a date column) which helps with time-based queries but does not optimize searches on user statistics "customer_id", a high-cardinality column.**
# MAGIC
# MAGIC **The table is usually queried with filters on "customer_id" within specific date ranges, but since this data is spread across multiple files in each partition, it results in full partition scans and increased runtime and costs.**
# MAGIC
# MAGIC **How should the data engineer optimize the Data Layout for efficient reads?**
# MAGIC
# MAGIC A. Alter table implementing liquid clustering on "customer_id" while keeping the existing partitioning.  
# MAGIC B. Alter the table implementing liquid clustering by "customer_id" and "purchase_date".  
# MAGIC C. Alter the table to partition by "customer_id".  
# MAGIC D. Enable delta caching on the cluster so that frequent reads are cached for performance.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:25**
# MAGIC
# MAGIC **A Delta Live Table pipeline includes two datasets defined using STREAMING LIVE TABLE. Three datasets are defined against Delta Lake table sources using LIVE TABLE. The table is configured to run in Production mode using the Continuous Pipeline Mode.**
# MAGIC
# MAGIC **What is the expected outcome after clicking Start to update the pipeline assuming previously unprocessed data exists and all definitions are valid?**
# MAGIC
# MAGIC A. All datasets will be updated at set intervals until the pipeline is shut down. The compute resources will persist to allow for additional testing.  
# MAGIC B. All datasets will be updated once and the pipeline will shut down. The compute resources will persist to allow for additional testing.  
# MAGIC C. All datasets will be updated at set intervals until the pipeline is shut down. The compute resources will be deployed for the update and terminated when the pipeline is stopped.  
# MAGIC D. All datasets will be updated once and the pipeline will shut down. The compute resources will be terminated.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:26**
# MAGIC
# MAGIC A data engineer has a Job with multiple tasks that runs nightly. Each of the tasks runs slowly because the clusters take a long time to start.
# MAGIC
# MAGIC Which action can the data engineer perform to improve the start up time for the clusters used for the Job?
# MAGIC
# MAGIC A. They can use endpoints available in Databricks SQL  
# MAGIC B. They can use jobs clusters instead of all-purpose clusters  
# MAGIC C. They can configure the clusters to autoscale for larger data sizes  
# MAGIC D. They can use clusters that are from a cluster pool

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:27**
# MAGIC
# MAGIC A data engineer has a single-task Job that runs each morning before they begin working. After identifying an upstream data issue, they need to set up another task to run a new notebook prior to the original task.
# MAGIC
# MAGIC **Which approach can the data engineer use to set up the new task?**
# MAGIC
# MAGIC A. They can clone the existing task in the existing Job and update it to run the new notebook.  
# MAGIC B. They can create a new task in the existing Job and then add it as a dependency of the original task.  
# MAGIC C. They can create a new task in the existing Job and then add the original task as a dependency of the new task.  
# MAGIC D. They can create a new job from scratch and add both tasks to run concurrently.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:28**
# MAGIC
# MAGIC A single Job runs two notebooks as two separate tasks. A data engineer has noticed that one of the notebooks is running slowly in the Job's current run. The data engineer asks a tech lead for help in identifying why this might be the case.
# MAGIC
# MAGIC **Which approach can the tech lead use to identify why the notebook is running slowly as part of the Job?**
# MAGIC
# MAGIC A. They can navigate to the Runs tab in the Jobs UI to immediately review the processing notebook.  
# MAGIC B. They can navigate to the Tasks tab in the Jobs UI and click on the active run to review the processing notebook.  
# MAGIC C. They can navigate to the Runs tab in the Jobs Ul and click on the active run to review the processing notebook.  
# MAGIC D. They can navigate to the Tasks tab in the Jobs Ul to immediately review the processing notebook.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:29**
# MAGIC
# MAGIC A data engineer and data analyst are working together on a data pipeline. The data engineer is working on the raw, bronze, and silver layers of the pipeline using Python, and the data analyst is working on the gold layer of the pipeline using SQL. The raw source of the pipeline is a streaming input. They now want to migrate their pipeline to use Delta Live Tables.
# MAGIC
# MAGIC Which of the following changes will need to be made to the pipeline when migrating to Delta Live Tables?
# MAGIC
# MAGIC A. The pipeline will need to be written entirely in Python  
# MAGIC B. The pipeline will need to stop using the medallion-based multi-hop architecture  
# MAGIC C. The pipeline will need to be written entirely in SQL  
# MAGIC D. The pipeline will need to use a batch source in place of a streaming source

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:30**
# MAGIC
# MAGIC A data engineer is working in a Databricks notebook to design and manage a batch ETL pipeline. The engineer is writing SQL and Python code to clean data, transform it, and join large datasets from different sources. The engineer wants to organize these steps into a structured process that can be run regularly and scheduled as part of a data pipeline.
# MAGIC
# MAGIC Which Databricks notebook feature is applicable in the use case?
# MAGIC
# MAGIC A. Real-time streaming support  
# MAGIC B. Collaborative editing  
# MAGIC C. Task workflows and job scheduling  
# MAGIC D. Notebook version control

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #:31**
# MAGIC
# MAGIC **A data engineer needs to develop integration tests for an ETL process and deploy a version-controlled, packaged workflow into production using an external job scheduler. Which tool should the data engineer use for this job?**
# MAGIC
# MAGIC A. Databricks Connect  
# MAGIC B. Databricks Asset Bundles  
# MAGIC C. Databricks Command Line Interface  
# MAGIC D. Databricks Software Development

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #:32**
# MAGIC
# MAGIC **Which Databricks asset bundle format is valid?**
# MAGIC
# MAGIC A:
# MAGIC resources:
# MAGIC   jobs:
# MAGIC     hello-job:
# MAGIC       name: hello-job
# MAGIC       tasks:
# MAGIC         task_key: hello-task
# MAGIC         existing_cluster_id: 1234-567890-abcde123
# MAGIC         notebook_task:
# MAGIC           notebook_path: ./hello.py
# MAGIC
# MAGIC B:
# MAGIC "resources": {
# MAGIC   "jobs": {
# MAGIC     "name": "hello-job",
# MAGIC     "tasks": {
# MAGIC       "task_key": "hello-task",
# MAGIC       "existing_cluster_id": "1234-567890-abcde123",
# MAGIC       "notebook_task": {
# MAGIC         "notebook_path": ".hello.py"
# MAGIC       }
# MAGIC     }
# MAGIC   }
# MAGIC }
# MAGIC
# MAGIC C:
# MAGIC configuration = {
# MAGIC   "resources": {
# MAGIC     "jobs": {
# MAGIC       "name": "hello-job",
# MAGIC       "tasks": {
# MAGIC         "task_key": "hello-task",
# MAGIC         "existing_cluster_id": "1234-567890-abcde123",
# MAGIC         "notebook_task": {
# MAGIC           "notebook_path": ".hello.py"
# MAGIC         }
# MAGIC       }
# MAGIC     }
# MAGIC   }
# MAGIC }
# MAGIC
# MAGIC D:
# MAGIC resources {
# MAGIC   jobs {
# MAGIC     name = "hello-job"
# MAGIC     tasks {
# MAGIC       task_key = "hello-task"
# MAGIC       existing_cluster_id = "1234-567890-abcde123"
# MAGIC       notebook_task {
# MAGIC         notebook_path = ".hello.py"
# MAGIC       }
# MAGIC     }
# MAGIC   }
# MAGIC }

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #:33**
# MAGIC
# MAGIC A data engineer is designing an ETL pipeline to process both streaming and batch data from multiple sources. The pipeline must ensure data quality, handle schema evolution, and provide easy maintenance. The team is considering using Delta Live Tables (DLT) in Databricks to achieve these goals. They want to understand the key features and benefits of DLT that make it suitable for this use case.
# MAGIC
# MAGIC **Why is Delta Live Tables (DLT) an appropriate choice?**
# MAGIC
# MAGIC a. Automatic data quality checks, built-in support for schema evolution, and declarative pipeline development  
# MAGIC b. Manual schema enforcement, high operational overhead, and limited scalability  
# MAGIC c. Requires custom code for data quality checks, no support for streaming data, and complex pipeline maintenance  
# MAGIC d. Supports only batch processing, no data versioning, and high infrastructure costs  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #:34**
# MAGIC
# MAGIC A Data Engineer is building a simple data pipeline using Delta Live Tables (DLT) in Databricks to ingest customer data. The raw customer data is stored in a cloud storage location in JSON format. The task is to create a DLT pipeline that reads the raw JSON data and writes it into a Delta table for further processing.
# MAGIC
# MAGIC **Which code snippet will correctly ingest the raw JSON data and create a Delta table using DLT?**
# MAGIC
# MAGIC A.
# MAGIC python
# MAGIC import dlt
# MAGIC
# MAGIC @dlt.table
# MAGIC def raw_customers():
# MAGIC     return spark.read.format("csv").load("s3://my-bucket/raw-customers/")
# MAGIC
# MAGIC
# MAGIC B.
# MAGIC python
# MAGIC import dlt
# MAGIC
# MAGIC @dlt.view
# MAGIC def raw_customers():
# MAGIC     return spark.format.json("s3://my-bucket/raw-customers/")
# MAGIC
# MAGIC
# MAGIC C.
# MAGIC python
# MAGIC import dlt
# MAGIC
# MAGIC @dlt.table
# MAGIC def raw_customers():
# MAGIC     return spark.read.json("s3://my-bucket/raw-customers/")
# MAGIC
# MAGIC
# MAGIC D.
# MAGIC python
# MAGIC import dlt
# MAGIC
# MAGIC @dlt.table
# MAGIC def raw_customers():
# MAGIC     return spark.read.format("parquet").load("s3://my-bucket/raw-customers/")
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:35**
# MAGIC
# MAGIC A Python file is ready to go into production and the client wants to use the cheapest but most efficient type of cluster possible. The workload is quite small, only processing 10GBS of data with only simple joins and no complex aggregations or wide transformations.
# MAGIC
# MAGIC **Which cluster meets the requirement?**
# MAGIC
# MAGIC a. Interactive cluster  
# MAGIC b. Job cluster with spot instances enabled  
# MAGIC c. Job cluster with spot instances disabled  
# MAGIC d. Job cluster with Photon enabled

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #:36**
# MAGIC
# MAGIC A Databricks workflow fails at the last stage due to an error in a notebook. This workflow runs daily. The data engineer fixes the mistake and wants to rerun the pipeline. This workflow is very costly and time-intensive to run.
# MAGIC
# MAGIC **Which action should the data engineer do in order to minimise downtime and cost?**
# MAGIC
# MAGIC a. Re-run the entire workflow  
# MAGIC b. Repair run  
# MAGIC c. Restart the cluster  
# MAGIC d. Switch to another cluster

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #:37**
# MAGIC
# MAGIC A Databricks single-task workflow fails at the last task due to an error in a notebook. The data engineer fixes the mistake in the notebook.
# MAGIC
# MAGIC **What should the data engineer do to rerun the workflow?**
# MAGIC
# MAGIC a. Repair the task  
# MAGIC b. Rerun the pipeline  
# MAGIC c. Restart the cluster  
# MAGIC d. Switch the cluster

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:38**
# MAGIC
# MAGIC **What is the structure of an Asset Bundle?**
# MAGIC
# MAGIC a. A Docker image containing runtime environments and the source code of the assets  
# MAGIC b. A compressed archive (ZIP) that solely contains workspace assets without any accompanying metadata  
# MAGIC c. A single plain text file enumerating the names of assets to be migrated to a new workspace  
# MAGIC d. A YAML configuration file that specifies the artifacts, resources, and configurations for the project

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:39**
# MAGIC
# MAGIC A data engineer is maintaining an ETL pipeline code with a GitHub repository linked to their Databricks account. The data engineer wants to deploy the ETL pipeline to production as a Databricks workflow.
# MAGIC
# MAGIC **Which approach should the data engineer use?**
# MAGIC
# MAGIC A. Databricks Asset Bundles (DAB) + GitHub Integration  
# MAGIC B. Maintain workflow_config.json and deploy it using Databricks CLI  
# MAGIC C. Maintain workflow_config.json and deploy it using Terraform  
# MAGIC D. Manually create and manage the workflow in UI

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:40**
# MAGIC
# MAGIC A data engineer works for an organization that must meet a stringent Service Level Agreement (SLA) that demands minimal runtime errors and high availability for its data processing pipelines. The data engineer wants to avoid the operational overhead of managing and tuning clusters.
# MAGIC
# MAGIC **Which architectural solution will meet the requirements?**
# MAGIC
# MAGIC a. Use an auto-scaling cluster configured and monitored by the user.  
# MAGIC b. Implement a hybrid approach with scheduled batch jobs on custom cloud VMs.  
# MAGIC c. Deploy a dedicated, manually managed cluster optimized by in-house IT staff.  
# MAGIC d. Utilize Databricks serverless compute that automatically optimizes resources and abstracts cluster management.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:41**
# MAGIC
# MAGIC A data engineer wants to reduce costs and optimize cloud spending. The data engineer has decided to use Databricks Serverless for lowering cloud costs while maintaining existing SLAs.
# MAGIC
# MAGIC **What is the first step in migrating to Databricks Serverless?**
# MAGIC
# MAGIC A. Legacy Ingestion pipelines that include ingestion from sources API's, files, JDBC/ODBC connections  
# MAGIC B. A frequently running and efficient Python-based data transformation pipeline compatible with the latest Databricks runtime and Unity Catalog  
# MAGIC C. A frequently running and efficient Scala-based data transformation pipeline compatible with the latest Databricks runtime and Unity Catalog  
# MAGIC D. Low frequency BI Dashboarding and Adhoc SQL Analytics

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #:42**
# MAGIC
# MAGIC A data engineering project involves processing large batches of data on a daily schedule using ETL. The jobs are resource-intensive and vary in size, requiring a scalable, cost-efficient compute solution that can automatically scale based on the workload.
# MAGIC
# MAGIC **Which compute approach will satisfy the needs described?**
# MAGIC
# MAGIC a. Job Cluster  
# MAGIC b. Dedicated Cluster  
# MAGIC c. All-Purpose Cluster  
# MAGIC d. Databricks SQL Serverless

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #:43**
# MAGIC
# MAGIC A data engineer is maintaining a data pipeline. Upon data ingestion, the data engineer notices that the source data is starting to have a lower level of quality. The data engineer would like to automate the process of monitoring the quality level.
# MAGIC
# MAGIC **Which of the following tools can the data engineer use to solve this problem?**
# MAGIC
# MAGIC a. Auto Loader  
# MAGIC b. Unity Catalog  
# MAGIC c. Delta Lake  
# MAGIC d. Delta Live Tables

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:44**
# MAGIC
# MAGIC A company uses Delta Sharing to collaborate with partners across different cloud providers and geographic regions.
# MAGIC
# MAGIC **What will result in additional costs due to cross-region or egress fees?**
# MAGIC
# MAGIC a. Sharing data within the same cloud provider and region  
# MAGIC b. Transferring data via Delta Sharing across clouds and across different geographic regions  
# MAGIC c. Accessing Delta Sharing data using a VPN within the same data center  
# MAGIC d. Utilizing Delta Sharing for internal data analytics within a single cloud environment

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:45**
# MAGIC
# MAGIC An organization has data stored across multiple external systems, including MySQL, Amazon Redshift, and Google BigQuery. The data engineer wants to perform analytics without ingesting directly into Databricks, ensuring unified governance and minimizing data duplication.
# MAGIC
# MAGIC **Which feature of Databricks enables querying these external data sources while maintaining centralized governance?**
# MAGIC
# MAGIC a. Delta Lake  
# MAGIC b. Lakehouse Federation  
# MAGIC c. MLflow  
# MAGIC d. Databricks Connect

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:46**
# MAGIC
# MAGIC An organization needs to share a dataset stored in its Databricks Unity Catalog with an external partner who uses a different data platform that is not Databricks. The goal is to maintain data security and ensure the partner can access the data efficiently.
# MAGIC
# MAGIC **Which method should the data engineer use to securely share the dataset with the external partner?**
# MAGIC
# MAGIC a. Using Delta Sharing with the open sharing protocol  
# MAGIC b. Exporting data as CSV files and emailing them  
# MAGIC c. Using a third-party API to access the Delta table  
# MAGIC d. Databricks-to-Databricks Sharing

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #:47**
# MAGIC
# MAGIC A data engineer is reviewing the documentation on audit logs in Databricks for compliance purposes and needs to understand the format in which audit logs output events.
# MAGIC
# MAGIC **How are events formatted in Databricks audit logs?**
# MAGIC
# MAGIC a. In Databricks, audit logs output events in a JSON format.  
# MAGIC b. In Databricks, audit logs output events in a CSV format.  
# MAGIC c. In Databricks, audit logs output events in an XML format.  
# MAGIC d. In Databricks, audit logs output events in a plain text format.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #:48**
# MAGIC
# MAGIC A data engineer is managing a data pipeline in Databricks, where multiple Delta tables are used for various transformations. The team wants to track how data flows through the pipeline, including identifying dependencies between Delta tables, notebooks, jobs, and dashboards. The data engineer is utilizing the Unity Catalog lineage feature to monitor this process.
# MAGIC
# MAGIC **How does Unity Catalog's data lineage feature support the visualization of relationships between Delta tables, notebooks, jobs, and dashboards?**
# MAGIC
# MAGIC A. Unity Catalog lineage visualizes dependencies between Delta tables, notebooks, and jobs, but does not provide column-level tracing or relationships with dashboards.  
# MAGIC B. Unity Catalog lineage only supports visualizing relationships at the table level and does not extend to notebooks, jobs, or dashboards.  
# MAGIC C. Unity Catalog lineage provides an interactive graph that tracks dependencies between tables and notebooks but excludes any job-related dependencies or dashboard visualizations.  
# MAGIC D. Unity Catalog provides an interactive graph that visualizes the dependencies between Delta tables, notebooks, jobs, and dashboards, while also supporting column-level tracking of data transformations.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:49**
# MAGIC
# MAGIC A data engineer is configuring Unity Catalog in Databricks and needs to assign a role to a user who should have the ability to grant and revoke privileges on various data objects within a specific schema, but should not have read/write access over the schema or its objects.
# MAGIC
# MAGIC **Which role should the data engineer assign to this user?**
# MAGIC
# MAGIC A. Table Owner  
# MAGIC B. Catalog Owner  
# MAGIC C. Schema Owner  
# MAGIC D. USE catalog/schema privilege on the schema

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #:50**
# MAGIC
# MAGIC A company is collaborating with a partner that does not use Databricks but needs access to a large historical dataset stored in Delta format. The data engineer needs to ensure that the partner can access the data securely, without the need for them to set up an account, and with read-only access.
# MAGIC
# MAGIC **How should the data be shared?**
# MAGIC
# MAGIC A. Share the dataset by exporting it to a CSV file and manually transferring the file to the partner's system.  
# MAGIC B. Grant your partner access to your Databricks workspace and assign them full write permissions to the Delta table, enabling them to modify the dataset.  
# MAGIC C. Share the dataset using Unity Catalog, ensuring that both teams have full write access to the data within the same organization.  
# MAGIC D. Share the dataset using Delta Sharing, which allows your partner to access the data using a secure, read-only URL without requiring a Databricks account, ensuring that they cannot modify the data.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:51**
# MAGIC
# MAGIC A data engineer at a company that uses Databricks with Unity Catalog needs to share a collection of tables with an external partner who also uses a Databricks workspace enabled for Unity Catalog. The data engineer decides to use Delta Sharing to accomplish this.
# MAGIC
# MAGIC **What is the first piece of information the data engineer should request from the external partner to set up Delta Sharing?**
# MAGIC
# MAGIC A. The IP address of their Databricks workspace  
# MAGIC B. The name of their Databricks cluster  
# MAGIC C. The sharing identifier of their Unity Catalog metastore  
# MAGIC D. Their Databricks account password

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #:52**
# MAGIC
# MAGIC A data engineer needs to provide access to a group named manufacturing-team. The team needs privileges to create tables in the quality schema.
# MAGIC
# MAGIC **Which set of SQL commands will grant a group named manufacturing-team to create tables in a schema named production with the parent catalog named manufacturing with the least privileges?**
# MAGIC
# MAGIC A.  
# MAGIC GRANT CREATE TABLE ON SCHEMA manufacturing.quality To manufacturing-team;  
# MAGIC GRANT USE SCHEMA ON SCHEMA manufacturing.quality To manufacturing- team;  
# MAGIC GRANT USE CATALOG ON CATALOG manufacturing TO manufacturing-team;
# MAGIC
# MAGIC B.  
# MAGIC GRANT USE TABLE ON SCHEMA manufacturing.quality TO manufacturing-team;  
# MAGIC GRANT USE SCHEMA ON SCHEMA manufacturing.quality TO manufacturing-team;  
# MAGIC GRANT USE CATALOG ON CATALOG manufacturing TO manufacturing-team;
# MAGIC
# MAGIC C.  
# MAGIC GRANT CREATE TABLE ON SCHEMA manufacturing.quality TO manufacturing-team;  
# MAGIC GRANT CREATE SCHEMA ON SCHEMA manufacturing.quality TO manufacturing-team;  
# MAGIC GRANT CREATE CATALOG ON CATALOG manufacturing TO manufacturing-team;
# MAGIC
# MAGIC D.  
# MAGIC GRANT CREATE TABLE ON SCHEMA manufacturing.quality TO manufacturing-team;  
# MAGIC GRANT CREATE SCHEMA ON SCHEMA manufacturing.quality TO manufacturing-team;  
# MAGIC GRANT USE CATALOG ON CATALOG manufacturing TO manufacturing-team;

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:53**
# MAGIC
# MAGIC A data engineer is configuring Delta Sharing for a multi-team project where teams from different departments will need to access shared data. The data engineer has successfully created a Unity Catalog metastore and is now setting up the Delta Share. The goal is to ensure that internal teams can access the shared data with full permissions, while external partners can only read the data. 
# MAGIC
# MAGIC **Which action should the Data Engineer take to configure the sharing correctly?**
# MAGIC
# MAGIC a. Create a Delta Share, set up a secure access URL for internal teams and external partners, and distribute the URL to provide them access to the shared data.  
# MAGIC b. Create a Delta Share, add the internal team's tables and views, and assign READ/WRITE permissions to both external partners and internal teams.  
# MAGIC c. Assign READ permissions to external partners through the Delta Share and READ/WRITE permissions to internal teams, and ensure the correct tables and views are shared.  
# MAGIC d. Grant READ permissions to external partners and READ/WRITE permissions to internal teams through the Delta Share.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:54**
# MAGIC
# MAGIC A data engineer manages multiple external tables linked to various data sources. The data engineer wants to manage these external tables efficiently and ensure that only the necessary permissions are granted to users for accessing specific external tables.
# MAGIC
# MAGIC **How should the data engineer manage access to these external tables?**
# MAGIC
# MAGIC A. Set up Azure Blob Storage permissions at the container level, allowing access to all external tables.  
# MAGIC B. Create a single user role with full access to all external tables and assign it to all users.  
# MAGIC C. Grant permissions on the Databricks workspace level, which will automatically apply to all external tables.  
# MAGIC D. Use Unity Catalog to manage access controls and permissions for each external table individually.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:55**
# MAGIC
# MAGIC An organization plans to share a large dataset stored in a Databricks workspace on AWS with a partner organization whose Databricks workspace is hosted on Azure. The data engineer wants to minimize data transfer costs while ensuring secure and efficient data sharing.
# MAGIC
# MAGIC **Which strategy will reduce data egress costs associated with cross-cloud data sharing?**
# MAGIC
# MAGIC A. Migrating the dataset to Cloudflare R2 object storage before sharing  
# MAGIC B. Configure VPN connection between AWS and Azure for faster data sharing  
# MAGIC C. Using Delta Sharing without any additional configurations  
# MAGIC D. Sharing data via pre-signed URLS without monitoring egress costs

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:56**
# MAGIC
# MAGIC A data engineer is setting up access control in Unity Catalog and needs to ensure that a group of data analysts can query tables but not modify data. 
# MAGIC
# MAGIC **Which permission should the data engineer grant to the data analysts?**
# MAGIC
# MAGIC A. ALL PRIVILEGES  
# MAGIC B. MODIFY  
# MAGIC C. SELECT  
# MAGIC D. INSERT

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:57**
# MAGIC
# MAGIC What Databricks feature can be used to check the data sources and tables used in a workspace?
# MAGIC
# MAGIC A. Use the lineage feature to visualize a graph that highlights where the table is used only in reports.  
# MAGIC B. Use the lineage feature to visualize a graph that highlights where the table is used only in notebooks.  
# MAGIC C. Use the lineage feature to visualize a graph that shows all dependencies, including where the table is used in notebooks, other tables, and reports.  
# MAGIC D. Do not use the lineage feature as it only tracks activity from the last 3 months and will not provide full details on dependencies.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:58**
# MAGIC
# MAGIC A data engineer is getting a partner organization up to speed with Databricks account. Both the teams share some business use cases. The data engineer has to share some of your Unity-Catalog managed delta tables and the notebook jobs creating those tables with the partner organization.
# MAGIC
# MAGIC **How can the data engineer seamlessly share the required information?**
# MAGIC
# MAGIC A. Zip all the code and share via email and allow data ingestion from your data lake  
# MAGIC B. Share required datasets and notebooks via Delta Sharing. Manage permissions via Unity Catalog.  
# MAGIC C. Data and Notebooks can be shared simply using Unity Catalog.  
# MAGIC D. Share access to codebase via Github and allow them to ingest datasets from your Datalake.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:59**
# MAGIC
# MAGIC **An organization needs an optimized storage layer that supports ACID transactions and schema enforcement.**
# MAGIC
# MAGIC **Which technology should the organization use?**
# MAGIC
# MAGIC A. Delta Lake  
# MAGIC B. Unity Catalog  
# MAGIC C. Cloud File Storage  
# MAGIC D. Data lake

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:60**
# MAGIC
# MAGIC **A data engineer is attempting to write Python and SQL in the same command cell and is running into an error. The engineer believed it was possible to use a Python variable in a SQL select statement.**
# MAGIC
# MAGIC **Why does the command fail?**
# MAGIC
# MAGIC A. Databricks supports language interoperability in the same cell but only between Scala and SQL.  
# MAGIC B. Databricks supports multiple languages but only one per notebook.  
# MAGIC C. Databricks supports one language per cell.  
# MAGIC D. Databricks supports language interoperability but only if a special character is used.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:61**
# MAGIC
# MAGIC **Which compute option should be chosen in a scenario where small-scale ad-hoc Python scripts need to be run at high frequency and should wind down quickly after these queries have finished running?**
# MAGIC
# MAGIC A. All-purpose Cluster  
# MAGIC B. Job Cluster  
# MAGIC C. Serverless Compute  
# MAGIC D. SQL Warehouse

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:62**
# MAGIC
# MAGIC **A data engineer is working on a personal laptop and needs to perform complex transformations on data stored in a Delta Lake on cloud storage. The engineer decides to use Databricks Connect to interact with Databricks clusters and work in their local IDE.**
# MAGIC
# MAGIC **How does Databricks Connect enable the engineer to develop, test, and debug code seamlessly on their personal laptop while interacting with Databricks clusters?**
# MAGIC
# MAGIC A. By providing a local environment that mimics the Databricks runtime, enabling the engineer to develop, test, and debug code using a specific IDE that is required by Databricks  
# MAGIC B. By providing a local environment that mimics the Databricks runtime, enabling the engineer to develop, test, and debug code only through Databricks' own web interface  
# MAGIC C. By allowing direct execution of Spark jobs from the local machine without needing a network connection  
# MAGIC D. By providing a local environment that mimics the Databricks runtime, enabling the engineer to develop, test, and debug code using their preferred IDE

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:63**
# MAGIC
# MAGIC **What is the maximum output supported by a job cluster to ensure a notebook does not fail?**
# MAGIC
# MAGIC A. 25MBs  
# MAGIC B. 10MBs  
# MAGIC C. 30MBS  
# MAGIC D. 15MBs

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:64**
# MAGIC
# MAGIC **A data engineer needs to conduct Exploratory Analysis on data residing in a database that is within the company's custom-defined network in the cloud. The data engineer is using SQL for this task.**
# MAGIC
# MAGIC **Which type of SQL Warehouse will enable the data engineer to process large numbers of queries quickly and cost-effectively?**
# MAGIC
# MAGIC A. Serverless compute for notebooks  
# MAGIC B. Pro SQL Warehouse  
# MAGIC C. Classic SQL Warehouse  
# MAGIC D. Serverless SQL Warehouse

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:65**
# MAGIC
# MAGIC **A data engineer is debugging a Python notebook in Databricks that processes a dataset using PySpark. The notebook fails with an error during a DataFrame transformation. The engineer wants to inspect the state of variables, such as the input DataFrame and intermediate results, to identify where the error occurs.**
# MAGIC
# MAGIC **Which tool should the engineer use to debug the notebook and inspect the values of variables like DataFrames?**
# MAGIC
# MAGIC A. Use the Databricks CLI to download and analyze driver logs for detailed error messages  
# MAGIC B. Use the Python Notebook Interactive Debugger to set breakpoints and inspect variable values in real-time  
# MAGIC C. Use the Ganglia UI to monitor cluster resource usage and identify hardware issues  
# MAGIC D. Use the Spark Ul to analyze the execution plan and identify stages where the job failed

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:66**
# MAGIC
# MAGIC **A data engineer wants to create an external table in Databricks that references data stored in an Azure Data Lake Storage (ADLS) location. The goal is to enable Databricks to access and query this external data without moving it into the Databricks-managed storage.**
# MAGIC
# MAGIC **Which step should the data engineer take to successfully create the external table?**
# MAGIC
# MAGIC A. Use the CREATE MANAGED TABLE statement and specify the LOCATION clause with the path to the external data.  
# MAGIC B. CREATE UNMANAGED TABLE statement without specifying a LOCATION clause.  
# MAGIC C. Use the CREATE TABLE statement and specify the LOCATION clause with the path to the external data.  
# MAGIC D. CREATE EXTERNAL TABLE statement without specifying a LOCATION clause.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:67**
# MAGIC
# MAGIC **A data engineer is developing a small proof of concept in a notebook. When running the entire notebook, the Cluster usage spikes. The data engineer wants to keep the development requirements and get real-time results.**
# MAGIC
# MAGIC **Which Cluster meets these requirements?**
# MAGIC
# MAGIC A. All Purpose Cluster with autoscaling  
# MAGIC B. Job Cluster with Photon enabled and autoscaling  
# MAGIC C. Job Cluster with autoscaling enabled  
# MAGIC D. All-Purpose Cluster with a large fixed memory size

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:68**
# MAGIC
# MAGIC **A data engineer needs to process SQL queries on a large dataset with fluctuating workloads. The workload requires automatic scaling based on the volume of queries, without the need to manage or provision infrastructure. The solution should be cost-efficient and charge only for the compute resources used during query execution.**
# MAGIC
# MAGIC **Which compute option should the data engineer use?**
# MAGIC
# MAGIC A. Databricks SQL Analytics  
# MAGIC B. Databricks Runtime for ML  
# MAGIC C. Databricks Jobs  
# MAGIC D. Serverless SQL Warehouse  

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:69**
# MAGIC
# MAGIC **An organization has implemented a data pipeline in Databricks and needs to ensure it can scale automatically based on varying workloads without manual cluster management. The goal is to meet the company's Service Level Agreements (SLAs), which require high availability and minimal downtime, while Databricks automatically handles resource allocation and optimization.**
# MAGIC
# MAGIC **Which approach fulfills these requirements?**
# MAGIC
# MAGIC A. Deploy Job Clusters with fixed configurations, dedicated to specific tasks, without automatic scaling.  
# MAGIC B. Use Spot Instances to allocate resources dynamically while minimizing costs, with potential interruptions.  
# MAGIC C. Use Interactive Clusters in Databricks, adjusting cluster sizes manually based on workload demands.  
# MAGIC D. Use Serverless compute in Databricks to automatically scale and provision resources with minimal manual intervention.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:70**
# MAGIC
# MAGIC **A data engineer has written a function in a Databricks Notebook to calculate the population of bacteria in a given medium.**
# MAGIC
# MAGIC ```python
# MAGIC  def calculate_population_of_bacteria (intital population, exponential_factor) return future_population = intitial_population ** expontential_factor
# MAGIC ```
# MAGIC
# MAGIC **Analysts use this function in the notebook and sometimes provide input arguments of the wrong data type, which can cause errors during execution.** 
# MAGIC
# MAGIC **Which Databricks feature will help the data engineer quickly identify if an incorrect data type has been provided as input?**
# MAGIC
# MAGIC A. The Spark User interface has a Debug tab that contains the variables used in this session.  
# MAGIC B. The Databricks debugger enables breakpoints that will raise an error if the wrong data type is submitted.  
# MAGIC C. The Databricks debugger enables the use of a variable explorer to see at a glance the value of the variables.  
# MAGIC D. The Data Engineer should add print statements to determine the value of the variable.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question #:71**
# MAGIC
# MAGIC **Which languages are supported by Serverless compute clusters? (Choose two.)**
# MAGIC
# MAGIC A. SQL<br> 
# MAGIC B. Python<br>
# MAGIC C. R<br>
# MAGIC D. Scala<br>
# MAGIC E. Java

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:72**
# MAGIC
# MAGIC **A Data Engineer is designing Bronze layer in Databricks Medallion Architecture. The raw data is collected from multiple sources (Clickstream in JSON, Transactions in CSV). The task is to design the Bronze layer of the Medallion Architecture to ingest and store this raw data for further processing.**
# MAGIC
# MAGIC **Which operation applies to the Bronze layer?**
# MAGIC
# MAGIC A. Ingest raw data without transformations, preserving original schemas, and store in Delta format.  
# MAGIC B. Clean and standardize raw data by removing null values and enforcing schemas.  
# MAGIC C. Apply complex business logic to enrich raw data with customer segmentation labels.  
# MAGIC D. Aggregate and transform source data to calculate daily sales performance metrics.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:73**
# MAGIC
# MAGIC **What is the primary function of the Silver layer in the Databricks medallion architecture?**
# MAGIC
# MAGIC A. Store historical data solely for auditing purposes  
# MAGIC B. Aggregate and enrich data for business analytics  
# MAGIC C. Validate, clean, and deduplicate data for further processing  
# MAGIC D. Ingest raw data in its original state

# COMMAND ----------

# MAGIC %md
# MAGIC **Question#: 74**
# MAGIC
# MAGIC **What is the primary function of the Silver layer in the Databricks medallion architecture?**
# MAGIC
# MAGIC A. Store historical data solely for auditing purposes  
# MAGIC B. Aggregate and enrich data for business analytics  
# MAGIC C. Validate, clean, and deduplicate data for further processing  
# MAGIC D. Ingest raw data in its original state

# COMMAND ----------

# MAGIC %md
# MAGIC **Question#: 75**
# MAGIC
# MAGIC **A data engineer needs to combine sales data from an on-premises PostgreSQL database with customer data in Azure Synapse for a comprehensive report. The goal is to avoid data duplication and ensure up-to-date information.**
# MAGIC
# MAGIC **How should the data engineer achieve this using Databricks?**
# MAGIC
# MAGIC A. Export data from both sources to CSV files and upload them to Databricks  
# MAGIC B. Use Lakehouse Federation to query both data sources directly  
# MAGIC C. Manually synchronize data from both sources into a single database  
# MAGIC D. Develop custom ETL pipelines to ingest data into

# COMMAND ----------

# MAGIC %md
# MAGIC **Question#: 76**
# MAGIC
# MAGIC **A data engineering team wants to validate a new ingestion pipeline locally while ensuring large aggregations run in serverless compute in their Databricks workspace. They plan to use Databricks Connect and have the option to attach to either a shared cluster or serverless.**
# MAGIC
# MAGIC **Which workspace requirement should be confirmed first to avoid connection failures?**
# MAGIC
# MAGIC A. Verify that the workspace has Unity Catalog disabled and the Databricks Connect version is less than the serverless Runtime version.<br>
# MAGIC B. Verify that the workspace has Unity Catalog enabled and that the Databricks Connect version supports serverless for the target Runtime release.<br>
# MAGIC C. Verify that only assigned access mode clusters are used because serverless is not supported by Databricks Connect.<br>
# MAGIC D. Verify that the local Spark version equals the serverless Spark version to satisfy Spark Connect parity.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question#: 77**
# MAGIC
# MAGIC **A data engineer needs to conduct Exploratory Analysis on data residing in a database that is within the company's custom-defined network in the cloud. The data engineer is using SQL for this task.**
# MAGIC
# MAGIC **Which type of SQL Warehouse will enable the data engineer to process large numbers of queries quickly and cost-effectively?**
# MAGIC
# MAGIC A. Classic SQL Warehouse  
# MAGIC B. Serverless SQL Warehouse  
# MAGIC C. Pro SQL Warehouse  
# MAGIC D. All-purpose compute cluster

# COMMAND ----------

# MAGIC %md
# MAGIC **Question#: 78**
# MAGIC
# MAGIC **A data engineer must deliver a trustworthy customer 360 dataset in Databricks for data scientists and BI teams. The engineer plans to join deduplicated customer records with cleaned transaction data, enforce schema and data quality checks, and create a conformed "customer_transactions" view. Later, highly aggregated, domain-specific tables (for weekly spend and executive summaries) will be produced for dashboards.**
# MAGIC
# MAGIC **Where should the engineer build the conformed "customer_transactions" dataset, and where should the aggregated, report-ready tables reside?**
# MAGIC
# MAGIC A. Build both "customer_transactions" and aggregated, report-ready tables in Silver to keep the model simpler.  
# MAGIC B. Build "customer_transactions" in Bronze and put the aggregated, report-ready tables in Silver.  
# MAGIC C. Build "customer_transactions" in Gold and put the aggregated, report-ready tables in Silver.  
# MAGIC D. Build "customer_transactions" in Silver and put the aggregated, report-ready tables in Gold

# COMMAND ----------

# MAGIC %md
# MAGIC **Question#: 79**
# MAGIC
# MAGIC **A data engineer requires rapid iteration on pipelines while maintaining reliable rollbacks after bad ingests, ensuring audit trails for regulatory compliance, and providing consistent access to a single source of truth for both AI and BI workloads.**
# MAGIC
# MAGIC **Which strategy should the data engineer apply to meet the needs?**
# MAGIC
# MAGIC A. Delta Lake ACID transactions and time travel, governed by Unity Catalog for consistent access and lineage.  
# MAGIC B. DBFS CSV storage with manual file versioning and nightly copies for rollback.  
# MAGIC C. Ephemeral in-memory DataFrames for audit trails and BI distribution.  
# MAGIC D. Cloud objects storage only, with ad hoc SQL queries for recovery and governance.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:80**
# MAGIC
# MAGIC A data engineer is setting up a new Databricks pipeline that ingests clickstream events from Kafka and daily product catalogs from cloud object storage. To ensure auditability and easy reprocessing, the engineer wants to land all source data. Later stages will handle cleaning, deduplication, and business modeling before the data is used in dashboards.
# MAGIC
# MAGIC **Which approach aligns to Medallion Architecture principles?**
# MAGIC
# MAGIC A. Land both sources in Gold with denormalized star schemas to optimize BI while retaining full source fidelity.  
# MAGIC B. Land streaming events from Kafka in silver, and the product catalog directly in Gold to minimize layers for batch data.  
# MAGIC C. Land both sources in the Bronze layer append-only with minimal validation, then build Silver/Gold downstream for quality and analytics.  
# MAGIC D. Land both sources directly into the Silver layer with schema enforcement and deduplication to reduce downstream complexity.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:81**
# MAGIC
# MAGIC A data engineer is building a PySpark ingestion pipeline in a local IDE and must execute heavy DataFrame transformations on a remote Databricks cluster for scale while stepping through business logic locally. The workspace uses Unity Catalog and a cluster running Databricks Runtime 15.4 LTS. The engineer also plans to register UDFs.
# MAGIC
# MAGIC **What should the data engineer do to avoid runtime issues during development with Databricks Connect?**
# MAGIC
# MAGIC A. Match the local Python minor version to the cluster's Python minor version when using UDF's, and use a Databricks Connect package compatible with the cluster's Runtime version  
# MAGIC B. Use any local Python version as long as the PySpark minor version matches, because the cluster's Python version is isolated from the client.  
# MAGIC C. Use serverless, because Databricks Connect does not support assigned or shared clusters.  
# MAGIC D. Disable Unity Catalog on the workspace because it conflicts with remote execution through Databricks Connect.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:82**
# MAGIC
# MAGIC A data engineer working in Databricks needs to control BI query latency and cost for a sales analytics domain. Silver tables already contain validated, normalized sales and product data. The team wants dashboard-friendly query performance and to align datasets with business concepts (e.g., weekly sales and account_performance) without overloading analysts with complex joins.
# MAGIC
# MAGIC **Which design approach should a data engineer choose for the Gold layer in a medallion architecture?**
# MAGIC
# MAGIC A. Move raw, append-only source data directly into Gold to avoid transformation costs and enable time travel.  
# MAGIC B. Create denormalized, domain-aligned tables and materialized aggregates (e.g., weekly_sales) optimized for reporting and dashboards.  
# MAGIC C. Build only lightly cleansed views in Gold and preserve most business logic in Silver to reduce duplication.  
# MAGIC D. Keep all data heavily normalized in Gold to minimize storage and rely on BI tools to join data at query time.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:83**
# MAGIC
# MAGIC A developer has configured Databricks Connect and starts running PySpark code locally. They notice that Data Frame operations are executed on the remote cluster, but actions like .show() return results directly in their local console.
# MAGIC
# MAGIC **What does this behaviour illustrate about how Databricks Connect is used?**
# MAGIC
# MAGIC A. It requires manual synchronization of results from the cluster  
# MAGIC B. It runs all Spark compute locally and only reads remote files  
# MAGIC C. It proxies Spark commands from the local client to the remote cluster  
# MAGIC D. It mirrors the entire cluster environment on the developer's machine

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:84**
# MAGIC
# MAGIC A data engineer must support self-serve BI dashboards for hundreds of business users who run ad hoc, high-concurrency SQL queries throughout the day against governed Unity Catalog tables. The team needs a near-instant start, autoscaling without manual tuning, and the best performance for SQL while minimizing operational overhead.
# MAGIC
# MAGIC **Which Databricks compute should the data engineer use?**
# MAGIC
# MAGIC A. SQL Warehouse (Classic) with a fixed cluster size.  
# MAGIC B. Jobs compute clusters triggered by dashboards on a schedule.  
# MAGIC C. All-purpose classic cluster with manual autoscaling enabled.  
# MAGIC D. SQL Warehouse (Serverless) with Photon enabled.

# COMMAND ----------

# MAGIC %md
# MAGIC Question#: 85
# MAGIC
# MAGIC A data engineer needs to compute metrics such as:
# MAGIC - rolling 7-day sales
# MAGIC - percent of total revenue
# MAGIC - top-N most profitable categories
# MAGIC
# MAGIC Which two approaches are appropriate for implementing these metrics with PySpark DataFrames? (Choose two.)
# MAGIC
# MAGIC A. Using RDD aggregations for better performance.  
# MAGIC B. Using mapPartitions to manually implement rolling windows.  
# MAGIC C. Using window functions for rolling and ranking calculations.  
# MAGIC D. Collecting the DataFrame to the driver for faster iterative processing.  
# MAGIC E. Using joins and groupBy to compute percent-of-total metrics.

# COMMAND ----------

# MAGIC %md
# MAGIC Question#: 86
# MAGIC
# MAGIC A data engineering team is analyzing customer transactions using a PySpark DataFrame named transactions with columns customer_id, amount, and category. The team needs to compute, for each customer, the total transaction amount, the average transaction amount, and the maximum amount - all in a single operation for efficiency. Which code fragment should be used to achieve this in PySpark?
# MAGIC
# MAGIC A.  
# MAGIC transactions.groupBy ("customer_id")  
# MAGIC .aqg (sum("amount"), avg("amount"), max ("amount")))  
# MAGIC
# MAGIC B.  
# MAGIC transactions.groupBy ("customer id")  
# MAGIC .select(sum("amount"), avg("amount"), max("amount"))  
# MAGIC
# MAGIC C.  
# MAGIC transactions.agq (groupBy ("customer_id"), sum ("amount"),  
# MAGIC avg("amount"),  
# MAGIC max ("amount"))  
# MAGIC
# MAGIC D.  
# MAGIC transactions.groupBy ("customer_id") .sum ("amount")  
# MAGIC .avq("amount") .max ("amount")

# COMMAND ----------

# MAGIC %md
# MAGIC **Question#: 87**
# MAGIC
# MAGIC When using MERGE INTO in Delta Lake on Databricks, which clause allows you to atomically delete target rows that no longer match any source rows?
# MAGIC
# MAGIC A. WHEN MATCHED BY SOURCE THEN UPDATE SET NULL  
# MAGIC B. WHEN MATCHED AND THEN DELETE  
# MAGIC C. WHEN NOT MATCHED BY SOURCE THEN DELETE  
# MAGIC D. WHEN NOT MATCHED THEN DELETE

# COMMAND ----------

# MAGIC %md
# MAGIC Question#: 88
# MAGIC
# MAGIC A team is using a Databricks workspace and needs to continuously ingest JSON files as they arrive.
# MAGIC
# MAGIC Which code snippet shows a valid Auto Loader source configuration?
# MAGIC
# MAGIC A.  
# MAGIC spark.readStream.format("json")  
# MAGIC .option ("cloudFiles.format", "json")  
# MAGIC .load("<path>")  
# MAGIC
# MAGIC B.  
# MAGIC spark.readstream. format ("cloudFiles")  
# MAGIC .option("cloudFiles.format", "json")  
# MAGIC .load("jdbc:sqlserver://;database=")  
# MAGIC
# MAGIC C.  
# MAGIC spark.readStream. format ("cloudFiles")  
# MAGIC .option ("format", "json")  
# MAGIC .load("<path>")  
# MAGIC
# MAGIC D.  
# MAGIC spark.readStream.format("cloudFiles")  
# MAGIC .option ("cloudFiles.format", "json")  
# MAGIC .load("<path>")

# COMMAND ----------

# MAGIC %md
# MAGIC **Question#: 89**
# MAGIC
# MAGIC A Databricks single-task workflow fails due to an error in a notebook. The data engineer fixes the mistake in the notebook. What should the data engineer do to rerun the workflow?
# MAGIC
# MAGIC A. Repair the task  
# MAGIC B. Repair the run  
# MAGIC C. Restart the Cluster  
# MAGIC D. Swap the cluster

# COMMAND ----------

# MAGIC %md
# MAGIC Question#: 90
# MAGIC
# MAGIC A Python file is ready for production and the client wants to use the most efficient yet cost-effective type of cluster possible. The workload is quite small, only processing 10GBs of data with only simple joins and no complex aggregations or wide transformations.
# MAGIC
# MAGIC Which cluster meets the requirement?
# MAGIC
# MAGIC A. Job cluster with spot instances enabled  
# MAGIC B. Job cluster with Photon enabled  
# MAGIC C. Job cluster with spot instances disabled  
# MAGIC D. Interactive cluster

# COMMAND ----------

# MAGIC %md
# MAGIC **Question#: 91**
# MAGIC
# MAGIC A data engineer is migrating pipeline tasks to reduce operational toil. The workspace used Unity Catalog and is in a region that supports serverless. The engineer wants Databricks to auto-select instance types, manage scaling, apply Photon, and handle runtime upgrades automatically for job runs.
# MAGIC
# MAGIC **How should the data engineer meet this requirement while adhering to Databricks constraints?**
# MAGIC
# MAGIC A. Run the job on a serverless compute for workflows configuration, ensuring Unity Catalog is enabled and regional support is available.  
# MAGIC B. Use a Pro SQL warehouse and schedule Python notebook tasks to execute as pipeline steps.  
# MAGIC C. Create a job with a single-task job cluster and manually set instance families and min/max workers.  
# MAGIC D. Use an all-purpose cluster with cluster policies to enforce standard sizes and enable autoscaling.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question#: 92**
# MAGIC
# MAGIC A data engineer is standardizing repository layouts for multiple teams adopting Databricks Asset Bundles. The engineer wants to ensure every project has a single authoritative configuration file at the repository root that defines the bundle name, targets, workspace settings, permissions, and resource mappings (for jobs and pipelines).
# MAGIC
# MAGIC What strategy should the data engineer use to meet the goal?
# MAGIC
# MAGIC A. Place multiple databricks.yml files under each subfolder (for example, jobs/pipelines/, workspace/) and merge them at deploy time using the include mapping.  
# MAGIC B. Place exactly one databricks.yml at the repository root; it is the main configuration file and may reference additional configuration files via the include mapping.  
# MAGIC C. Place a databricks.yml in a databricks/hidden folder at the repository root; only hidden locations are valid for bundle configs.  
# MAGIC D. Place a databricks.yaml at the repository root and optional databricks.yml in subfolders; the CLI prefers .yaml over.yml when both exist.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question#: 93**
# MAGIC
# MAGIC A team is designing their Databricks Asset Bundle for deployment. They want to ensure their bundle includes all necessary resources, targeted environment configurations, and deployment settings in a single version-controlled file.
# MAGIC
# MAGIC **What is required as the main configuration file at the root of their project?**
# MAGIC
# MAGIC A. A Python script called configure_bundle.py that dynamically creates resources at runtime  
# MAGIC B. A databricks.yml YAML file that contains the bundle's name, targets, includes resources, and variables  
# MAGIC C. A directory with multiple TXT files, each describing a single resource for the bundle  
# MAGIC D. A JSON file named bundle_config.json that stores all resource details and environment variables

# COMMAND ----------

# MAGIC %md
# MAGIC **Question#: 94**
# MAGIC
# MAGIC After a failed multi-task job run, a data engineer changes the cluster size and updates a notebook path for one task. The data engineer wants to re-run just the failed/skipped tasks with the updated settings and keep the run lineage intact.
# MAGIC
# MAGIC **Which strategy should the data engineer use to preserve the run history?**
# MAGIC
# MAGIC A. Use Jobs REST API repairRun to re-run failed tasks; the repair uses the current job and task settings and appears in the run history.  
# MAGIC B. Increase the task retry count and click 'Retry' on the failed task to automatically apply new cluster settings within the same run.  
# MAGIC C. Export the job as a Databricks Asset Bundle, redeploy it, and re-run only the modified tasks from the bundle.  
# MAGIC D. Use 'Run now' to start a new run, so that the updated settings apply; the new run replaces the prior run history.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question#: 95**
# MAGIC
# MAGIC A Lakeflow Jobs workflow fails at the last task because of an error in a notebook task. This workflow is scheduled to run daily. The data engineer fixes the notebook and wants to rerun the pipeline. This workflow is very compute-intensive and expensive to run.
# MAGIC
# MAGIC **Which action should the data engineer take in order to minimize downtime and compute cost?**
# MAGIC
# MAGIC A. Restart the cluster  
# MAGIC B. Re-run the entire workflow  
# MAGIC C. Switch to another cluster  
# MAGIC D. Repair run

# COMMAND ----------

# MAGIC %md
# MAGIC **Question#: 96**
# MAGIC
# MAGIC A data engineer is investigating a Lakehouse ETL job on Databricks that has suddenly become four times slower.
# MAGIC
# MAGIC They need to:
# MAGIC - Identify the specific Spark stages that regressed.
# MAGIC - Drill down to per-task metrics such as shuffle read/write size, spill, and GC time.
# MAGIC - Correlate these with the executor resource usage during that run.
# MAGIC
# MAGIC Which Databricks-native capability is the starting point for this detailed job-level root-cause analysis?
# MAGIC
# MAGIC A. Cluster Metrics (Metrics tab on the compute) to view historical Spark and hardware metrics, without using the Spark UI.  
# MAGIC B. The Jobs run details page timeline and graph views, without opening the Spark Ul, to analyze all stage and task-level Spark metrics.  
# MAGIC C. Ganglia metrics for the cluster, which provide full visibility into Spark stages, tasks, and shuffle metrics for the job run.  
# MAGIC D. Spark UI opened from the job run's compute, using the Jobs and Stages tabs to inspect task metrics.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question#: 97**
# MAGIC
# MAGIC A data engineer is troubleshooting a Lakeflow Spark Declarative Pipelines (SDP) where several rows are dropped by expectations. The product owner requests details on which expectation failed most frequently during the last run and the corresponding affected table. The engineer wants to use Databricks' built-in observability data to answer this without adding new logging code.
# MAGIC
# MAGIC **How should the data engineer troubleshoot SDP to verify the expectation failure?**
# MAGIC
# MAGIC A. Export notebook run results to HTML and search for the expectations summary in the rendered output to compile the metrics.  
# MAGIC B. Query the Lakeflow Spark Declarative Pipelines event log to retrieve expectation metrics and failure details for the pipeline's most recent update.  
# MAGIC C. Use the Spark UI's SQL tab to identify failed rows and expectation names from physical query plans.  
# MAGIC D. Increase the cluster's log level to DEBUG and parse the driver's Log4j logs for expectation metrics for the last run.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question#: 98**
# MAGIC
# MAGIC A data engineer wants to delegate day-to-day permission management for the schema `main.marketing` to the `mkt-admins` group, without making them workspace admins. They should be able to grant and revoke privileges for other users on objects within that schema.
# MAGIC
# MAGIC **Which approach aligns with UC's ownership and privilege model?**
# MAGIC
# MAGIC A. Grant MANAGE permissions on the metastore to mkt-admins, which allows managing privileges for all schemas and tables globally.  
# MAGIC B. Make mkt-admins a workspace-level admins group, then SELECT on main.marketing to allow privilege delegation.  
# MAGIC C. Transfer ownership of the schema main.marketing to mkt-admins; owners can manage privileges on the schema and its contained objects.  
# MAGIC D. Grant USE SCHEMA on main.marketing and MODIFY on all tables to mkt-admins, which enables managing grants within the schema.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Question#: 99**
# MAGIC
# MAGIC A data engineer is decommissioning a sandbox schema in Unity Catalog. Some tables are ephemeral staging outputs that can be safety removed entirely, but a few tables point at shared cloud storage used by downstream jobs outside Databricks. The engineer must avoid deleting any shared files when cleaning up catalog objects.
# MAGIC
# MAGIC **How does Unity Catalog behave when dropping Managed vs External tables?**
# MAGIC
# MAGIC A. DROP all tables; Databricks will only remove metadata for both managed and external tables.  
# MAGIC B. DROP managed tables that are ephemeral and DROP external tables; files for both remain for 7 days.  
# MAGIC C. DROP managed staging tables to remove data and metadata, and DROP external tables to remove only metadata  
# MAGIC D. DROP external tables first to delete their files, then DROP managed tables to keep their files for recovery.

# COMMAND ----------

# MAGIC %md
# MAGIC    
# MAGIC **Question#: 100**
# MAGIC
# MAGIC **A data engineer is onboarding a new bronze ingestion pipeline in Databricks with Unity Catalog. The team wants Databricks to handle storage layout, apply platform optimizations over time, and simplify lifecycle management so that when a table is dropped, its underlying data is also cleaned up according to Databricks-managed retention policies.** 
# MAGIC
# MAGIC **Which table type should the data engineer create for these ingestion tables?**
# MAGIC
# MAGIC A. Managed tables so that Unity Catalog manages both metadata and underlying data lifecycle.  
# MAGIC B. External tables with a LOCATION pointing to an external volume for full control of file layout.  
# MAGIC C. Foreign tables federated from an external catalog to delegate optimization to the source system.  
# MAGIC D. Temporary views over files to avoid table-level governance and lifecycle coupling.

# COMMAND ----------

# MAGIC %md
# MAGIC **Question#: 101**
# MAGIC
# MAGIC **A data engineer needs to configure an external location and a storage credential so that a new bronze ingestion pipeline can land data in cloud storage governed by Unity Catalog. The engineer has CREATE TABLE permission on schemas but receives a permission error when attempting to create the external location.**
# MAGIC
# MAGIC **Which role is required to unblock this setup, the principle of least privilege?**
# MAGIC
# MAGIC A. Grant CREATE EXTERNAL LOCATION on both the metastore and the referenced storage credential so the engineer can define the external location.  
# MAGIC B. Grant ALL PRIVILEGES on the catalog so the engineer can create external locations under its schemas.  
# MAGIC C. Promote the engineer to Workspace Admin so they can manage objects and jobs.  
# MAGIC D. Assign the engineer as Metastore Admin because only Metastore Admins can create external locations.

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
