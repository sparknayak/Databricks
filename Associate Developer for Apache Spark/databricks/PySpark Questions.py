# Databricks notebook source
# MAGIC %md
# MAGIC # PySpark Questions
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:1<br>
# MAGIC **Which of the following describes the Spark driver?** <br>
# MAGIC A. The Spark driver is responsible for performing all execution in all execution modes – it is the
# MAGIC entire Spark application.<br>
# MAGIC B. The Spare driver is fault tolerant – if it fails, it will recover the entire Spark application.<br>
# MAGIC C. The Spark driver is the coarsest level of the Spark execution hierarchy – it is synonymous
# MAGIC with the Spark application.<br>
# MAGIC D. The Spark driver is the program space in which the Spark application’s main method runs
# MAGIC coordinating the Spark entire application.<br>
# MAGIC E. The Spark driver is horizontally scaled to increase overall processing throughput of a Spark
# MAGIC application.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:2 <br>
# MAGIC **Which of the following describes the relationship between nodes and executors?** <br>
# MAGIC A. Executors and nodes are not related. <br>
# MAGIC B. A node is a processing engine running on an executor. <br>
# MAGIC C. An executor is a processing engine running on a node. <br>
# MAGIC D. There are always the same number of executors and nodes. <br>
# MAGIC E. There are always more nodes than executors. <br>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:3 <br>
# MAGIC **Which of the following will occur if there are more slots than there are tasks?** <br>
# MAGIC A. The Spark job will likely not run as efficiently as possible. <br>
# MAGIC B. The Spark application will fail – there must be at least as many tasks as there are slots. <br>
# MAGIC C. Some executors will shut down and allocate all slots on larger executors first. <br>
# MAGIC D. More tasks will be automatically generated to ensure all slots are being used. <br>
# MAGIC E. The Spark job will use just one single slot to perform all tasks. <br>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:4 <br>
# MAGIC **Which of the following is the most granular level of the Spark execution hierarchy?** <br>
# MAGIC A. Task <br>
# MAGIC B. Executor <br>
# MAGIC C. Node <br>
# MAGIC D. Job <br>
# MAGIC E. Slot <br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:5 <br>
# MAGIC **Which of the following statements about Spark jobs is incorrect?** <br>
# MAGIC A. Jobs are broken down into stages. <br>
# MAGIC B. There are multiple tasks within a single job when a DataFrame has more than one partition. <br>
# MAGIC C. Jobs are collections of tasks that are divided up based on when an action is called. <br>
# MAGIC D. There is no way to monitor the progress of a job. <br>
# MAGIC E. Jobs are collections of tasks that are divided based on when language variables are defined. <br>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:6<br>
# MAGIC **Which of the following operations is most likely to result in a shuffle?**<br>
# MAGIC A. DataFrame.join()<br>
# MAGIC B. DataFrame.filter()<br>
# MAGIC C. DataFrame.union()<br>
# MAGIC D. DataFrame.where()<br>
# MAGIC E. DataFrame.drop()<br>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:7<br>
# MAGIC **The default value of spark.sql.shuffle.partitions is 200. Which of the following describes what
# MAGIC that means?**<br>
# MAGIC A. By default, all DataFrames in Spark will be spit to perfectly fill the memory of 200
# MAGIC executors.<br>
# MAGIC B. By default, new DataFrames created by Spark will be split to perfectly fill the memory of
# MAGIC 200 executors.<br>
# MAGIC C. By default, Spark will only read the first 200 partitions of DataFrames to improve speed.<br>
# MAGIC D. By default, all DataFrames in Spark, including existing DataFrames, will be split into 200
# MAGIC unique segments for parallelization.<br>
# MAGIC E. By default, DataFrames will be split into 200 unique partitions when data is being shuffled.<br>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:8<br>
# MAGIC **Which of the following is the most complete description of lazy evaluation?**<br>
# MAGIC A. None of these options describe lazy evaluation<br>
# MAGIC B. A process is lazily evaluated if its execution does not start until it is put into action by some
# MAGIC type of trigger<br>
# MAGIC C. A process is lazily evaluated if its execution does not start until it is forced to display a result
# MAGIC to the user<br>
# MAGIC D. A process is lazily evaluated if its execution does not start until it reaches a specified date
# MAGIC and time<br>
# MAGIC E. A process is lazily evaluated if its execution does not start until it is finished compiling<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:9<br>
# MAGIC **Which of the following DataFrame operations is classified as an action?**<br>
# MAGIC A. DataFrame.drop()<br>
# MAGIC B. DataFrame.coalesce()<br>
# MAGIC C. DataFrame.take()<br>
# MAGIC D. DataFrame.join()<br>
# MAGIC E. DataFrame.filter()<br>

# COMMAND ----------

# MAGIC %md
# MAGIC <span style="color:#FF0000;">Question #:10</span>
# MAGIC <br>
# MAGIC **Which of the following DataFrame operations is classified as a wide transformation?**<br>
# MAGIC A. DataFrame.filter()<br>
# MAGIC B. DataFrame.join()<br>
# MAGIC C. DataFrame.select()<br>
# MAGIC D. DataFrame.drop()<br>
# MAGIC E. DataFrame.union()<br>

# COMMAND ----------

# MAGIC %md
# MAGIC <span style="color:red"><b>Question #:11</b></span><br>
# MAGIC **Which of the following describes the difference between cluster and client execution modes?**<br>
# MAGIC A. The cluster execution mode runs the driver on a worker node within a cluster, while the client execution mode runs the driver on the client machine (also known as a gateway machine
# MAGIC or edge node).<br>
# MAGIC B. The cluster execution mode is run on a local cluster, while the client execution mode is run in
# MAGIC the cloud.<br>
# MAGIC C. The cluster execution mode distributes executors across worker nodes in a cluster, while the
# MAGIC client execution mode runs a Spark job entirely on one client machine.<br>
# MAGIC D. The cluster execution mode runs the driver on the cluster machine (also known as a gateway
# MAGIC machine or edge node), while the client execution mode runs the driver on a worker node within
# MAGIC a cluster.<br>
# MAGIC E. The cluster execution mode distributes executors across worker nodes in a cluster, while the
# MAGIC client execution mode submits a Spark job from a remote machine to be run on a remote,
# MAGIC unconfigurable cluster.<br>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:12<br>
# MAGIC **Which of the following statements about Spark’s stability is incorrect?**<br>
# MAGIC A. Spark is designed to support the loss of any set of worker nodes.<br>
# MAGIC B. Spark will rerun any failed tasks due to failed worker nodes.<br>
# MAGIC C. Spark will recompute data cached on failed worker nodes.<br>
# MAGIC D. Spark will spill data to disk if it does not fit in memory.<br>
# MAGIC E. Spark will reassign the driver to a worker node if the driver’s node fails.<br>
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:13<br>
# MAGIC **Which of the following cluster configurations is most likely to experience an out-of-memoryerror in response to data skew in a single partition?**<br>
# MAGIC
# MAGIC ![png](/Workspace/Users/tayarani.amir@gmail.com/image_Question13.png)
# MAGIC
# MAGIC **Note: each configuration has roughly the same compute power using 100 GB of RAM and 200 cores**<br>
# MAGIC A. Scenario #4<br>
# MAGIC B. Scenario #5<br>
# MAGIC C. Scenario #6<br>
# MAGIC D. More information is needed to determine an answer.<br>
# MAGIC E. Scenario #1<br>
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:14<br>
# MAGIC **Of the following situations, in which will it be most advantageous to store DataFrame df at the MEMORY_AND_DISK storage level rather than the MEMORY_ONLY storage level?**<br>
# MAGIC A. When all of the computed data in DataFrame df can fit into memory.<br>
# MAGIC B. When the memory is full and it’s faster to recompute all the data in DataFrame df rather than read it from disk.<br>
# MAGIC C. When it’s faster to recompute all the data in DataFrame df that cannot fit into memory based on its logical plan rather than read it from disk.<br>
# MAGIC D. When it’s faster to read all the computed data in DataFrame df that cannot fit into memory from disk rather than recompute it based on its logical plan.<br>
# MAGIC E. The storage level MENORY_ONLY will always be more advantageous because it’s faster to read data from memory than it is to read data from disk.<br>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:15<br>
# MAGIC **A Spark application has a 128 GB DataFrame A and a 1 GB DataFrame B. If a broadcast join were to be performed on these two DataFrames, which of the following describes which DataFrame should be broadcasted and why?**<br>
# MAGIC A. Either DataFrame can be broadcasted. Their results will be identical in result and efficiency.<br>
# MAGIC B. DataFrame B should be broadcasted because it is smaller and will eliminate the need for the shuffling of itself.<br>
# MAGIC C. DataFrame A should be broadcasted because it is larger and will eliminate the need for the shuffling of DataFrame B.<br>
# MAGIC D. DataFrame B should be broadcasted because it is smaller and will eliminate the need for the shuffling of DataFrame A.<br>
# MAGIC E. DataFrame A should be broadcasted because it is smaller and will eliminate the need for the shuffling of itself.<br>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:16<br>
# MAGIC **Which of the following operations can be used to create a new DataFrame that has 12 partitions from an original DataFrame df that has 8 partitions?**<br>
# MAGIC A. df.repartition(12)<br>
# MAGIC B. df.cache()<br>
# MAGIC C. df.partitionBy(1.5)<br>
# MAGIC D. df.coalesce(12)<br>
# MAGIC E. df.partitionBy(12)<br>

# COMMAND ----------

# DBTITLE 1,Cell 20
# MAGIC %md
# MAGIC Question #:17<br>**Which of the following object types cannot be contained within a column of a Spark DataFrame?**<br>A. DataFrame<br>B. String<br>C. Array<br>D. null<br>E. Vector<br>

# COMMAND ----------

# DBTITLE 1,Cell 21
# MAGIC %md
# MAGIC Question #:18<br>**Which of the following operations can be used to create a DataFrame with a subset of columns from DataFrame storesDF that are specified by name?**<br>A. storesDF.subset()<br>B. storesDF.select()<br>C. storesDF.selectColumn()<br>D. storesDF.filter()<br>E. storesDF.drop()<br>

# COMMAND ----------

# DBTITLE 1,Cell 22
# MAGIC %md
# MAGIC Question #:19<br>**The code block shown below contains an error. The code block is intended to return a DataFrame containing all columns from DataFrame storesDF except for column sqft and column customerSatisfaction. Identify the error.**<br>Code block: ```storesDF.drop(sqft, customerSatisfaction)```<br>A. 
# MAGIC The drop() operation only works if one column name is called at a time – there should be two calls in succession like storesDF.drop("sqft").drop("customerSatisfaction").<br>
# MAGIC B. The drop() operation only works if column names are wrapped inside the col() function like storesDF.drop(col(sqft), col(customerSatisfaction)).<br>C. There is no drop() operation for storesDF.<br>D. The sqft and customerSatisfaction column names should be quoted like "sqft" and "customerSatisfaction".<br>E. The sqft and customerSatisfaction column names should be subset from the DataFrame storesDF like storesDF."sqft" and storesDF."customerSatisfaction".<br>

# COMMAND ----------

# DBTITLE 1,Cell 23
# MAGIC %md
# MAGIC Question #:20<br>**Which of the following code blocks returns a DataFrame containing only the rows from DataFrame storesDF where the value in column sqft is less than or equal to 25,000?**<br>A. storesDF.filter("sqft" <= 25000)<br>B. storesDF.filter(sqft > 25000)<br>C. storesDF.where(storesDF[sqft] > 25000)<br>D. storesDF.where(sqft > 25000)<br>E. storesDF.filter(col("sqft") <= 25000)<br>

# COMMAND ----------

# DBTITLE 1,Cell 25
# MAGIC %md
# MAGIC Question #:21<br>**Which of the following code blocks returns a DataFrame containing only the rows from DataFrame storesDF where the value in column sqft is less than or equal to 25,000 OR the value in column customerSatisfaction is greater than or equal to 30?**<br>A. storesDF.filter(col("sqft") <= 25000 | col("customerSatisfaction") >= 30)<br>B. storesDF.filter(col("sqft") <= 25000 or col("customerSatisfaction") >= 30)<br>C. storesDF.filter(sqft <= 25000 or customerSatisfaction >= 30)<br>D. storesDF.filter(col(sqft) <= 25000 | col(customerSatisfaction) >= 30)<br>E. storesDF.filter((col("sqft") <= 25000) | (col("customerSatisfaction") >= 30))<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:22<br>**Which of the following code blocks returns a new DataFrame from DataFrame storesDF where column storeId is of the type string?**<br>
# MAGIC A. storesDF.withColumn("storeId", cast(col("storeId"), StringType()))<br>
# MAGIC B. storesDF.withColumn("storeId", col("storeId").cast(StringType()))<br>
# MAGIC C. storesDF.withColumn("storeId", cast(storeId).as(StringType))<br>
# MAGIC D. storesDF.withColumn("storeId", col(storeId).cast(StringType))<br>
# MAGIC E. storesDF.withColumn("storeId", cast("storeId").as(StringType()))<br>

# COMMAND ----------

# DBTITLE 1,Cell 26
# MAGIC %md
# MAGIC Question #:23<br>**Which of the following code blocks returns a new DataFrame with a new column employeesPerSqft that is the quotient of column numberOfEmployees and column sqft, both of which are from DataFrame storesDF? Note that column employeesPerSqft is not in the original DataFrame storesDF.**<br>A. storesDF.withColumn("employeesPerSqft", col("numberOfEmployees") / col("sqft"))<br>B. storesDF.withColumn("employeesPerSqft", "numberOfEmployees" / "sqft")<br>C. storesDF.select("employeesPerSqft", "numberOfEmployees" / "sqft")<br>D. storesDF.select("employeesPerSqft", col("numberOfEmployees") / col("sqft"))<br>E. storesDF.withColumn(col("employeesPerSqft"), col("numberOfEmployees") / col("sqft"))<br>

# COMMAND ----------

# DBTITLE 1,Cell 27
# MAGIC %md
# MAGIC Question #:24<br>**The code block shown below should return a new DataFrame from DataFrame storesDF where column modality is the constant string "PHYSICAL". Assume DataFrame storesDF is the only defined language variable. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**<br>
# MAGIC Code block: `storesDF._1_(_2_, _3_(_4_))`<br>
# MAGIC
# MAGIC A.  
# MAGIC 1. withColumn  
# MAGIC 2. "modality"  
# MAGIC 3. col  
# MAGIC 4. "PHYSICAL"  
# MAGIC
# MAGIC B.  
# MAGIC 1. withColumn  
# MAGIC 2. "modality"  
# MAGIC 3. lit  
# MAGIC 4. PHYSICAL  
# MAGIC
# MAGIC C.  
# MAGIC 1. withColumn  
# MAGIC 2. "modality"  
# MAGIC 3. lit  
# MAGIC 4. "PHYSICAL"  
# MAGIC
# MAGIC D.  
# MAGIC 1. withColumn  
# MAGIC 2. "modality"  
# MAGIC 3. SrtringType  
# MAGIC 4. "PHYSICAL"  
# MAGIC
# MAGIC E.  
# MAGIC 1. newColumn  
# MAGIC 2. modality  
# MAGIC 3. SrtringType  
# MAGIC 4. PHYSICAL

# COMMAND ----------

# DBTITLE 1,Cell 28
# MAGIC %md
# MAGIC Question #:25<br>
# MAGIC **Which of the following code blocks returns a DataFrame where column storeCategory from DataFrame storesDF is split at the underscore character into column storeValueCategory and column storeSizeCategory?**
# MAGIC
# MAGIC A sample of DataFrame storesDF is displayed below:<br>
# MAGIC ![image_1773927193522.png](./image_1773927193522.png "image_1773927193522.png")<br>
# MAGIC
# MAGIC - **A.**  
# MAGIC   `(storesDF.withColumn("storeValueCategory", split(col("storeCategory"), "_")[1])`  
# MAGIC   `.withColumn("storeSizeCategory", split(col("storeCategory"), "_")[2]))`
# MAGIC
# MAGIC - **B.**  
# MAGIC   `(storesDF.withColumn("storeValueCategory", col("storeCategory").split("_")[0])`  
# MAGIC   `.withColumn("storeSizeCategory", col("storeCategory").split("_")[1]))`
# MAGIC
# MAGIC - **C.**  
# MAGIC   `(storesDF.withColumn("storeValueCategory", split(col("storeCategory"), "_")[0])`  
# MAGIC   `.withColumn("storeSizeCategory", split(col("storeCategory"), "_")[1]))`
# MAGIC
# MAGIC - **D.**  
# MAGIC   `(storesDF.withColumn("storeValueCategory", split("storeCategory", "_")[0])`  
# MAGIC   `.withColumn("storeSizeCategory", split("storeCategory", "_")[1]))`
# MAGIC
# MAGIC - **E.**  
# MAGIC   `(storesDF.withColumn("storeValueCategory", col("storeCategory").split("_")[1])`  
# MAGIC   `.withColumn("storeSizeCategory", col("storeCategory").split("_")[2]))`

# COMMAND ----------

# DBTITLE 1,Cell 29
# MAGIC %md
# MAGIC Question #:26<br>**Which of the following code blocks returns a new DataFrame where column productCategories only has one word per row, resulting in a DataFrame with many more rows than DataFrame storesDF?**<br>A sample of storesDF is displayed below:<br>![image_1773927252244.png](./image_1773927252244.png "image_1773927252244.png")<br>A. storesDF.withColumn("productCategories", explode(col("productCategories")))<br>B. storesDF.withColumn("productCategories", split(col("productCategories")))<br>C. storesDF.withColumn("productCategories", col("productCategories").explode())<br>D. storesDF.withColumn("productCategories", col("productCategories").split())<br>E. storesDF.select(explode(col("productCategories")).alias("productCategories"))<br>

# COMMAND ----------

# DBTITLE 1,Cell 30
# MAGIC %md
# MAGIC Question #:27<br>**Which of the following code blocks returns a new DataFrame with column storeDescription where the pattern "Description: " has been removed from the beginning of column storeDescription in DataFrame storesDF?**<br>A sample of DataFrame storesDF is below:<br>![image_1773927314484.png](./image_1773927314484.png "image_1773927314484.png")<br>A. storesDF.withColumn("storeDescription", regexp_extract(col("storeDescription"), "^Description: (.+)", 1))<br>B. storesDF.withColumn("storeDescription", col("storeDescription").regexp_replace("^Description: ", ""))<br>C. storesDF.withColumn("storeDescription", regexp_extract(col("storeDescription"), "^Description: (.+)", 0))<br>D. storesDF.withColumn("storeDescription", col("storeDescription").regexp_extract("^Description: (.+)", 1))<br>E. storesDF.withColumn("storeDescription", col("storeDescription").regexp_extract("^Description: (.+)", 0))<br>

# COMMAND ----------

# DBTITLE 1,Cell 31
# MAGIC %md
# MAGIC Question #:28<br>**Which of the following code blocks returns a new DataFrame where column division from DataFrame storesDF has been replaced and renamed to column state and column managerName from DataFrame storesDF has been replaced and renamed to column managerFullName?**<br>A. (storesDF.withColumnRenamed(["division", "state"], ["managerName", "managerFullName"])<br>B. (storesDF.withColumn("state", col("division"))<br>.withColumn("managerFullName", col("managerName")))<br>C. (storesDF.withColumn("state", col("division"))<br>.withColumn("managerFullName", col("managerName"))<br>.drop("division", "managerName"))<br>D. (storesDF.withColumnRenamed("division", "state")<br>.withColumnRenamed("managerName", "managerFullName"))<br>E. (storesDF.withColumn("state", col("division")).drop("division")<br>.withColumn("managerFullName", col("managerName")).drop("managerName"))<br>

# COMMAND ----------

# DBTITLE 1,Cell 32
# MAGIC %md
# MAGIC Question #:29<br>**The code block shown contains an error. The code block is intended to return a new DataFrame where column sqft from DataFrame storesDF has had its missing values replaced with the value 30,000. Identify the error.**<br>A sample of DataFrame storesDF is displayed below:<br>![image_1773927626725.png](./image_1773927626725.png "image_1773927626725.png")<br>Code block: storesDF.na.fill(30000, col("sqft"))<br>A. The argument to the subset parameter should be a list like ["sqft"].<br>B. The value and subset arguments should be switched in order.<br>C. The storesDF DataFrame should be wrapped by the col() function.<br>D. Missing values are automatically replaced in Spark – there is no need for this operation.<br>E. The entire operation should be replaced with storesDF.fillna(30000, ["sqft"]).<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:30<br>
# MAGIC **Which of the following operations fails to return a DataFrame with no duplicate rows?**<br>
# MAGIC A. DataFrame.dropDuplicates()<br>
# MAGIC B. DataFrame.distinct()<br>
# MAGIC C. DataFrame.drop_duplicates()<br>
# MAGIC D. DataFrame.drop_duplicates(subset = None)<br>
# MAGIC E. DataFrame.drop_duplicates(subset = "all")
# MAGIC
# MAGIC

# COMMAND ----------

# DBTITLE 1,Cell 34
# MAGIC %md
# MAGIC Question #:31<br>**Which of the following code blocks will most quickly return an approximation for the number of distinct values in column division in DataFrame storesDF?**<br>A. storesDF.agg(approx_count_distinct(col("division")).alias("divisionDistinct"))<br>B. storesDF.agg(approx_count_distinct(col("division"), 0.01).alias("divisionDistinct"))<br>C. storesDF.agg(count_distinct(col("division")).alias("divisionDistinct"))<br>D. storesDF.agg(approx_count_distinct("division").alias("divisionDistinct"))<br>E. storesDF.select(approx_count_distinct(col("division")).alias("divisionDistinct"))<br>

# COMMAND ----------

# DBTITLE 1,Cell 35
# MAGIC %md
# MAGIC Question #:32<br>**The code block shown below contains an error. The code block is intended to return a new DataFrame with the mean of column sqft from DataFrame storesDF in column sqftMean. Identify the error.**<br>Code block: storesDF.agg(mean("sqft").alias("sqftMean"))<br>A. The argument to the mean() operation should be wrapped in the col() operation.<br>B. There is no mean() operation – the avg() operation should be used instead.<br>C. The agg() operation should be replaced with the aggregate() operation.<br>D. The agg() operation should be replaced with the select() operation.<br>E. There is no error – this code will run as expected.<br>

# COMMAND ----------

# DBTITLE 1,Cell 36
# MAGIC %md
# MAGIC Question #:33<br>**Which of the following operations can be used to return the number of rows in a DataFrame?**<br>A. DataFrame.numberOfRows()<br>B. DataFrame.n()<br>C. DataFrame.sum()<br>D. DataFrame.count()<br>E. DataFrame.countDistinct()<br>

# COMMAND ----------

# DBTITLE 1,Cell 37
# MAGIC %md
# MAGIC Question #:34<br>**Which of the following operations returns a GroupedData object?**<br>A. DataFrame.GroupBy()<br>B. DataFrame.cubed()<br>C. DataFrame.group()<br>D. DataFrame.groupBy()<br>E. DataFrame.grouping_id()<br>

# COMMAND ----------

# DBTITLE 1,Cell 38
# MAGIC %md
# MAGIC Question #:35<br>**Which of the following code blocks returns a collection of summary statistics for all columns in DataFrame storesDF?**<br>A. storesDF.summary("mean")<br>B. storesDF.describe(all = True)<br>C. storesDF.describe("all")<br>D. storesDF.summary("all")<br>E. storesDF.describe()<br>

# COMMAND ----------

# DBTITLE 1,Cell 39
# MAGIC %md
# MAGIC Question #:36<br>**Which of the following code blocks fails to return a DataFrame reverse sorted alphabetically based on column division?**<br>A. storesDF.orderBy("division", ascending = False)<br>B. storesDF.orderBy(desc("division"))<br>C. storesDF.orderBy(col("division"), ascending = False)<br>D. storesDF.sort(col("division").desc())<br>E. storesDF.orderBy(col("division").asc())<br>

# COMMAND ----------

# DBTITLE 1,Cell 40
# MAGIC %md
# MAGIC Question #:37<br>**Which of the following code blocks returns a 15 percent sample of rows from DataFrame storesDF without replacement?**<br>A. storesDF.sample(fraction = 0.10)<br>B. storesDF.sample(withReplacement = False, fraction = 0.15)<br>C. storesDF.sample(fraction = 0.15)<br>D. storesDF.sample(withReplacement = False, fraction = 1.5)<br>E. storesDF.sample(withReplacement = True, fraction = 0.15)<br>

# COMMAND ----------

# DBTITLE 1,Cell 41
# MAGIC %md
# MAGIC Question #:38<br>**Which of the following code blocks returns all the rows from DataFrame storesDF?**<br>A. storesDF.head()<br>B. storesDF.collect()<br>C. storesDF.count()<br>D. storesDF.take()<br>E. storesDF.show()<br>

# COMMAND ----------

# DBTITLE 1,Cell 42
# MAGIC %md
# MAGIC Question #:39<br>**Which of the following code blocks applies the function assessPerformance() to each row of DataFrame storesDF?**<br>A. [assessPerformance(row) for row in storesDF.take(3)]<br>B. [assessPerformance() for row in storesDF]<br>C. storesDF.collect().apply(lambda: assessPerformance)<br>D. [assessPerformance(row) for row in storesDF.collect()]<br>E. [assessPerformance(row) for row in storesDF]<br>

# COMMAND ----------

# DBTITLE 1,Cell 43
# MAGIC %md
# MAGIC Question #:40<br>**The code block shown below contains an error. The code block is intended to print the schema of DataFrame storesDF. Identify the error.**<br>Code block: storesDF.printSchema<br>A. There is no printSchema member of DataFrame – schema and the print() function should be used instead.<br>B. The entire line needs to be a string – it should be wrapped by str().<br>C. There is no printSchema member of DataFrame – the getSchema() operation should be used instead.<br>D. There is no printSchema member of DataFrame – the schema() operation should be used instead.<br>E. The printSchema member of DataFrame is an operation and needs to be followed by parentheses.<br>

# COMMAND ----------

# DBTITLE 1,Cell 44
# MAGIC %md
# MAGIC Question #:41  
# MAGIC The code block shown below should create and register a SQL UDF named "ASSESS_PERFORMANCE" using the Python function `assessPerformance()` and apply it to column `customerSatisfaction` in table `stores`.  
# MAGIC Choose the response that correctly fills in the numbered blanks within the code block to complete this task.  
# MAGIC
# MAGIC **Code block:**  
# MAGIC
# MAGIC `spark._1_._2_(_3_, _4_)`  
# MAGIC `spark.sql("SELECT customerSatisfaction, _5_(customerSatisfaction) AS result FROM stores")`
# MAGIC
# MAGIC
# MAGIC **Options:**  
# MAGIC A.  
# MAGIC 1. udf  
# MAGIC 2. register  
# MAGIC 3. "ASSESS_PERFORMANCE"  
# MAGIC 4. assessPerformance  
# MAGIC 5. ASSESS_PERFORMANCE  
# MAGIC
# MAGIC B.  
# MAGIC 1. udf  
# MAGIC 2. register  
# MAGIC 3. assessPerformance  
# MAGIC 4. "ASSESS_PERFORMANCE"  
# MAGIC 5. "ASSESS_PERFORMANCE"  
# MAGIC
# MAGIC C.  
# MAGIC 1. udf  
# MAGIC 2. register  
# MAGIC 3. "ASSESS_PERFORMANCE"  
# MAGIC 4. assessPerformance  
# MAGIC 5. "ASSESS_PERFORMANCE"  
# MAGIC
# MAGIC D.  
# MAGIC 1. register  
# MAGIC 2. udf  
# MAGIC 3. "ASSESS_PERFORMANCE"  
# MAGIC 4. assessPerformance  
# MAGIC 5. "ASSESS_PERFORMANCE"  
# MAGIC
# MAGIC E.  
# MAGIC 1. udf  
# MAGIC 2. register  
# MAGIC 3. ASSESS_PERFORMANCE  
# MAGIC 4. assessPerformance  
# MAGIC 5. ASSESS_PERFORMANCE

# COMMAND ----------

# DBTITLE 1,Cell 45
# MAGIC %md
# MAGIC Question #:42<br>**The code block shown below contains an error. The code block is intended to create a Python UDF assessPerformanceUDF() using the integer-returning Python function assessPerformance() and apply it to column customerSatisfaction in DataFrame storesDF. Identify the error.**<br>Code block: assessPerformanceUDF = udf(assessPerformance)<br>storesDF.withColumn("result", assessPerformanceUDF(col("customerSatisfaction")))<br>A. The assessPerformance() operation is not properly registered as a UDF.<br>B. The withColumn() operation is not appropriate here – UDFs should be applied by iterating over rows instead.<br>C. UDFs can only be applied vie SQL and not through the DataFrame API.<br>D. The return type of the assessPerformanceUDF() is not specified in the udf() operation.<br>E. The assessPerformance() operation should be used on column customerSatisfaction rather than the assessPerformanceUDF() operation.<br>

# COMMAND ----------

# DBTITLE 1,Cell 46
# MAGIC %md
# MAGIC Question #:43<br>**The code block shown below contains an error. The code block is intended to use SQL to return a new DataFrame containing column storeId and column managerName from a table created from DataFrame storesDF. Identify the error.**<br>Code block:<br>storesDF.createOrReplaceTempView("stores")<br>storesDF.sql("SELECT storeId, managerName FROM stores")<br>A. The createOrReplaceTempView() operation does not make a Dataframe accessible via SQL.<br>B. The sql() operation should be accessed via the spark variable rather than DataFrame storesDF.<br>C. There is the sql() operation in DataFrame storesDF. The operation query() should be used instead.<br>D. This cannot be accomplished using SQL - the DataFrame API should be used instead.<br>E. The createOrReplaceTemView() operation should be accessed via the spark variable rather than DataFrame storeDF.<br>

# COMMAND ----------

# DBTITLE 1,Cell 47
# MAGIC %md
# MAGIC Question #:44  
# MAGIC The code block shown below should create a single-column DataFrame from Python list `years` which is made up of integers.  
# MAGIC Choose the response that correctly fills in the numbered blanks within the code block to complete this task.  
# MAGIC
# MAGIC **Code block:**  
# MAGIC `_1_._2_(_3_, _4_)`  
# MAGIC
# MAGIC **Options:**  
# MAGIC A.  
# MAGIC 1. spark  
# MAGIC 2. createDataFrame  
# MAGIC 3. years  
# MAGIC 4. IntegerType  
# MAGIC
# MAGIC B.  
# MAGIC 1. DataFrame  
# MAGIC 2. create  
# MAGIC 3. [years]  
# MAGIC 4. IntegerType  
# MAGIC
# MAGIC C.  
# MAGIC 1. spark  
# MAGIC 2. createDataFrame  
# MAGIC 3. [years]  
# MAGIC 4. IntegertType  
# MAGIC
# MAGIC D.  
# MAGIC 1. spark  
# MAGIC 2. createDataFrame  
# MAGIC 3. [years]  
# MAGIC 4. IntegertType()  
# MAGIC
# MAGIC E.  
# MAGIC 1. spark  
# MAGIC 2. createDataFrame  
# MAGIC 3. years  
# MAGIC 4. IntegertType()

# COMMAND ----------

# DBTITLE 1,Cell 48
# MAGIC %md
# MAGIC Question #:45<br>**The code block shown below contains an error. The code block is intended to cache DataFrame storesDF only in Spark's memory and then return the number of rows in the cached DataFrame. Identify the error.**<br>Code block: storesDF.cache().count()<br>A. The cache() operation caches DataFrames at the MEMORY_AND_DISK level by default – the storage level must be specified to MEMORY_ONLY as an argument to cache().<br>B. The cache() operation caches DataFrames at the MEMORY_AND_DISK level by default – the storage level must be set via storesDF.storageLevel prior to calling cache().<br>C. The storesDF DataFrame has not been checkpointed – it must have a checkpoint in order to be cached.<br>D. DataFrames themselves cannot be cached – DataFrame storesDF must be cached as a table.<br>E. The cache() operation can only cache DataFrames at the MEMORY_AND_DISK_ONLY storage level. The persist() operation should be used instead to cache only in memory.<br>

# COMMAND ----------

# DBTITLE 1,Cell 49
# MAGIC %md
# MAGIC Question #:46<br>**Which of the following operations can be used to return a new DataFrame from DataFrame storesDF without inducing a shuffle?**<br>A. storesDF.intersect()<br>B. storesDF.repartition(1)<br>C. storesDF.union()<br>D. storesDF.coalesce(1)<br>E. storesDF.rdd.getNumPartitions()<br>

# COMMAND ----------

# DBTITLE 1,Cell 50
# MAGIC %md
# MAGIC Question #:47<br>**The code block shown below contains an error. The code block is intended to return a new 12-partition DataFrame from the 8-partition DataFrame storesDF by inducing a shuffle. Identify the error.**<br>Code block: storesDF.coalesce(12)<br>A. The coalesce() operation cannot guarantee the number of target partitions – the repartition() operation should be used instead.<br>B. The coalesce() operation does not induce a shuffle and cannot increase the number of partitions – the repartition() operation should be used instead.<br>C. The coalesce() operation will only work if the DataFrame has been cached to memory – the repartition() operation should be used instead.<br>D. The coalesce() operation will only work if the number of target partitions is lower than the number of current partitions.<br>E. The coalesce() operation does not induce a shuffle and cannot increase the number of partitions. The shuffle() operation should be used instead.<br>

# COMMAND ----------

# DBTITLE 1,Cell 51
# MAGIC %md
# MAGIC Question #:48<br>**Which of the following Spark properties is used to configure whether DataFrame partitions that do not meet a minimum size threshold are automatically coalesced into larger partitions during a shuffle?**<br>A. spark.sql.shuffle.partitions<br>B. spark.sql.autoBroadcastJoinThreshold<br>C. spark.sql.adaptive.skewJoin.enabled<br>D. spark.sql.inMemoryColumnarStorage.batchSize<br>E. spark.sql.adaptive.coalescePartitions.enabled<br>

# COMMAND ----------

# DBTITLE 1,Cell 52
# MAGIC %md
# MAGIC Question #:49<br>**The code block shown below contains an error. The code block is intended to return a DataFrame containing a column openDateString, a string representation of Java's SimpleDateFormat. Identify the error.**<br>Note that column openDate is of type integer and represents a date in the UNIX epoch format – the number of seconds since midnight on January 1st, 1970.<br>An example of Java's SimpleDateFormat is "Sunday, Dec 4, 2008 1:05 PM".<br>A sample of storesDF is displayed below:<br>![image_1773928852784.png](./image_1773928852784.png "image_1773928852784.png")<br>Code block:<br>storesDF.withColumn("openDateString", from_unixtime(col("openDate"), "EEE, MMM d, yyyy h:mm a", TimestampType()))<br>A. The from_unixtime() operation can only accept one or two arguments – the third argument TimestampType() should be removed.<br>B. The from_unixtime() operation requires column openDate to be wrapped in the col() function like col(col("openDate")).<br>C. The from_unixtime() operation returns a timestamp and needs to be cast as a string.<br>D. The from_unixtime() operation does not exist – the to_timestamp() operation should be used instead.<br>E. The from_unixtime() operation requires the column name openDate to be in quotes like from_unixtime("openDate", "EEE, MMM d, yyyy h:mm a").<br>

# COMMAND ----------

# DBTITLE 1,Cell 53
# MAGIC %md
# MAGIC Question #:50<br>**Which of the following code blocks returns a DataFrame containing a column dayOfYear, an integer representation of the day of the year from column openDate from DataFrame storesDF?**<br>Note that column openDate is of type integer and represents a date in the UNIX epoch format – the number of seconds since midnight on January 1st, 1970.<br>A sample of storesDF is displayed below:<br>![image_1773928908521.png](./image_1773928908521.png "image_1773928908521.png")<br>A. (storesDF.withColumn("openTimestamp", col("openDate").cast("Timestamp"))<br>. withColumn("dayOfYear", dayofyear(col("openTimestamp"))))<br>B. storesDF.withColumn("dayOfYear", get dayofyear(col("openDate")))<br>C. storesDF.withColumn("dayOfYear", dayofyear("openDate"))<br>D. storesDF.withColumn("dayOfYear", dayofyear(col("openDate")))<br>E. (storesDF.withColumn("openTimestamp", col("openDate").cast(TimestampType()))<br>.withColumn("dayOfYear", dayofyear(col("openTimestamp"))))<br>

# COMMAND ----------

# DBTITLE 1,Cell 54
# MAGIC %md
# MAGIC Question #:51<br>**The code block shown below contains an error. The code block intended to return a new DataFrame that is the result of an inner join between DataFrame storesDF and DataFrame employeesDF on column storeId. Identify the error.**<br>Code block: StoresDF.join(employeesDF, "inner", "storeID")<br>A. The key column storeID needs to be wrapped in the col() operation.<br>B. The key column storeID needs to be in a list like ["storeID"].<br>C. The key column storeID needs to be specified in an expression of both DataFrame columns like storesDF.storeId == employeesDF.storeId.<br>D. There is no DataFrame.join() operation – DataFrame.merge() should be used instead.<br>E. The second and third arguments of the join() operation should be switched in order.<br>

# COMMAND ----------

# DBTITLE 1,Cell 55
# MAGIC %md
# MAGIC Question #:52<br>**Which of the following operations can perform an outer join on two DataFrames?**<br>A. DataFrame.crossJoin()<br>B. Standalone join() function<br>C. DataFrame.outerJoin()<br>D. DataFrame.join()<br>E. DataFrame.merge()<br>

# COMMAND ----------

# DBTITLE 1,Cell 56
# MAGIC %md
# MAGIC Question #:53<br>**Which of the following pairs of arguments cannot be used in DataFrame.join() to perform an inner join on two DataFrames, named and aliased with "a" and "b" respectively, to specify two key columns?**<br>A. on = [a.column1 == b.column1, a.column2 == b.column2]<br>B. on = [col("column1"), col("column2")]<br>C. on = [col("a.column1") == col("b.column1"), col("a.column2") == col("b.column2")]<br>D. All of these options can be used to perform an inner join with two key columns.<br>E. on = ["column1", "column2"]<br>

# COMMAND ----------

# DBTITLE 1,Cell 57
# MAGIC %md
# MAGIC Question #:54  
# MAGIC The below code block contains a logical error resulting in inefficiency. The code block is intended to efficiently perform a broadcast join of DataFrame `storesDF` and the much larger DataFrame `employeesDF` using key column `storeId`.  
# MAGIC
# MAGIC **Code block:**  
# MAGIC `storesDF.join(broadcast(employeesDF), "storeId")`  
# MAGIC
# MAGIC **Options:**  
# MAGIC A. The larger DataFrame `employeesDF` is being broadcasted rather than the smaller DataFrame `storesDF`.  
# MAGIC B. There is never a need to call the `broadcast()` operation in Apache Spark 3.  
# MAGIC C. The entire line of code should be wrapped in `broadcast()` rather than just DataFrame `employeesDF`.  
# MAGIC D. The `broadcast()` operation will only perform a broadcast join if the Spark property `spark.sql.autoBroadcastJoinThreshold` is manually set.  
# MAGIC E. Only one of the DataFrames is being broadcasted rather than both of the DataFrames.

# COMMAND ----------

# DBTITLE 1,Cell 59
# MAGIC %md
# MAGIC Question #:55  
# MAGIC **The code block shown below contains an error. The code block is intended to return a new DataFrame that is the result of a cross join between DataFrame storesDF and DataFrame employeesDF. Identify the error.**  
# MAGIC
# MAGIC Code block:  
# MAGIC `storesDF.join(employeesDF, "cross")`  
# MAGIC
# MAGIC A. A cross join is not implemented by the DataFrame.join() operations – the standalone CrossJoin() operation should be used instead.  
# MAGIC B. There is no direct cross join in Spark, but it can be implemented by performing an outer join on all columns of both DataFrames.  
# MAGIC C. A cross join is not implemented by the DataFrame.join() operation – the DataFrame.crossJoin() operation should be used instead.  
# MAGIC D. There is no key column specified – the key column "storeId" should be the second argument.  
# MAGIC E. A cross join is not implemented by the DataFrame.join() operations – the standalone join() operation should be used instead.

# COMMAND ----------

# DBTITLE 1,Cell 60
# MAGIC %md
# MAGIC Question #:56  
# MAGIC The code block shown below contains an error. The code block is intended to return a new DataFrame that is the result of a position-wise union between DataFrame storesDF and DataFrame acquiredStoresDF. Identify the error.  
# MAGIC
# MAGIC Code block:  
# MAGIC `storesDF.unionByName(acquiredStoresDF)`
# MAGIC
# MAGIC A. There is no DataFrame.unionByName() operation – the concat() operation should be used instead with both DataFrames as arguments.  
# MAGIC B. There are no key columns specified – similar column names should be the second argument.  
# MAGIC C. The DataFrame.unionByName() operation does not union DataFrames based on column position – it uses column name instead.  
# MAGIC D. The unionByName() operation is a standalone operation rather than a method of DataFrame – it should have both DataFrames as arguments.  
# MAGIC E. There are no column positions specified – the desired column positions should be the second argument.

# COMMAND ----------

# DBTITLE 1,Cell 61
# MAGIC %md
# MAGIC Question #:57<br>**Which of the following code blocks writes DataFrame storesDF to file path filePath as JSON?**<br>A. storesDF.write.option("json").path(filePath)<br>B. storesDF.write.json(filePath)<br>C. storesDF.write.path(filePath)<br>D. storesDF.write(filePath)<br>E. storesDF.write().json(filePath)<br>

# COMMAND ----------

# DBTITLE 1,Cell 62
# MAGIC %md
# MAGIC Question #:58  
# MAGIC **In what order should the below lines of code be run in order to write DataFrame `storesDF` to file path `filePath` as parquet and partition by values in column `division`?**  
# MAGIC
# MAGIC **Lines of code:**  
# MAGIC 1. `.write()`  
# MAGIC 2. `.partitionBy("division")`  
# MAGIC 3. `.parquet(filePath)`  
# MAGIC 4. `.storesDF`  
# MAGIC 5. `.repartition("division")`  
# MAGIC 6. `.write`  
# MAGIC 7. `.path(filePath, "parquet")`  
# MAGIC
# MAGIC **Options:**  
# MAGIC A. 4, 1, 2, 3  
# MAGIC B. 4, 1, 5, 7  
# MAGIC C. 4, 6, 2, 3  
# MAGIC D. 4, 1, 5, 3  
# MAGIC E. 4, 6, 2, 7

# COMMAND ----------

# DBTITLE 1,Cell 63
# MAGIC %md
# MAGIC Question #:59  
# MAGIC The code block shown below contains an error. The code block is intended to read a parquet at the file path `filePath` into a DataFrame. Identify the error.
# MAGIC
# MAGIC **Code block:**  
# MAGIC `spark.read.load(filePath, source – "parquet")`
# MAGIC
# MAGIC A. There is no source parameter to the load() operation – the schema parameter should be used instead.  
# MAGIC B. There is no load() operation – it should be parquet() instead.  
# MAGIC C. The spark.read operation should be followed by parentheses to return a DataFrameReader object.  
# MAGIC D. The filePath argument to the load() operation should be quoted.  
# MAGIC E. There is no source parameter to the load() operation – it can be removed.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:60  
# MAGIC **In what order should the below lines of code be run in order to read a JSON file at the file path `filePath` into a DataFrame with the specified schema `schema`?**  
# MAGIC
# MAGIC **Lines of code:**  
# MAGIC 1. `.json(filePath, schema = schema)`  
# MAGIC 2. `.storesDF`  
# MAGIC 3. `.spark \`  
# MAGIC 4. `.read() \`  
# MAGIC 5. `.read \`  
# MAGIC 6. `.json(filePath, format = schema)`  
# MAGIC
# MAGIC **Options:**  
# MAGIC A. 3, 5, 6  
# MAGIC B. 2, 4, 1  
# MAGIC C. 3, 5, 1  
# MAGIC D. 2, 5, 1  
# MAGIC E. 3, 4, 1

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:61  
# MAGIC **Which of the following storage levels should be used to store as much data as possible in memory on two cluster nodes while storing any data that does not fit in memory on disk to be read in when needed?**  
# MAGIC A. MEMORY_ONLY_2  
# MAGIC B. MEMORY_AND_DISK_SER  
# MAGIC C. MEMORY_AND_DISK  
# MAGIC D. MEMORY_AND_DISK_2  
# MAGIC E. MEMORY_ONLY

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:62<br>**Which of the following Spark properties is used to configure the maximum size of an automatically broadcasted DataFrame when performing a join?**<br>
# MAGIC A. spark.sql.broadcastTimeout<br>
# MAGIC B. spark.sql.autoBroadcastJoinThreshold<br>
# MAGIC C. spark.sql.shuffle.partitions<br>
# MAGIC D. spark.sql.inMemoryColumnarStorage.batchSize<br>
# MAGIC E. spark.sql.adaptive.skewedJoin.enabled<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:63  
# MAGIC **Which of the following Spark properties is used to configure whether skewed partitions are automatically detected and subdivided into smaller partitions when joining two DataFrames together?**  
# MAGIC A. spark.sql.adaptive.skewedJoin.enabled  
# MAGIC B. spark.sql.adaptive.coalescePartitions.enable  
# MAGIC C. spark.sql.adaptive.skewHints.enabled  
# MAGIC D. spark.sql.shuffle.partitions  
# MAGIC E. spark.sql.shuffle.skewHints.enabled

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:64  
# MAGIC **Which of the following statements about the Spark DataFrame is true?**  
# MAGIC A. Spark DataFrames are mutable unless they've been collected to the driver.  
# MAGIC B. A Spark DataFrame is rarely used aside from the import and export of data.  
# MAGIC C. Spark DataFrames cannot be distributed into partitions.  
# MAGIC D. A Spark DataFrame is a tabular data structure that is the most common Structured API in Spark.  
# MAGIC E. A Spark DataFrame is exactly the same as a data frame in Python or R.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:65  
# MAGIC **Which of the following operations can be used to return a new DataFrame from DataFrame storesDF without columns that are specified by name?**  
# MAGIC A. storesDF.filter()  
# MAGIC B. storesDF.select()  
# MAGIC C. storesDF.drop()  
# MAGIC D. storesDF.subset()  
# MAGIC E. storesDF.dropColumn()

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:66  
# MAGIC **Which of the following code blocks returns a DataFrame containing only the rows from DataFrame storesDF where the value in column sqft is less than or equal to 25,000?**  
# MAGIC A. storesDF.where(storesDF[sqft] > 25000)  
# MAGIC B. storesDF.filter(sqft > 25000)  
# MAGIC C. storesDF.filter("sqft" <= 25000)  
# MAGIC D. storesDF.filter(col("sqft") <= 25000)  
# MAGIC E. storesDF.where(sqft > 25000)

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:67  
# MAGIC **Which of the following code blocks returns a DataFrame containing only the rows from DataFrame storesDF where the value in column sqft is less than or equal to 25,000 OR the value in column customerSatisfaction is greater than or equal to 30?**  
# MAGIC A. storesDF.filter(col("sqft") <= 25000 and col("customerSatisfaction") >= 30)  
# MAGIC B. storesDF.filter(col("sqft") <= 25000 | col("customerSatisfaction") >= 30)  
# MAGIC C. storesDF.filter(col(sqft) <= 25000 or col(customerSatisfaction) >= 30)  
# MAGIC D. storesDF.filter(sqft <= 25000 | customerSatisfaction >= 30)  
# MAGIC E. storesDF.filter(col("sqft") <= 25000 or col("customerSatisfaction") >= 30)

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:68  
# MAGIC **The code block shown below should return a new DataFrame from DataFrame storesDF where column storeId is of the type string. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**
# MAGIC ```
# MAGIC Code block: storesDF.__1__("storeId", __2__("storeId").__3__(__4__)
# MAGIC ``` 
# MAGIC
# MAGIC <br> 
# MAGIC A. 1. withColumn  
# MAGIC    2. col  
# MAGIC    3. cast  
# MAGIC    4. StringType() 
# MAGIC <br> 
# MAGIC B. 1. withColumn  
# MAGIC    2. cast  
# MAGIC    3. col  
# MAGIC    4. StringType()  
# MAGIC <br>
# MAGIC C. 1. newColumn  
# MAGIC    2. col  
# MAGIC    3. cast  
# MAGIC    4. StringType() 
# MAGIC    <br> 
# MAGIC D. 1. withColumn  
# MAGIC    2. cast  
# MAGIC    3. col  
# MAGIC    4. StringType  
# MAGIC    <br>
# MAGIC E. 1. withColumn  
# MAGIC    2. col  
# MAGIC    3. cast  
# MAGIC    4. StringType
# MAGIC    <br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:69  
# MAGIC **Which of the following code blocks returns a new DataFrame from DataFrame storesDF where column modality is the constant string "PHYSICAL"? Assume DataFrame storesDF is the only defined language variable.**  
# MAGIC A. storesDF.withColumn("modality", lit(PHYSICAL))  
# MAGIC B. storesDF.withColumn("modality", col("PHYSICAL"))  
# MAGIC C. storesDF.withColumn("modality", lit("PHYSICAL"))  
# MAGIC D. storesDF.withColumn("modality", StringType("PHYSICAL"))  
# MAGIC E. storesDF.withColumn("modality", "PHYSICAL")

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:70  
# MAGIC **The code block shown below contains an error. The code block is intended to return a new DataFrame where column managerName from DataFrame storesDF is split at the space character into column managerFirstName and column managerLastName. Identify the error.**  
# MAGIC A sample of DataFrame storesDF is displayed below:
# MAGIC
# MAGIC ![](/Workspace/Users/tayarani.amir@gmail.com/Drafts/Screenshot 2026-03-30 164432.png)
# MAGIC
# MAGIC Code block:  
# MAGIC `storesDF.withColumn("managerFirstName", col("managerName").split(" ").getItem(0))`  
# MAGIC `.withColumn("managerLastName", col("managerName").split(" ").getItem(1))  `<br>
# MAGIC A. The index values of 0 and 1 are not correct – they should be 1 and 2, respectively.  
# MAGIC B. The index values of 0 and 1 should be provided as second arguments to the split() operation rather than indexing the result.  
# MAGIC C. The split() operation comes from the imported functions object. It accepts a string column name and split character as arguments. It is not a method of a Column object.  
# MAGIC D. The split() operation comes from the imported functions object. It accepts a Column object and split character as arguments. It is not a method of a Column object.  
# MAGIC E. The withColumn operation cannot be called twice in a row.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:71  
# MAGIC **The code block shown below should return a new DataFrame where single quotes in column storeSlogan have been replaced with double quotes. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**  
# MAGIC
# MAGIC A sample of DataFrame storesDF is below:  
# MAGIC
# MAGIC Code Block:  
# MAGIC `storesDF.__1__(__2__, __3__(__4__, __5__, __6__))`  
# MAGIC
# MAGIC A.  
# MAGIC 1. withColumn  
# MAGIC 2. "storeSlogan"  
# MAGIC 3. regexp_extract  
# MAGIC 4. col("storeSlogan")  
# MAGIC 5. "\""  
# MAGIC 6. "'"  
# MAGIC
# MAGIC B.  
# MAGIC 1. newColumn  
# MAGIC 2. storeSlogan  
# MAGIC 3. regexp_extract  
# MAGIC 4. col(storeSlogan)  
# MAGIC 5. "\""  
# MAGIC 6. "'"  
# MAGIC
# MAGIC C.  
# MAGIC 1. withColumn  
# MAGIC 2. "storeSlogan"  
# MAGIC 3. regexp_replace  
# MAGIC 4. col("storeSlogan")  
# MAGIC 5. "\""  
# MAGIC 6. "'"  
# MAGIC
# MAGIC D.  
# MAGIC 1. withColumn  
# MAGIC 2. "storeSlogan"  
# MAGIC 3. regexp_replace  
# MAGIC 4. col("storeSlogan")  
# MAGIC 5. "'"  
# MAGIC 6. "\""  
# MAGIC
# MAGIC E.  
# MAGIC 1. withColumn  
# MAGIC 2. "storeSlogan"  
# MAGIC 3. regexp_extract  
# MAGIC 4. col("storeSlogan")  
# MAGIC 5. "'"  
# MAGIC 6. "\""

# COMMAND ----------

# MAGIC %md
# MAGIC **Question #:72
# MAGIC Which of the following code blocks returns a new DataFrame where column division from DataFrame storesDF has been replaced and renamed to column state and column managerName from DataFrame storesDF has been replaced and renamed to column managerFullName?**  
# MAGIC A. ```storesDF.withColumnRenamed("division", "state")  
# MAGIC    .withColumnRenamed("managerName", "managerFullName")```  
# MAGIC B. ```storesDF.withColumn("state", "division")  
# MAGIC    .withColumn("managerFullName", "managerName")```  
# MAGIC C. ```storesDF.withColumn("state", col("division"))  
# MAGIC    .withColumn("managerFullName", col("managerName"))```  
# MAGIC D. ```storesDF.withColumnRenamed(Seq("division", "state"), Seq("managerName", "managerFullName"))```  
# MAGIC E. ```storesDF.withColumnRenamed("state", "division")  
# MAGIC    .withColumnRenamed("managerFullName", "managerName")```

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:73  
# MAGIC **Which of the following code blocks returns a new DataFrame where column sqft from DataFrame storesDF has had its missing values replaced with the value 30,000?**  
# MAGIC A sample of DataFrame storesDF is below:  
# MAGIC ![](/Workspace/Users/tayarani.amir@gmail.com/Screenshot 2026-03-30 164951.png)
# MAGIC
# MAGIC A. storesDF.na.fill(30000, Seq("sqft"))  
# MAGIC B. storesDF.nafill(30000, col("sqft"))  
# MAGIC C. storesDF.na.fill(30000, col("sqft"))  
# MAGIC D. storesDF.fillna(30000, col("sqft"))  
# MAGIC E. storesDF.na.fill(30000, "sqft")

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:74  
# MAGIC **Which of the following operations can be used to return a DataFrame with no duplicate rows? Please select the most complete answer.**  
# MAGIC A. DataFrame.distinct()  
# MAGIC B. DataFrame.dropDuplicates() and DataFrame.distinct()  
# MAGIC C. DataFrame.dropDuplicates()  
# MAGIC D. DataFrame.drop_duplicates()  
# MAGIC E. DataFrame.dropDuplicates(), DataFrame.distinct() and DataFrame.drop_duplicates()

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:75  
# MAGIC **Which of the following code blocks returns a DataFrame where column divisionDistinct is the approximate number of distinct values in column division from DataFrame storesDF?**  
# MAGIC A. ```storesDF.withColumn("divisionDistinct", approx_count_distinct(col("division")))```  
# MAGIC B. ```storesDF.agg(col("division").approx_count_distinct("divisionDistinct"))``` <br>
# MAGIC C. ```storesDF.agg(approx_count_distinct(col("division")).alias("divisionDistinct"))```  
# MAGIC D. ```storesDF.withColumn("divisionDistinct", col("division").approx_count_distinct())``` <br>
# MAGIC E. ```storesDF.agg(col("division").approx_count_distinct().alias("divisionDistinct"))```

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:76  
# MAGIC **The code block shown below should return a new DataFrame with the mean of column sqft from DataFrame storesDF in column sqftMean. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**
# MAGIC
# MAGIC Code block:  
# MAGIC `storesDF.__1__(__2__(__3__).alias("sqftMean"))`  
# MAGIC
# MAGIC A.  
# MAGIC 1. agg  
# MAGIC 2. mean  
# MAGIC 3. col("sqft")  
# MAGIC
# MAGIC B.  
# MAGIC 1. withColumn  
# MAGIC 2. mean  
# MAGIC 3. col("sqft")  
# MAGIC
# MAGIC C.  
# MAGIC 1. agg  
# MAGIC 2. average  
# MAGIC 3. col("sqft")  
# MAGIC
# MAGIC D.  
# MAGIC 1. mean  
# MAGIC 2. col  
# MAGIC 3. "sqft"  
# MAGIC
# MAGIC E.  
# MAGIC 1. agg  
# MAGIC 2. mean  
# MAGIC 3. "sqft"

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:77  
# MAGIC **Which of the following code blocks returns the number of rows in DataFrame storesDF for each unique value in column division?**  
# MAGIC
# MAGIC A. `storesDF.groupBy("division").agg(count()) ` <br>
# MAGIC B. `storesDF.agg(groupBy("division").count()) ` <br>
# MAGIC C. `storesDF.groupby.count("division")  `<br>
# MAGIC D. `storesDF.groupBy().count("division") ` <br>
# MAGIC E. `storesDF.groupBy("division").count()`

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:78  
# MAGIC **Which of the following code blocks returns a DataFrame sorted alphabetically based on column division?**  
# MAGIC A. `storesDF.sort("division")`  
# MAGIC B. `storesDF.orderBy(desc("division")) ` <br>
# MAGIC C. `storesDF.orderBy(col("division").desc())  `<br>
# MAGIC D. `storesDF.orderBy("division", ascending = True)`<br>  
# MAGIC E. `storesDF.sort(desc("division"))`

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:79  
# MAGIC **Which of the following code blocks returns a 10 percent sample of rows from DataFrame storesDF with replacement?**  
# MAGIC A. ```storesDF.sample(true)```  
# MAGIC B. ```storesDF.sample(true, fraction = 0.1)```  
# MAGIC C. ```storesDF.sample(true, fraction = 0.15) ``` <br>
# MAGIC D. ```storesDF.sampleBy(fraction = 0.1)  ```<br>
# MAGIC E. ```storesDF.sample(false, fraction = 0.1)```

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:80  
# MAGIC **Which of the following code blocks returns the first 3 rows of DataFrame storesDF?**
# MAGIC
# MAGIC A. storesDF.top_n(3)  
# MAGIC B. storesDF.n(3)  
# MAGIC C. storesDF.take(3)  
# MAGIC D. storesDF.head(3)  
# MAGIC E. storesDF.collect(3)

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:81  
# MAGIC **Which of the following code blocks applies the function assessPerformance() to each row of DataFrame storesDF?**  
# MAGIC A. storesDF.collect.foreach(assessPerformance(row))  
# MAGIC B. storesDF.collect().apply(assessPerformance)  
# MAGIC C. storesDF.collect.apply(row => assessPerformance(row))  
# MAGIC D. storesDF.collect.map(assessPerformance(row))  
# MAGIC E. storesDF.collect.foreach(row => assessPerformance(row))

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:82  
# MAGIC **The code block shown below contains an error. The code block is intended to print the schema of DataFrame storesDF. Identify the error.**  
# MAGIC Code block:  
# MAGIC `storesDF.printSchema.getAs[String]  `<br>
# MAGIC A. There is no printSchema member of DataFrame – the getSchema() operation should be used instead.  
# MAGIC B. There is no printSchema member of DataFrame – the schema() operation should be used instead.  
# MAGIC C. The entire line needs to be a string – it should be wrapped by str().  
# MAGIC D. The printSchema member of DataFrame is an operation that prints the DataFrame – there is no need to call getAs.  
# MAGIC E. There is no printSchema member of DataFrame – schema and the print() function should be used instead.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:83  
# MAGIC **Which of the following code blocks creates and registers a SQL UDF named "ASSESS_PERFORMANCE" using the Scala function assessPerformance() and applies it to column customerSatisfaction in table stores?**  
# MAGIC
# MAGIC A.  
# MAGIC spark.udf.register("ASSESS_PERFORMANCE", assessPerformance)  
# MAGIC spark.sql("SELECT customerSatisfaction, ASSESS_PERFORMANCE(customerSatisfaction) AS result FROM stores")  
# MAGIC
# MAGIC B.  
# MAGIC spark.udf.register("ASSESS_PERFORMANCE", assessPerformance)  
# MAGIC
# MAGIC C.  
# MAGIC spark.udf.register("ASSESS_PERFORMANCE", assessPerformance)  
# MAGIC spark.sql("SELECT customerSatisfaction, assessPerformance(customerSatisfaction) AS result FROM stores")  
# MAGIC
# MAGIC D.  
# MAGIC spark.udf.register("ASSESS_PERFORMANCE", assessPerformance)  
# MAGIC storesDF.withColumn("result", assessPerformance(col("customerSatisfaction")))  
# MAGIC
# MAGIC E.  
# MAGIC spark.udf.register("ASSESS_PERFORMANCE", assessPerformance)  
# MAGIC storesDF.withColumn("result", ASSESS_PERFORMANCE(col("customerSatisfaction")))   

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:84  
# MAGIC **The code block shown below should use SQL to return a new DataFrame containing column storeId and column managerName from a table created from DataFrame storesDF. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**  
# MAGIC
# MAGIC Code block:  
# MAGIC `__1__.__2__("stores")`  
# MAGIC `__3__.__4__("SELECT storeId, managerName FROM stores")`  
# MAGIC
# MAGIC A.  
# MAGIC 1. spark  
# MAGIC 2. createOrReplaceTempView  
# MAGIC 3. storesDF  
# MAGIC 4. query  
# MAGIC
# MAGIC B.  
# MAGIC 1. spark  
# MAGIC 2. createTable  
# MAGIC 3. storesDF  
# MAGIC 4. sql  
# MAGIC
# MAGIC C.  
# MAGIC 1. storesDF  
# MAGIC 2. createOrReplaceTempView  
# MAGIC 3. spark  
# MAGIC 4. query  
# MAGIC
# MAGIC D.  
# MAGIC 1. spark  
# MAGIC 2. createOrReplaceTempView  
# MAGIC 3. storesDF  
# MAGIC 4. sql  
# MAGIC
# MAGIC E.  
# MAGIC 1. storesDF  
# MAGIC 2. createOrReplaceTempView  
# MAGIC 3. spark  
# MAGIC 4. sql

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:85  
# MAGIC **The code block shown below contains an error. The code block is intended to create a single-column DataFrame from Scala List years which is made up of integers. Identify the error.** 
# MAGIC
# MAGIC Code block:  
# MAGIC `spark.createDataset(years)`  
# MAGIC
# MAGIC A. The years list should be wrapped in another list like List(years) to make clear that it is a column rather than a row.  
# MAGIC B. The data type is not specified – the second argument to createDataset should be IntegerType.  
# MAGIC C. There is no operation createDataset – the createDataFrame operation should be used instead.  
# MAGIC D. The result of the above is a Dataset rather than a DataFrame – the toDF operation must be called at the end.  
# MAGIC E. The column name must be specified as the second argument to createDataset.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #:86  
# MAGIC **Which of the following code blocks will always return a new 4-partition DataFrame from the 8-partition DataFrame storesDF without inducing a shuffle?**  
# MAGIC
# MAGIC A. storesDF.repartition(4, "sqft")  
# MAGIC B. storesDF.repartition()  
# MAGIC C. storesDF.coalesce(4)  
# MAGIC D. storesDF.repartition(4)  
# MAGIC E. storesDF.coalesce  
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:87  
# MAGIC **The code block shown below should return a new 12-partition DataFrame from DataFrame storesDF. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**  
# MAGIC
# MAGIC Code block:  
# MAGIC `__1__.__2__(__3__) ` 
# MAGIC
# MAGIC A.  
# MAGIC 1. storesDF  
# MAGIC 2. coalesce  
# MAGIC 3. 4  
# MAGIC
# MAGIC B.  
# MAGIC 1. storesDF  
# MAGIC 2. coalesce  
# MAGIC 3. 4, "storeId"  
# MAGIC
# MAGIC C.  
# MAGIC 1. storesDF  
# MAGIC 2. repartition  
# MAGIC 3. "storeId"  
# MAGIC
# MAGIC D.  
# MAGIC 1. storesDF  
# MAGIC 2. repartition  
# MAGIC 3. 12  
# MAGIC
# MAGIC E.  
# MAGIC 1. storesDF  
# MAGIC 2. repartition  
# MAGIC 3. Nothing

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:88  
# MAGIC **The code block shown below contains an error. The code block is intended to adjust the number of partitions used in wide transformations like join() to 32. Identify the error.**  
# MAGIC
# MAGIC Code block:  
# MAGIC `spark.conf.set("spark.default.parallelism", "32")`  
# MAGIC
# MAGIC A. spark.default.parallelism is not the right Spark configuration parameter – spark.sql.shuffle.partitions should be used instead.  
# MAGIC B. There is no way to adjust the number of partitions used in wide transformations – it defaults to the number of total CPUs in the cluster.  
# MAGIC C. Spark configuration parameters cannot be set in runtime.  
# MAGIC D. Spark configuration parameters are not set with spark.conf.set().  
# MAGIC E. The second argument should not be the string version of "32" – it should be the integer 32.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:89  
# MAGIC **The code block shown below contains an error. The code block is intended to return a DataFrame containing a column dayOfYear, an integer representation of the day of the year from column openDate from DataFrame storesDF. Identify the error.**  
# MAGIC Note that column openDate is of type integer and represents a date in the UNIX epoch format – the number of seconds since midnight on January 1st, 1970.  
# MAGIC A sample of storesDF is displayed below:  
# MAGIC ![image_1775624828558.png](./image_1775624828558.png "image_1775624828558.png")
# MAGIC
# MAGIC Code block:  
# MAGIC `storesDF.withColumn("dayOfYear", dayofyear(col("openDate")))`  
# MAGIC
# MAGIC A. The dayofyear() operation cannot extract the day of year from a column of type integer – column openDate must first be converted to type Timestamp.  
# MAGIC B. The dayofyear() operation takes a quoted column name rather than a Column object as its first argument – the first argument should be "openDate".  
# MAGIC C. The dayofyear() operation cannot extract the day of year from a column of type integer – column openDate must first be converted to type Date.  
# MAGIC D. The dayofyear() operation is not applicable in a withColumn() call – the newColumn() operation must be used instead.  
# MAGIC E. There is no dayofyear() operation – the day of year number must be extracted using substring utilities.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:90  
# MAGIC **The code block shown below should return a new DataFrame that is the result of an inner join between DataFrame storesDF and DataFrame employeesDF on column storeId. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**  
# MAGIC
# MAGIC Code block:  
# MAGIC `storesDF.__1__(__2__, __3__, __4__) ` 
# MAGIC
# MAGIC A.  
# MAGIC 1. join  
# MAGIC 2. employeesDF  
# MAGIC 3. "inner"  
# MAGIC 4. storesDF.storeId === employeesDF.storeId  
# MAGIC
# MAGIC B.  
# MAGIC 1. join  
# MAGIC 2. employeesDF  
# MAGIC 3. "storeId"  
# MAGIC 4. "inner"  
# MAGIC
# MAGIC C.  
# MAGIC 1. merge  
# MAGIC 2. employeesDF  
# MAGIC 3. "storeId"  
# MAGIC 4. "inner"  
# MAGIC
# MAGIC D.  
# MAGIC 1. join  
# MAGIC 2. employeesDF  
# MAGIC 3. "inner"  
# MAGIC 4. "storeId"  
# MAGIC
# MAGIC E.  
# MAGIC 1. join  
# MAGIC 2. employeesDF  
# MAGIC 3. "inner"  
# MAGIC 4. "storeId"

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:91  
# MAGIC **The code block shown below should return a new DataFrame that is the result of an outer join between DataFrame storesDF and DataFrame employeesDF on column storeId. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**  
# MAGIC
# MAGIC Code block:  
# MAGIC `storesDF.__1__(__2__, __3__, __4__) ` 
# MAGIC
# MAGIC A.  
# MAGIC 1. join  
# MAGIC 2. employeesDF  
# MAGIC 3. "outer"  
# MAGIC 4. Seq("storeId")  
# MAGIC
# MAGIC B.  
# MAGIC 1. merge  
# MAGIC 2. employeesDF  
# MAGIC 3. "outer"  
# MAGIC 4. Seq("storeId")  
# MAGIC
# MAGIC C.  
# MAGIC 1. join  
# MAGIC 2. employeesDF  
# MAGIC 3. "outer"  
# MAGIC 4. storesDF.storeId === employeesDF.storeId  
# MAGIC
# MAGIC D.  
# MAGIC 1. merge  
# MAGIC 2. employeesDF  
# MAGIC 3. Seq("storeId")  
# MAGIC 4. "outer"  
# MAGIC
# MAGIC E.  
# MAGIC 1. join  
# MAGIC 2. employeesDF  
# MAGIC 3. Seq("storeId")  
# MAGIC 4. "outer"

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:92  
# MAGIC **Which of the following code blocks fails to return a new DataFrame that is the result of an inner join between DataFrame storesDF and DataFrame employeesDF on column storeId and column employeeId?**  
# MAGIC
# MAGIC A. `storesDF.join(employeesDF, Seq(col("storeId"), col("employeeId")))`  
# MAGIC B. `storesDF.join(employeesDF, Seq("storeId", "employeeId"))`  
# MAGIC C. `storesDF.join(employeesDF, storesDF("storeId") === employeesDF("storeId") && storesDF("employeeId") === employeesDF("employeeId"))`  
# MAGIC D. `storesDF.join(employeesDF, Seq("storeId", "employeeId"), "inner")`  
# MAGIC E. `storesDF.alias("s").join(employeesDF.alias("e"), col("s.storeId") === col("e.storeId") && col("s.employeeId") === col("e.employeeId"))`

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:93  
# MAGIC **The code block shown below should efficiently perform a broadcast join of DataFrame storesDF and the much larger DataFrame employeesDF using key column storeId. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**  
# MAGIC
# MAGIC Code block:  
# MAGIC `__1__.join(__2__(__3__), "storeId")`
# MAGIC
# MAGIC A.  
# MAGIC 1. employeesDF  
# MAGIC 2. broadcast  
# MAGIC 3. storesDF  
# MAGIC
# MAGIC B.  
# MAGIC 1. broadcast(employeesDF)  
# MAGIC 2. broadcast  
# MAGIC 3. storesDF  
# MAGIC
# MAGIC C.  
# MAGIC 1. broadcast  
# MAGIC 2. employeesDF  
# MAGIC 3. storesDF  
# MAGIC
# MAGIC D.  
# MAGIC 1. storesDF  
# MAGIC 2. broadcast  
# MAGIC 3. employeesDF  
# MAGIC
# MAGIC E.  
# MAGIC 1. broadcast(storesDF)  
# MAGIC 2. broadcast  
# MAGIC 3. employeesDF

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:94  
# MAGIC **Which of the following operations performs a cross join on two DataFrames?**  
# MAGIC A. DataFrame.join()  
# MAGIC B. The standalone join() function  
# MAGIC C. The standalone crossJoin() function  
# MAGIC D. DataFrame.crossJoin()  
# MAGIC E. DataFrame.merge()

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:95  
# MAGIC **Which of the following code blocks writes DataFrame storesDF to file path filePath as CSV?**  
# MAGIC A. storesDF.write().csv(filePath)  
# MAGIC B. storesDF.write(filePath)  
# MAGIC C. storesDF.write.csv(filePath)  
# MAGIC D. storesDF.write.option("csv").path(filePath)  
# MAGIC E. storesDF.write.path(filePath)

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:96  
# MAGIC **Which of the following code blocks writes DataFrame storesDF to file path filePath as parquet and partitions by values in column division?**  
# MAGIC
# MAGIC A. storesDF.write.partitionBy(col("division")).path(filePath)  
# MAGIC B. storesDF.write.option("parquet").partitionBy("division").path(filePath)  
# MAGIC C. storesDF.write.option("parquet").partitionBy(col("division")).path(filePath)  
# MAGIC D. storesDF.write.partitionBy("division").parquet(filePath)  
# MAGIC E. storesDF.write().partitionBy("division").parquet(filePath)  
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Question #:97
# MAGIC
# MAGIC **Of the following, which is the coarsest level in the Spark execution hierarchy?**
# MAGIC
# MAGIC A. Slot  
# MAGIC B. Job  
# MAGIC C. Task  
# MAGIC D. Stage  
# MAGIC E. Executor

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:98  
# MAGIC **Which of the following statements about slots is incorrect?**  
# MAGIC
# MAGIC A. Slots are the most granular level of execution in the Spark execution hierarchy.  
# MAGIC B. Slots are resources for parallelization within an executor.  
# MAGIC C. Tasks are assigned to slots for computation.  
# MAGIC D. There can be more slots than tasks.  
# MAGIC E. There must be at least as many slots as there are executors.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:99  
# MAGIC **Which of the following code blocks returns a new DataFrame from DataFrame storesDF with no duplicate rows?**  
# MAGIC A. storesDF.removeDuplicates()  
# MAGIC B. storesDF.getDistinct()  
# MAGIC C. storesDF.duplicates.drop()  
# MAGIC D. storesDF.duplicates()  
# MAGIC E. storesDF.dropDuplicates()

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:100  
# MAGIC **The code block shown below contains an error. The code block is intended to return the exact number of distinct values in column division in DataFrame storesDF. Identify the error.**  
# MAGIC
# MAGIC Code block:  
# MAGIC `storesDF.agg(approx_count_distinct(col("division")).alias("divisionDistinct"))`  
# MAGIC
# MAGIC A. The approx_count_distinct() operation needs a second argument to set the rsd parameter to ensure it returns the exact number of distinct values.  
# MAGIC B. There is no alias() operation for the approx_count_distinct() operation's output.  
# MAGIC C. There is no way to return an exact distinct number in Spark because the data is distributed across partitions.  
# MAGIC D. The approx_count_distinct() operation is not a standalone function - it should be used as a method from a Column object.  
# MAGIC E. The approx_count_distinct() operation cannot determine an exact number of distinct values in a column.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:101  
# MAGIC **Which of the following code blocks returns the number of rows in DataFrame storesDF for each distinct combination of values in column division and column storeCategory?**  
# MAGIC A. storesDF.groupBy(Seq(col("division"), col("storeCategory"))).count()  
# MAGIC B. storesDF.groupBy(division, storeCategory).count()  
# MAGIC C. storesDF.groupBy("division", "storeCategory").count()  
# MAGIC D. storesDF.groupBy("division").groupBy("storeCategory").count()  
# MAGIC E. storesDF.groupBy(Seq("division", "storeCategory")).count()

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:102  
# MAGIC **The code block shown below contains an error. The code block is intended to return a collection of summary statistics for column sqft in DataFrame storesDF. Identify the error.**  
# MAGIC Code block:  
# MAGIC `storesDF.describes(col("sgft"))`  
# MAGIC
# MAGIC A. The column sqft should be subsetted from DataFrame storesDF prior to computing summary statistics on it alone.  
# MAGIC B. The describe() operation does not accept a Column object as an argument outside of a sequence — the sequence Seq(col("sqft")) should be specified instead.  
# MAGIC C. The describe() operation doesn’t compute summary statistics for a single column — the summary() operation should be used instead.  
# MAGIC D. The describe() operation doesn't compute summary statistics for numeric columns — the summary() operation should be used instead.  
# MAGIC E. The describe() operation does not accept a Column object as an argument — the column name string "sqft" should be specified instead.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:103  
# MAGIC **The code block shown below should extract the integer value for column sqft from the first row of DataFrame storesDF. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**
# MAGIC
# MAGIC Code block:  
# MAGIC ```__1__.__2__.__3__[Int](__4__)  ```
# MAGIC
# MAGIC A.  
# MAGIC 1. storesDF  
# MAGIC 2. first()  
# MAGIC 3. getAs()  
# MAGIC 4. "sqft"  
# MAGIC
# MAGIC B.  
# MAGIC 1. storesDF  
# MAGIC 2. first  
# MAGIC 3. getAs  
# MAGIC 4. sqft  
# MAGIC
# MAGIC C.  
# MAGIC 1. storesDF  
# MAGIC 2. first()  
# MAGIC 3. getAs  
# MAGIC 4. col("sqft")  
# MAGIC
# MAGIC D.  
# MAGIC 1. storesDF  
# MAGIC 2. first  
# MAGIC 3. getAs  
# MAGIC 4. "sqft"  

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:104  
# MAGIC The code block shown below should print the schema of DataFrame storesDF. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.  
# MAGIC
# MAGIC Code block:  
# MAGIC ```__1__.__2__ ``` 
# MAGIC
# MAGIC A.  
# MAGIC 1. storesDF  
# MAGIC 2. printSchema("all")  
# MAGIC
# MAGIC B.  
# MAGIC 1. storesDF  
# MAGIC 2. schema  
# MAGIC
# MAGIC C.  
# MAGIC 1. storesDF  
# MAGIC 2. getAs[str]  
# MAGIC
# MAGIC D.  
# MAGIC 1. storesDF  
# MAGIC 2. printSchema(true)  
# MAGIC
# MAGIC E.  
# MAGIC 1. storesDF  
# MAGIC 2. printSchema

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:105  
# MAGIC **The code block shown below contains an error. The code block is intended to create and register a SQL UDF named “ASSESS_PERFORMANCE” using the Scala function assessPerformance() and apply it to column customerSatisfaction in the table stores. Identify the error.**  
# MAGIC Code block:  
# MAGIC
# MAGIC ```python
# MAGIC spark.udf.register("ASSESS_PERFORMANCE", assessPerforance) 
# MAGIC spark.sql("SELECT customerSatisfaction, assessPerformance(customerSatisfaction) AS result FROM stores")
# MAGIC ``` 
# MAGIC
# MAGIC A. The customerSatisfaction column cannot be called twice inside the SQL statement.  
# MAGIC B. Registered UDFs cannot be applied inside of a SQL statement.  
# MAGIC C. The order of the arguments to spark.udf.register() should be reversed.  
# MAGIC D. The wrong SQL function is used to compute column result - it should be ASSESS_PERFORMANCE instead of assessPerformance.  
# MAGIC E. There is no sql() operation - the DataFrame API must be used to apply the UDF assessPerformance().

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:106  
# MAGIC **The code block shown below contains an error. The code block is intended to create the Scala UDF assessPerformanceUDF() and apply it to the integer column customerSatisfaction in DataFrame storesDF. Identify the error.**  
# MAGIC
# MAGIC Code block:  
# MAGIC ![image_1775650701397.png](./image_1775650701397.png "image_1775650701397.png")
# MAGIC
# MAGIC A. The input type of customerSatisfaction is not specified in the udf() operation.  
# MAGIC B. The return type of assessPerformanceUDF() must be specified.  
# MAGIC C. The withColumn() operation is not appropriate here - UDFs should be applied by iterating over rows instead.  
# MAGIC D. The assessPerformanceUDF() must first be defined as a Scala function and then converted to a UDF.  
# MAGIC E. UDFs can only be applied via SQL and not through the Data Frame API.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:107  
# MAGIC **The code block shown below should create a single-column DataFrame from Scala list years which is made up of integers. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**  
# MAGIC
# MAGIC Code block:  
# MAGIC ```__1__.__2__(__3__).__4__```  
# MAGIC
# MAGIC A.  
# MAGIC 1. spark  
# MAGIC 2. createDataFrame  
# MAGIC 3. years  
# MAGIC 4. IntegerType  
# MAGIC
# MAGIC B.  
# MAGIC 1. spark  
# MAGIC 2. createDataset  
# MAGIC 3. years  
# MAGIC 4. IntegerType  
# MAGIC
# MAGIC C.  
# MAGIC 1. spark  
# MAGIC 2. createDataset  
# MAGIC 3. List(years)  
# MAGIC 4. toDF  
# MAGIC
# MAGIC D.  
# MAGIC 1. spark  
# MAGIC 2. createDataFrame  
# MAGIC 3. List(years)  
# MAGIC 4. IntegerType
# MAGIC
# MAGIC `--need to test again`

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:108  
# MAGIC The code block shown below should cache DataFrame `storesDF` only in Spark's memory. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.
# MAGIC
# MAGIC Code block:  
# MAGIC ```__1__.__2__(__3__).count()```
# MAGIC
# MAGIC A.  
# MAGIC 1. storesDF  
# MAGIC 2. cache  
# MAGIC 3. StorageLevel.MEMORY_ONLY  
# MAGIC
# MAGIC B.  
# MAGIC 1. storesDF  
# MAGIC 2. storageLevel  
# MAGIC 3. cache  
# MAGIC
# MAGIC C.  
# MAGIC 1. storesDF  
# MAGIC 2. cache  
# MAGIC 3. Nothing  
# MAGIC
# MAGIC D.  
# MAGIC 1. storesDF  
# MAGIC 2. persist  
# MAGIC 3. Nothing  
# MAGIC
# MAGIC E.  
# MAGIC 1. storesDF  
# MAGIC 2. persist  
# MAGIC 3. StorageLevel.MEMORY_ONLY

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:109  
# MAGIC **Which of the following code blocks returns a DataFrame containing a column month, an integer representation of the day of the year from column openDate from DataFrame storesDF?**  
# MAGIC **Note that column openDate is of type integer and represents a date in the UNIX epoch format – the number of seconds since midnight on January 1st, 1970.**  
# MAGIC **A sample of storesDF is displayed below:**  
# MAGIC ![](/Workspace/Users/tayarani.amir@gmail.com/Screenshot 2026-03-30 171205.png)<br>
# MAGIC Code block:  
# MAGIC ```python 
# MAGIC stored.withColumn("openTimestamp", col("openDate").cast(__1__))  
# MAGIC .withColumn(__2__, __3__(__4__))  
# MAGIC ```
# MAGIC A.  
# MAGIC 1. "Data"  
# MAGIC 2. month  
# MAGIC 3. "month"  
# MAGIC 4. "openTimestamp"  
# MAGIC
# MAGIC B.  
# MAGIC 1. "Timestamp"  
# MAGIC 2. month  
# MAGIC 3. "month"  
# MAGIC 4. col("openTimestamp")  
# MAGIC
# MAGIC C.  
# MAGIC 1. "Timestamp"  
# MAGIC 2. month  
# MAGIC 3. getMonth  
# MAGIC 4. col("openTimestamp")  
# MAGIC
# MAGIC D.  
# MAGIC 1. "Timestamp"  
# MAGIC 2. "month"  
# MAGIC 3. month  
# MAGIC 4. col("openTimestamp")

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:110  
# MAGIC **The code block shown below contains an error. The code block is intended to return a new DataFrame that is the result of an inner join between DataFrame storesDF and DataFrame employeesDF on column storeId. Identify the error.**  
# MAGIC
# MAGIC Code block:  
# MAGIC `StoresDF.join(employeesDF, Seq("storeId")`  
# MAGIC
# MAGIC A. The key column storeId needs to be a string like “storeId”.  
# MAGIC B. The key column storeId needs to be specified in an expression of both Data Frame columns like `storesDF.storeId === employeesDF.storeId`.  
# MAGIC C. The default argument to the joinType parameter is “inner” - an additional argument of “left” must be specified.  
# MAGIC D. There is no DataFrame.join() operation - DataFrame.merge() should be used instead.  
# MAGIC E. The key column storeId needs to be wrapped in the col() operation.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:111  
# MAGIC **Which of the following pairs of arguments cannot be used in DataFrame.join() to perform an inner join on two DataFrames, named and aliased with "a" and "b" respectively, to specify two key columns column1 and column2?**  
# MAGIC
# MAGIC A. `joinExprs = col("a.column1") === col("b.column1") and col("a.column2") === col("b.column2")`  
# MAGIC B. `usingColumns = Seq(col("column1"), col("column2"))`  
# MAGIC C. All of these options can be used to perform an inner join with two key columns.  
# MAGIC D. `joinExprs = storesDF("column1") === employeesDF("column1") and storesDF("column2") === employeesDF("column2")`  
# MAGIC E. `usingColumns = Seq("column1", "column2")`

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:112  
# MAGIC **The code block shown below contains an error. The code block is intended to return a new DataFrame that is the result of a position-wise union between DataFrame storesDF and DataFrame acquiredStoresDF.**  
# MAGIC
# MAGIC A. `concat(storesDF, acquiredStoresDF)`  
# MAGIC B. `storesDF.unionByName(acquiredStoresDF)`  
# MAGIC C. `union(storesDF, acquiredStoresDF)`  
# MAGIC D. `unionAll(storesDF, acquiredStoresDF)`  
# MAGIC E. `storesDF.union(acquiredStoresDF)`

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:113  
# MAGIC **Which of the following code blocks writes DataFrame storesDF to file path filePath as parquet, overwriting any existing files in that location?**
# MAGIC
# MAGIC A. `storesDF.write(filePath, mode = "overwrite")`  
# MAGIC B. `storesDF.write().mode("overwrite").parquet(filePath)`  
# MAGIC C. `storesDF.write.mode("overwrite").parquet(filePath)`  
# MAGIC D. `storesDF.write.option("parquet", "overwrite").path(filePath)`  
# MAGIC E. `storesDF.write.mode("overwrite").path(filePath)`

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:114  
# MAGIC Which of the following code blocks reads a CSV at the file path `filePath` into a DataFrame with the specified schema `schema`?
# MAGIC
# MAGIC A. `spark.read().csv(filePath)`  
# MAGIC B. `spark.read().schema("schema").csv(filePath)`  
# MAGIC C. `spark.read.schema(schema).csv(filePath)`  
# MAGIC D. `spark.read.schema("schema").csv(filePath)`  
# MAGIC E. `spark.read().schema(schema).csv(filePath)`

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:115  
# MAGIC Which of the following code blocks returns a DataFrame containing only the rows from DataFrame `storesDF` where the value in column `sqft` is less than or equal to 25,000 **AND** the value in column `customerSatisfaction` is greater than or equal to 30?
# MAGIC
# MAGIC A. `storesDF.filter(col("sqft") <= 25000 and col("customerSatisfaction") >= 30)`  
# MAGIC B. `storesDF.filter(col("sqft") <= 25000 or col("customerSatisfaction") >= 30)`  
# MAGIC C. `storesDF.filter(sqft) <= 25000 and customerSatisfaction >= 30)`  
# MAGIC D. `storesDF.filter(col("sqft") <= 25000 & col("customerSatisfaction") >= 30)`  
# MAGIC E. `storesDF.filter(sqft <= 25000) & customerSatisfaction >= 30)`
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:116  
# MAGIC **Which of the following sets of DataFrame methods will both return a new DataFrame only containing rows that meet a specified logical condition?**  
# MAGIC A. drop(), where()  
# MAGIC B. filter(), select()  
# MAGIC C. filter(), where()  
# MAGIC D. select(), where()  
# MAGIC E. filter(), drop()

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:117  
# MAGIC **The code block shown below should return a DataFrame containing all columns from DataFrame `storesDF` except for column `sqft` and column `customerSatisfaction`.**  
# MAGIC **Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**  
# MAGIC
# MAGIC Code block:  
# MAGIC `__1__.__2__(__3__)`  
# MAGIC
# MAGIC A.  
# MAGIC 1. drop  
# MAGIC 2. storesDF  
# MAGIC 3. col("sqft"), col("customerSatisfaction")  
# MAGIC
# MAGIC B.  
# MAGIC 1. storesDF  
# MAGIC 2. drop  
# MAGIC 3. sqft, customerSatisfaction  
# MAGIC
# MAGIC C.  
# MAGIC 1. storesDF  
# MAGIC 2. drop  
# MAGIC 3. "sqft", "customerSatisfaction"  
# MAGIC
# MAGIC D.  
# MAGIC 1. storesDF  
# MAGIC 2. drop  
# MAGIC 3. col(sqft), col(customerSatisfaction)  
# MAGIC
# MAGIC E.  
# MAGIC 1. drop  
# MAGIC 2. storesDF  
# MAGIC 3. col(sqft), col(customerSatisfaction)

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:118  
# MAGIC **Which of the following describes the difference between `DataFrame.repartition(n)` and `DataFrame.coalesce(n)`?**  
# MAGIC
# MAGIC A.  
# MAGIC `DataFrame.repartition(n)` will split a DataFrame into *n* number of new partitions with data distributed evenly.  
# MAGIC `DataFrame.coalesce(n)` will more quickly combine the existing partitions of a DataFrame but might result in an uneven distribution of data across the new partitions.  
# MAGIC
# MAGIC B.  
# MAGIC While the results are similar, `DataFrame.repartition(n)` will be more efficient than `DataFrame.coalesce(n)` because it can partition a DataFrame by the column.  
# MAGIC
# MAGIC C.  
# MAGIC `DataFrame.repartition(n)` will split a DataFrame into any number of new partitions while minimizing shuffling.  
# MAGIC `DataFrame.coalesce(n)` will split a DataFrame onto any number of new partitions utilizing a full shuffle.  
# MAGIC
# MAGIC D.  
# MAGIC While the results are similar, `DataFrame.repartition(n)` will be less efficient than `DataFrame.coalesce(n)` because it can partition a DataFrame by the column.  
# MAGIC
# MAGIC E.  
# MAGIC `DataFrame.repartition(n)` will combine the existing partitions of a DataFrame but may result in an uneven distribution of data across the new partitions.  
# MAGIC `DataFrame.coalesce(n)` will more slowly split a DataFrame into *n* number of new partitions with data distributed evenly.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:119  
# MAGIC **Which of the following cluster configurations is most likely to experience delays due to garbage collection of a large DataFrame?**  
# MAGIC ![](/Workspace/Users/tayarani.amir@gmail.com/Screenshot%202026-03-30%20172933.png)  
# MAGIC **Note:** Each configuration has roughly the same compute power using 100GB of RAM and 200 cores.
# MAGIC
# MAGIC A. More information is needed to determine an answer.  
# MAGIC B. Scenario #5  
# MAGIC C. Scenario #4  
# MAGIC D. Scenario #1  
# MAGIC E. Scenario #2

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:120  
# MAGIC **Which of the following DataFrame operations is classified as a transformation?**  
# MAGIC
# MAGIC A. `DataFrame.select()`  
# MAGIC B. `DataFrame.count()`  
# MAGIC C. `DataFrame.show()`  
# MAGIC D. `DataFrame.first()`  
# MAGIC E. `DataFrame.collect()`

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:121  
# MAGIC **Which of the following operations will fail to trigger evaluation?**  
# MAGIC
# MAGIC A. `DataFrame.collect()`  
# MAGIC B. `DataFrame.count()`  
# MAGIC C. `DataFrame.first()`  
# MAGIC D. `DataFrame.join()`  
# MAGIC E. `DataFrame.take()`

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:122  
# MAGIC The code block shown below should read a JSON at the file path `filePath` into a DataFrame with the specified schema `schema`. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.  
# MAGIC
# MAGIC Code block:  
# MAGIC `__1__.__2__.__3__(__4__).format("csv").__5__(__6__)`  
# MAGIC
# MAGIC A.  
# MAGIC 1. spark  
# MAGIC 2. read()  
# MAGIC 3. schema  
# MAGIC 4. schema  
# MAGIC 5. json  
# MAGIC 6. filePath  
# MAGIC
# MAGIC B.  
# MAGIC 1. spark  
# MAGIC 2. read()  
# MAGIC 3. json  
# MAGIC 4. filePath  
# MAGIC 5. format  
# MAGIC 6. schema  
# MAGIC
# MAGIC C.  
# MAGIC 1. spark  
# MAGIC 2. read()  
# MAGIC 3. schema  
# MAGIC 4. schema  
# MAGIC 5. load  
# MAGIC 6. filePath  
# MAGIC
# MAGIC D.  
# MAGIC 1. spark  
# MAGIC 2. read  
# MAGIC 3. schema  
# MAGIC 4. schema  
# MAGIC 5. load  
# MAGIC 6. filePath  
# MAGIC
# MAGIC E.  
# MAGIC 1. spark  
# MAGIC 2. read  
# MAGIC 3. format  
# MAGIC 4. "json"  
# MAGIC 5. load  
# MAGIC 6. filePath

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:123  
# MAGIC **Which of the following code blocks returns a new DataFrame with a new column** **`customerSatisfactionAbs` that is the absolute value of column `customerSatisfaction` in DataFrame `storesDF`? ** 
# MAGIC **Note that column `customerSatisfactionAbs` is not in the original DataFrame `storesDF`.**
# MAGIC
# MAGIC A. `storesDF.withColumn("customerSatisfactionAbs", abs(col("customerSatisfaction")))`  
# MAGIC B. `storesDF.withColumnRenamed("customerSatisfactionAbs", abs(col("customerSatisfaction")))`  
# MAGIC C. `storesDF.withColumn(col("customerSatisfactionAbs", abs(col("customerSatisfaction")))`  
# MAGIC D. `storesDF.withColumn("customerSatisfactionAbs", abs(col(customerSatisfaction)))`  
# MAGIC E. `storesDF.withColumn("customerSatisfactionAbs", abs("customerSatisfaction"))`

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:124  
# MAGIC **Which of the following statements about the Spark driver is true?**  
# MAGIC
# MAGIC A. Spark driver is horizontally scaled to increase overall processing throughput.  
# MAGIC B. Spark driver is the most coarse level of the Spark execution hierarchy.  
# MAGIC C. Spark driver is fault tolerant — if it fails, it will recover the entire Spark application.  
# MAGIC D. Spark driver is responsible for scheduling the execution of data by various worker nodes in cluster mode.  
# MAGIC E. Spark driver is only compatible with its included cluster manager.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:125  
# MAGIC The code block shown below should write DataFrame `storesDF` to file path `filePath` as parquet and partition by values in column `division`.  
# MAGIC Choose the response that correctly fills in the numbered blanks within the code block to complete this task.  
# MAGIC
# MAGIC Code block:  
# MAGIC `storesDF.__1__.__2__(__3__).__4__(__5__)`
# MAGIC
# MAGIC A.  
# MAGIC 1. write  
# MAGIC 2. partitionBy  
# MAGIC 3. "division"  
# MAGIC 4. path  
# MAGIC 5. filePath, node = parquet  
# MAGIC
# MAGIC B.  
# MAGIC 1. write  
# MAGIC 2. partitionBy  
# MAGIC 3. "division"  
# MAGIC 4. parquet  
# MAGIC 5. filePath  
# MAGIC
# MAGIC C.  
# MAGIC 1. write  
# MAGIC 2. partitionBy  
# MAGIC 3. col("division")  
# MAGIC 4. parquet  
# MAGIC 5. filePath  
# MAGIC
# MAGIC D.  
# MAGIC 1. write()  
# MAGIC 2. partitionBy  
# MAGIC 3. col("division")  
# MAGIC 4. parquet  
# MAGIC 5. filePath  
# MAGIC
# MAGIC E.  
# MAGIC 1. write  
# MAGIC 2. repartition  
# MAGIC 3. "division"  
# MAGIC 4. path  
# MAGIC 5. filePath, mode = "parquet"

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:126  
# MAGIC **Which of the following types of processes induces a stage boundary?**
# MAGIC
# MAGIC A. Shuffle  
# MAGIC B. Caching  
# MAGIC C. Executor failure  
# MAGIC D. Job delegation  
# MAGIC E. Application failure

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:127  
# MAGIC **Which of the following cluster configurations will induce the least network traffic during a shuffle operation?**  
# MAGIC ![](/Workspace/Users/tayarani.amir@gmail.com/Screenshot 2026-03-30 172933.png)
# MAGIC **Note:** Each configuration has roughly the same compute power using 100GB of RAM and 200 cores.
# MAGIC
# MAGIC A. This cannot be determined without knowing the number of partitions.  
# MAGIC B. Scenario 5  
# MAGIC C. Scenario 1  
# MAGIC D. Scenario 4  
# MAGIC E. Scenario 6

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:128  
# MAGIC **Which of the following describes a partition?**  
# MAGIC
# MAGIC A. A partition is the amount of data that fits in a single executor.  
# MAGIC B. A partition is an automatically-sized segment of data that is used to create efficient logical plans.  
# MAGIC C. A partition is the amount of data that fits on a single worker node.  
# MAGIC D. A partition is a portion of a Spark application that is made up of similar jobs.  
# MAGIC E. A partition is a collection of rows of data that fit on a single machine in a cluster.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #:129  
# MAGIC **Which of the following identifies multiple narrow operations that are executed in sequence?**
# MAGIC
# MAGIC A. Slot  
# MAGIC B. Job  
# MAGIC C. Stage  
# MAGIC D. Task  
# MAGIC E. Executor

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:130  
# MAGIC
# MAGIC **Spark's execution/deployment mode determines where the driver and executors are physically located when a Spark application is run.**  
# MAGIC **Which of the following Spark execution/deployment modes does **not** exist? If they all exist, please indicate so with Response E.**
# MAGIC
# MAGIC A. Client mode  
# MAGIC B. Cluster mode  
# MAGIC C. Standard mode  
# MAGIC D. Local mode  
# MAGIC E. All of these execution/deployment modes exist

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:131 <br>
# MAGIC **Which of the following will cause a Spark job to fail?** <br>
# MAGIC A. Never pulling any amount of data onto the driver node. <br>
# MAGIC B. Trying to cache data larger than an executor's memory. <br>
# MAGIC C. Data needing to spill from memory to disk. <br>
# MAGIC D. A failed worker node. <br>
# MAGIC E. A failed driver node.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:132  
# MAGIC **Which of the following best describes the similarities and differences between the MEMORY_ONLY storage level and the MEMORY_AND_DISK storage level?**
# MAGIC
# MAGIC A. The MEMORY_ONLY storage level will store as much data as possible in memory and will store any data that does not fit in memory on disk and read it as it's called.  
# MAGIC The MEMORY_AND_DISK storage level will store as much data as possible in memory and will recompute any data that does not fit in memory as it’s called.
# MAGIC
# MAGIC B. The MEMORY_ONLY storage level will store as much data as possible in memory on two cluster nodes and will recompute any data that does not fit in memory as it’s called.  
# MAGIC The MEMORY_AND_DISK storage level will store as much data as possible in memory on two cluster nodes and will store any data that does not fit in memory on disk and read it as it's called.
# MAGIC
# MAGIC C. The MEMORY_ONLY storage level will store as much data as possible in memory on two cluster nodes and will store any data that does not fit in memory on disk and read it as it's called.  
# MAGIC The MEMORY_AND_DISK storage level will store as much data as possible in memory on two cluster nodes and will recompute any data that does not fit in memory as it's called.
# MAGIC
# MAGIC D. The MEMORY_ONLY storage level will store as much data as possible in memory and will recompute any data that does not fit in memory as it's called.  
# MAGIC The MEMORY_AND_DISK storage level will store as much data as possible in memory and will store any data that does not fit in memory on disk and read it as it's called.
# MAGIC
# MAGIC E. The MEMORY_ONLY storage level will store as much data as possible in memory and will recompute any data that does not fit in memory as it’s called.  
# MAGIC The MEMORY_AND_DISK storage level will store half of the data in memory and store half of the memory on disk. This provides quick preview and better logical plan design.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:133  
# MAGIC **Which of the following Spark properties is used to configure whether DataFrames found to be below a certain size threshold at runtime will be automatically broadcasted?**
# MAGIC
# MAGIC A. `spark.sql.broadcastTimeout`  
# MAGIC B. `spark.sql.autoBroadcastJoinThreshold`  
# MAGIC C. `spark.sql.shuffle.partitions`  
# MAGIC D. `spark.sql.inMemoryColumnarStorage.batchSize`  
# MAGIC E. `spark.sql.adaptive.localShuffleReader.enabled`
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:134  
# MAGIC **The code block shown below contains an error. The code block is intended to return a new DataFrame from DataFrame `storesDF` where column `storeId` is of the type string. Identify the error.**
# MAGIC
# MAGIC Code block:  
# MAGIC `storesDF.withColumn("storeId", cast(col("storeId"), StringType()))`
# MAGIC
# MAGIC A. Calls to `withColumn()` cannot create a new column of the same name on which it is operating.  
# MAGIC B. DataFrame columns cannot be converted to a new type inside of a call to `withColumn()`.  
# MAGIC C. The call to `StringType` should not be followed by parentheses.  
# MAGIC D. The column name `storeId` inside the `col()` operation should not be quoted.  
# MAGIC E. The `cast()` operation is a method in the `Column` class rather than a standalone function.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:135  
# MAGIC **Which of the following code blocks returns a new DataFrame where column `division` is the first two characters of column `division` in DataFrame `storesDF`?**  
# MAGIC
# MAGIC A. `storesDF.withColumn("division", substr(col("division"), 0, 2))`  
# MAGIC B. `storesDF.withColumn("division", susbtr(col("division"), 1, 2))`  
# MAGIC C. `storesDF.withColumn("division", col("division").substr(0, 3))`  
# MAGIC D. `storesDF.withColumn("division", col("division").substr(0, 2))`  
# MAGIC E. `storesDF.withColumn("division", col("division").substr(1, 2))`

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:136  
# MAGIC The code block shown below should return a new DataFrame where column `division` from DataFrame `storesDF` has been renamed to column `state` and column `managerName` from DataFrame `storesDF` has been renamed to column `managerFullName`.  
# MAGIC Choose the response that correctly fills in the numbered blanks within the code block to complete this task.  
# MAGIC
# MAGIC Code block:  
# MAGIC `storesDF.__1__(__2__, __3__).__4__(__5__, __6__)`  
# MAGIC
# MAGIC A.  
# MAGIC 1. withColumnRenamed  
# MAGIC 2. "state"  
# MAGIC 3. "division"  
# MAGIC 4. withColumnRenamed  
# MAGIC 5. "managerFullName"  
# MAGIC 6. "managerName"  
# MAGIC
# MAGIC B.  
# MAGIC 1. withColumnRenamed  
# MAGIC 2. division  
# MAGIC 3. col("state")  
# MAGIC 4. withColumnRenamed  
# MAGIC 5. "managerName"  
# MAGIC 6. col("managerFullName")  
# MAGIC
# MAGIC C.  
# MAGIC 1. WithColumnRenamed  
# MAGIC 2. "division"  
# MAGIC 3. "state"  
# MAGIC 4. withColumnRenamed  
# MAGIC 5. "managerName"  
# MAGIC 6. "managerFullName"  
# MAGIC
# MAGIC D.  
# MAGIC 1. withColumn  
# MAGIC 2. "division"  
# MAGIC 3. "state"  
# MAGIC 4. withColumn  
# MAGIC 5. "managerName"  
# MAGIC 6. "managerFullName"  
# MAGIC
# MAGIC E.  
# MAGIC 1. withColumn  
# MAGIC 2. "division"  
# MAGIC 3. "state"  
# MAGIC 4. withColumn  
# MAGIC 5. "managerName"  
# MAGIC 6. "managerFullName"

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:137  
# MAGIC The code block shown below should return a new DataFrame where rows in DataFrame `storesDF` with missing values in every column have been dropped.  
# MAGIC Choose the response that correctly fills in the numbered blanks within the code block to complete this task.  
# MAGIC
# MAGIC Code block:  
# MAGIC `storesDF.__1__.__2__(__3__ = __4__)`  
# MAGIC
# MAGIC A.  
# MAGIC 1. na  
# MAGIC 2. drop  
# MAGIC 3. how  
# MAGIC 4. "any"  
# MAGIC
# MAGIC B.  
# MAGIC 1. na  
# MAGIC 2. drop  
# MAGIC 3. subset  
# MAGIC 4. "all"  
# MAGIC
# MAGIC C.  
# MAGIC 1. na  
# MAGIC 2. drop  
# MAGIC 3. subset  
# MAGIC 4. "any"  
# MAGIC
# MAGIC D.  
# MAGIC 1. na  
# MAGIC 2. drop  
# MAGIC 3. how  
# MAGIC 4. "all"  
# MAGIC
# MAGIC E.  
# MAGIC 1. drop  
# MAGIC 2. na  
# MAGIC 3. how  
# MAGIC 4. "all"

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:138  
# MAGIC **The code block shown below should return a collection of summary statistics for column `sqft` in DataFrame `storesDF`.**  
# MAGIC Choose the response that correctly fills in the numbered blanks within the code block to complete this task.  
# MAGIC
# MAGIC Code block:  
# MAGIC `storesDF.__1__(__2__)`  
# MAGIC
# MAGIC A.  
# MAGIC 1. summary  
# MAGIC 2. col("sqft")  
# MAGIC
# MAGIC B.  
# MAGIC 1. describe  
# MAGIC 2. col("sqft")  
# MAGIC
# MAGIC C.  
# MAGIC 1. summary  
# MAGIC 2. "sqft"  
# MAGIC
# MAGIC D.  
# MAGIC 1. describe  
# MAGIC 2. "sqft"  
# MAGIC
# MAGIC E.  
# MAGIC 1. summary  
# MAGIC 2. "all"

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:139</br>
# MAGIC **Which of the following code blocks returns a 15 percent sample of rows from DataFrame
# MAGIC storesDF without replacement?**</br>
# MAGIC A. storesDF.sample(True, fraction = 0.15)</br>
# MAGIC B. storesDF.sample(fraction = 0.15)</br>
# MAGIC C. storesDF.sampleBy(fraction = 0.15)</br>
# MAGIC D. storesDF.sample(fraction = 0.10)</br>
# MAGIC E. storesDF.sample()</br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:140  
# MAGIC **Which of the following code blocks extracts the value for column sqft from the first row of DataFrame storesDF?**<br>
# MAGIC A. storesDF.first()[col("sqft")]  
# MAGIC B. storesDF[0]["sqft"]  
# MAGIC C. storesDF.collect(1)[0]["sqft"]  
# MAGIC D. storesDF.first.sqft  
# MAGIC E. storesDF.first().sqft

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:141  
# MAGIC **Which of the following code blocks uses SQL to return a new DataFrame containing column `storeId` and column `managerName` from a table created from DataFrame `storesDF`?**
# MAGIC
# MAGIC A.  
# MAGIC storesDF.createOrReplaceTempView()  
# MAGIC spark.sql("SELECT storeId, managerName FROM stores")  
# MAGIC
# MAGIC B.  
# MAGIC storesDF.query("SELECT storeid, managerName from stores")  
# MAGIC
# MAGIC C.  
# MAGIC spark.createOrReplaceTempView("storesDF")  
# MAGIC storesDF.sql("SELECT storeId, managerName from stores")  
# MAGIC
# MAGIC D.  
# MAGIC storesDF.createOrReplaceTempView("stores")  
# MAGIC spark.sql("SELECT storeId, managerName FROM stores")  
# MAGIC
# MAGIC E.  
# MAGIC storesDF.createOrReplaceTempView("stores")  
# MAGIC storesDF.query("SELECT storeId, managerName FROM stores")

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:142  
# MAGIC **The code block shown below should adjust the number of partitions used in wide transformations like join() to 32. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.** 
# MAGIC Code block:  
# MAGIC `__1__(__2__, __3__)`  
# MAGIC
# MAGIC A.  
# MAGIC 1. spark.conf.get  
# MAGIC 2. "spark.sql.shuffle.partitions"  
# MAGIC 3. "32"  
# MAGIC
# MAGIC B.  
# MAGIC 1. spark.conf.set  
# MAGIC 2. "spark.default.parallelism"  
# MAGIC 3. 32  
# MAGIC
# MAGIC C.  
# MAGIC 1. spark.conf.text  
# MAGIC 2. "spark.default.parallelism"  
# MAGIC 3. "32"  
# MAGIC
# MAGIC D.  
# MAGIC 1. spark.conf.set  
# MAGIC 2. "spark.default.parallelism"  
# MAGIC 3. "32"  
# MAGIC
# MAGIC E.  
# MAGIC 1. spark.conf.set  
# MAGIC 2. "spark.sql.shuffle.partitions"  
# MAGIC 3. "32"

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:143</br>
# MAGIC **Which of the following code blocks returns a DataFrame containing a column openDateString,
# MAGIC a string representation of Java’s SimpleDateFormat?**<br>
# MAGIC Note that column openDate is of type integer and represents a date in the UNIX epoch format
# MAGIC — the number of seconds since midnight on January 1st, 1970.</br>
# MAGIC An example of Java's SimpleDateFormat is "Sunday, Dec 4, 2008 1:05 pm".</br>
# MAGIC A sample of storesDF is displayed below:</br>
# MAGIC ![image_1774874934631.png](./image_1774874934631.png "image_1774874934631.png")</br>
# MAGIC A. storesDF.withColumn("openDatestring", from unixtime(col("openDate“),"EEEE, MMM d,
# MAGIC yyyy h:mm a"))<br>
# MAGIC B. storesDF.withColumn("openDateString", from_unixtime(col("openDate“), "EEEE, MMM d,
# MAGIC yyyy h:mm a", TimestampType()))</br>
# MAGIC C. storesDF.withColumn("openDateString", date(col("openDate"), "EEEE, MMM d, yyyy
# MAGIC h:mm a"))</br>
# MAGIC D. storesDF.newColumn(col("openDateString"), from_unixtime("openDate", "EEEE, MMM d,
# MAGIC yyyy h:mm a"))</br>
# MAGIC E. storesDF.withColumn("openDateString", date(col("openDate“), "EEEE, MMM d, yyyy
# MAGIC h:mm a", TimestampType))</br>
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:144  
# MAGIC **Which of the following code blocks returns a new DataFrame that is the result of a cross join between DataFrame `storesDF` and DataFrame `employeesDF`?**
# MAGIC
# MAGIC A. `storesDF.crossJoin(employeesDF)`  
# MAGIC B. `storesDF.join(employeesDF, "storeId", "cross")`  
# MAGIC C. `crossJoin(storesDF, employeesDF)`  
# MAGIC D. `join(storesDF, employeesDF, "cross")`  
# MAGIC E. `storesDF.join(employeesDF, "cross")`  
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:145 
# MAGIC **Which of the following code blocks returns a new DataFrame that is the result of a position-wise union between DataFrame `storesDF` and DataFrame `acquiredStoresDF`?**
# MAGIC
# MAGIC A. `storesDF.unionByName(acquiredStoresDF)` <br>
# MAGIC B. unionAll(storesDF, acquiredStoresDF) <br> C. union(storesDF, acquiredStoresDF) <br>
# MAGIC D. concat(storesDF, acquiredStoresDF) <br>
# MAGIC E. storesDF.union(acquiredStoresDF) <br>
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:146  
# MAGIC **In what order should the below lines of code be run in order to read a parquet at the file path `filePath` into a DataFrame?**
# MAGIC Lines of code:  
# MAGIC 1. storesDF  
# MAGIC 2. .load(filePath, source = "parquet")  
# MAGIC 3. .read \  
# MAGIC 4. spark \  
# MAGIC 5. .read() \  
# MAGIC 6. .parquet(filePath)  
# MAGIC
# MAGIC A. 1, 5, 2  
# MAGIC B. 4, 5, 2  
# MAGIC C. 4, 3, 6  
# MAGIC D. 4, 5, 6  
# MAGIC E. 4, 3, 2

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:147  
# MAGIC **Which of the following describes slots?**  
# MAGIC A. Slots are the most coarse level of execution in the Spark execution hierarchy.  
# MAGIC B. Slots are resource threads that can be used for parallelization within a Spark application.  
# MAGIC C. Slots are resources that are used to run multiple Spark applications at once on a single cluster.  
# MAGIC D. Slots are the most granular level of execution in the Spark execution hierarchy.  
# MAGIC E. Slots are unique segments of data from a DataFrame that are split up by row.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:148  
# MAGIC **Which of the following lists the units of work performed by Spark from largest to smallest?**  
# MAGIC
# MAGIC A. Task, Stage, Job  
# MAGIC B. Stage, Job, Task  
# MAGIC C. Job, Stage, Task  
# MAGIC D. Stage, Task, Job  
# MAGIC E. Job, Task, Stage

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:149  
# MAGIC **Which of the following operations is least likely to result in a shuffle?**  
# MAGIC
# MAGIC A. `DataFrame.join()`  
# MAGIC B. `DataFrame.filter()`  
# MAGIC C. `DataFrame.orderBy()`  
# MAGIC D. `DataFrame.distinct()`  
# MAGIC E. `DataFrame.intersect()`

# COMMAND ----------

# DBTITLE 1,Cell 151
# MAGIC %md
# MAGIC Question #:150  
# MAGIC **Which of the following cluster configurations is least likely to experience delays due to garbage collection of a large DataFrame?**  
# MAGIC ![image_1774870685925.png](./image_1774870685925.png "image_1774870685925.png")  
# MAGIC **Note:** each configuration has roughly the same compute power using 100GB of RAM and 200 cores.
# MAGIC
# MAGIC A. Scenario #4  
# MAGIC B. Scenario #1  
# MAGIC C. Scenario #5  
# MAGIC D. More information is needed to determine an answer.  
# MAGIC E. Scenario #6

# COMMAND ----------

# DBTITLE 1,Cell 152
# MAGIC %md
# MAGIC Question #:151  
# MAGIC **The code block shown below should return a new DataFrame where column productСategories only has one word per row, resulting in a DataFrame with many more rows than DataFrame storesDF. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**  
# MAGIC A sample of storesDF is displayed below:  
# MAGIC ![image_1774870758100.png](./image_1774870758100.png "image_1774870758100.png")  
# MAGIC Code block:  
# MAGIC `storesDF.__1__(__2__, __3__(__4__(__5__)))`
# MAGIC
# MAGIC A.  
# MAGIC 1. newColumn  
# MAGIC 2. "productCategories"  
# MAGIC 3. col  
# MAGIC 4. split  
# MAGIC 5. "productCategories"  
# MAGIC
# MAGIC B.  
# MAGIC 1. withColumn  
# MAGIC 2. "productCategory"  
# MAGIC 3. split  
# MAGIC 4. col  
# MAGIC 5. "productCategories"  
# MAGIC
# MAGIC C.  
# MAGIC 1. withColumn  
# MAGIC 2. "productCategory"  
# MAGIC 3. explode  
# MAGIC 4. col  
# MAGIC 5. "productCategories"  
# MAGIC
# MAGIC D.  
# MAGIC 1. newColumn  
# MAGIC 2. "productCategory"  
# MAGIC 3. explode  
# MAGIC 4. col  
# MAGIC 5. "productCategories"  
# MAGIC
# MAGIC E.  
# MAGIC 1. withColumn  
# MAGIC 2. "productCategories"  
# MAGIC 3. explode  
# MAGIC 4. col  
# MAGIC 5. "productCategories"

# COMMAND ----------

# DBTITLE 1,Cell 153
# MAGIC %md
# MAGIC Question #:152  
# MAGIC **Which of the following code blocks returns a new DataFrame with column storeReview where the pattern "End" has been removed from the end of column storeReview in DataFrame storesDF?**  
# MAGIC A sample DataFrame storesDF is below:  
# MAGIC ![image_1774870828432.png](./image_1774870828432.png "image_1774870828432.png")
# MAGIC
# MAGIC A. `storesDF.withColumn("storeReview", col("storeReview").regexp_replace(" End$", ""))`  
# MAGIC B. `storesDF.withColumn("storeReview", regexp_replace(col("storeReview"), " End$", ""))`  
# MAGIC C. `storesDF.withColumn("storeReview", regexp_replace(col("storeReview"), " End$"))`  
# MAGIC D. `storesDF.withColumn("storeReview", regexp_replace("storeReview", " End$", ""))`  
# MAGIC E. `storesDF.withColumn("storeReview", regexp_extract(col("storeReview"), " End$", ""))`

# COMMAND ----------

# DBTITLE 1,Cell 154
# MAGIC %md
# MAGIC Question #:153  
# MAGIC **The code block shown below should return a new DataFrame where rows in DataFrame storesDF containing at least one missing value have been dropped. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**  
# MAGIC Code block:  
# MAGIC `StoresDF.__1__.__2__(__3__ = __4__)`
# MAGIC
# MAGIC A.  
# MAGIC 1. na  
# MAGIC 2. drop  
# MAGIC 3. subset  
# MAGIC 4. "any"  
# MAGIC
# MAGIC B.  
# MAGIC 1. na  
# MAGIC 2. drop  
# MAGIC 3. how  
# MAGIC 4. "all"  
# MAGIC
# MAGIC C.  
# MAGIC 1. na  
# MAGIC 2. drop  
# MAGIC 3. subset  
# MAGIC 4. "all"  
# MAGIC
# MAGIC D.  
# MAGIC 1. na  
# MAGIC 2. drop  
# MAGIC 3. how  
# MAGIC 4. "any"  
# MAGIC
# MAGIC E.  
# MAGIC 1. drop  
# MAGIC 2. na  
# MAGIC 3. how  
# MAGIC 4. "any"

# COMMAND ----------

# DBTITLE 1,Cell 155
# MAGIC %md
# MAGIC Question #:154  
# MAGIC **Which of the following operations calculates the simple average of a group of values, like a column?**
# MAGIC
# MAGIC A. `simpleAvg()`  
# MAGIC B. `mean()`  
# MAGIC C. `agg()`  
# MAGIC D. `average()`  
# MAGIC E. `approxMean()`

# COMMAND ----------

# DBTITLE 1,Cell 156
# MAGIC %md
# MAGIC Question #:155  
# MAGIC **Which of the following code blocks fails to return the number of rows in DataFrame storesDF for each distinct combination of values in column division and column storeCategory?**
# MAGIC
# MAGIC A. `storesDF.groupBy((col("division"), col("storeCategory")]).count()`  
# MAGIC B. `storesDF.groupBy("division").groupBy("storeCategory").count()`  
# MAGIC C. `storesDF.groupBy(["division", "storeCategory"]).count()`  
# MAGIC D. `storesDF.groupBy("division", "storeCategory").count()`  
# MAGIC E. `storesDF.groupBy(col("division"), col("storeCategory")).count()`

# COMMAND ----------

# DBTITLE 1,Cell 157
# MAGIC %md
# MAGIC Question #:156  
# MAGIC **The code block shown below contains an error. The code block is intended to return a collection of summary statistics for column sqft in DataFrame storesDF. Identify the error.**  
# MAGIC Code block:  
# MAGIC `storesDF.describes(col("sgft"))`
# MAGIC
# MAGIC A. The `describe()` operation doesn't compute summary statistics for a single column — the `summary()` operation should be used instead.  
# MAGIC B. The column `sqft` should be subsetted from DataFrame storesDF prior to computing summary statistics on it alone.  
# MAGIC C. The `describe()` operation does not accept a Column object as an argument outside of a list — the list `[col("sqft")]` should be specified instead.  
# MAGIC D. The `describe()` operation does not accept a Column object as an argument — the column name string `"sqft"` should be specified instead.  
# MAGIC E. The `describe()` operation doesn't compute summary statistics for numeric columns — the `summary()` operation should be used instead.

# COMMAND ----------

# DBTITLE 1,Cell 158
# MAGIC %md
# MAGIC Question #:157  
# MAGIC **The code block shown below should return a 25 percent sample of rows from DataFrame storesDF with reproducible results. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**  
# MAGIC Code block:  
# MAGIC `StoresDF.__1__(__2__ = __3__, __4__ = __5__)`
# MAGIC
# MAGIC A.  
# MAGIC 1. sample  
# MAGIC 2. fraction  
# MAGIC 3. 0.25  
# MAGIC 4. seed  
# MAGIC 5. True  
# MAGIC
# MAGIC B.  
# MAGIC 1. sample  
# MAGIC 2. withReplacement  
# MAGIC 3. True  
# MAGIC 4. seed  
# MAGIC 5. True  
# MAGIC
# MAGIC C.  
# MAGIC 1. sample  
# MAGIC 2. fraction  
# MAGIC 3. 0.25  
# MAGIC 4. seed  
# MAGIC 5. 1234  
# MAGIC
# MAGIC D.  
# MAGIC 1. sample  
# MAGIC 2. fraction  
# MAGIC 3. 0.15  
# MAGIC 4. seed  
# MAGIC 5. 1234  
# MAGIC
# MAGIC E.  
# MAGIC 1. sample  
# MAGIC 2. withReplacement  
# MAGIC 3. True  
# MAGIC 4. seed  
# MAGIC 5. 1234

# COMMAND ----------

# DBTITLE 1,Cell 159
# MAGIC %md
# MAGIC Question #:158  
# MAGIC **Which of the following code blocks creates a Python UDF assessPerformanceUDF() using the integer-returning Python function assessPerformance() and applies it to Column customerSatisfaction in DataFrame storesDF?**
# MAGIC
# MAGIC A.  
# MAGIC ```python
# MAGIC assessPerformanceUDF = udf(assessPerformance, IntegerType)
# MAGIC storesDF.withColumn("result", assessPerformanceUDF(col("customerSatisfaction")))
# MAGIC ```
# MAGIC
# MAGIC B.  
# MAGIC ```python
# MAGIC assessPerformanceUDF = udf(assessPerformance, IntegerType())
# MAGIC storesDF.withColumn("result", assessPerformanceUDF(col("customerSatisfaction")))
# MAGIC ```
# MAGIC
# MAGIC C.  
# MAGIC ```python
# MAGIC assessPerformanceUDF = udf(assessPerformance)
# MAGIC storesDF.withColumn("result", assessPerformance(col("customerSatisfaction")))
# MAGIC ```
# MAGIC
# MAGIC D.  
# MAGIC ```python
# MAGIC assessPerformanceUDF = udf(assessPerformance)
# MAGIC storesDF.withColumn("result", assessPerformanceUDF(col("customerSatisfaction")))
# MAGIC ```
# MAGIC
# MAGIC E.  
# MAGIC ```python
# MAGIC assessPerformanceUDF = udf(assessPerformance, IntegerType())
# MAGIC storesDF.withColumn("result", assessPerformance(col("customerSatisfaction")))
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Cell 160
# MAGIC %md
# MAGIC Question #:159  
# MAGIC **The code block shown below contains an error. The code block is intended to create a single-column DataFrame from Python list years which is made up of integers. Identify the error.**  
# MAGIC Code block:  
# MAGIC `spark.createDataFrame(years, IntegerType)`
# MAGIC
# MAGIC A. The column name must be specified.  
# MAGIC B. The years list should be wrapped in another list like `[years]` to make clear that it is a column rather than a row.  
# MAGIC C. There is no `createDataFrame` operation in spark.  
# MAGIC D. The `IntegerType` call must be followed by parentheses.  
# MAGIC E. The `IntegerType` call should not be present — Spark can tell that list years is full of integers.

# COMMAND ----------

# DBTITLE 1,Cell 161
# MAGIC %md
# MAGIC Question #:160  
# MAGIC **The code block shown below should return a DataFrame containing a column openDateString, a string representation of Java's SimpleDateFormat. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**  
# MAGIC **Note:** column openDate is of type integer and represents a date in the UNIX epoch format — the number of seconds since midnight on January 1st, 1970.  
# MAGIC An example of Java's SimpleDateFormat is "Sunday, Dec 4, 2008 1:05 pm".  
# MAGIC A sample of storesDF is displayed below:  
# MAGIC ![image_1774871185812.png](./image_1774871185812.png "image_1774871185812.png")  
# MAGIC Code block:  
# MAGIC `storesDF.__1__("openDateString", __2__(__3__, __4__))`
# MAGIC
# MAGIC A.  
# MAGIC 1. withColumn  
# MAGIC 2. from_unixtime  
# MAGIC 3. col("openDate")  
# MAGIC 4. "EEEE, MMM d, yyyy h:mm a"  
# MAGIC
# MAGIC B.  
# MAGIC 1. withColumn  
# MAGIC 2. date_format  
# MAGIC 3. col("openDate")  
# MAGIC 4. "EEEE, mmm d, yyyy h:mm a"  
# MAGIC
# MAGIC C.  
# MAGIC 1. newColumn  
# MAGIC 2. from_unixtime  
# MAGIC 3. "openDate"  
# MAGIC 4. "EEEE, MMM d, yyyy h:mm a"  
# MAGIC
# MAGIC D.  
# MAGIC 1. withColumn  
# MAGIC 2. from_unixtime  
# MAGIC 3. col("openDate")  
# MAGIC 4. SimpleDateFormat  
# MAGIC
# MAGIC E.  
# MAGIC 1. withColumn  
# MAGIC 2. from_unixtime  
# MAGIC 3. col("openDate")  
# MAGIC 4. "dw, MMM d, yyyy h:mm a"

# COMMAND ----------

# DBTITLE 1,Cell 162
# MAGIC %md
# MAGIC Question #:161  
# MAGIC **Which of the following operations can be used to perform a left join on two DataFrames?**
# MAGIC
# MAGIC A. `DataFrame.join()`  
# MAGIC B. `DataFrame.crossJoin()`  
# MAGIC C. `DataFrame.merge()`  
# MAGIC D. `DataFrame.leftJoin()`  
# MAGIC E. Standalone `join()` function

# COMMAND ----------

# DBTITLE 1,Cell 163
# MAGIC %md
# MAGIC Question #:162  
# MAGIC **The code block shown below should return a new DataFrame that is the result of an inner join between DataFrame storesDF and DataFrame employeesDF on column storeId and column employeeId. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**  
# MAGIC Code block:  
# MAGIC `storesDF.join(employeesDF, [__1__ == __2__, __3__ == __4__])`
# MAGIC
# MAGIC A.  
# MAGIC 1. storesDF.storeId  
# MAGIC 2. storesDF.employeeId  
# MAGIC 3. employeesDF.storeId  
# MAGIC 4. employeesDF.employeeId  
# MAGIC
# MAGIC B.  
# MAGIC 1. col("storeId")  
# MAGIC 2. col("storeId")  
# MAGIC 3. col("employeeId")  
# MAGIC 4. col("employeeId")  
# MAGIC
# MAGIC C.  
# MAGIC 1. storeId  
# MAGIC 2. storeId  
# MAGIC 3. employeeId  
# MAGIC 4. employeeId  
# MAGIC
# MAGIC D.  
# MAGIC 1. col("storeId")  
# MAGIC 2. col("employeeId")  
# MAGIC 3. col("employeeId")  
# MAGIC 4. col("storeId")  
# MAGIC
# MAGIC E.  
# MAGIC 1. storesDF.storeId  
# MAGIC 2. employeesDF.storeId  
# MAGIC 3. storesDF.employeeId  
# MAGIC 4. employeesDF.employeeId

# COMMAND ----------

# DBTITLE 1,Cell 164
# MAGIC %md
# MAGIC Question #:163  
# MAGIC **The code block shown below should return a new DataFrame that is the result of a position-wise union between DataFrame storesDF and DataFrame acquiredStoresDF. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**  
# MAGIC Code block:  
# MAGIC `__1__.__2__(__3__)`
# MAGIC
# MAGIC A.  
# MAGIC 1. DataFrame  
# MAGIC 2. union  
# MAGIC 3. storesDF, acquiredStoresDF  
# MAGIC
# MAGIC B.  
# MAGIC 1. DataFrame  
# MAGIC 2. concat  
# MAGIC 3. storesDF, acquiredStoresDF  
# MAGIC
# MAGIC C.  
# MAGIC 1. storesDF  
# MAGIC 2. union  
# MAGIC 3. acquiredStoresDF  
# MAGIC
# MAGIC D.  
# MAGIC 1. storesDF  
# MAGIC 2. unionByName  
# MAGIC 3. acquiredStoresDF  
# MAGIC
# MAGIC E.  
# MAGIC 1. DataFrame  
# MAGIC 2. unionAll  
# MAGIC 3. storesDF, acquiredStoresDF

# COMMAND ----------

# DBTITLE 1,Cell 165
# MAGIC %md
# MAGIC Question #:164  
# MAGIC **Which of the following code blocks writes DataFrame storesDF to file path filePath as text files overwriting any existing files in that location?**
# MAGIC
# MAGIC A. `storesDF.write(filePath, mode = "overwrite", source = "text")`  
# MAGIC B. `storesDF.write.mode("overwrite").text(filePath)`  
# MAGIC C. `storesDF.write.mode("overwrite").path(filePath)`  
# MAGIC D. `storesDF.write.option("text", "overwrite").path(filePath)`  
# MAGIC E. `storesDF.write().mode("overwrite").text(filePath)`

# COMMAND ----------

# DBTITLE 1,Cell 166
# MAGIC %md
# MAGIC Question #:165  
# MAGIC **The code block shown below contains an error. The code block is intended to read JSON at the file path filePath into a DataFrame with the specified schema schema. Identify the error.**  
# MAGIC Code block:  
# MAGIC `spark.read.schema("schema").format("json").load(filePath)`
# MAGIC
# MAGIC A. The `schema` operation from read takes a schema object rather than a string — the argument should be `schema`.  
# MAGIC B. There is no `load()` operation for DataFrameReader — it should be replaced with the `json()` operation.  
# MAGIC C. The `spark.read` operation should be followed by parentheses in order to return a DataFrameReader object.  
# MAGIC D. There is no read property of spark — spark should be replaced with DataFrame.  
# MAGIC E. The `schema` operation from read takes a column rather than a string — the argument should be `col("schema")`.

# COMMAND ----------

# DBTITLE 1,Cell 167
# MAGIC %md
# MAGIC Question #:166  
# MAGIC **Which of the following describes executors?**
# MAGIC
# MAGIC A. Executors are the communication pathways from the driver node to the worker nodes.  
# MAGIC B. Executors are the most granular level of execution in the Spark execution hierarchy.  
# MAGIC C. Executors always have a one-to-one relationship with worker nodes.  
# MAGIC D. Executors are synonymous with worker nodes.  
# MAGIC E. Executors are processing engine instances for performing data computations which run on a worker node.

# COMMAND ----------

# DBTITLE 1,Cell 168
# MAGIC %md
# MAGIC Question #:167  
# MAGIC **The code block shown below should return a DataFrame containing only the rows from DataFrame storesDF where the value in column sqft is less than or equal to 25,000 AND the value in column customerSatisfaction is greater than or equal to 30. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**  
# MAGIC Code block:  
# MAGIC `storesDF.__1__(__2__ __3__ __4__)`
# MAGIC
# MAGIC A.  
# MAGIC 1. filter  
# MAGIC 2. (col("sqft") <= 25000)  
# MAGIC 3. &  
# MAGIC 4. (col("customerSatisfaction") >= 30)  
# MAGIC
# MAGIC B.  
# MAGIC 1. filter  
# MAGIC 2. (col("sqft") <= 25000  
# MAGIC 3. &  
# MAGIC 4. col("customerSatisfaction") >= 30  
# MAGIC
# MAGIC C.  
# MAGIC 1. filter  
# MAGIC 2. (col("sqft") <= 25000)  
# MAGIC 3. and  
# MAGIC 4. (col("customerSatisfaction") >= 30)  
# MAGIC
# MAGIC D.  
# MAGIC 1. drop  
# MAGIC 2. (col(sqft) <= 25000)  
# MAGIC 3. &  
# MAGIC 4. (col(customerSatisfaction) >= 30)  
# MAGIC
# MAGIC E.  
# MAGIC 1. filter  
# MAGIC 2. col("sqft") <= 25000  
# MAGIC 3. and  
# MAGIC 4. col("customerSatisfaction") >= 30

# COMMAND ----------

# DBTITLE 1,Cell 169
# MAGIC %md
# MAGIC Question #:168  
# MAGIC **Which of the following code blocks returns a DataFrame with column storeSlogan where single quotes in column storeSlogan in DataFrame storesDF have been replaced with double quotes?**  
# MAGIC A sample of DataFrame storesDF is below:  
# MAGIC ![image_1774871551059.png](./image_1774871551059.png "image_1774871551059.png")
# MAGIC
# MAGIC A. `storesDF.withColumn("storeSlogan", col("storeSlogan").regexp_replace("'", "\""))`  
# MAGIC B. `storesDF.withColumn("storeSlogan", regexp_replace(col("storeSlogan"), "'"))`  
# MAGIC C. `storesDF.withColumn("storeSlogan", regexp_replace(col("storeSlogan"), "'", "\""))`  
# MAGIC D. `storesDF.withColumn("storeSlogan", regexp_replace("storeSlogan", "'", "\""))`  
# MAGIC E. `storesDF.withColumn("storeSlogan", regexp_extract(col("storeSlogan"), "'", "\""))`

# COMMAND ----------

# DBTITLE 1,Cell 170
# MAGIC %md
# MAGIC ---
# MAGIC Question #:169  
# MAGIC **Which of the following operations can be used to rename and replace an existing column in a DataFrame?**
# MAGIC
# MAGIC A. `DataFrame.renamedColumn()`  
# MAGIC B. `DataFrame.withColumnRenamed()`  
# MAGIC C. `DataFrame.wlthColumn()`  
# MAGIC D. `col()`  
# MAGIC E. `DataFrame.newColumn()`  
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Cell 176
# MAGIC %md
# MAGIC Question #:170  
# MAGIC **The code block shown below should print the schema of DataFrame storesDF. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**  
# MAGIC Code block:  
# MAGIC `__1__.__2__(__3__)`
# MAGIC
# MAGIC A.  
# MAGIC 1. storesDF  
# MAGIC 2. schema  
# MAGIC 3. Nothing  
# MAGIC
# MAGIC B.  
# MAGIC 1. storesDF  
# MAGIC 2. str  
# MAGIC 3. schema  
# MAGIC
# MAGIC C.  
# MAGIC 1. storesDF  
# MAGIC 2. printSchema  
# MAGIC 3. True  
# MAGIC
# MAGIC D.  
# MAGIC 1. storesDF  
# MAGIC 2. printSchema  
# MAGIC 3. Nothing  
# MAGIC
# MAGIC E.  
# MAGIC 1. storesDF  
# MAGIC 2. printSchema  
# MAGIC 3. "all"

# COMMAND ----------

# DBTITLE 1,Cell 177
# MAGIC %md
# MAGIC Question #:171  
# MAGIC **The code block shown below contains an error. The code block is intended to create and register a SQL UDF named "ASSESS_PERFORMANCE" using the Python function assessPerformance() and apply it to column customerSatisfaction in table stores. Identify the error.**  
# MAGIC Code block:  
# MAGIC ```python
# MAGIC spark.udf.register("ASSESS_PERFORMANCE", assessPerformance)
# MAGIC spark.sql("SELECT customerSatisfaction, assessPerformance(customerSatisfaction) AS result FROM stores")
# MAGIC ```
# MAGIC
# MAGIC A. There is no `sql()` operation — the DataFrame API must be used to apply the UDF `assessPerformance()`.  
# MAGIC B. The order of the arguments to `spark.udf.register()` should be reversed.  
# MAGIC C. The `customerSatisfaction` column cannot be called twice inside the SQL statement.  
# MAGIC D. Registered UDFs cannot be applied inside of a SQL statement.  
# MAGIC E. The wrong SQL function is used to compute column result — it should be `ASSESS_PERFORMANCE` instead of `assessPerformance`.

# COMMAND ----------

# DBTITLE 1,Cell 178
# MAGIC %md
# MAGIC Question #:172  
# MAGIC **Which of the following code blocks attempts to cache the partitions of DataFrame storesDF only in Spark's memory?**
# MAGIC
# MAGIC A. `storesDF.cache(StorageLevel.MEMORY_ONLY).count()`  
# MAGIC B. `storesDF.persist().count()`  
# MAGIC C. `storesDF.cache().count()`  
# MAGIC D. `storesDF.persist(StorageLevel.MEMORY_ONLY).count()`  
# MAGIC E. `storesDF.persist("MEMORY_ONLY").count()`

# COMMAND ----------

# DBTITLE 1,Cell 179
# MAGIC %md
# MAGIC Question #:173  
# MAGIC **Which of the following operations will always return a new DataFrame with updated partitions from DataFrame storesDF by inducing a shuffle?**
# MAGIC
# MAGIC A. `storesDF.coalesce()`  
# MAGIC B. `storesDF.rdd.getNumPartitions()`  
# MAGIC C. `storesDF.repartition()`  
# MAGIC D. `storesDF.union()`  
# MAGIC E. `storesDF.intersect()`

# COMMAND ----------

# DBTITLE 1,Cell 180
# MAGIC %md
# MAGIC Question #:174  
# MAGIC **Which of the following code blocks returns a DataFrame containing a column month, an integer representation of the month from column openDate from DataFrame storesDF?**  
# MAGIC **Note:** column openDate is of type integer and represents a date in the UNIX epoch format — the number of seconds since midnight on January 1st, 1970.  
# MAGIC A sample of storesDF is displayed below:  
# MAGIC ![image_1774871689887.png](./image_1774871689887.png "image_1774871689887.png")
# MAGIC
# MAGIC A. `storesDF.withColumn("month", getMonth(col("openDate")))`  
# MAGIC B. `storesDF.withColumn("month", substr(col("openDate"), 4, 2))`  
# MAGIC C.  
# MAGIC ```python
# MAGIC (storesDF.withColumn("openDateFormat", col("openDate").cast("Date"))
# MAGIC  .withColumn("month", month(col("openDateFormat"))))
# MAGIC ```  
# MAGIC D.  
# MAGIC ```python
# MAGIC (storesDF.withColumn("openTimestamp", from_unixtime(col("openDate")))
# MAGIC  .withColumn("month", month(col("openTimestamp"))))
# MAGIC ```  
# MAGIC E. `storesDF.withColumn("month", date_part(col("openDate"), "month"))`

# COMMAND ----------

# DBTITLE 1,Cell 181
# MAGIC %md
# MAGIC Question #:175  
# MAGIC **The code block shown below should read a parquet at the file path filePath into a DataFrame. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**  
# MAGIC Code block:  
# MAGIC `__1__.__2__.__3__(__4__)`
# MAGIC
# MAGIC A.  
# MAGIC 1. spark  
# MAGIC 2. read()  
# MAGIC 3. parquet  
# MAGIC 4. filePath  
# MAGIC
# MAGIC B.  
# MAGIC 1. spark  
# MAGIC 2. read()  
# MAGIC 3. load  
# MAGIC 4. filePath  
# MAGIC
# MAGIC C.  
# MAGIC 1. spark  
# MAGIC 2. read  
# MAGIC 3. load  
# MAGIC 4. filePath, source = "parquet"  
# MAGIC
# MAGIC D.  
# MAGIC 1. storesDF  
# MAGIC 2. read()  
# MAGIC 3. load  
# MAGIC 4. filePath  
# MAGIC
# MAGIC E.  
# MAGIC 1. spark  
# MAGIC 2. read  
# MAGIC 3. load  
# MAGIC 4. filePath

# COMMAND ----------

# DBTITLE 1,Cell 184
# MAGIC %md
# MAGIC Question #:176  
# MAGIC
# MAGIC **Which of the following statements describing a difference between transformations and actions is incorrect?**
# MAGIC
# MAGIC A. There are wide and narrow transformations but there are not wide and narrow actions.  
# MAGIC B. Transformations do not trigger execution while actions do trigger execution.  
# MAGIC C. Transformations work on DataFrames/Datasets while actions are reserved for native language objects.  
# MAGIC D. Some actions can be used to return data objects in a format native to the programming language being used to access the Spark API while transformations do not provide this ability.  
# MAGIC E. Transformations are typically logic operations while actions are typically focused on returning results.
# MAGIC

# COMMAND ----------

# DBTITLE 1,Cell 185
# MAGIC %md
# MAGIC
# MAGIC Question #:177  
# MAGIC **Which of the following describes why garbage collection in Spark is important?**
# MAGIC
# MAGIC A. Logical results will be incorrect if inaccurate data is not collected and removed from the Spark job.  
# MAGIC B. Spark jobs will fail or run slowly if inaccurate data is not collected and removed from the Spark job.  
# MAGIC C. Spark jobs will fail or run slowly if memory is not available for new objects to be created.  
# MAGIC D. Spark jobs will produce inaccurate results if there are too many different transformations called before a single action.  
# MAGIC E. Spark jobs will produce inaccurate results if memory is not available for new tasks to run and complete.  
# MAGIC

# COMMAND ----------

# DBTITLE 1,Cell 186
# MAGIC %md
# MAGIC
# MAGIC Question #:178  
# MAGIC **Which of the following code blocks returns a new DataFrame where column `managerNameLength` is the number of characters in column `managerName` in DataFrame `storesDF`?**  
# MAGIC Assume DataFrame `storesDF` is the only defined language variable.
# MAGIC
# MAGIC A. `storesDF.withColumn("managerNameLength", length(col("managerName")))`  
# MAGIC B. `storesDF.withColumn("managerNameLength", length("managerName"))`  
# MAGIC C. `storesDF.withColumn("managerNameLength", col("managerName").length())`  
# MAGIC D. `storesDF.withColumn("managerNameLength", stringLength(col("managerName")))`  
# MAGIC E. `storesDF.withColumn("managerNameLength", length(managerName))`  
# MAGIC

# COMMAND ----------

# DBTITLE 1,Cell 187
# MAGIC %md
# MAGIC Question #:179  
# MAGIC **Which of the following code blocks returns a DataFrame where rows in DataFrame storesDF containing missing values in every column have been dropped?**
# MAGIC
# MAGIC A. `storesDF.na.drop()`  
# MAGIC B. `storesDF.dropna()`  
# MAGIC C. `storesDF.na.drop("all", subset = "sqft")`  
# MAGIC D. `storesDF.na.drop("all")`  
# MAGIC E. `storesDF.nadrop("all")`

# COMMAND ----------

# DBTITLE 1,Cell 188
# MAGIC %md
# MAGIC ---
# MAGIC Question #:180  
# MAGIC **The code block shown below contains an error. The code block is intended to return a new DataFrame that is the result of a left join between DataFrame storesDF and DataFrame employeesDF on column storeId. Identify the error.**
# MAGIC
# MAGIC Code block:  
# MAGIC `storesDF.join(employeesDF, "storeId")`
# MAGIC
# MAGIC A. The key column storeId needs to be in a list like ["storeId"].  
# MAGIC B. The key column storeId needs to be wrapped in the col() operation.  
# MAGIC C. There is no DataFrame.join() operation – DataFrame.merge() should be used instead.  
# MAGIC D. The default argument to the how parameter is "inner" – an additional argument of "left" must be specified.  
# MAGIC E. The key column storeId needs to be specified in an expression of both DataFrame columns like storesDF.storeId == employeesDF.storeId.  
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Cell 189
# MAGIC %md
# MAGIC ---
# MAGIC Question #:181  
# MAGIC **The code block shown below contains an error. The code block is intended to return a new DataFrame where column productCategories only has one word per row, resulting in a DataFrame with many more rows than DataFrame storesDF. Identify the error and how to fix it.**  
# MAGIC
# MAGIC A sample of storesDF is displayed below:  
# MAGIC ![image_1774871887637.png](./image_1774871887637.png "image_1774871887637.png")  
# MAGIC
# MAGIC **Code block:**  
# MAGIC `storesDF.withColumn("productCategories", split(col("productCategories")))`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC A. The split() operation does not accomplish the requested task in the way that it is used. It should be used provided an alias.  
# MAGIC B. The split() operation does not accomplish the requested task. The broadcast() operation should be used instead.  
# MAGIC C. The split() operation does not accomplish the requested task in the way that it is used. It should be used as a column object method instead.  
# MAGIC D. The split() operation does not accomplish the requested task. The explode() operation should be used instead.  
# MAGIC E. The split() operation does not accomplish the requested task. The array_distinct() operation should is used instead.  
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Cell 190
# MAGIC %md
# MAGIC ---
# MAGIC Question #:182  
# MAGIC **Which of the following code blocks returns a DataFrame where column managerName from DataFrame storesDF is split at the space character into column managerFirstName and column managerLastName?**  
# MAGIC
# MAGIC A sample of DataFrame storesDF is displayed below:  
# MAGIC ![image_1774871939540.png](./image_1774871939540.png "image_1774871939540.png")
# MAGIC
# MAGIC A.  
# MAGIC (storesDF.withColumn("managerFirstName", split(col("managerName"), " "))[0]
# MAGIC  .withColumn("managerLastName", split(col("managerName"), " "))[1])
# MAGIC
# MAGIC B.  
# MAGIC (storesDF.withColumn("managerFirstName", col("managerName").split(" "))[1]
# MAGIC  .withColumn("managerLastName", col("managerName").split(" "))[2])
# MAGIC
# MAGIC C.  
# MAGIC (storesDF.withColumn("managerFirstName", split(col("managerName"), " "))[1]
# MAGIC  .withColumn("managerLastName", split(col("managerName"), " "))[2])
# MAGIC
# MAGIC D.  
# MAGIC (storesDF.withColumn("managerFirstName", col("managerName").split(" "))[0]
# MAGIC  .withColumn("managerLastName", col("managerName").split(" "))[1])
# MAGIC
# MAGIC E.  
# MAGIC (storesDF.withColumn("managerFirstName", split("managerName"), " ")[0]
# MAGIC  .withColumn("managerLastName", split("managerName"), " ")[1])
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Cell 191
# MAGIC %md
# MAGIC Question #:183  
# MAGIC **Which of the following cluster configurations will fail to ensure completion of a Spark application in light of a worker node failure?**  
# MAGIC ![image_1774872029400.png](./image_1774872029400.png "image_1774872029400.png")  
# MAGIC **Note:** each configuration has roughly the same compute power using 100GB of RAM and 200 cores.
# MAGIC
# MAGIC A. Scenario #5  
# MAGIC B. Scenario #4  
# MAGIC C. Scenario #6  
# MAGIC D. Scenario #1  
# MAGIC E. They should all ensure completion because worker nodes are fault tolerant.

# COMMAND ----------

# DBTITLE 1,Cell 192
# MAGIC %md
# MAGIC Question #:184  
# MAGIC
# MAGIC **Which of the following code blocks returns a new DataFrame where column managerName from DataFrame storesDF has had its missing values replaced with the value "No Manager"?**  
# MAGIC
# MAGIC A sample of DataFrame storesDF is displayed below:  
# MAGIC ![image_1774872083776.png](./image_1774872083776.png "image_1774872083776.png")
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC A. `storesDF.na.fill("No Manager", "managerName")`  
# MAGIC B. `storesDF.nafill("No Manager", col("managerName"))`  
# MAGIC C. `storesDF.na.fill("No Manager", col("managerName"))`  
# MAGIC D. `storesDF.fillna("No Manager", col("managerName"))`  
# MAGIC E. `storesDF.nafill("No Manager", "managerName")`
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Cell 193
# MAGIC %md
# MAGIC Question #:185  
# MAGIC **Which of the following code blocks prints the schema of DataFrame storesDF?**
# MAGIC
# MAGIC A. `print(storesDF)`  
# MAGIC B. `storesDF.printSchema()`  
# MAGIC C. `print(storesDF.schema())`  
# MAGIC D. `storesDF.schema`  
# MAGIC E. `storesDF.schema()`

# COMMAND ----------

# DBTITLE 1,Cell 194
# MAGIC %md
# MAGIC Question #:186  
# MAGIC **Which of the following code blocks returns a DataFrame containing only the rows from DataFrame storesDF where the value in column sqft is less than or equal to 25,000 AND the value in column customerSatisfaction is greater than or equal to 30?**
# MAGIC
# MAGIC A. `storesDF.filter(col("sqft") <= 25000 and col("customerSatisfaction") >= 30)`  
# MAGIC B. `storesDF.filter(col("sqft") <= 25000 & col("customerSatisfaction") >= 30)`  
# MAGIC C. `storesDF.filter(col("sqft") <= 25000 or col("customerSatisfaction") >= 30)`  
# MAGIC D. `storesDF.filter((col("sqft") <= 25000) & (col("customerSatisfaction") >= 30))`  
# MAGIC E. `E. storesDF.filter(sqft <= 25000 and customerSatisfaction >= 30)`

# COMMAND ----------

# DBTITLE 1,Cell 195
# MAGIC %md
# MAGIC Question #:187  
# MAGIC **Which of the following statements about Spark DataFrames is incorrect?**
# MAGIC
# MAGIC A. Spark DataFrames are the same as a data frame in Python or R.  
# MAGIC B. Spark DataFrames are built on top of RDDs.  
# MAGIC C. Spark DataFrames are immutable.  
# MAGIC D. Spark DataFrames are distributed.  
# MAGIC E. Spark DataFrames have common Structured APIs.

# COMMAND ----------

# DBTITLE 1,Cell 196
# MAGIC %md
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Question #188**
# MAGIC
# MAGIC The code block shown below should return a new 4-partition DataFrame from the 8-partition DataFrame `storesDF` without inducing a shuffle.  
# MAGIC Choose the response that correctly fills in the numbered blanks within the code block to complete this task.
# MAGIC
# MAGIC **Code block:**  
# MAGIC ```_1_._2_(_3_)```
# MAGIC
# MAGIC
# MAGIC **A.**  
# MAGIC 1. storesDF  
# MAGIC 2. coalesce  
# MAGIC 3. Nothing
# MAGIC
# MAGIC **B.**  
# MAGIC 1. storesDF  
# MAGIC 2. coalesce  
# MAGIC 3. 4
# MAGIC
# MAGIC **C.**  
# MAGIC 1. storesDF  
# MAGIC 2. coalesce  
# MAGIC 3. 4, "storeId"
# MAGIC
# MAGIC **D.**  
# MAGIC 1. storesDF  
# MAGIC 2. coalesce  
# MAGIC 3. "storeId"
# MAGIC
# MAGIC

# COMMAND ----------

# DBTITLE 1,Cell 197
# MAGIC %md
# MAGIC
# MAGIC Question #:189  
# MAGIC
# MAGIC **The code block shown below contains an error. The code block is intended to return a new DataFrame that is the result of an outer join between DataFrame storesDF and DataFrame employeesDF on column storeId. Identify the error.**  
# MAGIC
# MAGIC Code block:  
# MAGIC `storesDF.join(employeesDF, "storeId")`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC A. The default argument to the how parameter is "inner" – an additional argument of "outer" must be specified.  
# MAGIC B. The key column storeId needs to be wrapped in the col() operation.  
# MAGIC C. The key column storeId needs to be specified in an expression of both DataFrame columns like storesDF.storeId == employeesDF.storeId.  
# MAGIC D. The key column storeId needs to be in a list like ["storeId"].  
# MAGIC E. There is no DataFrame.join() operation – DataFrame.merge() should be used instead.  
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Cell 198
# MAGIC %md
# MAGIC Question #:190  
# MAGIC **Which of the following code blocks returns a new DataFrame with the mean of column sqft from DataFrame storesDF in column sqftMean?**
# MAGIC
# MAGIC A. `storesDF.withColumn(mean(col("sqft")).alias("sqftMean"))`  
# MAGIC B. `storesDF.agg(col("sqft").mean().alias("sqftMean"))`  
# MAGIC C. `storesDF.agg(mean("sqft").alias("sqftMean"))`  
# MAGIC D. `storesDF.agg(mean(col("sqft")).alias("sqftMean"))`  
# MAGIC E. `storesDF.withColumn("sqftMean", mean(col("sqft")))`

# COMMAND ----------

# DBTITLE 1,Cell 199
# MAGIC %md
# MAGIC Question #:191  
# MAGIC **Which of the following allows for parallel execution to be performed on Spark DataFrames?**
# MAGIC
# MAGIC A. Delta Tables  
# MAGIC B. RDDs  
# MAGIC C. Multiprocessing  
# MAGIC D. Multithreading  
# MAGIC E. Vectors

# COMMAND ----------

# DBTITLE 1,Cell 200
# MAGIC %md
# MAGIC Question #:192  
# MAGIC
# MAGIC **Which of the following strategies for reducing garbage collection time in Spark is ineffective?**
# MAGIC
# MAGIC - **A.** Use the G1GC garbage collector to improve performance where garbage collection is a bottleneck.<br>
# MAGIC - **B.** Use the Structured APIs as much as possible to reduce memory pressure.
# MAGIC - **C.** Use fewer transformations and more actions.
# MAGIC - **D.** Determine whether garbage collection is being run too often.
# MAGIC - **E.** Allow more memory for major garbage collections.

# COMMAND ----------

# DBTITLE 1,Cell 201
# MAGIC %md
# MAGIC Question #:193  
# MAGIC
# MAGIC **In what order should the below lines of code be run in order to return a DataFrame containing a column dayOfYear, an integer representation of the day of the year from column openDate from DataFrame storesDF?**  
# MAGIC
# MAGIC **Note:** column openDate is of type integer and represents a date in the UNIX epoch format — the number of seconds since midnight on January 1st, 1970.  
# MAGIC
# MAGIC Lines of code:  
# MAGIC ![image_1775819575269.png](./image_1775819575269.png "image_1775819575269.png")
# MAGIC
# MAGIC Lines of code:  
# MAGIC 1. storesDF.withColumn("openTimestamp", col("openDate").cast("Timestamp"))
# MAGIC 2. storesDF.withColumn("dayOfYear", dayofyear(col("openDate")))
# MAGIC 3. storesDF.withColumn("openDateFormat", col("openDate").cast("Date"))
# MAGIC 4. storesDF.withColumn("dayOfYear", dayofyear(col("openTimestamp")))
# MAGIC 5. storesDF.withColumn("dayOfYear", dayofyear(col("openDateFormat")))
# MAGIC 6. storesDF.withColumn("dayOfYear", get_dayofyear(col("openDateFormat")))
# MAGIC
# MAGIC A. 3, 6  
# MAGIC B. 2  
# MAGIC C. 3, 5  
# MAGIC D. 1, 6  
# MAGIC E. 1, 4  
# MAGIC

# COMMAND ----------

# DBTITLE 1,Cell 202
# MAGIC %md
# MAGIC
# MAGIC Question #:: 194
# MAGIC
# MAGIC **Which of the following describes a task?**
# MAGIC
# MAGIC - **A.** A task is the smallest unit of work that can fit on a single executor.
# MAGIC - **B.** A task is a collection of slots that are all in the same executor.
# MAGIC - **C.** A task is the smallest unit of work that can be performed without a shuffle.
# MAGIC - **D.** A task is the most coarse level of execution on the Spark execution hierarchy.
# MAGIC - **E.** A task is a combination of a block of data and a set of transformers that will run on a single executor.

# COMMAND ----------

# DBTITLE 1,Cell 203
# MAGIC %md
# MAGIC Question #:195  
# MAGIC **Which of the following code blocks fails to return a DataFrame sorted alphabetically based on column division?**
# MAGIC
# MAGIC A. `storesDF.sort(asc("division"))`  
# MAGIC B. `storesDF.orderBy(["division"], ascending = [1])`  
# MAGIC C. `storesDF.orderBy(col("division").desc())`  
# MAGIC D. `storesDF.orderBy("division")`  
# MAGIC E. `storesDF.sort("division")`

# COMMAND ----------

# DBTITLE 1,Cell 204
# MAGIC %md
# MAGIC
# MAGIC Question #:: 196
# MAGIC
# MAGIC **Which of the following is an advantage of lazy evaluation?**
# MAGIC
# MAGIC - **A.** Spark jobs can be better optimized because all of the transformations in the job are visible prior to evaluation
# MAGIC - **B.** Spark jobs are less complex because they don’t execute all of the operations in the program
# MAGIC - **C.** Spark jobs run faster because they do not distribute small tasks across the cluster due to the cost of cluster overhead
# MAGIC - **D.** Spark jobs are less likely to fail because the execution does not start until the job is finished compiling
# MAGIC - **E.** Spark jobs run faster because there is increased communication between the Spark driver and its worker nodes
# MAGIC

# COMMAND ----------

# DBTITLE 1,Cell 205
# MAGIC %md
# MAGIC Question #:197  
# MAGIC **Which of the following code blocks returns a DataFrame where every row is unique?**
# MAGIC
# MAGIC A. `storesDF.getDistinct()`  
# MAGIC B. `storesDF.duplicates.drop()`  
# MAGIC C. `storesDF.removeDuplicates()`  
# MAGIC D. `storesDF.distinct()`  
# MAGIC E. `storesDF.duplicates()`

# COMMAND ----------

# DBTITLE 1,Cell 206
# MAGIC %md
# MAGIC Question #:198  
# MAGIC **Which of the following operations can be used to sort the rows of a DataFrame?**
# MAGIC
# MAGIC A. `sort()` and `orderBy()`  
# MAGIC B. `orderBy()`  
# MAGIC C. `sort()`  
# MAGIC D. `sort()` and `orderby()`  
# MAGIC E. `orderby()`

# COMMAND ----------

# DBTITLE 1,Cell 207
# MAGIC %md
# MAGIC Question #:199  
# MAGIC **Which of the following operations can be used to return all of the rows from a DataFrame?**
# MAGIC
# MAGIC A. `DataFrame.count()`  
# MAGIC B. `DataFrame.head()`  
# MAGIC C. `DataFrame.collect()`  
# MAGIC D. `DataFrame.show()`  
# MAGIC E. `DataFrame.take()`

# COMMAND ----------

# DBTITLE 1,Cell 208
# MAGIC %md
# MAGIC Question #:200  
# MAGIC **The code block shown below should return a new DataFrame from DataFrame storesDF where column numberOfManagers is the constant integer 1. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**  
# MAGIC Code block:  
# MAGIC `storesDF.__1__(__2__, __3__(__4__))`
# MAGIC
# MAGIC A.  
# MAGIC 1. withColumn  
# MAGIC 2. "numberOfManagers"  
# MAGIC 3. lit  
# MAGIC 4. 1  
# MAGIC
# MAGIC B.  
# MAGIC 1. withColumn  
# MAGIC 2. "numberOfManagers"  
# MAGIC 3. IntegerType  
# MAGIC 4. 1  
# MAGIC
# MAGIC C.  
# MAGIC 1. newColumn  
# MAGIC 2. numberOfManagers  
# MAGIC 3. IntegerType  
# MAGIC 4. 1  
# MAGIC
# MAGIC D.  
# MAGIC 1. withColumn  
# MAGIC 2. "numberOfManagers"  
# MAGIC 3. col  
# MAGIC 4. 1  
# MAGIC
# MAGIC E.  
# MAGIC 1. withColumn  
# MAGIC 2. "numberOfManagers"  
# MAGIC 3. lit  
# MAGIC 4. "1"

# COMMAND ----------

# DBTITLE 1,Cell 209
# MAGIC %md
# MAGIC Question #:201  
# MAGIC **If Spark is running in cluster mode, which of the following statements about nodes is incorrect?**
# MAGIC
# MAGIC A. The Spark driver runs in its own node without any executors.  
# MAGIC B. Each executor is a running processing engine inside of a worker node.  
# MAGIC C. There may be more executors than total nodes or more total nodes than executors.  
# MAGIC D. There is always more than one node.  
# MAGIC E. There is a single node that contains the Spark driver and the executors.

# COMMAND ----------

# DBTITLE 1,Cell 210
# MAGIC %md
# MAGIC Question #:202  
# MAGIC **Which of the following code blocks does fail to return a new DataFrame that is the result of an inner join between DataFrame storesDF and DataFrame employeesDF on column storeId and column employeeId?**
# MAGIC
# MAGIC A. `storesDF.join(employeesDF, [col("storeId"), col("employeeId")])`  
# MAGIC B. `storesDF.join(employeesDF, [storesDF.storeId == employeesDF.storeId, storesDF.employeeId == employeesDF.employeeId])`  
# MAGIC C. `storesDF.join(employeesDF, ["storeId", "employeeId"])`  
# MAGIC D. `storesDF.alias("s").join(employeesDF.alias("e"), [col("s.storeId") == col("e.storeId"), col("s.employeeId") == col("e.employeeId")])`  
# MAGIC E. `storesDF.join(employeesDF, ["storeId", "employeeId"], "inner")`

# COMMAND ----------

# DBTITLE 1,Cell 211
# MAGIC %md
# MAGIC Question #:203  
# MAGIC **Which of the following code blocks efficiently performs a broadcast join of DataFrame storesDF and the much larger DataFrame employeesDF using the key column storeId?**
# MAGIC
# MAGIC A. `storesDF.join(broadcast(employeesDF), "storeId")`  
# MAGIC B. `broadcast(storesDF.join(employeesDF), "storeId")`  
# MAGIC C. `broadcast(employeesDF.join(storesDF), "storeId")`  
# MAGIC D. `employeesDF.join(broadcast(storesDF), "storeId")`  
# MAGIC E. `storesDF.broadcastJoin(employeesDF, "storeId")`

# COMMAND ----------

# DBTITLE 1,Cell 212
# MAGIC %md
# MAGIC Question #:204  
# MAGIC **Which of the following operations can be used to fill missing values in a specified column with a specified value?**
# MAGIC
# MAGIC A. `DataFrame.na.fill()`  
# MAGIC B. `DataFrame.nafill()`  
# MAGIC C. `DataFrame.fillna()`  
# MAGIC D. `DataFrame.na.fill()` and `DataFrame.nafill()`  
# MAGIC E. `DataFrame.na.fill()` and `DataFrame.fillna()`

# COMMAND ----------

# DBTITLE 1,Cell 213
# MAGIC %md
# MAGIC Question #:205  
# MAGIC **Which of the following code blocks returns a DataFrame sorted in ascending order (with missing values first) based on column sqft?**
# MAGIC
# MAGIC A. `storesDF.orderBy(col("sqft").asc_nulls_last())`  
# MAGIC B. `storesDF.orderBy(asc_nulls_first(col("sqft")))`  
# MAGIC C. `storesDF.orderBy("sqft".asc().nulls_first())`  
# MAGIC D. `storesDF.orderBy(col("sqft").asc_nulls_first())`  
# MAGIC E. `storesDF.orderBy(col("sqft").nulls_first())`

# COMMAND ----------

# DBTITLE 1,Cell 214
# MAGIC %md
# MAGIC Question #:206  
# MAGIC **Which of the following Spark execution/deployment modes requires all executors to be on a single worker node?**
# MAGIC
# MAGIC A. Standard mode  
# MAGIC B. Cluster mode  
# MAGIC C. Local mode  
# MAGIC D. All of these responses require all executors to be on a single worker node.  
# MAGIC E. Client mode

# COMMAND ----------

# DBTITLE 1,Cell 215
# MAGIC %md
# MAGIC Question #:207  
# MAGIC **The code block shown below contains an error. The code block is intended to read CSV at the file path filePath into a DataFrame with the specified schema schema. Identify the error.**  
# MAGIC Code block:  
# MAGIC `spark.read.schema("schema").csv(filePath)`
# MAGIC
# MAGIC A. The `schema` operation from read takes a schema object rather than a string — the argument should be `schema`.  
# MAGIC B. There is no `csv()` operation for DataFrameReader — it should be replaced with the `load()` operation.  
# MAGIC C. There is no read property of spark — spark should be replaced with DataFrame.  
# MAGIC D. The `schema` operation from read takes a column rather than a string — the argument should be `col("schema")`.  
# MAGIC E. The `spark.read` operation should be followed by parentheses in order to return a DataFrameReader object.

# COMMAND ----------

# DBTITLE 1,Cell 216
# MAGIC %md
# MAGIC Question #:208  
# MAGIC **The code block shown below should create a Python UDF assessPerformanceUDF using the Python function assessPerformance() and apply it to column customerSatisfaction in DataFrame storesDF. Choose the response that correctly fills in the numbered blanks within the code block to complete this task.**  
# MAGIC Code block:  
# MAGIC ```python
# MAGIC assessPerformanceUDF = udf(__1__)
# MAGIC storesDF.__2__("result", assessPerformanceUDF(__3__))
# MAGIC ```
# MAGIC
# MAGIC A.  
# MAGIC 1. assessPerformance  
# MAGIC 2. withColumn  
# MAGIC 3. col("customerSatisfaction")  
# MAGIC
# MAGIC B.  
# MAGIC 1. "assessPerformance"  
# MAGIC 2. withColumn  
# MAGIC 3. "customerSatisfaction"  
# MAGIC
# MAGIC C.  
# MAGIC 1. "assessPerformance"  
# MAGIC 2. select  
# MAGIC 3. col("customerSatisfaction")  
# MAGIC
# MAGIC D.  
# MAGIC 1. assessPerformance  
# MAGIC 2. select  
# MAGIC 3. col("customerSatisfaction")  
# MAGIC
# MAGIC E.  
# MAGIC 1. assessPerformance  
# MAGIC 2. withColumn  
# MAGIC 3. "customerSatisfaction"

# COMMAND ----------

# DBTITLE 1,Cell 217
# MAGIC %md
# MAGIC Question #:209  
# MAGIC **Which of the following code blocks writes DataFrame storesDF to file path filePath as text files?**
# MAGIC
# MAGIC A. `storesDF.write(filePath)`  
# MAGIC B. `storesDF.write.path(filePath)`  
# MAGIC C. `storesDF.write().text(filePath)`  
# MAGIC D. `storesDF.write.text(filePath)`  
# MAGIC E. `storesDF.write.option("text").path(filePath)`

# COMMAND ----------

# MAGIC %md
# MAGIC %md
# MAGIC Question #:210<br>
# MAGIC **Which of the following code blocks returns a new DataFrame where column managerName is in all uppercase version of column managerName in DataFrame stores**
# MAGIC **DF? Assume DataFrame stores DF is the only defined language variable.**<br>
# MAGIC A. storesDF.withColumn ("managerName", upper (managerName))<br>
# MAGIC B. storesDF.withColumn ("managerName", toupper (col ("managerName")))<br>
# MAGIC C. storesDF.withColumn ("managerName", upper (col ("managerName")))<br>
# MAGIC D.storesDF.withColumn ("managerName", col ("managerName") .upper())<br>
# MAGIC E. storesDF.withColumn ("managerName", upper ("managerName"))<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:211<br>
# MAGIC **Which of the following code blocks returns a DataFrame containing a column month, an integer representation of the month from column openDate from DataFrame storesDF?**
# MAGIC **Note that column openDate is of type integer and represents a date in the UNIX epoch format - the number of seconds since midnight on January 1st, 1970.**<br>
# MAGIC **A sample of storesDF is displayed below:**<br>
# MAGIC ![Sample of storesDF table](/Workspace/Users/nikx2198@gmail.com/Pyspark_leaning/Screenshot 2026-03-19 181854.png)
# MAGIC
# MAGIC A. storesDF.withColumn("month", getMonth(col("openDate")))<br>
# MAGIC B. (storesDF.withColumn("openTimestamp", col("openDate").cast("Timestamp")) .withColumn("month", month(col("openTimestamp"))))<br>
# MAGIC C. storesDF.withColumn("month", month(col("openDate")))<br>
# MAGIC D. storesDF.withColumn("month", substr(col("openDate"), 4, 2))<br>
# MAGIC E. (storesDF.withColumn("openDateFormat", col("openDate").cast("Date")) .withColumn("month", month(col("openDateFormat"))))
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:212<br>
# MAGIC **Which of the following code blocks returns a new DataFrame that is the result of a left join between DataFrame storesDF and DataFrame employeesDF on column storeId?**<br>
# MAGIC A. storesDF.join(employeesDF, "left", col("storeId"))<br>
# MAGIC B. stores DF.join(employees DF, "storeId")<br>
# MAGIC C. storesDF.join(employees DF, "storeId", "left")<br>
# MAGIC D. storesDF.merge (employees DF, "left", col ("storeId"))<br>
# MAGIC E. storesDF.join(employeesDF, "left", storesDF.storeId == employees DF.storeId)<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:213<br>
# MAGIC **Which of the following code blocks writes DataFrame storesDF to file path filePath as JSON overwriting any existing files in that location?**<br>
# MAGIC A. storesDF.write (filePath, mode = "overwrite", source = "json")<br>
# MAGIC B. stores DF.write.mode ("overwrite") .json (filePath)<br>
# MAGIC C. storesDF.write.mode ("overwrite").path (filePath)<br>
# MAGIC D. stores DF.write.option ("json", "overwrite").path (filePath)<br>
# MAGIC E. storesDF.write() .mode ("overwrite").json (filePath)<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:214<br>
# MAGIC **A data scientist of an e-commerce company is working with user data obtained from its subscriber database and has stored the data in a DataFrame df_user. Before further processing the data, the data scientist wants to create another DataFrame df_user_non_pii and store only the non pii columns in this DataFrame. The pii columns in df_user are first_name, last_name, email, and birthdate.**<br>
# MAGIC **Which code snippet can be used to meet this requirement?**<br>
# MAGIC A. df_user_non_pii = df_user.drop("first_name", "last_name", "email", "birthdate")<br>
# MAGIC B. df_user_non_pii = df_user.drop("first_name", last_name, email, birthdate")<br>
# MAGIC C. df_user_non_pii = df_user.dropfields ("first_name", "last_name", "email", "birthdate")<br>
# MAGIC D. df_user_non_pii = df_user.dropfields ("first_name, last_name, email, birthdate")<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:215<br>
# MAGIC **A data engineer is working on a Streaming DataFrame streaming_df with the given streaming data:**
# MAGIC ![](/Workspace/Users/nikx2198@gmail.com/Pyspark_leaning/Screenshot 2026-03-19 182646.png) </br>
# MAGIC **Which operation is supported with streaming_df?**<br>
# MAGIC A. streaming_df.select (count Distinct ("Name"))<br>
# MAGIC B. streaming_df.groupby("Id").count()<br>
# MAGIC C. streaming_df.orderBy("timestamp").limit (4)<br>
# MAGIC D. streaming_df.filter (col ("count") < 30).show()<br>
# MAGIC

# COMMAND ----------

# DBTITLE 1,Question 216: Pandas UDF performance improvement
# MAGIC %md
# MAGIC Question #:216
# MAGIC **An MLOps engineer is building a Pandas UDF that applies a language model that translates English strings into Spanish. The initial code is loading the model on every call to the UDF which is hurting the performance of the data pipeline. The initial code is:**
# MAGIC ```python
# MAGIC def in_spanish_inner(df: pd.Series) -> pd.Series:
# MAGIC     model = get_translation_model(target_lang='es')
# MAGIC     return df.apply(model)
# MAGIC in_spanish = sf.pandas_udf(in_spanish_inner, StringType())
# MAGIC ```
# MAGIC **How can the MLOps engineer change this code to reduce how many times the language model is loaded?**<br>
# MAGIC A. Convert the Pandas UDF to a PySpark UDF<br>
# MAGIC B. Convert the Pandas UDF from a Series -> Series UDF to a Series to Scalar UDF<br>
# MAGIC C. Run the in_spanish_inner() function in a mapInPandas() function call<br>
# MAGIC D. Convert the Pandas UDF from a Series -> Series UDF to an Iterator[Series] -> Iterator[Series]

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:217<br>
# MAGIC **Spark DataFrame af is cached using the MEMORY_AND_DISK storage level, but the DataFrame is too large to fit entirely in memory.**
# MAGIC **What is the likely behaviour when Spark runs out of memory to store the DataFrame?**<br>
# MAGIC A. Spark duplicates the DataFrame in both memory and disk. It doesn't fit in memory, the DataFrame is stored and retrieved from the disk entirely. O <br>B. Spark splits
# MAGIC the DataFrame evenly between memory and disk, ensuring balanced storage utilization.<br>
# MAGIC C. Spark will store as much data as possible in memory and spill the rest to disk when memory is full, continuing processing with performance overhead.<br>
# MAGIC D. Spark stores the frequently accessed rows in memory and less frequently accessed rows on disk, utilizing both resources to offer balanced performance.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:218<br>
# MAGIC **A data engineer is building a Structured Streaming pipeline and wants the pipeline to recover from failures or intentional shutdowns by continuing where the pipeline left off. How can this be achieved?**<br>
# MAGIC A. By configuring the option checkpointLocation during readStream<br>
# MAGIC B. By configuring the option recoveryLocation during the SparkSession initialization<br>
# MAGIC C. By configuring the option recoveryLocation during writeStream<br>
# MAGIC D. By configuring the option checkpoint Location during writeStream

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:219<br>
# MAGIC **A data scientist is analyzing a large dataset and has written a PySpark script that includes several transformations and actions on a DataFrame. The script ends with a**
# MAGIC **collect () action to retrieve the results.**
# MAGIC **How does Apache SparkTM's execution hierarchy process the operations when the data scientist runs this script?**<br>
# MAGIC A. The script is first divided into multiple applications, then each application is split into jobs, stages, and finally tasks.<br>
# MAGIC B. The entire script is treated as a single job, which is then divided into multiple stages, and each stage is further divided into tasks based on data partitions.<br>
# MAGIC C. The collect () action triggers a job, which is divided into stages at shuffle boundaries, and each stage is split into tasks that operate on individual data partitions.<br>
# MAGIC D. Spark creates a single task for each transformation and action in the script, and these tasks are grouped into stages and jobs based on their dependencies.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:220<br>
# MAGIC **A developer is trying to join two tables, sales.purchases_fct and sales.customer_dim, using the code:**
# MAGIC ```python
# MAGIC import pyspark.sql. functions as F
# MAGIC purch_df = spark.table('sales.purchases fct')
# MAGIC cust_df = spark.table('sales.customer_dim').drop Duplicates (['cust_id'])
# MAGIC fact_df = purch_df.join (cust_df, F.col('customer_id')==F.col('cust_id'))
# MAGIC ```
# MAGIC **The developer has discovered that customers in the purchases_fct table that do not exist in the customer_dim table are being dropped from the joined table. Which**
# MAGIC **change should be made to the code to stop these customer records from being dropped?**<br>
# MAGIC A. fact_df = purch_df.join(cust_df, F. col('customer_id') == F.col('cust_id'), 'left')<br>
# MAGIC B. fact_df = cust_df.join(purch_df, F. col('customer_id') == F.col('cust_id'))<br>
# MAGIC C. fact_df = purch_df.join(cust_df, F.col('cust_id')==F.col('customer_id'))<br>
# MAGIC D. fact_df = purch_df.join(cust_df, F.col('customer_id') == F.col('cust_id'), 'right_outer')

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:221<br>
# MAGIC **A data engineer is reviewing a Spark application that applies several transformations to a DataFrame but notices that the job does not start executing immediately.**
# MAGIC **Which two characteristics of Apache Spark's execution model explain this behavior? (Choose two.)**<br>
# MAGIC A. The Spark engine requires manual intervention to start executing transformations.<br>
# MAGIC B. Only actions trigger the execution of the transformation pipeline.<br>
# MAGIC C. Transformations are executed immediately to build the lineage graph.<br>
# MAGIC D. The Spark engine optimizes the execution plan during the transformations, causing delays.<br>
# MAGIC E. Transformations are evaluated lazily.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:222<br>
# MAGIC **A developer needs to produce a Python dictionary using data stored in a small Parquet table, which looks like this:**
# MAGIC ![](/Workspace/Users/nikx2198@gmail.com/Pyspark_leaning/Screenshot 2026-03-19 184916.png)
# MAGIC
# MAGIC **The resulting Python dictionary must contain a mapping of region -> region_id containing the smallest 3 region_id values.**
# MAGIC **Which code fragment meets the requirements?**<br>
# MAGIC A. regions = dict( regions_df .select('region', 'region_id') \ .sort('region_id') \ .take(3) )<br>
# MAGIC B. regions = dict( regions_df .select('region_id', 'region') \ .sort('region_id') \ .take(3) )<br>
# MAGIC C. regions = dict( regions_df .select('region_id', 'region') \ .limit(3) \ .collect() )<br>
# MAGIC D. regions = dict( regions_df .select('region', 'region_id') \ .sort(desc('region_id')) \ .take(3) )
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC    
# MAGIC Question #:223<br>
# MAGIC **An engineer has a large ORC file located at /file/test_data.orc and wants to read only specific columns to reduce memory usage. Which code fragment will select the columns, i.e., col1, col2, during the reading process?**<br>
# MAGIC A. spark.read.orc("/file/test_data.orc").filter("col1 = 'value'").select("col2")<br>
# MAGIC B. spark.read.format("orc").select("col1", "col2").load("/file/test_data.orc")<br>
# MAGIC C. spark.read.orc("/file/test_data.orc").select("col1", "col2")<br>
# MAGIC D. spark.read.format("orc").load("/file/test_data.orc").select("col1", "col2")<br>

# COMMAND ----------

# MAGIC %md
# MAGIC    
# MAGIC Question #:224<br>
# MAGIC **Given the code fragment:**<br>
# MAGIC python<br>
# MAGIC import pyspark.pandas as ps<br>
# MAGIC psdf = ps.DataFrame({'col': [1,2], 'col2': [3, 4]})
# MAGIC
# MAGIC **Which method is used to convert a Pandas API on Spark DataFrame (pyspark.pandas.DataFrame) into a standard PySpark DataFrame (pyspark.sql.DataFrame)?**<br>
# MAGIC A. psdf.to_spark()<br>
# MAGIC B. psdf.to_pyspark()<br>
# MAGIC C. psdf.to_pandas()<br>
# MAGIC D. psdf.to_dataframe()<br>

# COMMAND ----------

# MAGIC %md
# MAGIC    
# MAGIC Question #:225<br>
# MAGIC **A Spark engineer is troubleshooting a Spark application that has been encountering out-of-memory errors during execution. By reviewing the Spark driver logs, the engineer notices multiple "GC overhead limit exceeded" messages.**
# MAGIC **Which action should the engineer take to resolve this issue?**<br>
# MAGIC A. Optimize the data processing logic by repartitioning the DataFrame.<br>
# MAGIC B. Modify the Spark configuration to disable garbage collection.<br>
# MAGIC C. Increase the memory allocated to the Spark Driver.<br>
# MAGIC D. Cache large DataFrames to persist them in memory.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC    
# MAGIC Question #:226<br>
# MAGIC **A DataFrame df has columns name, age, and salary. The developer needs to sort the DataFrame age in ascending order and salary in descending order. Which code snippet meets the requirement of the developer?**<br>
# MAGIC A. df.orderBy(col("age").asc(), col("salary").asc()).show()<br>
# MAGIC B. df.sort("age", "salary", ascending([True, True])).show()<br>
# MAGIC C. df.sort("age", "salary", ascending([False, True])).show()<br>
# MAGIC D. df.orderBy("age", "salary", ascending=[True, False]).show()<br>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #:227<br>
# MAGIC **What is the difference between df.cache() and df.persist() in Spark DataFrame?**<br>
# MAGIC A. Both cache() and persist() can be used to set the default storage level (MEMORY_AND_DISK_DESER).<br>
# MAGIC B. Both functions perform the same operation. The persist() function provides improved performance as its default storage level is DISK_ONLY.<br>
# MAGIC C. persist() - Persists the DataFrame with the default storage level (MEMORY_AND_DISK_DESER) and cache() - Can be used to set different storage levels to persist the contents of the DataFrame.<br>
# MAGIC D. cache() - Persists the DataFrame with the default storage level (MEMORY_AND_DISK_DESER) and persist() - Can be used to set different storage levels to persist the contents of the DataFrame.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:228<br>
# MAGIC **A data analyst builds a Spark application to analyze finance data and performs the following operations: filter, select, groupBy, and coalesce. Which operation results in a shuffle?**<br>
# MAGIC A. groupBy<br>
# MAGIC B. filter<br>
# MAGIC C. select<br>
# MAGIC D. coalesce<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:229  
# MAGIC **A data engineer is asked to build an ingestion pipeline for a set of parquet files delivered by an upstream team on a nightly basis. The data is stored in a directory structure with a base path of `/path/events/data`. The upstream team drops daily data into the underlying subdirectories following the convention `year/month/day`.**
# MAGIC **A few examples of the directory structure are:**
# MAGIC - `/path/events/data/2024/01/01`  
# MAGIC - `/path/events/data/2024/01/02`  
# MAGIC - `/path/events/data/2024/01/03`  
# MAGIC - `/path/events/data/2023/01/01`  
# MAGIC - `/path/events/data/2023/01/02`  
# MAGIC - `/path/events/data/2023/01/03`  
# MAGIC
# MAGIC **Which of the following code snippets will read all the data within the directory structure?**<br>
# MAGIC A. `df = spark.read.option("inferSchema", "true").parquet("/path/evets/data/")`  
# MAGIC B. `df = spark.read.option("recursiveFileLookup", "true").parquet("/path/events/data/")`  
# MAGIC C. `df = spark.read.parquet("/path/events/data/*")`<br>
# MAGIC D. `df = spark.read.parquet ("/path/events/data/")`

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:230<br>
# MAGIC **Given a DataFrame that has 10 partitions, after running the code:**<br>
# MAGIC `result = df.coalesce(20)`<br>
# MAGIC **How many partitions will the result DataFrame have?**<br>
# MAGIC A. 10<br>
# MAGIC B. same number as the cluster executors<br>
# MAGIC C. 1<br>
# MAGIC D. 20<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:231<br>
# MAGIC **Given the following code snippet in `my_spark_app.py`:**
# MAGIC ```python
# MAGIC from pyspark.sql import SparkSession
# MAGIC spark = SparkSession.builder.appName("CoreComponentsExample").getOrCreate()
# MAGIC data = [("Alice", 34), ("Bob", 36), ("Cathy", 31)]
# MAGIC columns = ["Name", "Age"]
# MAGIC df = spark.createDataFrame(data, columns).withColumn("Status", "Pass")
# MAGIC df_filtered = df.filter(df.Age > 35)
# MAGIC df_filtered.show()
# MAGIC spark.stop()
# MAGIC ```
# MAGIC **What is the role of the driver node?**<br>
# MAGIC A. The driver node orchestrates the execution by transforming actions into tasks and distributing them to worker nodes.<br>
# MAGIC B. The driver node only provides the user interface for monitoring the application.<br>
# MAGIC C. The driver node holds the DataFrame data and performs all computations locally.<br>
# MAGIC D. The driver node stores the final result after computations are completed by worker nodes.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:232<br>
# MAGIC **A Spark developer wants to improve the performance of an existing PySpark UDF that runs a hash function that is not available in the standard Spark functions library.**<br>
# MAGIC **The existing UDF code is:**
# MAGIC ```python
# MAGIC import hashlib
# MAGIC import pyspark.sql.functions as sf
# MAGIC from pyspark.sql.types import StringType
# MAGIC
# MAGIC def shake_256(raw):
# MAGIC     return hashlib.shake_256(raw.encode()).hexdigest(20)
# MAGIC
# MAGIC shake_256_udf = sf.udf(shake_256, StringType())
# MAGIC ```
# MAGIC **The developer wants to replace this existing UDF with a Pandas UDF to improve performance.**<br>
# MAGIC **The developer changes the definition of `shake_256_udf` to this:**
# MAGIC ```python
# MAGIC shake_256_udf = sf.pandas_udf(shake_256, StringType())
# MAGIC ```
# MAGIC **However, the developer receives the error:**<br>
# MAGIC `[UNSUPPORTED_SIGNATURE] Unsupported signature: (raw: str) -> str.`<br>
# MAGIC **What should the signature of the `shake_256()` function be changed to in order to fix this error?**<br>
# MAGIC A. `def shake_256(df: pd.Series) -> str:`<br>
# MAGIC B. `def shake_256(df: Iterator[pd.Series]) -> Iterator[pd.Series]:`<br>
# MAGIC C. `def shake_256(raw: str) -> str:`<br>
# MAGIC D. `def shake_256(df: pd.Series) -> pd.Series:`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:233<br>
# MAGIC **A Developer is working with a pandas DataFrame containing user behaviour data from a web application.**<br>
# MAGIC **Which approach should be used for executing groupby operation in parallel across all workers of Apache Spark 3.5?**<br>
# MAGIC A. Use the applyInPandas API:<br>
# MAGIC ```python
# MAGIC import pandas as pd
# MAGIC def mean_func(key, pdf):
# MAGIC     return pd.DataFrame([(key + (pdf['value'].mean(),))])
# MAGIC df.groupBy('user_id').applyInPandas(mean_func, schema="user_id long, value double").show()
# MAGIC ```
# MAGIC B. Utilize the mapInPandas API:<br>
# MAGIC ```python
# MAGIC def mean_func(pdf_iter):
# MAGIC     for pdf in pdf_iter:
# MAGIC         yield pdf.groupby('user_id').agg({'value': 'mean'}).reset_index()
# MAGIC df.mapInPandas(mean_func, schema="user_id long, value double").show()
# MAGIC ```
# MAGIC C. Use a regular Spark UDF (User-Defined Function):<br>
# MAGIC ```python
# MAGIC from pyspark.sql.functions import mean
# MAGIC df.groupBy('user_id').agg(mean('value')).show()
# MAGIC ```
# MAGIC D. Create a Pandas UDF (User-Defined Function):<br>
# MAGIC ```python
# MAGIC from pyspark.sql.functions import pandas_udf
# MAGIC @pandas_udf("double")
# MAGIC def mean_func(value: pd.Series) -> float:
# MAGIC     return value.mean()
# MAGIC df.groupBy("user_id").agg(mean_func(df['value'])).show()
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:234<br>
# MAGIC **Given:**<br>
# MAGIC `spark.sparkContext.setLogLevel("<LOG_LEVEL>")`<br>
# MAGIC **Which set contains the suitable configuration settings for Spark driver LOG_LEVEL's?**<br>
# MAGIC A. ALL, DEBUG, FAIL, INFO<br>
# MAGIC B. ERROR, WARN, TRACE, OFF<br>
# MAGIC C. WARN, NONE, ERROR, FATAL<br>
# MAGIC D. FATAL, NONE, INFO, DEBUG<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:235  
# MAGIC **An engineer wants to join two DataFrames, df1 and df2, on the respective employee_id and emp_id columns:**  
# MAGIC - **df1:** employee_id INT, name STRING  
# MAGIC - **df2:** emp_id INT, department STRING  
# MAGIC
# MAGIC **The engineer used the code snippet to join df1 and df2:**  
# MAGIC python
# MAGIC result = df1.join(df2, df1.employee_id == df2.emp_id, how="inner")
# MAGIC
# MAGIC
# MAGIC **What is the behaviour of the code snippet?**  
# MAGIC A. The code fails to execute because the column names employee_id and emp_id do not match automatically  
# MAGIC B. The code fails to execute because it must use on='employee_id' to specify the join column explicitly  
# MAGIC C. The code fails to execute because PySpark does not support joining DataFrames with a different structure.  
# MAGIC D. The code works as expected because the join condition explicitly matches employee_id from df1 with emp_id from df2.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:236<br>
# MAGIC **A data engineer has been asked to produce a Parquet table which is overwritten every day with the latest data. The downstream consumer of this Parquet table has a hard requirement that the data in this table is produced with all records sorted by the `market_time` field. Which line of Spark code will produce a Parquet table that meets these requirements?**<br>
# MAGIC
# MAGIC A.<br>
# MAGIC python
# MAGIC final_df \
# MAGIC     .sort("market_time") \
# MAGIC     .write \
# MAGIC     .format("parquet") \
# MAGIC     .mode("overwrite") \
# MAGIC     .saveAsTable("output.market_events")
# MAGIC
# MAGIC B.<br>
# MAGIC python
# MAGIC final_df \
# MAGIC     .orderBy("market_time") \
# MAGIC     .write \
# MAGIC     .format("parquet") \
# MAGIC     .mode("overwrite") \
# MAGIC     .saveAsTable("output.market_events")
# MAGIC
# MAGIC C.<br>
# MAGIC python
# MAGIC final_df \
# MAGIC     .sort("market_time") \
# MAGIC     .coalesce(1) \
# MAGIC     .write \
# MAGIC     .format("parquet") \
# MAGIC     .mode("overwrite") \
# MAGIC     .saveAsTable("output.market_events")
# MAGIC
# MAGIC D.<br>
# MAGIC python
# MAGIC final_df \
# MAGIC     .sortWithinPartitions("market_time") \
# MAGIC     .write \
# MAGIC     .format("parquet") \
# MAGIC     .mode("overwrite") \
# MAGIC     .saveAsTable("output.market_events")

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:237<br>
# MAGIC **In the code block below, aggDf contains aggregations on a streaming DataFrame.**
# MAGIC ```python
# MAGIC     aggDf \
# MAGIC     .writeStream \
# MAGIC     .outputMode("_________") \
# MAGIC     .format("console") \
# MAGIC     .start()
# MAGIC ```
# MAGIC **Which output mode at line 3 ensures that the entire result table is written to the console during each trigger execution?**<br>
# MAGIC A. complete<br>
# MAGIC B. append<br>
# MAGIC C. replace<br>
# MAGIC D. aggregate<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:238<br>
# MAGIC **A data engineer is running a Spark job to process a dataset of 1 TB stored in a distributed storage system (e.g., S3 or ADLS). The cluster has 10 nodes, each with 16 CPUs. The engineer checks the Spark UI and observes the following:**<br>
# MAGIC - The Executors page shows low number of Active Tasks relative to the total available cores.<br>
# MAGIC - The Stages page shows many tasks completed in milliseconds.<br>
# MAGIC - The Jobs page indicates that the number of tasks is significantly smaller than the available CPUs.<br>
# MAGIC
# MAGIC **Which approach should be used to adjust the partitioning for optimal resource allocation?**<br>
# MAGIC A. Set the number of partitions equal to the total number of CPUs in the cluster to fully utilize parallel processing.<br>
# MAGIC B. Set the number of partitions to a fixed value, such as 200, to ensure consistency across jobs.<br>
# MAGIC C. Set the number of partitions equal to the number of nodes in the cluster to balance data across nodes evenly.<br>
# MAGIC D. Set the number of partitions by dividing the dataset size (1 TB) by a reasonable partition size, such as 128 MB.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:239<br>
# MAGIC **What is the behaviour for function `date_sub(start, days)` if a negative value is passed into the days parameter?**<br>
# MAGIC A. The same start date will be returned.<br>
# MAGIC B. An error message of an invalid parameter will be returned.<br>
# MAGIC C. The number of days specified will be added to the start date.<br>
# MAGIC D. The number of days specified will be removed from the start date.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:240<br>
# MAGIC **A data engineer is building an Apache Spark™ Structured Streaming application to process a stream of JSON events in real time. The engineer wants the application to be fault-tolerant and resume processing from the last successfully processed record in case of a failure. To achieve this, the data engineer decides to implement checkpoints.**<br>
# MAGIC **Which code snippet should the data engineer use?**<br>
# MAGIC
# MAGIC A.<br>
# MAGIC python
# MAGIC query = streaming_df.writeStream \
# MAGIC     .format("console") \
# MAGIC     .option("checkpoint", "/path/to/checkpoint") \
# MAGIC     .outputMode("append") \
# MAGIC     .start()
# MAGIC
# MAGIC
# MAGIC B.<br>
# MAGIC python
# MAGIC query = streaming_df.writeStream \
# MAGIC     .format("console") \
# MAGIC     .outputMode("append") \
# MAGIC     .option("checkpointLocation", "/path/to/checkpoint") \
# MAGIC     .start()
# MAGIC
# MAGIC
# MAGIC C.<br>
# MAGIC python
# MAGIC query = streaming_df.writeStream \
# MAGIC     .format("console") \
# MAGIC     .outputMode("complete") \
# MAGIC     .start()
# MAGIC
# MAGIC
# MAGIC D.<br>
# MAGIC python
# MAGIC query = streaming_df.writeStream \
# MAGIC     .format("console") \
# MAGIC     .outputMode("append") \
# MAGIC     .start()

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:241<br>
# MAGIC **A data engineer is running a batch processing job on a Spark cluster with the following configuration:**
# MAGIC
# MAGIC - 10 worker nodes
# MAGIC - 16 CPU cores per worker node
# MAGIC - 64 GB RAM per node
# MAGIC
# MAGIC The data engineer wants to allocate **four executors per node**, each executor using **four cores**.
# MAGIC
# MAGIC **What is the total number of CPU cores used by the application?**<br>
# MAGIC A. 160
# MAGIC B. 64
# MAGIC C. 80
# MAGIC D. 40

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:242<br>
# MAGIC **A developer is working on a Spark application that processes a large dataset using SQL queries. Despite having a large cluster, the developer notices that the job is under utilizing the available resources. Executors remain idle for most of the time, and logs reveal that the number of tasks per stage is very low. The developer suspects that this is causing suboptimal cluster performance.**<br>
# MAGIC **Which action should the developer take to improve cluster utilization?**<br>
# MAGIC A. Increase the value of spark.sql.shuffle.partitions<br>
# MAGIC B. Reduce the value of spark.sql.shuffle.partitions<br>
# MAGIC C. Increase the size of the dataset to create more partitions<br>
# MAGIC D. Enable dynamic resource allocation to scale resources as needed<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:243<br>
# MAGIC **What is the risk associated with this operation when converting an extensive Pandas API on Spark DataFrame back to a Pandas DataFrame?**<br>
# MAGIC A. The conversion will automatically distribute the data across worker nodes.<br>
# MAGIC B. The operation will fail if the Pandas DataFrame exceeds 1000 rows.<br>
# MAGIC C. Data will be lost during conversion.<br>
# MAGIC D. The operation will load all data into the driver's memory, potentially causing memory overflow.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:244<br>
# MAGIC **A developer notices that all the post-shuffle partitions in a dataset are smaller than the value set for** `spark.sql.adaptive.maxShuffledHashJoinLocalMapThreshold`.<br>
# MAGIC **Which type of join will Adaptive Query Execution (AQE) choose in this case?**<br>
# MAGIC A. A Cartesian join<br>
# MAGIC B. A shuffled hash join<br>
# MAGIC C. A broadcast nested loop Join<br>
# MAGIC D. A sort-merge join<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:245<br>
# MAGIC **Which configuration can be enabled to optimize the conversion between Pandas and PySpark DataFrames using Apache Arrow?**<br>
# MAGIC A. `spark.conf.set("spark.pandas.arrow.enabled", "true")`<br>
# MAGIC B. `spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")`<br>
# MAGIC C. `spark.conf.set("spark.sql.execution.arrow.enabled", "true")`<br>
# MAGIC D. `spark.conf.set("spark.sql.arrow.pandas.enabled", "true")`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:246<br>
# MAGIC **A data engineer has written the given code to join two DataFrames dfl and df2:**<br>
# MAGIC ```python
# MAGIC dfl = spark.read.csv("sales_data.csv")
# MAGIC df2 = spark.read.csv("product_data.csv")
# MAGIC result = dfl.join(df2, dfl.product_id == df2.product_id)
# MAGIC ```
# MAGIC **The DataFrame dfl contains e-commerce sales data, which is approximately 10 GB in size, and the DataFrame df2 contains product data, which is approximately 8 MB. Which join strategy will Spark use?**<br>
# MAGIC A. Shuffle join, because AQE is not enabled, and Spark uses a static query plan.<br>
# MAGIC B. Broadcast join, as df2 is smaller than the default broadcast threshold.<br>
# MAGIC C. Shuffle join, as the size difference between dfl and df2 is too large for a broadcast join to work efficiently.<br>
# MAGIC D. Shuffle join because no broadcast hints were provided.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:247<br>
# MAGIC **A Spark application needs to read multiple Parquet files from a directory where the files have differing but compatible schemas. The data engineer wants to create a DataFrame that includes all columns from all files. Which code should the data engineer use to read the Parquet files and include all columns using Apache Spark?**<br>
# MAGIC A. `df = spark.read.option("mergeschema", "true").parquet("/data/parquet_files")`<br>
# MAGIC B. `df = spark.read.parquet("/data/parquet_files").mergeAllcolumns()`<br>
# MAGIC C. `df = spark.read.schema("merge").parquet("/data/parquet_files")`<br>
# MAGIC D. `df = spark.read.format("parquet").load("/data/parquet_files")`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:248  
# MAGIC **A developer wants to test Spark Connect with an existing Spark application.**  
# MAGIC **What are the two alternatives the developer can start a local Spark Connect server without changing their existing application code? (Choose two.)**  
# MAGIC - A. Execute their pyspark shell with the option `--remote "https://localhost"`
# MAGIC - B. Execute their pyspark shell with the option `--remote "sc://localhost"`
# MAGIC - C. Set the environment variable `SPARK_REMOTE="sc://localhost"` before starting the pyspark shell
# MAGIC - D. Add `.remote("sc://localhost")` to their `SparkSession.builder` calls in their Spark code
# MAGIC - E. Ensure the spark property `spark.connect.grpc.binding.port` is set to `15002` in the application code

# COMMAND ----------

# MAGIC %md
# MAGIC    
# MAGIC Question #:249<br>
# MAGIC **A Spark developer is developing a Spark application to monitor task performance across a cluster. One of the application's requirements is to track the maximum processing time for tasks on each worker node and consolidate this information on the driver for further analysis. Which technique should the developer use to achieve this?**<br>
# MAGIC A. Use an RDD action like reduce() to compute the maximum time.<br>
# MAGIC B. Use an accumulator to record the maximum time on the driver.<br>
# MAGIC C. Broadcast a variable to share the maximum time among workers.<br>
# MAGIC D. Configure the Spark UI to automatically collect maximum times.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:250<br>
# MAGIC **A Spark application developer is analyzing the performance of a Spark job involving transformations on a large distributed dataset. The developer needs to identify which operation in the job triggers data shuffling, causing a stage boundary in the Spark execution plan. Which operation results in a shuffle and a new stage in the execution plan?**<br>
# MAGIC A. `DataFrame.groupBy().agg()`<br>
# MAGIC B. `DataFrame.filter()`<br>
# MAGIC C. `DataFrame.withColumn()`<br>
# MAGIC D. `DataFrame.select()`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:251<br>
# MAGIC **Which UDF implementation calculates the length of strings in a Spark DataFrame?**<br>
# MAGIC A. `df.withColumn("length", spark.udf("len", StringType()))`<br>
# MAGIC B. `df.select(length(col("stringColumn")).alias("Length"))`<br>
# MAGIC C. `spark.udf.register("stringLength", lambda s: len(s))`<br>
# MAGIC D. `df.withColumn("length", udf(lambda s: len(s), StringType()))`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:252<br>
# MAGIC **A data engineer observes that the upstream streaming source feeds the event table frequently and sends duplicate records. Upon analyzing the current production table, the data engineer found that the time difference in the** **event_timestamp column of the duplicate records is, at most, 30 minutes.**<br>
# MAGIC **To remove the duplicates, the engineer adds the code:**<br>
# MAGIC `dropDuplicatesWithinWatermark("event_timestamp", "30 minutes")`<br>
# MAGIC **What is the result?**<br>
# MAGIC A. It is not able to handle deduplication in this scenario.<br>
# MAGIC B. It removes duplicates that arrive within the 30-minute window specified by the watermark.<br>
# MAGIC C. It removes all duplicates regardless of when they arrive.<br>
# MAGIC D. It accepts watermarks in seconds and the code results in an error.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:253<br>
# MAGIC **A Data Analyst is working on the employees_df and needs to obtain a list of employees with five or more years of tenure for recognition. Which code snippet filters and shows the list of employees that match the criteria?**<br>
# MAGIC A. `employees_df.filter(employees_df.tenure >= 5).show()`<br>
# MAGIC B. `employees_df.where(employees_df.tenure >= 5)`<br>
# MAGIC C. `filter(employees_df.tenure >= 5)`<br>
# MAGIC D. `employees_df.filter(employees_df.tenure >= 5).collect()`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:254<br>
# MAGIC **Given a CSV file that has the following data inside:**<br>
# MAGIC bambi, hello<br>
# MAGIC alladin, 20<br>
# MAGIC **Given the code fragment:**<br>
# MAGIC ```python
# MAGIC from pyspark.sql.types import *
# MAGIC schema = StructType([StructField("name", StringType()), StructField("age", IntegerType())])
# MAGIC spark.read.schema(schema).csv(path).collect()
# MAGIC ```
# MAGIC **What will be the output of the code?**<br>
# MAGIC A. [Row(name='bambi'), Row(name='alladin', age=20)]<br>
# MAGIC B. [Row(name='alladin', age=20)]<br>
# MAGIC C. [Row(name='bambi', age=None), Row(name='alladin', age=20)]<br>
# MAGIC D. The code throws an error due to a schema mismatch.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:256<br>
# MAGIC **A Data Analyst is working on the sensor_df; this data frame contains two columns: a `record_datetime` (timestamp) and `record` (array<struct<sensor_id: int, status: string, health: string>>). Which code fragment returns a DataFrame that splits the `record` column into separate columns and has one array item per row?**<br>
# MAGIC A.<br>
# MAGIC ```python
# MAGIC exploded_df = sensor_df.withColumn("record_exploded", explode("record"))
# MAGIC exploded_df = exploded_df.select("record_datetime", "sensor_id", "status", "health")
# MAGIC exploded_df = sensor_df.withColumn("record_exploded", col("record"))
# MAGIC ```
# MAGIC B.<br>
# MAGIC ```python
# MAGIC exploded_df = exploded_df.select("record_datetime", "record_exploded.sensor_id", "record_exploded.status", "record_exploded.health")
# MAGIC exploded_df = sensor_df.withColumn("record_exploded", explode("record"))
# MAGIC ```
# MAGIC C.<br>
# MAGIC ```python
# MAGIC exploded_df = exploded_df.select("record_datetime", "record_exploded.sensor_id", "record_exploded.status", "record_exploded.health")
# MAGIC exploded_df = sensor_df.withColumn("record_exploded", explode("record"))
# MAGIC ```
# MAGIC D.<br>
# MAGIC ```python
# MAGIC exploded_df = exploded_df.select("record_datetime", "record_exploded")
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:255<br>
# MAGIC **A Spark application is experiencing performance issues in Client Mode due to the driver being resource-constrained. How should this issue be resolved?**<br>
# MAGIC A. Add more executor instances to the cluster.<br>
# MAGIC B. Increase the driver memory on the client machine.<br>
# MAGIC C. Switch the deployment mode to cluster mode.<br>
# MAGIC D. Switch the deployment mode to local mode.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:257  
# MAGIC **A data engineer needs to write a Streaming DataFrame as parquet files.**
# MAGIC ```python df  
# MAGIC .writeStream  
# MAGIC // -- insert code here --  
# MAGIC .checkpointLocation("path/to/checkpoint/dir")  
# MAGIC .start() 
# MAGIC ``` 
# MAGIC **Which code fragment should be inserted to meet the requirement?**  
# MAGIC A.  
# MAGIC ```python .format("parquet")  
# MAGIC .option("location", "path/to/destination/dir")  
# MAGIC ```
# MAGIC B.  
# MAGIC ```python .format("format", "parquet")  
# MAGIC .option("destination", "path/to/destination/dir")  
# MAGIC ```
# MAGIC C.  
# MAGIC ```python .format("format", "parquet")  
# MAGIC .option("location", "path/to/destination/dir")  
# MAGIC ```
# MAGIC D.  
# MAGIC ```python .format("parquet")  
# MAGIC .option("path", "path/to/destination/dir")
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:258<br>
# MAGIC **A data engineer has noticed that upgrading the Spark version in their applications from Spark 3.0 to Spark 3.5 has improved the runtime of some of their scheduled Spark applications. Looking further, the data engineer realizes that Adaptive Query Execution (AQE) is enabled now.**<br>
# MAGIC **Which operation should AQE be implementing to automatically improve the Spark application performance?**<br>
# MAGIC A. Dynamically switching join strategies<br>
# MAGIC B. Collecting persistent table statistics and storing them in the metastore for future use<br>
# MAGIC C. Improving the performance of single-stage Spark jobs<br>
# MAGIC D. Optimizing the layout of Delta files on disk<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:259<br>
# MAGIC **A data engineer needs to write a Spark job to create a new managed table containing finance data. If the table already exists, then the job should fail without modifying any data. Which save mode and method should the data engineer use?**<br>
# MAGIC A. `saveAsTable` with mode `ErrorIfExists`<br>
# MAGIC B. `saveAsTable` with mode `Overwrite`<br>
# MAGIC C. `save` with mode `Ignore`<br>
# MAGIC D. `save` with mode `ErrorIfExists`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:260<br>
# MAGIC **A data engineer is building a Structured Streaming pipeline that streams data from a Kafka topic.  
# MAGIC While the priority is to have it run at a minimal latency, the engineer also wants to maintain an Exactly-Once processing guarantee in the pipeline. Which trigger mode should the engineer use for their writeStream?**<br>
# MAGIC A. `.trigger(processingTime='1 second')`<br>
# MAGIC B. `.trigger(continuous=True)`<br>
# MAGIC C. `.trigger(continuous='1 second')`<br>
# MAGIC D. `.trigger(availableNow=True)`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:261<br>
# MAGIC **A data engineer is responding to complaints that a feature engineering job has been degrading in performance over time. After some discussion with the data science team using the feature table, it has been decided it is ok to replace the `percentile()` Spark function with the `approx_percentile()` Spark function in order to trade off some accuracy for performance.**<br>
# MAGIC ```python
# MAGIC features_df = raw_df \
# MAGIC     .select(F.approx_percentile("price", percentage=[0.25, 0.5, 0.75], accuracy=1000).alias("price_perc"))
# MAGIC ```
# MAGIC **The initial change to the code does give a greater than expected boost to the job runtime; however, the data scientists are finding the percentiles returned are now drifting too far from the correct values. Which change should the data engineer make to solve the issue?**<br>
# MAGIC A. Decrease the first value of the percentage parameter to increase the accuracy of the percentile ranges<br>
# MAGIC B. Decrease the value of the accuracy parameter in order to decrease the memory usage but also improve the accuracy<br>
# MAGIC C. Increase the last value of the percentage parameter to increase the accuracy of the percentile ranges<br>
# MAGIC D. Increase the value of the accuracy parameter in order to increase the memory usage but also improve the accuracy<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:262<br>
# MAGIC **A data engineer is working on a Spark application that contains two DataFrames:**<br>
# MAGIC - DataFrame A contains detailed transaction records for the last year, with a size of 128 GB.<br>
# MAGIC - DataFrame B contains a lookup table of user details, with a size of 1 GB.<br>
# MAGIC **Considering performance optimization, the developer decides to use a broadcast join.**<br>
# MAGIC **Which strategy should the engineer use for selecting the DataFrame to broadcast?**<br>
# MAGIC A. DataFrame B should be broadcasted because it is smaller and will eliminate the need for shuffling itself.<br>
# MAGIC B. DataFrame B should be broadcasted because it is smaller and will eliminate the need for shuffling DataFrame A<br>
# MAGIC C. DataFrame A should be broadcasted because it is larger and will eliminate the need for shuffling DataFrame B.<br>
# MAGIC D. DataFrame A should be broadcasted because it is smaller and will eliminate the need for shuffling itself.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:263<br>
# MAGIC **Which feature of Spark Connect is considered when designing an application that plans to implement Spark Connect to enable remote interaction with the Spark cluster?**<br>
# MAGIC A. It provides a to run Spark applications remotely in any programming language.<br>
# MAGIC B. It can be used to interact with any remote cluster using the REST API<br>
# MAGIC C. It allows for remote execution of Spark jobs.<br>
# MAGIC D. It is primarily used for data ingestion into Spark from external sources.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:264<br>
# MAGIC **A data engineer uses a broadcast variable to share a DataFrame containing millions of rows across executors for lookup purposes. What will be the outcome?**<br>
# MAGIC A. The job may fail if the memory on each executor is not large enough to accommodate the DataFrame being broadcasted.<br>
# MAGIC B. The job may fail if the executors do not have enough CPU cores to process the broadcasted dataset.<br>
# MAGIC C. The job will hang indefinitely as Spark will struggle to distribute and serialize such a large broadcast variable to all executors.<br>
# MAGIC D. The job may fail because the driver does not have enough CPU cores to serialize the large DataFrame.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:265<br>
# MAGIC **What is a feature of Spark Connect?**<br>
# MAGIC A. It supports DataStreamReader, DataStreamWriter, StreamingQuery Streaming APIs.<br>
# MAGIC B. Supports DataFrame, Functions, Column, SparkContext PySpark APIs.<br>
# MAGIC C. It supports only PySpark applications.<br>
# MAGIC D. It has built-in authentication.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:266<br>
# MAGIC **A data engineer wants to process a streaming DataFrame that receives sensor readings every second with columns `sensor_id`, `temperature`, and `timestamp`. The engineer needs to calculate the average temperature for each sensor over the last 5 minutes while the data is streaming.**<br>
# MAGIC **Which code implementation achieves the requirement?**<br>
# MAGIC A.<br>
# MAGIC ```python
# MAGIC df.withColumn("avg_temp", avg("temperature")
# MAGIC     .over(Window.partitionBy("sensor_id")
# MAGIC     .orderBy("timestamp").rangeBetween(-300, 0)))
# MAGIC ```
# MAGIC B.<br>
# MAGIC ```python
# MAGIC df.groupBy("sensor_id", "timestamp")
# MAGIC     .agg(avg("temperature").alias("avg_temp"))
# MAGIC ```
# MAGIC C.<br>
# MAGIC ```python
# MAGIC df.groupBy("sensor_id").avg("temperature")
# MAGIC ```
# MAGIC D.<br>
# MAGIC ```python
# MAGIC df.withWatermark("timestamp", "5 minutes")
# MAGIC     .groupBy("sensor_id", window("timestamp", "5 minutes"))
# MAGIC     .agg(avg("temperature").alias("avg_temp"))
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:267<br>
# MAGIC **A data engineer is working on the DataFrame:**
# MAGIC ![](/Workspace/Users/nikx2198@gmail.com/Pyspark_leaning/Screenshot 2026-03-19 193910.png)
# MAGIC **Which code fragment should the engineer use to extract the unique values in the Name column into an alphabetically ordered list?**<br>
# MAGIC A. df.select ("Name").orderBy (df ["Name"] .asc ())<br>
# MAGIC B. df.select ("Name") .distinct ().orderBy (df ["Name"])<br>
# MAGIC C. df.select ("Name") .distinct ()<br>
# MAGIC D. df.select ("Name") .distinct ().orderBy(df ["Name"].desc())
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:268  
# MAGIC **A data scientist is working on a large dataset in Apache Spark using PySpark. The data scientist has a DataFrame `df` with columns `user_id`, `product_id`, and `purchase_amount` and needs to perform some operations on this data efficiently. Which sequence of operations results in transformations that require shuffle followed by transformations that do not?**  
# MAGIC A. `df.filter(df.purchase_amount > 100).groupBy("user_id").sum("purchase_amount")`  
# MAGIC B. `df.withColumn("discount", df.purchase_amount * 0.1).select("discount")`  
# MAGIC C. `df.withColumn("purchase_date", current_date()).where("total_purchase > 50")`  
# MAGIC D. `df.groupBy("user_id").agg(sum("purchase_amount").alias("total_purchase")).repartition(10)`

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:269<br>
# MAGIC **An engineer notices a significant increase in the job execution time during the execution of a Spark job. After some investigation, the engineer decides to check the logs produced by the Executors. How should the engineer retrieve the Executor logs to diagnose performance issues in the Spark application?**<br>
# MAGIC A. Locate the executor logs on the Spark master node, typically under the /tmp directory.<br>
# MAGIC B. Use the command `spark-submit` with the `--verbose` flag to print the logs to the console.<br>
# MAGIC C. Use the Spark UI to select the stage and view the executor logs directly.<br>
# MAGIC D. Fetch the logs by running a Spark job with the 'spark-sql' CLI tool.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:270<br>
# MAGIC **A Spark engineer must select an appropriate deployment mode for the Spark jobs.  
# MAGIC What is the benefit of using cluster mode in Apache Spark™?**<br>
# MAGIC A. In cluster mode, resources are allocated from the resource manager on the cluster, enabling better performance and scalability for large jobs.<br>
# MAGIC B. In cluster mode, the driver is responsible for executing all tasks locally without distributing them across the worker nodes.<br>
# MAGIC C. In cluster mode, the driver runs on the client machine, which can limit the application's ability to handle large datasets efficiently.<br>
# MAGIC D. In cluster mode, the driver program runs on one of the worker nodes, allowing the application to fully utilize the distributed resources of the cluster.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:271<br>
# MAGIC **A developer initializes a SparkSession:**<br>
# MAGIC ```python
# MAGIC spark = SparkSession.builder \
# MAGIC     .appName("Analytics Application") \
# MAGIC     .getOrCreate()
# MAGIC ```
# MAGIC **Which statement describes the spark SparkSession?**<br>
# MAGIC A. The getOrCreate() method explicitly destroys any existing SparkSession and creates a new one.<br>
# MAGIC B. A SparkSession is unique for each appName, and calling getOrCreate() with the same name will return an existing SparkSession, once has been created.<br>
# MAGIC C. If a SparkSession already exists, this code will return the existing session instead of creating a new one.<br>
# MAGIC D. A new SparkSession is created every time the getOrCreate() method is invoked.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:272<br>
# MAGIC **The following code fragment results in an error:**<br>
# MAGIC ```python
# MAGIC @F.udf(T.IntegerType())
# MAGIC def simple_udf(t: str) -> str:
# MAGIC     return answer 3.14159
# MAGIC ```
# MAGIC **Which code fragment should be used instead?**<br>
# MAGIC A.<br>
# MAGIC ```python
# MAGIC @F.udf(T.IntegerType())
# MAGIC def simple_udf(t: int) -> int:
# MAGIC     return t * 3.14159
# MAGIC ```
# MAGIC B.<br>
# MAGIC ```python
# MAGIC @F.udf(T.DoubleType())
# MAGIC def simple_udf(t: float) -> float:
# MAGIC     return t * 3.14159
# MAGIC ```
# MAGIC C.<br>
# MAGIC ```python
# MAGIC @F.udf(T.DoubleType())
# MAGIC def simple_udf(t: int) -> int:
# MAGIC     return t * 3.14159
# MAGIC ```
# MAGIC D.<br>
# MAGIC ```python
# MAGIC @F.udf(T.IntegerType())
# MAGIC def simple_udf(t: float) -> float:
# MAGIC     return t * 3.14159
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:273<br>
# MAGIC **A data scientist at a financial services company is working with a Spark DataFrame containing transaction records. The DataFrame has millions of rows and includes columns for `transaction_id`, `account_number`, `transaction_amount`, and `timestamp`. Due to an issue with the source system, some transactions were accidentally recorded multiple times with identical information across all fields. The data scientist needs to remove rows with duplicates across all fields to ensure accurate financial reporting. Which approach should the data scientist use to deduplicate the orders using PySpark?**<br>
# MAGIC A. `df = df.dropDuplicates()`<br>
# MAGIC B. `df = df.groupBy("transaction_id").agg(F.first("account_number"), F.first("transaction_amount"), F.first("timestamp"))`<br>
# MAGIC C. `df = df.filter(F.col("transaction_id").isNotNull())`<br>
# MAGIC D. `df.dropDuplicates(["transaction_amount"])`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:274<br>
# MAGIC **A data engineer needs to write a DataFrame `df` to a Parquet file, partitioned by the column `country`, and overwrite any existing data at the destination path. Which code should the data engineer use to accomplish this task in Apache Spark?**<br>
# MAGIC A. `df.write.mode("overwrite").partitionBy("country").parquet("/data/output")`<br>
# MAGIC B. `df.write.mode("append").partitionBy("country").parquet("/data/output")`<br>
# MAGIC C. `df.write.mode("overwrite").parquet("/data/output")`<br>
# MAGIC D. `df.write.partitionBy("country").parquet("/data/output")`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:275<br>
# MAGIC **A data engineer is working with a large JSON dataset containing order information. The dataset is stored in a distributed file system and needs to be loaded into a Spark DataFrame for analysis. The data engineer wants to ensure that the schema is correctly defined and that the data is read efficiently.**<br>
# MAGIC **Which approach should the data scientist use to efficiently load the JSON data into a Spark DataFrame with a predefined schema?**<br>
# MAGIC A. Use `spark.read.json()` to load the data, then use `DataFrame.printSchema()` to view the inferred schema, and finally use `DataFrame.cast()` to modify column types.<br>
# MAGIC B. Use `spark.read.json()` with the `inferSchema` option set to true.<br>
# MAGIC C. Use `spark.read.format("json").load()` and then use `DataFrame.withColumn()` to cast each column to the desired data type.<br>
# MAGIC D. Define a `StructType` schema and use `spark.read.schema(predefinedSchema).json()` to load the data.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:276<br>
# MAGIC **A data engineer wants to create a Streaming DataFrame that reads from a Kafka topic called `feed`.**<br>
# MAGIC 1. `spark`
# MAGIC 2. `.readStream`
# MAGIC 3. `.format("kafka")`
# MAGIC 4. `.option("kafka.bootstrap.servers", "host1:port1,host2:port2")`
# MAGIC 5. `._________`
# MAGIC 6. `.load()`<br>
# MAGIC **Which code fragment should be inserted in line 5 to meet the requirement?**<br>
# MAGIC A. `.option("subscribe", "feed")`<br>
# MAGIC B. `.option("subscribe.topic", "feed")`<br>
# MAGIC C. `.option("kafka.topic", "feed")`<br>
# MAGIC D. `.option("topic", "feed")`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:277<br>
# MAGIC **A data scientist is working on a project that requires processing large amounts of structured data, performing SQL queries, and applying machine learning algorithms.  
# MAGIC The data scientist is considering using Apache Spark for this task. Which combination of Apache Spark modules should the data scientist use in this scenario?**<br>
# MAGIC A. Spark DataFrames, Structured Streaming, and Graphx<br>
# MAGIC B. Spark SQL, Pandas API on Spark, and Structured Streaming<br>
# MAGIC C. Spark Streaming, GraphX, and Pandas API on Spark<br>
# MAGIC D. Spark DataFrames, Spark SQL, and MLlib<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:278<br>
# MAGIC **A data scientist is working with a Spark DataFrame called `customerDF` that contains customer information. The DataFrame has a column named `email` with customer email addresses. The data scientist needs to split this column into `username` and `domain` parts. Which code snippet splits the `email` column into `username` and `domain` columns?**<br>
# MAGIC A.<br>
# MAGIC `customerDF.select(col("email").substr(0, 5).alias("username"), col("email").substr(-5).alias("domain"))`<br>
# MAGIC B.<br>
# MAGIC `python
# MAGIC customerDF.withColumn("username", split(col("email"), "@").getItem(0))
# MAGIC           .withColumn("domain", split(col("email"), "@").getItem(1))`
# MAGIC
# MAGIC C.<br>
# MAGIC `customerDF.withColumn("username", substring_index(col("email"), "@", 1)).withColumn("domain", substring_index(col("email"), "@", -1))`<br>
# MAGIC D.<br>
# MAGIC `customerDF.select(regexp_replace(col("email"), "@", "").alias("username"), regexp_replace(col("email"), "@", "").alias("domain"))`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:279<br>
# MAGIC **A data engineer is working with Spark SQL and has a large JSON file stored at `/data/input.json`. The file contains records with varying schemas and the engineer wants to create an external table in Spark SQL that directly queries this file without loading it into a DataFrame first.**<br>
# MAGIC **The engineer needs to:**<br>
# MAGIC - Create an external table named `users` that reads data from `/data/input.json`.<br>
# MAGIC - Ensure that Spark infers the schema automatically.<br>
# MAGIC - Handle records with differing schemas by merging them.<br>
# MAGIC **Which code snippet should the data engineer use to accomplish this task?**<br>
# MAGIC A. `CREATE TABLE users USING json OPTIONS (path '/data/input.json')`<br>
# MAGIC B. `CREATE EXTERNAL TABLE users USING json OPTIONS (path '/data/input.json')`<br>
# MAGIC C. `CREATE EXTERNAL TABLE users USING json OPTIONS (path '/data/input.json', mergeSchema 'true')`<br>
# MAGIC D. `CREATE EXTERNAL TABLE users USING json OPTIONS (path '/data/input.json', schemaMerge 'true')`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:280<br>
# MAGIC **A data engineer is implementing a streaming pipeline with watermarking to handle late-arriving records. The engineer has written the following code:**<br>
# MAGIC ```python
# MAGIC inputStream \
# MAGIC     .withWatermark("event_time", "10 minutes") \
# MAGIC     .groupBy(window("event_time", "15 minutes")) \
# MAGIC     .count()
# MAGIC ```
# MAGIC **What happens to data that arrives after the watermark threshold?**<br>
# MAGIC A. Records that arrive later than the watermark threshold (10 minutes) will automatically be included in the aggregation if they fall within the 15-minute window.<br>
# MAGIC B. Any data arriving more than 10 minutes after the watermark threshold will be ignored and not included in the aggregation.<br>
# MAGIC C. Data arriving more than 10 minutes after the latest watermark will still be included in the aggregation but will be placed into the next window.<br>
# MAGIC D. The watermark ensures that late data arriving within 10 minutes of the latest event_time will be processed and included in the windowed aggregation.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:281<br>
# MAGIC **A Developer created a DataFrame with columns `color`, `fruit`, `v1`, and `v2`:**<br>
# MAGIC ```python
# MAGIC df.write.partitionBy("color", "fruit").parquet("/path/to/output")
# MAGIC ```
# MAGIC **What is the result of the code?**<br>
# MAGIC A. It stores all data in a single Parquet file.<br>
# MAGIC B. It throws an error if there are null values in either partition column.<br>
# MAGIC C. It appends new partitions to an existing Parquet file.<br>
# MAGIC D. It creates separate directories for each unique combination of color and fruit.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:282<br>
# MAGIC **Which command overwrites an existing JSON file when writing a DataFrame?**<br>
# MAGIC A. `df.write.mode("overwrite").json("path/to/file")`<br>
# MAGIC B. `df.write.overwrite.json("path/to/file")`<br>
# MAGIC C. `df.write.json("path/to/file", overwrite=True)`<br>
# MAGIC D. `df.write.format("json").save("path/to/file", mode="overwrite")`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:283<br>
# MAGIC **A data scientist is working with a large dataset in Apache Spark and has written the following code:**<br>
# MAGIC ```python
# MAGIC df = spark.read.csv("large_dataset.csv")
# MAGIC filtered_df = df.filter(col("error_column").contains("error"))
# MAGIC mapped_df = filtered_df.select(
# MAGIC     split(col("timestamp"), "").getItem(0).alias("date"),
# MAGIC     lit(1).alias("count")
# MAGIC )
# MAGIC reduced_df = mapped_df.groupBy("date").sum("count")
# MAGIC reduced_df.count()
# MAGIC reduced_df.show()
# MAGIC ```
# MAGIC **At which point in this code will Spark actually begin processing the data?**<br>
# MAGIC A. When the filter transformation is applied<br>
# MAGIC B. When the count action is applied<br>
# MAGIC C. When the groupBy transformation is applied<br>
# MAGIC D. When the show action is applied<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:284<br>
# MAGIC **A data engineer has identified duplicate records in one of the Parquet tables built from ingesting some IoT data.  
# MAGIC The records in the table have the following schema:**<br>
# MAGIC - `event_ts` TIMESTAMP  
# MAGIC - `sensor_id` STRING  
# MAGIC - `metric_value` LONG  
# MAGIC - `ingest_ts` TIMESTAMP  
# MAGIC - `source_file_path` STRING  
# MAGIC
# MAGIC **When events are produced at each IoT sensor, they have the fields `event_ts`, `sensor_id`, and `metric_value`. The ingestion process adds the `ingest_ts` and `source_file_path` fields to each record. Analysis shows that the ingestion process is introducing duplicate records.**<br>
# MAGIC
# MAGIC A. `dedup_df = iot_bronze_df.dropDuplicates({"ingest_ts", "sensor_id", "metric_value", "source_file_path"})`<br>
# MAGIC B. `dedup_df = iot_bronze_df.dropDuplicates()`<br>
# MAGIC C. `dedup_df = iot_bronze_df.groupBy({"event_ts", "sensor_id", "metric_value"})`<br>
# MAGIC D. `dedup_df = iot_bronze_df.dropDuplicates({"event_ts", "sensor_id", "metric_value"})`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:285<br>
# MAGIC **An engineer has two dataframes `df1` and `df2`, with `df1` being small and `df2` being large. To optimize the join, the engineer uses a broadcast join:**<br>
# MAGIC ```python
# MAGIC from pyspark.sql.functions import broadcast
# MAGIC result = df2.join(broadcast(df1), on='id', how='inner')
# MAGIC ```
# MAGIC **What is the purpose of using `broadcast()` in this scenario?**<br>
# MAGIC A. It filters the id values before performing the join.<br>
# MAGIC B. It increases the partition size for df1 and df2.<br>
# MAGIC C. It reduces the number of shuffle operations by replicating the smaller dataframe to all nodes.<br>
# MAGIC D. It ensures that the join happens only when the id values are identical.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:286<br>
# MAGIC **A data engineer notices that a Spark application is running slowly because of a large number of small tasks caused by too many partitions in a DataFrame.  
# MAGIC How can the data engineer reduce the number of partitions to improve performance without causing a full shuffle?**<br>
# MAGIC A. Use the `distinct()` transformation to combine similar partitions.<br>
# MAGIC B. Use the `coalesce()` transformation with a lower number of partitions.<br>
# MAGIC C. Use the `sortBy()` transformation to reorganize the data.<br>
# MAGIC D. Use the `repartition()` transformation with a lower number of partitions.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:287<br>
# MAGIC **A data engineering team is deciding on technical stacks for its big data processing needs. The team requires a framework that excels in large-scale data processing, offers high-level APIs for SQL queries, and efficiently handles both batch and streaming data workloads. Which two advantages does Apache Spark™ offer in this scenario? (Choose two.)**<br>
# MAGIC A. It uses a serverless architecture, eliminating the need for cluster management.<br>
# MAGIC B. It seamlessly integrates with web development frameworks for building front-end applications.<br>
# MAGIC C. It excels at distributed machine learning model training that is out of the box.<br>
# MAGIC D. It provides built-in support for SQL queries through Spark SQL.<br>
# MAGIC E. It offers mature APIs for DataFrames and Datasets for data manipulation.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:288  
# MAGIC **What is the relationship between jobs, stages, and tasks during execution in Apache Spark?**  
# MAGIC A. A job contains multiple stages, and each stage contains multiple tasks.  
# MAGIC B. A job contains multiple tasks, and each task contains multiple stages  
# MAGIC C. A stage contains multiple jobs, and each job contains multiple tasks.  
# MAGIC D. A stage contains multiple tasks, and each task contains multiple jobs.

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:289<br>
# MAGIC **What is the benefit of using Pandas on Spark for Data Transformations?**<br>
# MAGIC A. It is available only with Python, thereby reducing the learning curve.<br>
# MAGIC B. It computes results immediately using eager execution, making it simple to use.<br>
# MAGIC C. It runs on a single node only, utilizing the memory with memory-bound DataFrames and hence cost-efficient.<br>
# MAGIC D. It executes queries faster using all the available cores in the cluster as well as provides Pandas's rich set of features.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:290<br>
# MAGIC **A data scientist wants to ingest a directory full of plain text files so that each record in the output DataFrame contains the entire contents of a single file and the full path of the file the text was read from. The first attempt at the code does read the text files but each record contains a single line. This code is shown below:**<br>
# MAGIC ```python
# MAGIC raw_txt_path = '/datasets/raw_txt/*'
# MAGIC corpus = spark.read.text(raw_txt_path)\
# MAGIC     .select("*", "_metadata.file_path")
# MAGIC ```
# MAGIC **Which code change can be implemented in a DataFrame that meets the data scientist's requirements?**<br>
# MAGIC A. Add the option `wholetext=True` to the `text()` function<br>
# MAGIC B. Add the option `linesep="\n"` to the `text()` function<br>
# MAGIC C. Add the option `wholetext=False` to the `text()` function<br>
# MAGIC D. Add the option `lineSep=","` to the `text()` function<br>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #:291<br>
# MAGIC **Which Spark configuration controls the number of tasks that can run in parallel on the executor?**<br>
# MAGIC A. `spark.executor.cores`<br>
# MAGIC B. `spark.task.maxFailures`<br>
# MAGIC C. `spark.driver.cores`<br>
# MAGIC D. `spark.executor.memory`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:292<br>
# MAGIC **How can a Spark developer ensure optimal resource utilization when running Spark jobs in Local Mode for testing?**<br>
# MAGIC A. Configure the application to run in cluster mode instead of local mode.<br>
# MAGIC B. Increase the number of local threads based on the number of CPU cores.<br>
# MAGIC C. Use the spark.dynamicAllocation.enabled property to scale resources dynamically.<br>
# MAGIC D. Set the spark.executor.memory property to a large value.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:293<br>
# MAGIC **A data analyst is working on a DataFrame named `dates_df` and needs to add a new column, `date`, derived from the `timestamp` field. Which code fragment should be used to extract the date from a timestamp?**<br>
# MAGIC A. `dates_df.withColumn("date", f.unix_timestamp("timestamp")).show()`<br>
# MAGIC B. `dates_df.withColumn("date", f.to_date("timestamp")).show()`<br>
# MAGIC C. `dates_df.withColumn("date", f.date_format("timestamp", "yyyy-MM-dd")).show()`<br>
# MAGIC D. `dates_df.withColumn("date", f.from_unixtime("timestamp")).show()`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:294<br>
# MAGIC **A data engineer is working on a real-time analytics pipeline using Apache Spark Structured Streaming. The engineer wants to process incoming data and ensure that triggers control when the query is executed. The system needs to process data in micro-batches with a fixed interval of 5 seconds.**<br>
# MAGIC **Which code snippet the data engineer could use to fulfil this requirement?**<br>
# MAGIC A.<br>
# MAGIC ```python
# MAGIC query = df.writeStream
# MAGIC     .outputMode("append")
# MAGIC     .trigger(continuous="5 seconds")
# MAGIC     .start()
# MAGIC ```
# MAGIC B.<br>
# MAGIC ```python
# MAGIC query = df.writeStream
# MAGIC     .outputMode("append")
# MAGIC     .trigger()
# MAGIC     .start()
# MAGIC ```
# MAGIC C.<br>
# MAGIC ```python
# MAGIC query = df.writeStream
# MAGIC     .outputMode("append")
# MAGIC     .trigger(processingTime="5 seconds")
# MAGIC     .start()
# MAGIC ```
# MAGIC D.<br>
# MAGIC ```python
# MAGIC query = df.writeStream
# MAGIC     .outputMode("append")
# MAGIC     .trigger(processingTime=5000)
# MAGIC     .start()
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:295<br>
# MAGIC **A data scientist has been investigating user profile data to build features for their model. After some exploratory data analysis the data scientist has identified that some records in the user profiles contain NULL values in too many fields to be useful. The schema of the user profile table looks like this:**<br>
# MAGIC `user_id STRING,`<br>
# MAGIC `username STRING,`<br>
# MAGIC `full_name STRING,`<br>
# MAGIC `date_of_birth DATE,`<br>
# MAGIC `primary_email STRING,`<br>
# MAGIC `created_ts TIMESTAMP,`<br>
# MAGIC `updated_ts TIMESTAMP,`<br>
# MAGIC `last_login_ts TIMESTAMP`<br>
# MAGIC **The data scientist has decided that if any record contains a NULL value for any field, the data scientist wants to remove that record from the output before further processing.**<br>
# MAGIC **Which block of Spark code can be used to achieve these requirements?**<br>
# MAGIC A. `filtered_df = users_raw_df.na.drop(thresh=0)`<br>
# MAGIC B. `filtered_df = users_raw_df.na.drop(how='all')`<br>
# MAGIC C. `filtered_df = users_raw_df.na.drop(how='any')`<br>
# MAGIC D. `filtered_df = users_raw_df.na.drop(how='all', thresh=None)`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:296<br>
# MAGIC **A data engineer needs to persist a file-based data source to a specific location. However, upon review, the data is also stored in the warehouse directory by default.  
# MAGIC Which line of code should the data engineer use to ensure the data is saved to a specific location instead of the default warehouse directory?**<br>
# MAGIC A. `users.write(path="/some/path").saveAsTable("default_table")`<br>
# MAGIC B. `users.write.saveAsTable("default_table").option("path", "/some/path")`<br>
# MAGIC C. `users.write.option("path", "/some/path").saveAsTable("default_table")`<br>
# MAGIC D. `users.write.saveAsTable("default_table", path="/some/path")`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:297<br>
# MAGIC **A Data Engineer created the view `users_vw` using the code:**<br>
# MAGIC ```python
# MAGIC df.createOrReplaceTempView("users_vw")
# MAGIC ```
# MAGIC **Which approach can be used to query the `users_vw` view after the session is terminated?**<br>
# MAGIC A. Query the `users_vw` using Spark.<br>
# MAGIC B. Persist the `users_vw` data as a table.<br>
# MAGIC C. Recreate the `users_vw` and query the data using Spark.<br>
# MAGIC D. Save the `users_vw` definition and query using Spark.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:298<br>
# MAGIC **A developer wants to refactor some older Spark code in order to take advantage of built-in functions introduced in Spark 3.5.0.  
# MAGIC The developer comes across the following existing DataFrame code:**<br>
# MAGIC ```python
# MAGIC import pyspark.sql.functions as F
# MAGIC min_price = 110.50
# MAGIC result_df = prices_df \
# MAGIC     .filter(F.col("spot_price") >= F.lit(min_price)) \
# MAGIC     .agg(F.count("*"))
# MAGIC ```
# MAGIC **Which code block should the developer use to refactor the code?**<br>
# MAGIC A.<br>
# MAGIC ```python
# MAGIC result_df = prices_df \
# MAGIC     .withColumn("valid_price", F.when(F.col("spot_price") > F.lit(min_price), 1).otherwise(0))
# MAGIC ```
# MAGIC B.<br>
# MAGIC ```python
# MAGIC result_df = prices_df \
# MAGIC     .agg(F.count_if(F.col("spot_price") >= F.lit(min_price)))
# MAGIC ```
# MAGIC C.<br>
# MAGIC ```python
# MAGIC result_df = prices_df \
# MAGIC     .agg(F.min("spot_price"), F.max("spot_price"))
# MAGIC ```
# MAGIC D.<br>
# MAGIC ```python
# MAGIC result_df = prices_df \
# MAGIC     .agg(F.count("spot_price").alias("spot_price")) \
# MAGIC     .filter(F.col("spot_price") > F.it("min_price"))
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:299<br>
# MAGIC **What is the benefit of Adaptive Query Execution (AQE)?**<br>
# MAGIC A. It allows Spark to optimize the query plan before execution but does not adapt during runtime.<br>
# MAGIC B. It enables the adjustment of the query plan during runtime, handling skewed data, optimizing join strategies, and improving overall query performance.<br>
# MAGIC C. It optimizes query execution by parallelising tasks and does not adjust strategies based on runtime metrics like data skew.<br>
# MAGIC D. It automatically distributes tasks across nodes in the clusters and does not perform runtime adjustments to the query plan.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:300<br>
# MAGIC **A data scientist is working on a large-scale data analysis project using Apache Spark on Databricks. The data scientist needs to join a large DataFrame containing customer transactions (200 million rows) with a smaller DataFrame containing product information (3000 rows). How should the data scientist optimize the join operation for better performance?**<br>
# MAGIC A. Perform broadcast join by broadcasting the larger DataFrame<br>
# MAGIC B. Perform a Sort-Merge Join join operation, pre-sorting the DataFrames before the join<br>
# MAGIC C. Perform a shuffle hash join, evenly distributing both DataFrames across the cluster<br>
# MAGIC D. Perform a broadcast join by broadcasting the smaller DataFrame<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:301<br>
# MAGIC **A data engineer creates a large Spark DataFrame `df` with 1000 partitions and needs to reduce it to 100 partitions. Which method provides the option to reduce the partition count without reshuffling the data across the partitions?**<br>
# MAGIC A. `new_df = df.repartition(100)`<br>
# MAGIC B. `new_df = df.limit(100)`<br>
# MAGIC C. `new_df = df.head(100)`<br>
# MAGIC D. `new_df = df.coalesce(100)`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:302<br>
# MAGIC **To improve performance, a developer decides to reduce the number of partitions of a data frame to 100. The developer must choose between using `coalesce()` or `repartition()` for this operation. What will be the behavior of these two functions?**<br>
# MAGIC A. `coalesce()` minimizes shuffling by merging partitions, while `repartition()` performs a full shuffle.<br>
# MAGIC B. Both methods shuffle the data across the cluster evenly.<br>
# MAGIC C. Both methods preserve the existing partitioning and require the same amount of memory.<br>
# MAGIC D. `coalesce()` performs a full shuffle, whereas `repartition()` minimizes shuffling.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:303<br>
# MAGIC **Which feature of Apache Spark's execution model is responsible for deferring the execution of transformations and optimizing the execution plan before an action is triggered?**<br>
# MAGIC A. Immediate Execution<br>
# MAGIC B. Lazy Evaluation with the Catalyst Optimizer<br>
# MAGIC C. Transformations Pre-Caching<br>
# MAGIC D. Parallel Execution of Transformations<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:304<br>
# MAGIC **A data engineer is optimizing a Spark application that performs the following operations in sequence:**<br>
# MAGIC 1. Reads data from distributed storage into a DataFrame.<br>
# MAGIC 2. Applies a filter transformation to remove certain records.<br>
# MAGIC 3. Performs a join operation with another large DataFrame.<br>
# MAGIC 4. Applies a groupBy and agg to aggregate data.<br>
# MAGIC 5. Writes the result to storage.<br>
# MAGIC **Which two statements describe how Apache Spark constructs the execution hierarchy for this application? (Choose two.)**<br>
# MAGIC A. The groupBy and agg operations may cause a shuffle, resulting in additional stages.<br>
# MAGIC B. The application will execute as a single job initiated by the write action.<br>
# MAGIC C. The DataFrame API eliminates all shuffles through automatic optimization.<br>
# MAGIC D. The join operation causes a shuffle, leading to a new stage in the execution plan.<br>
# MAGIC E. The filter and join transformations, are executed in the same stage because they are narrow transformations.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:305<br>
# MAGIC **A data analyst at an e-commerce company needs to process daily sales data. The data consists of approximately 50,000 records stored in a single CSV file, totaling about 20 MB. The analyst needs to perform aggregations and generate a summary report. Which approach could the data analyst use in this situation?**<br>
# MAGIC A. Deploy a real-time streaming solution using Spark Streaming to process incoming data.<br>
# MAGIC B. Use a local Python script with the pandas library to read and analyze the CSV file.<br>
# MAGIC C. Implement Apache Spark with a distributed cluster to process the data in parallel.<br>
# MAGIC D. Set up a Hadoop ecosystem with HDFS and MapReduce for distributed processing.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:306<br>
# MAGIC **A DataFrame has null values in the `salary` column.  
# MAGIC Which command will replace all null values in this column with the value 0?**<br>
# MAGIC A. `df.fillna("salary", 0)`<br>
# MAGIC B. `df.replaceNulls("salary", 0)`<br>
# MAGIC C. `df.dropna(subset=["salary"])`<br>
# MAGIC D. `df.fillna({"salary": 0})`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:307<br>
# MAGIC **What is a characteristic of client mode in Apache Spark?**<br>
# MAGIC A. In client mode, tasks are distributed to worker nodes directly from the client, improving performance due to reduced communication overhead.<br>
# MAGIC B. In client mode, the driver runs on the client machine, which can lead to higher latency due to network overhead.<br>
# MAGIC C. In client mode, the driver runs on the cluster manager, allowing for resources to be utilized across multiple machines.<br>
# MAGIC D. In client mode, the driver runs on the machine that submits the application, making easier to debug but potentially limiting resource availability.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:308<br>
# MAGIC **Given the code fragment:**<br>
# MAGIC ```python
# MAGIC div_by_2 = my_df.filter("number % 2 = 0")
# MAGIC print(div_by_2)
# MAGIC ```
# MAGIC **The output of the code fragment is:**<br>
# MAGIC `DataFrame [number: bigint]`<br>
# MAGIC **What describes the output for this transformation on the Apache Spark engine?**<br>
# MAGIC A. The filter transformation triggers an immediate computation and action returning only rows that match the condition.<br>
# MAGIC B. All transformations in Spark are lazy, in that they do not compute their results right away.<br>
# MAGIC C. After each transformation in Spark the results are processed using an action.<br>
# MAGIC D. The filter is an action in Spark; it immediately executes the filtering operation on my_df and returns the results as div_by_2.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:309<br>
# MAGIC **A developer has a file `employee.csv`, with columns ID, Name, and Salary. The developer wants to load the file into a DataFrame and explicitly specify that the columns should be interpreted as integer, string, and float types, respectively. Which code snippet solves this?**<br>
# MAGIC A.<br>
# MAGIC ```python
# MAGIC schema = StructType([
# MAGIC     StructField("ID", IntegerType(), True),
# MAGIC     StructField("Name", StringType(), True),
# MAGIC     StructField("Salary", FloatType(), True)
# MAGIC ])
# MAGIC df = spark.read.option("header", "true").csv("employee.csv")
# MAGIC ```
# MAGIC B.<br>
# MAGIC ```python
# MAGIC df = spark.read.option("inferSchema", "true").csv("employee.csv")
# MAGIC ```
# MAGIC C.<br>
# MAGIC ```python
# MAGIC df = spark.read.option("header", "true").csv("employee.csv", schema="ID INT, Name STRING, Salary FLOAT")
# MAGIC ```
# MAGIC D.<br>
# MAGIC ```python
# MAGIC schema = StructType([
# MAGIC     StructField("ID", IntegerType(), True),
# MAGIC     StructField("Name", StringType(), True),
# MAGIC     StructField("Salary", FloatType(), True)
# MAGIC ])
# MAGIC df = spark.read.option("header", "true").csv("employee.csv", schema=schema)
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:310<br>
# MAGIC **A data engineer works with streaming data, where records arrive randomly. The engineer needs to de-duplicate records based on `order_id` while ensuring that the latest records are kept in the stream. Which strategy should the engineer use for de-duplicating records while considering late-arriving data and managing memory usage?**<br>
# MAGIC A. Apply `withWatermark()` and then use `dropDuplicates()` on `order_id` to remove duplicates.<br>
# MAGIC B. Use `dropDuplicates()` on `timestamp` to remove duplicates based on the most recent timestamp.<br>
# MAGIC C. Deduplication is not supported in streaming while accounting for late-arriving data.<br>
# MAGIC D. Use `dropDuplicates()` on `order_id` without watermarking to remove all duplicates.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:311<br>
# MAGIC **Given two DataFrames `df1` and `df2`:**<br>
# MAGIC ```python
# MAGIC df1 = spark.createDataFrame([(1, 'Alice', 1000), (2, 'Bob', 1500)], ['id', 'name', 'salary'])
# MAGIC df2 = spark.createDataFrame([(1, 'Alice', 'HR'), (2, 'Charlie', 'Engineering')], ['id', 'name', 'dept'])
# MAGIC # Perform the join.
# MAGIC joined_df = df1.join(df2, x)
# MAGIC ```
# MAGIC **Which code fragment can be replaced at `x` to perform an inner join on the columns `id` and `name` ensuring that both columns match between the DataFrames?**<br>
# MAGIC A. `(df1.id == df2.id) & (df1.name == df2.name)`<br>
# MAGIC B. `(df1.id == df2.id)`<br>
# MAGIC C. `['id', 'dept']`<br>
# MAGIC D. `['id']`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:312<br>
# MAGIC **A developer needs to manipulate large-scale structured data and the data is too big to fit into the memory of a single machine. The developer also needs to execute queries for complex aggregations and transformations. Which two Apache Spark modules provide the required functionalities? (Choose two.)**<br>
# MAGIC A. Structured Streaming<br>
# MAGIC B. Spark SQL<br>
# MAGIC C. DataFrames<br>
# MAGIC D. GraphX<br>
# MAGIC E. MLib<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:313<br>
# MAGIC **A data engineer needs to overwrite the existing underlying data on the path `path/to/data`.  
# MAGIC Which code should be used to overwrite the underlying data on the target location?**<br>
# MAGIC A. `INSERT 'path/to/data' USING delta OPTIONS (coll 1, col2 2, col3 'test') SELECT * FROM source_data;`<br>
# MAGIC B. `INSERT OVERWRITE DIRECTORY 'path/to/data' USING delta OPTIONS (coll 1, col2 2, col3 'test') SELECT * FROM source_data;`<br>
# MAGIC C. `INSERT OVERWRITE 'path/to/data' USING delta OPTIONS (coll 1, co12 2, col3 'test') SELECT * FROM source_data;`<br>
# MAGIC D. `OVERWRITE 'path/to/data' USING delta OPTIONS (coll 1, col2 2, col3 'test') SELECT * FROM source_data;`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:314<br>
# MAGIC **A developer wants to write data as parquet with `name` and `platform` column values in the file `devices.json`. The developer created the code with three placeholders: X, Y, and Z:**<br>
# MAGIC ```python
# MAGIC devices_df = spark.read.json("devices.json")
# MAGIC devices_df.createOrReplaceTempView("devices")
# MAGIC spark.sql("SELECT name, platform FROM X").Y.Z("names.parquet", format="parquet")
# MAGIC ```
# MAGIC **What should be replaced at X, Y, and Z placeholders, respectively, to meet the requirement?**<br>
# MAGIC A. devices_df, write, save<br>
# MAGIC B. devices, save, write<br>
# MAGIC C. devices, write, saveAsTable<br>
# MAGIC D. devices, write, save<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:315<br>
# MAGIC **What happens if a developer registers two DataFrames with the same view name, `myView` using the `createOrReplaceTempView` function?**<br>
# MAGIC A. Both DataFrames will be accessible under the same view name.<br>
# MAGIC B. The DataFrames merged into one under the view name `myView`.<br>
# MAGIC C. An Exception is thrown, indicating a duplicate view named `myView`.<br>
# MAGIC D. The previous view will be replaced by the new DataFrame's view.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:316<br>
# MAGIC **A data engineer needs to control the size of micro-batches when running with the option of Available-now micro-batch.  
# MAGIC Which trigger should the engineer use?**<br>
# MAGIC A. `maxExecutorsPerTrigger`<br>
# MAGIC B. `maxCoresPerTrigger`<br>
# MAGIC C. `maxBytesPerTrigger`<br>
# MAGIC D. `maxFilesPerTrigger`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:317<br>
# MAGIC **How does the Directed Acyclic Graph (DAG) represent the execution hierarchy in Apache SparkTM?**<br>
# MAGIC A. It represents the execution of multiple jobs, where each job runs independently of stages and tasks.<br>
# MAGIC B. It represents the execution of a job as a series of interdependent stages, each broken into parallel tasks.<br>
# MAGIC C. It represents the tasks executed by Spark as individual jobs, with each job containing multiple applications.<br>
# MAGIC D. It represents only the final tasks without considering stages or jobs.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:318<br>
# MAGIC **A data engineer has a PySpark DataFrame named `sales_data` containing millions of rows.  
# MAGIC They need to calculate the total sales amount grouped by region using Spark SQL for improved readability and maintainability.  
# MAGIC Which steps should the data engineer take to achieve this?**<br>
# MAGIC A. Write the query directly on the DataFrame using PySpark's `groupBy` and `agg` methods.<br>
# MAGIC B. Export the DataFrame as a CSV file, read it into a relational database, and write SQL queries in the database.<br>
# MAGIC C. Use the `createOrReplaceTempView` method to register `sales_data` as a temporary view and write the query in Spark SQL.<br>
# MAGIC D. Convert `sales_data` to Pandas DataFrame and use SQL-like queries with Pandas to achieve the grouping.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:319<br>
# MAGIC **An organization has been running a Spark application in production and is considering disabling the Spark History Server to reduce resource usage.  
# MAGIC What will be the impact of disabling the Spark History Server in a production environment?**<br>
# MAGIC A. Prevention of Driver log accumulation during long-running jobs<br>
# MAGIC B. Improved job execution speed due to reduced logging overhead<br>
# MAGIC C. Loss of access to past job logs and reduced debugging capability for completed jobs<br>
# MAGIC D. Enhanced Executor performance due to reduced log size<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:320<br>
# MAGIC **A parquet file has two columns called `name` and `address` of type String.  
# MAGIC What will be the schema of the resulting DataFrame:**<br>
# MAGIC ```python
# MAGIC df = spark.read.parquet("path/to/file")
# MAGIC ```
# MAGIC A. `name: String, address: String`<br>
# MAGIC B. `c0: String`<br>
# MAGIC C. `Name: String, Address: String`<br>
# MAGIC D. `c0: String, c2: String`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:321<br>
# MAGIC **A developer is analyzing a DataFrame `df_epoch_time` with a column `epoch_time` containing Unix epoch time. Unix epoch time is a timestamp in seconds since January 1, 1970, 00:00:00 UTC. The developer wants to extract the month from the column and add it as a new column `month`.**<br>
# MAGIC **Which code block achieves this requirement?**<br>
# MAGIC A. `df_epoch_time = df_epoch_time.withColumn("month", from_unixtime("epoch_time").substr(4,2))`<br>
# MAGIC B. `df_epoch_time = df_epoch_time.withColumn("month", month(from_unixtime("epoch_time")))`<br>
# MAGIC C. `df_epoch_time = df_epoch_time.withColumn("month", month(("epoch_time")))`<br>
# MAGIC D. `df_epoch_time = df_epoch_time.withColumn("month", col("epoch_time").substr(6,2))`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:322<br>
# MAGIC **A data engineer has been inspecting one of their scheduled Spark applications which has started running slowly on the most recent executions.  
# MAGIC Looking at the query plan the engineer notices that Adaptive Query Execution (AQE) is no longer converting one of their join operations from a sort-merge join to a broadcast join, causing extra shuffling in the Spark job.  
# MAGIC What explains the change in the behaviour of the application?**<br>
# MAGIC A. The size of the smallest table has grown larger than the configured threshold where AQE will convert the join to a broadcast join.<br>
# MAGIC B. It has been too long since ANALYZE TABLE has been run on the tables and the table statistics are stale.<br>
# MAGIC C. A Spark version upgrade has disabled AQE.<br>
# MAGIC D. The distribution of the join keys between the two tables has become more skewed over time.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:323<br>
# MAGIC **The database administrator team has informed an application support engineer that a Spark application is creating too many connections to one of their PostgreSQL databases. The engineer looks at the Spark application's source code and sees the following code is used to read from the PostgreSQL Database.**<br>
# MAGIC ```SQL
# MAGIC SET spark.sql.shuffle.partitions=1007;
# MAGIC CREATE TEMPORARY VIEW sales_fct
# MAGIC USING org.apache.spark.sql.jdbc
# MAGIC OPTIONS (
# MAGIC   url "jdbc:postgresql://pgdb1:5432/dw",
# MAGIC   dbtable "dw.sales_fct",
# MAGIC   user "sparkrep01",
# MAGIC   password "G7xPq9vL2M",
# MAGIC   numPartitions "25",
# MAGIC   partitionColumn "sales_id",
# MAGIC   lowerBound "1",
# MAGIC   upperBound "10000"
# MAGIC )
# MAGIC ```
# MAGIC **Which change to the code will reduce the number of connections the Spark application is making to the PostgreSQL database?**<br>
# MAGIC A. Reduce the value of the numPartitions option from 25 to 8<br>
# MAGIC B. Raise the value of the upperBound option from 10,000 to 100,000 to increase the partition stride<br>
# MAGIC C. Reduce the value of the spark.sql.shuffle.partitions property from 100 to 8<br>
# MAGIC D. Change the value of the partitionColumn option from sales_id to a PostgreSQL column that has an index available<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:324<br>
# MAGIC **A data scientist is working with a massive dataset that exceeds the memory capacity of a single machine.  
# MAGIC The data scientist is considering using Apache SparkTM instead of processing the data using traditional single-machine programming languages like standard Python scripts.  
# MAGIC Which two advantages does Apache SparkTM offer over a normal single-machine language in this scenario? (Choose two.)**<br>
# MAGIC A. It eliminates the need to write any code, automatically handling all data processing.<br>
# MAGIC B. It has built-in fault tolerance, allowing it to recover seamlessly from node failures during computation.<br>
# MAGIC C. It processes data solely on disk storage, reducing the need for memory resources.<br>
# MAGIC D. It can distribute data processing tasks across a cluster of machines, enabling horizontal scalability.<br>
# MAGIC E. It requires specialized hardware to run, making it unsuitable for commodity hardware clusters.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:325<br>
# MAGIC **The data engineering team created a pipeline that extracts data from a transaction system. The transaction system has timestamps stored in UTC so the data engineers  
# MAGIC ingested the timestamps in the raw DataFrame in UTC. The data engineers must now transform the transaction_datetime to the "America/New_York" timezone to  
# MAGIC create reports accurately.**<br>
# MAGIC **Which code should be used to convert the transaction_datetime?**<br>
# MAGIC A. `raw.withColumn("transaction_datetime", from_utc_timestamp(col("transaction_datetime"), "America/New_York"))`<br>
# MAGIC B. `raw.withColumn("transaction_datetime", date_format(col("transaction_datetime"), "America/New_York"))`<br>
# MAGIC C. `raw.withColumn("transaction_datetime", to_utc_timestamp(col("transaction_datetime"), "America/New_York"))`<br>
# MAGIC D. `raw.withColumn("transaction_datetime", from_utc_timestamp(col("transaction_datetime")))`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:326<br>
# MAGIC **A data scientist at a large e-commerce company needs to process and analyze 2 TB of daily customer transaction data.  
# MAGIC The company wants to implement real-time fraud detection and personalized product recommendations.  
# MAGIC To process their data the company uses a traditional relational database system, which is struggling to handle the increasing data volume and velocity.**<br>
# MAGIC **Which feature of Apache Spark effectively addresses the challenge posed in this scenario?**<br>
# MAGIC A. Ability to process small datasets efficiently<br>
# MAGIC B. Support for SQL queries on structured data<br>
# MAGIC C. In-memory computation and parallel processing capabilities<br>
# MAGIC D. Built-in machine learning libraries<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:327<br>
# MAGIC **A Data Analyst is working on the `employees_df` and needs to add a new column where a 10% tax is calculated on the salary. Additionally, the DataFrame contains the column `age`, which is not needed.**<br>
# MAGIC **Which code fragment adds the tax column and removes the age column?**<br>
# MAGIC A.<br>
# MAGIC `employees_df = employees_df.withColumn("tax", employees_df.salary * 10).dropField(age)`<br>
# MAGIC B.<br>
# MAGIC `employees_df = employees_df.withColumn("tax", employees_df.salary * 0.1).drop("age")`<br>
# MAGIC C.<br>
# MAGIC `employees_df = employees_df.withColumn("tax", lit(0.1) * col("salary")).dropField("age")`<br>
# MAGIC D.<br>
# MAGIC `employees_df = employees_df.withColumn("tax", employees_df.salary * 10).drop("age")`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Question #:328<br>
# MAGIC **A data engineer is investigating a Spark cluster that is experiencing underutilization during scheduled batch jobs.  
# MAGIC After checking the Spark logs, they noticed that tasks are often getting killed due to timeout errors, and there are several warnings about insufficient resources in the logs.  
# MAGIC Which action should the engineer take to resolve the underutilization issue?**<br>
# MAGIC A. Increase the executor memory allocation in the Spark configuration.<br>
# MAGIC B. Set the spark.network.timeout property to allow tasks more time to complete without being killed.<br>
# MAGIC C. Increase the number of executor instances to handle more concurrent tasks.<br>
# MAGIC D. Reduce the size of the data partition to improve task scheduling.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:329<br>
# MAGIC **An application architect has been investigating Spark Connect as a way to modernize the existing Spark applications running in their organization.  
# MAGIC Which requirement blocks the adoption of Spark Connect in this organization?**<br>
# MAGIC A. Debuggability: the ability to perform interactive debugging directly from the application code<br>
# MAGIC B. Stability: isolation of application code and dependencies from each other and the Spark driver<br>
# MAGIC C. Complete Spark API support: the ability to migrate all existing code to Spark Connect without modification, including the RDD APIs<br>
# MAGIC D. Upgradability: the ability to upgrade the Spark applications independently from the Spark driver itself.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:330<br>
# MAGIC **A developer has been asked to debug an issue with a Spark application. The developer identified that the data being loaded from a CSV file incorrectly into a DataFrame. The CSV file has been read using the following Spark SQL statement:**<br>
# MAGIC ```sql
# MAGIC CREATE TABLE default.air_ref
# MAGIC (
# MAGIC   iata STRING,
# MAGIC   iso_country STRING,
# MAGIC   city STRING,
# MAGIC   lat DOUBLE,
# MAGIC   long DOUBLE
# MAGIC )
# MAGIC USING CSV
# MAGIC OPTIONS ('path' = '/landing/air_ref_20241001.csv')
# MAGIC ```
# MAGIC **The first lines of the command `SELECT * FROM default.air_ref` look like this:**<br>
# MAGIC ![](/Workspace/Users/nikx2198@gmail.com/Pyspark_leaning/Screenshot 2026-03-20 004024.png)<br>
# MAGIC **Which parameter can the developer add to the OPTIONS in the CREATE TABLE statement to read the csv data correctly again?**<br>
# MAGIC A. `'quote' = '|'`<br>
# MAGIC B. `'inferSchema' = 'true'`<br>
# MAGIC C. `'header' = 'true', 'sep' = '|'`<br>
# MAGIC D. `'header' 'true'`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:331  
# MAGIC **A data engineer is working with a dataset containing 2 billion rows distributed across 10 Spark partitions. The engineer needs to compute the approximate count of distinct users by their `user_id` field and also calculate the average value of `transaction_amount`. Both calculations must be done in a single transformation step to minimize shuffling.** <br>
# MAGIC **Which set of Spark code will achieve this goal while ensuring performance?**
# MAGIC
# MAGIC A.  
# MAGIC ```python
# MAGIC from pyspark.sql.functions import approx_count_distinct, avg
# MAGIC df.agg(
# MAGIC     approx_count_distinct("user_id").alias("approx_count_distinct"),
# MAGIC     avg("transaction_amount").alias("average_transaction")
# MAGIC ).show()
# MAGIC ```
# MAGIC
# MAGIC B.  
# MAGIC ```python
# MAGIC from pyspark.sql.functions import countDistinct, avg
# MAGIC df.agg(
# MAGIC     countDistinct("user_id").alias("approx_count_distinct"),
# MAGIC     avg("transaction_amount").alias("average_transaction")
# MAGIC ).show()
# MAGIC ```
# MAGIC
# MAGIC C.  
# MAGIC ```python
# MAGIC df.createOrReplaceTempView("transactions")
# MAGIC spark.sql("""
# MAGIC SELECT
# MAGIC     COUNT(DISTINCT user_id) AS approx_count_distinct,
# MAGIC     AVG(transaction_amount) AS average_transaction
# MAGIC FROM transactions
# MAGIC """).show()
# MAGIC ```
# MAGIC
# MAGIC D.  
# MAGIC ```python
# MAGIC from pyspark.sql.functions import col
# MAGIC approx_count = df.select("user_id").distinct().count()
# MAGIC average_transaction = df.select("transaction_amount").groupBy().avg().collect()[0][0]
# MAGIC print(approx_count, average_transaction)
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:332<br>
# MAGIC **What is the main advantage of partitioning the data when persisting tables?**<br>
# MAGIC A. It automatically cleans up unused partitions to optimize storage.<br>
# MAGIC B. It compresses the data to save disk space.<br>
# MAGIC C. It optimizes by reading only the relevant subset of data from fewer partitions.<br>
# MAGIC D. It ensures that data is loaded into memory all at once for faster query execution.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:333<br>
# MAGIC **A data engineer is working on the DataFrame `df`:**
# MAGIC ![](/Workspace/Users/nikx2198@gmail.com/Pyspark_leaning/Screenshot 2026-03-20 004447.png)
# MAGIC **The data engineer wants the Name with the highest count comes first on top, followed by the Name with the next highest count, and so on.**<br>
# MAGIC **Which code fragment should the engineer use to sort the data in the Name and count columns?**
# MAGIC
# MAGIC A.<br>
# MAGIC `df.select("Name", "count").orderBy("count", "Name", ascending=False)`<br>
# MAGIC B.<br>
# MAGIC `df.select("Name", "count").orderBy("count")`<br>
# MAGIC C.<br>
# MAGIC `df.select("Name", "count").sort("Name", "count")`<br>
# MAGIC D.<br>
# MAGIC `df.select("Name", "count").sort("Name")`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:334<br>
# MAGIC **A data engineer is working on a Spark job that reads data from a large text file, applies a filter to remove invalid records, and then groups the data by a specific column. After writing the results in a table, the engineer wants to understand the execution pattern of the Spark job to optimize its performance.**<br>
# MAGIC **What is the sequence of operations in the Spark job?**<br>
# MAGIC A. The Spark job reads the entire text file into memory, applies the filter, and then groups the data by the specified column.<br>
# MAGIC B. The Spark job reads the text file, applies the filter as an action, and then groups the data by the specified column as a transformation.<br>
# MAGIC C. The Spark job reads the text file lazily, applies the filter and grouping as a single transformation, and then executes the entire pipeline as an action.<br>
# MAGIC D. The Spark job reads the text file lazily, applies the filter as a narrow transformation, and then groups the data by the specified column as a wide transformation, causing a shuffle.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:335<br>
# MAGIC **A data engineer needs to add all the rows from one table to all the rows from another. Not all the columns in the first table exist in the second table. The error message is:**  
# MAGIC `AnalysisException: [NUM_COLUMNS_MISMATCH] UNION can only be performed on inputs with the same number of columns`  
# MAGIC **The existing code is:**  
# MAGIC `anz_df = au_df.union(nz_df)`  
# MAGIC **The DataFrame `au_df` has one extra column that does not exist in the DataFrame `nz_df`, but otherwise, both DataFrames have the same column names and data types.**  
# MAGIC **What should the data engineer fix in the code to ensure the combined DataFrame can be produced as expected?**  
# MAGIC A. `anz_df = au_df.unionByName(nz_df, allowMissingColumns=False)`<br>
# MAGIC B.  
# MAGIC `anz_df`<br>
# MAGIC `au_df.unionAll(nz_df)`
# MAGIC
# MAGIC <br>
# MAGIC C. `anz_df = au_df.unionByName(nz_df, allowMissingColumns=True)`<br>
# MAGIC D. `anz_df = au_df.join(nz_df, how='full_outer')`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:336<br>
# MAGIC **Which components of Apache SparkTM's Architecture are responsible for carrying out tasks when assigned to them?**<br>
# MAGIC A. CPU Cores<br>
# MAGIC B. Driver Nodes<br>
# MAGIC C. Worker Nodes<br>
# MAGIC D. Executors<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:337<br>
# MAGIC **A developer needs to write the output of a complex chain of Spark transformations to a Parquet table called `events.live_latest`.**  
# MAGIC **The consumers of this Parquet table primarily access this table with a Spark SQL query with a WHERE clause that filters by both the year and month of the `event_ts` column.**  
# MAGIC **The `event_ts` column is of TIMESTAMP type.**<br>
# MAGIC **The following code is initially deployed but the downstream consumers have complained about poor read performance.**<br>
# MAGIC
# MAGIC ```python
# MAGIC import pyspark.sql.functions as F
# MAGIC final_df \
# MAGIC     .withColumn("event_year", F.year("event_ts")) \
# MAGIC     .withColumn("event_month", F.month("event_ts")) \
# MAGIC     .write \
# MAGIC     .bucketBy(42, ["event_year", "event_month"]) \
# MAGIC     .format("parquet") \
# MAGIC     .saveAsTable("events.live_latest")
# MAGIC ```
# MAGIC
# MAGIC **Which change will enable efficient querying by the downstream consumers of the table on both the year and the month in the `event_ts` column?**<br>
# MAGIC A. Replace `.bucketBy()` with `.partitionBy("event_year")`<br>
# MAGIC B. Replace `.bucketBy()` with `.partitionBy(["event_year", "event_month"])`<br>
# MAGIC C. Change the first value in `.bucketBy()` from 42 to a lower number<br>
# MAGIC D. Add `.sortBy("event_month")` after `.bucketBy()`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:338<br>
# MAGIC **A data scientist is working with a large dataset in Apache Spark and wants to enable SQL queries on a DataFrame. The dataset contains sensitive information that should only be accessible within the current Spark session. Which method can the data scientist use to create a view of the DataFrame that can be queried using SQL syntax without conflicting with previous instances of the view?**<br>
# MAGIC A. `df.createTempView("my_view")`<br>
# MAGIC B. `df.registerTempTable("my_view")`<br>
# MAGIC C. `df.createGlobalTempView("my_view")`<br>
# MAGIC D. `df.createOrReplaceTempView("my_view")`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:339<br>
# MAGIC **Which code should be used to display the schema of the parquet file stored in the location `events_parquet`?**<br>
# MAGIC A. `spark.sql("SELECT * FROM " + events_parquet + "").printSchema()`<br>
# MAGIC B. `spark.sql("SELECT * FROM parquet." + events_parquet + " ").printSchema()`<br>
# MAGIC C. `spark.sql("SELECT * FROM " + events_parquet + "").show()`<br>
# MAGIC D. `spark.sql("SELECT * FROM parquet." + events_parquet + " ").show()`<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:340<br>
# MAGIC **A data engineer is working on `num_df` DataFrame:**<br>
# MAGIC ```python
# MAGIC num_df = spark.range(5).toDF("num")
# MAGIC ```
# MAGIC **The engineer is using the Python UDF:**<br>
# MAGIC ```python
# MAGIC def cubefunc(val):
# MAGIC     return val ** 3
# MAGIC ```
# MAGIC **Which code fragment registers and uses this UDF as a Spark SQL function to work with the DataFrame `num_df`?**<br>
# MAGIC A.<br>
# MAGIC ```python
# MAGIC spark.udf.register("cubeudf", cubefunc, IntegerType())
# MAGIC num_df.selectExpr("cubeudf(num)")
# MAGIC ```
# MAGIC B.<br>
# MAGIC ```python
# MAGIC cubeudf = udf(cubefunc)
# MAGIC num_df.select(cubeudf(col("num")))
# MAGIC ```
# MAGIC C.<br>
# MAGIC ```python
# MAGIC spark.udf.register("cubeudf", cubefunc, DoubleType())
# MAGIC num_df.selectExpr("cubeudf(num)")
# MAGIC ```
# MAGIC D.<br>
# MAGIC ```python
# MAGIC cubeudf = udf(cubefunc)
# MAGIC num_df.selectExpr(cubeudf(num)")
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:341<br>
# MAGIC **A data engineer is working on a Spark Job that requires joining multiple DataFrames. Given the code snippet that performs the joins:**<br>
# MAGIC ```python
# MAGIC datal = [Row(id=1, value="A")]
# MAGIC dfl = spark.createDataFrame(datal)
# MAGIC data2 = [Row(id=1, description="Descl")]
# MAGIC df2 = spark.createDataFrame(data2)
# MAGIC data3 = [Row(id=1, details="Details1")]
# MAGIC df3 = spark.createDataFrame(data3)
# MAGIC joined_df = dfl.join(broadcast(df2), dfl.id == df2.id, "inner") \
# MAGIC                .join(broadcast(df3), df2.id == df3.id, "inner")
# MAGIC ```
# MAGIC **What will be the output of this code?**<br>
# MAGIC A. The code will fail because only one broadcast join can be performed at a time.<br>
# MAGIC B. The code will fail because the second join condition (`df2.id == df3.id`) is not correct. The correct condition should be (`dfl.id == df3.id`).<br>
# MAGIC C. The code will work correctly and perform two broadcast joins simultaneously to join `dfl` with `df2` and then the result with `df3`.<br>
# MAGIC D. The code will result in an error because the broadcast function is used incorrectly, `df2` and `df3` must be explicitly broadcasted before performing the joins.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:342<br>
# MAGIC **A developer is creating a Spark application that performs multiple DataFrame transformations and actions. The developer wants to maintain optimal performance by properly managing the SparkSession. How should the developer handle the SparkSession throughout the application?**<br>
# MAGIC A. Stop and restart the SparkSession after each action.<br>
# MAGIC B. Avoid using a SparkSession and rely on SparkContext only.<br>
# MAGIC C. Create a new SparkSession instance before each transformation.<br>
# MAGIC D. Use a single SparkSession instance for the entire application.<br>
