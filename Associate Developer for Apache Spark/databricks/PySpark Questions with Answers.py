# Databricks notebook source
# MAGIC %md
# MAGIC # PySpark Questions with Answers
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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **D. The Spark driver is the program space in which the Spark application’s main method runs coordinating the entire Spark application.**
# MAGIC
# MAGIC **✅ Explanation:**  
# MAGIC The Spark Driver is the central coordinator of a Spark application. It:
# MAGIC
# MAGIC - Runs the `main()` method of your program  
# MAGIC - Creates the `SparkSession` / `SparkContext`  
# MAGIC - Translates your code into tasks  
# MAGIC - Schedules those tasks on executors  
# MAGIC - Collects results back  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **❌ Why the other options are incorrect:**  
# MAGIC
# MAGIC - **A:** Incorrect — execution is distributed across executors, not just the driver.  
# MAGIC - **B:** Incorrect — the driver is not fault-tolerant by default; if it fails, the application fails.  
# MAGIC - **C:** Incorrect — the driver is part of the application, but not synonymous with the entire application.  
# MAGIC - **E:** Incorrect — the driver is not horizontally scaled; executors handle parallel processing.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **C. An executor is a processing engine running on a node.**
# MAGIC
# MAGIC **✅ Explanation:**  
# MAGIC A node is a machine (physical or virtual) in a cluster.  
# MAGIC An executor is a process that runs on a node and performs computations.  
# MAGIC Each node can run one or more executors, depending on configuration.
# MAGIC
# MAGIC So the relationship is:
# MAGIC
# MAGIC - **Nodes** provide the infrastructure  
# MAGIC - **Executors** do the work on those nodes
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **❌ Why the other options are incorrect:**  
# MAGIC
# MAGIC - **A:** Incorrect — executors run on nodes, so they are directly related.  
# MAGIC - **B:** Incorrect — reversed definition (node is not inside an executor).  
# MAGIC - **D:** Incorrect — the number of executors and nodes can differ.  
# MAGIC - **E:** Incorrect — not necessarily true; you can have multiple executors per node.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **A. The Spark job will likely not run as efficiently as possible.**
# MAGIC
# MAGIC **✅ Explanation:**  
# MAGIC In Spark:  
# MAGIC - **Tasks** = units of work  
# MAGIC - **Slots (cores)** = available parallel processing capacity  
# MAGIC
# MAGIC If you have more slots than tasks:  
# MAGIC - Some slots remain idle  
# MAGIC - Cluster resources are underutilized  
# MAGIC - The job still runs successfully, just not at full efficiency  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **❌ Why the other options are incorrect:**  
# MAGIC - **B:** Incorrect — Spark does not fail if tasks < slots.  
# MAGIC - **C:** Incorrect — executors do not shut down automatically for this reason.  
# MAGIC - **D:** Incorrect — Spark does not create extra tasks artificially.  
# MAGIC - **E:** Incorrect — Spark will still use multiple slots, just not all of them.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **A. Task**
# MAGIC
# MAGIC **✅ Explanation:**
# MAGIC
# MAGIC Spark execution hierarchy (from largest → smallest):
# MAGIC
# MAGIC - **Application**
# MAGIC - **Job**
# MAGIC - **Stage**
# MAGIC - **Task** ✅ *(most granular)*
# MAGIC
# MAGIC A task is the smallest unit of work in Spark.
# MAGIC - Each task operates on a single partition of data.
# MAGIC - Tasks are what actually run on executor cores (slots).
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **❌ Why the other options are incorrect:**
# MAGIC
# MAGIC - **B. Executor** — a process that runs multiple tasks, not the smallest unit.
# MAGIC - **C. Node** — a machine, much higher level.
# MAGIC - **D. Job** — a collection of stages, far less granular.
# MAGIC - **E. Slot** — a resource (CPU core), not a unit of work.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **D. There is no way to monitor the progress of a job.**
# MAGIC
# MAGIC **✅ Explanation:**  
# MAGIC This statement is incorrect because Spark provides built-in tools to monitor jobs:
# MAGIC
# MAGIC - **Spark UI (Web UI)** shows:
# MAGIC   - Jobs
# MAGIC   - Stages
# MAGIC   - Tasks
# MAGIC   - Execution time
# MAGIC   - Resource usage
# MAGIC
# MAGIC So, you can absolutely monitor job progress in Spark.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **✔️ Why the other options are correct:**
# MAGIC
# MAGIC - **A:** True — Jobs are divided into stages.
# MAGIC - **B:** True — More partitions ⇒ more tasks within a job.
# MAGIC - **C:** True — A job is triggered by an action (like `show()`, `count()`).
# MAGIC - **E:** While poorly worded, it's not the clearly incorrect one compared to D; Spark jobs are tied to execution flow, not variable definitions, but D is the obvious false statement.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Key takeaway:**  
# MAGIC Spark jobs are fully observable via the Spark UI — monitoring is a core feature.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **A. DataFrame.join()**
# MAGIC
# MAGIC **✅ Explanation:**
# MAGIC
# MAGIC A shuffle happens when Spark needs to redistribute data across partitions, typically based on a key.
# MAGIC
# MAGIC - **DataFrame.join():**
# MAGIC   - Requires matching rows based on a join key
# MAGIC   - Data must often be moved across the cluster
# MAGIC   - This triggers a shuffle
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **❌ Why the other options are incorrect:**
# MAGIC
# MAGIC - **B. filter()** — operates within partitions (no data movement)
# MAGIC - **C. union()** — simply appends datasets (no shuffle in most cases)
# MAGIC - **D. where()** — same as filter (no shuffle)
# MAGIC - **E. drop()** — removes columns (no data redistribution)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Key takeaway:**
# MAGIC
# MAGIC Operations that require data to be regrouped by key (like joins, groupBy) → cause shuffles

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **E. By default, DataFrames will be split into 200 unique partitions when data is being shuffled.**
# MAGIC
# MAGIC **✅ Explanation:**  
# MAGIC The configuration `spark.sql.shuffle.partitions = 200` controls:  
# MAGIC - The number of partitions created after a shuffle operation  
# MAGIC - This applies to operations like:  
# MAGIC   - `join()`  
# MAGIC   - `groupBy()`  
# MAGIC   - `orderBy()`  
# MAGIC
# MAGIC So whenever a shuffle occurs, Spark will create 200 partitions by default.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **❌ Why the other options are incorrect:**  
# MAGIC - **A & B:** Incorrect — partitions are not tied to executors' memory.  
# MAGIC - **C:** Incorrect — Spark does not ignore partitions when reading data.  
# MAGIC - **D:** Incorrect — this setting does not affect all DataFrames, only those involved in shuffle operations.  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Key takeaway:**  
# MAGIC `spark.sql.shuffle.partitions` = number of partitions **AFTER** a shuffle
# MAGIC
# MAGIC ⚡ **Pro tip (important for performance):**  
# MAGIC - 200 is often too high for small data → causes overhead  
# MAGIC - Too low for big data → reduces parallelism  
# MAGIC
# MAGIC 👉 Tuning this value can significantly improve performance.
# MAGIC
# MAGIC ![image_1774959916309.png](./image_1774959916309.png "image_1774959916309.png")

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **B. A process is lazily evaluated if its execution does not start until it is put into action by some type of trigger**
# MAGIC
# MAGIC **✅ Explanation:**
# MAGIC
# MAGIC In Spark, lazy evaluation means:
# MAGIC
# MAGIC - Transformations (like `select`, `filter`, `join`) are **not executed immediately**
# MAGIC - Spark builds a logical execution plan (**DAG**)
# MAGIC - Execution only begins when an **action** is called
# MAGIC
# MAGIC 👉 **Examples of actions (triggers):**
# MAGIC - `show()`
# MAGIC - `count()`
# MAGIC - `collect()`
# MAGIC - `write()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **❌ Why the other options are incorrect:**
# MAGIC
# MAGIC - **A:** Incorrect — B correctly describes lazy evaluation.
# MAGIC - **C:** Incorrect — execution is not limited to “displaying results”; many actions don’t display anything.
# MAGIC - **D:** Incorrect — nothing to do with time-based execution.
# MAGIC - **E:** Incorrect — compilation is unrelated to lazy evaluation.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Key takeaway:**
# MAGIC
# MAGIC Lazy evaluation = “Don’t execute until an action is called.”

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **C. DataFrame.take()**
# MAGIC
# MAGIC **✅ Explanation:**
# MAGIC
# MAGIC In Spark:
# MAGIC
# MAGIC - **Actions** → trigger execution and return results
# MAGIC - **Transformations** → define a plan but don’t execute immediately
# MAGIC
# MAGIC 👉 **DataFrame.take(n):**
# MAGIC - Retrieves the first n rows
# MAGIC - Triggers execution
# MAGIC - Returns data to the driver → **✅ Action**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **❌ Why the other options are incorrect:**
# MAGIC - **A. drop()** — transformation (removes columns, no execution)
# MAGIC - **B. coalesce()** — transformation (changes partitions)
# MAGIC - **D. join()** — transformation (creates a new DataFrame)
# MAGIC - **E. filter()** — transformation (lazy operation)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Key takeaway:**
# MAGIC
# MAGIC If it returns actual data to you → it’s an **action**
# MAGIC
# MAGIC **Examples of actions:**
# MAGIC - `show()`
# MAGIC - `count()`
# MAGIC - `collect()`
# MAGIC - `take()` ✅
# MAGIC
# MAGIC ⚡ **Quick trick:**
# MAGIC - Ends with data in your hands → **Action**
# MAGIC - Returns another DataFrame → **Transformation**

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🚀 PySpark Actions (DataFrame API)
# MAGIC
# MAGIC ### 📊 Actions that return data to the driver
# MAGIC - `collect()` &rarr; returns all rows
# MAGIC - `take(n)` &rarr; first n rows
# MAGIC - `head(n)` &rarr; first row(s)
# MAGIC - `first()` &rarr; first row
# MAGIC - `toLocalIterator()` &rarr; iterator over rows
# MAGIC
# MAGIC ### 🔢 Aggregation actions
# MAGIC - `count()` &rarr; number of rows
# MAGIC - `reduce()` *(RDD mostly)*
# MAGIC - `foreach()` *(side effects)*
# MAGIC - `foreachPartition()` *(side effects)*
# MAGIC
# MAGIC ### 👀 Actions that display output
# MAGIC - `show()` &rarr; prints to console
# MAGIC - `display()` *(Databricks only)*
# MAGIC
# MAGIC ### 💾 Actions that write data (very important)
# MAGIC - `write.save()`
# MAGIC - `write.csv()`
# MAGIC - `write.json()`
# MAGIC - `write.parquet()`
# MAGIC - `write.orc()`
# MAGIC - `write.text()`
# MAGIC - `write.jdbc()`
# MAGIC - `write.saveAsTable()`
# MAGIC
# MAGIC > These trigger execution because data is actually written.
# MAGIC
# MAGIC ### 📌 Other important DataFrame actions
# MAGIC - `describe()` &rarr; summary stats *(triggers job)*
# MAGIC - `summary()` &rarr; extended stats *(triggers job)*
# MAGIC - `cache()` / `persist()` &rarr; lazy *(NOT actions by themselves ⚠️)*
# MAGIC - `explain()` &rarr; prints plan *(does NOT trigger execution ❗)*
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🔁 RDD Actions (important for interviews)
# MAGIC - `collect()`
# MAGIC - `count()`
# MAGIC - `first()`
# MAGIC - `take(n)`
# MAGIC - `reduce()`
# MAGIC - `foreach()`
# MAGIC - `saveAsTextFile()`
# MAGIC - `saveAsSequenceFile()`
# MAGIC - `saveAsObjectFile()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Key Rule (Most Important)
# MAGIC - **If it produces a result (data/output/write) &rarr; it’s an action**
# MAGIC - **If it returns a new DataFrame &rarr; it’s a transformation**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ⚡ Quick Memory Trick
# MAGIC - **Show / Count / Collect / Write &rarr; ACTIONS**
# MAGIC - **Everything else &rarr; usually TRANSFORMATIONS**

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **B. DataFrame.join()**
# MAGIC
# MAGIC **✅ Explanation:**
# MAGIC
# MAGIC A wide transformation is one that:
# MAGIC - Requires data movement across partitions
# MAGIC - Causes a shuffle
# MAGIC
# MAGIC **👉 DataFrame.join():**
# MAGIC - Needs to match rows based on a key
# MAGIC - Data is often redistributed across the cluster
# MAGIC - This makes it a wide transformation
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🔄 Wide vs Narrow (visual idea)**
# MAGIC - **Wide transformation** → data moves across nodes (shuffle)
# MAGIC - **Narrow transformation** → data stays within the same partition
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **❌ Why the other options are incorrect:**
# MAGIC - **A. filter()** → narrow (no shuffle)
# MAGIC - **C. select()** → narrow
# MAGIC - **D. drop()** → narrow
# MAGIC - **E. union()** → typically narrow (no shuffle in most cases)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Key takeaway:**
# MAGIC
# MAGIC Wide transformation = requires shuffle (expensive)  
# MAGIC **Join** = classic example of wide transformation

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **A. The cluster execution mode runs the driver on a worker node within a cluster, while the client execution mode runs the driver on the client machine (also known as a gateway machine or edge node).**
# MAGIC
# MAGIC **✅ Explanation:**
# MAGIC
# MAGIC The key difference between the two modes is the location of the Spark driver:
# MAGIC
# MAGIC - **Cluster mode:**  
# MAGIC   Driver runs inside the cluster (on a worker node)
# MAGIC
# MAGIC - **Client mode:**  
# MAGIC   Driver runs on the client machine (your laptop / edge node)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **📊 Visual comparison**
# MAGIC
# MAGIC - 🖥️ **Client Mode:** Driver on your machine
# MAGIC - ☁️ **Cluster Mode:** Driver inside cluster
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **❌ Why the other options are incorrect:**
# MAGIC
# MAGIC - **B:** Incorrect — not about local vs cloud
# MAGIC - **C:** Incorrect — executors are distributed in both modes
# MAGIC - **D:** Incorrect — reversed definitions
# MAGIC - **E:** Incorrect — misleading and inaccurate description
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Key takeaway:**
# MAGIC
# MAGIC - **Cluster mode** = driver inside cluster  
# MAGIC - **Client mode** = driver on your machine

# COMMAND ----------

# MAGIC %md
# MAGIC ![image_1774962037488.png](./image_1774962037488.png "image_1774962037488.png")

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **E. Spark will reassign the driver to a worker node if the driver’s node fails.**
# MAGIC
# MAGIC **✅ Explanation:**
# MAGIC
# MAGIC This statement is incorrect because:
# MAGIC
# MAGIC - The Spark driver is **NOT fault-tolerant by default**
# MAGIC - If the driver fails, the entire application fails
# MAGIC - Spark does **not** automatically restart or reassign the driver
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **✔️ Why the other options are correct:**
# MAGIC
# MAGIC - **A:** Spark can handle loss of worker nodes (fault tolerance via recomputation)
# MAGIC - **B:** Failed tasks are rerun automatically
# MAGIC - **C:** Cached data is recomputed using lineage
# MAGIC - **D:** Spark uses disk spill when memory is insufficient
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Key takeaway:**
# MAGIC
# MAGIC - Executors (workers) are fault-tolerant ✅  
# MAGIC - Driver is a single point of failure ❌  
# MAGIC
# MAGIC ⚡ **Simple memory trick:**  
# MAGIC Worker fails → Spark recovers  
# MAGIC Driver fails → Job fails

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
# MAGIC 🧠 **Key Idea (VERY important)**
# MAGIC
# MAGIC When data skew happens, a single large partition:
# MAGIC - Is processed by **ONE task**
# MAGIC - Runs on **ONE executor**
# MAGIC - Must fit in that executor’s memory
# MAGIC
# MAGIC 👉 **So the risk = smallest executor memory**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **From the image:**
# MAGIC
# MAGIC | Scenario | Executors | Memory per Executor |
# MAGIC |----------|-----------|--------------------|
# MAGIC | #1       | 1         | 100 GB ✅ safest    |
# MAGIC | #4       | 2         | 50 GB              |
# MAGIC | #5       | 4         | 25 GB              |
# MAGIC | #6       | 8         | 12.5 GB ❌ worst    |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🚨 **Most likely to cause OOM:**
# MAGIC
# MAGIC **C. Scenario #6**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why?**
# MAGIC - Each executor has only **12.5 GB RAM**
# MAGIC - A skewed partition might be larger than 12.5 GB
# MAGIC - That single executor cannot handle it → 💥 OutOfMemoryError
# MAGIC
# MAGIC ✅ **Why others are safer:**
# MAGIC - #1 → Huge memory (**100 GB**) → very safe
# MAGIC - #4 → **50 GB** → safer
# MAGIC - #5 → **25 GB** → moderate risk
# MAGIC - #6 → **smallest memory** → highest risk
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Final takeaway:**
# MAGIC
# MAGIC - **OOM from skew = happens where executor memory is smallest**
# MAGIC
# MAGIC ⚡ **Exam Trick:**
# MAGIC - Ignore total cluster memory ❌
# MAGIC - Look at **memory per executor** ✅
# MAGIC - **Smallest executor = highest OOM risk**

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **D. When it’s faster to read all the computed data in DataFrame df that cannot fit into memory from disk rather than recompute it based on its logical plan.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **✅ Explanation:**
# MAGIC
# MAGIC **Spark storage levels:**
# MAGIC
# MAGIC - **MEMORY_ONLY:**
# MAGIC   - Stores data only in memory
# MAGIC   - If data doesn’t fit → it is NOT stored
# MAGIC   - Missing partitions are recomputed every time
# MAGIC
# MAGIC - **MEMORY_AND_DISK:**
# MAGIC   - Stores as much as possible in memory
# MAGIC   - Remaining data is spilled to disk
# MAGIC   - Avoids expensive recomputation
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 When is MEMORY_AND_DISK better?**
# MAGIC
# MAGIC 👉 When:
# MAGIC - Data is too large to fit in memory
# MAGIC - **AND** recomputation is expensive (slow transformations, joins, etc.)
# MAGIC
# MAGIC So instead of recomputing:
# MAGIC - Spark reads from disk (faster than recomputing in this case)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **❌ Why other options are incorrect:**
# MAGIC - **A:** If everything fits → MEMORY_ONLY is better ✅
# MAGIC - **B & C:** If recomputation is faster → MEMORY_ONLY is better
# MAGIC - **E:** Incorrect — disk can be better than recomputation in many cases
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Key takeaway:**
# MAGIC
# MAGIC Use **MEMORY_AND_DISK** when recomputation is expensive and data doesn’t fit in memory
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **⚡ Simple decision rule:**
# MAGIC - Fits in memory → MEMORY_ONLY
# MAGIC - Doesn’t fit + expensive to recompute → MEMORY_AND_DISK

# COMMAND ----------

# MAGIC %md
# MAGIC ![image_1775049351257.png](./image_1775049351257.png "image_1775049351257.png")

# COMMAND ----------

# MAGIC %md
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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **D. DataFrame B should be broadcasted because it is smaller and will eliminate the need for the shuffling of DataFrame A.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **✅ Explanation:**
# MAGIC
# MAGIC - In a broadcast join:
# MAGIC   - The **smaller DataFrame** is sent (broadcasted) to all executors
# MAGIC   - The **larger DataFrame** stays distributed
# MAGIC   - This avoids shuffling the large dataset, which is expensive
# MAGIC
# MAGIC **📊 Visual intuition:**
# MAGIC - Small table (**B = 1 GB**) → 📦 broadcast to all nodes
# MAGIC - Large table (**A = 128 GB**) → stays partitioned
# MAGIC - ❌ No shuffle of the large dataset → huge performance gain
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **❌ Why other options are incorrect:**
# MAGIC - **A:** Incorrect — broadcasting large data is inefficient
# MAGIC - **B:** Partially true but incomplete — key benefit is avoiding shuffle of large DataFrame A
# MAGIC - **C & E:** Incorrect — never broadcast the large dataset
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Key takeaway:**
# MAGIC
# MAGIC - Always broadcast the smaller dataset to avoid shuffling the larger one
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **⚡ Memory trick:**
# MAGIC - Small → Broadcast 📦
# MAGIC - Big → Stay distributed 🌐

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # 🚀 Join Strategies in PySpark
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 1️⃣ Broadcast Hash Join (BHJ)
# MAGIC
# MAGIC **How it works:**  
# MAGIC - Small DataFrame is broadcasted to all executors  
# MAGIC - Large DataFrame stays distributed  
# MAGIC - No shuffle of large dataset
# MAGIC
# MAGIC **When used:**  
# MAGIC - One table is small enough (default ~10MB, configurable)
# MAGIC
# MAGIC **Pros:**  
# MAGIC - Fastest join (no shuffle)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 2️⃣ Shuffle Hash Join
# MAGIC
# MAGIC **How it works:**  
# MAGIC - Both DataFrames are shuffled on join key  
# MAGIC - Hash table built per partition
# MAGIC
# MAGIC **When used:**  
# MAGIC - Medium-sized datasets  
# MAGIC - When broadcast is not possible
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 3️⃣ Sort Merge Join (SMJ)
# MAGIC
# MAGIC **How it works:**  
# MAGIC - Data is shuffled  
# MAGIC - Data is sorted  
# MAGIC - Data is merged
# MAGIC
# MAGIC **When used:**  
# MAGIC - Large datasets  
# MAGIC - Default strategy for big joins
# MAGIC
# MAGIC **Pros:**  
# MAGIC - Scales well for large data
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 4️⃣ Broadcast Nested Loop Join (BNLJ)
# MAGIC
# MAGIC **How it works:**  
# MAGIC - One table broadcasted  
# MAGIC - Each row compared with all rows of other table
# MAGIC
# MAGIC **When used:**  
# MAGIC - No join condition (cross join)  
# MAGIC - Non-equi joins
# MAGIC
# MAGIC **Cons:**  
# MAGIC - Very expensive
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🧠 Strategy Selection (Important)
# MAGIC
# MAGIC Spark chooses strategy based on:
# MAGIC - 📏 Data size
# MAGIC - 🔑 Join type (equi / non-equi)
# MAGIC - ⚙️ Configurations
# MAGIC - 📊 Statistics (if available)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## ⚡ Key Rules (Exam Gold)
# MAGIC
# MAGIC - Small table → Broadcast Hash Join
# MAGIC - Large tables → Sort Merge Join
# MAGIC - No equality condition → Nested Loop Join
# MAGIC - Shuffle happens → expensive
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🧠 One-line Memory Trick
# MAGIC
# MAGIC **Small → Broadcast | Big → SortMerge | Weird → NestedLoop**

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

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC **A. df.repartition(12)**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Explanation:**
# MAGIC
# MAGIC - Start: **8 partitions**
# MAGIC - Goal: **12 partitions**
# MAGIC - **repartition(12):**
# MAGIC   - Can **increase or decrease** partitions
# MAGIC   - Performs a **full shuffle**
# MAGIC   - Ensures **even distribution** of data
# MAGIC
# MAGIC python
# MAGIC df = df.repartition(12)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🔍 Why others are incorrect:**
# MAGIC
# MAGIC - **B. df.cache()**
# MAGIC   - Only stores DataFrame in memory
# MAGIC   - ❌ Does NOT change partitions
# MAGIC
# MAGIC - **C. df.partitionBy(1.5)**
# MAGIC   - ❌ Invalid usage
# MAGIC   - `partitionBy()` is used during write operations, not for repartitioning DataFrames
# MAGIC
# MAGIC - **D. df.coalesce(12)**
# MAGIC   - ⚠️ Only used to **reduce** partitions
# MAGIC   - ❌ Cannot reliably increase partitions (no shuffle)
# MAGIC
# MAGIC - **E. df.partitionBy(12)**
# MAGIC   - ❌ Incorrect syntax and purpose
# MAGIC   - Used when writing data, not transforming partitions
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **📊 Visual intuition**
# MAGIC
# MAGIC - **Increase partitions → repartition()**
# MAGIC - **Decrease partitions → coalesce()**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Memory Trick:**
# MAGIC
# MAGIC - “Repartition = Reshuffle (any direction)”
# MAGIC - “Coalesce = Collapse (only reduce)”

# COMMAND ----------

# DBTITLE 1,Cell 20
# MAGIC %md
# MAGIC Question #:17<br>**Which of the following object types cannot be contained within a column of a Spark DataFrame?**<br>A. DataFrame<br>B. String<br>C. Array<br>D. null<br>E. Vector<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC **A. DataFrame**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Explanation:**
# MAGIC
# MAGIC A Spark DataFrame column can only contain data types (values), not complex Spark objects like another DataFrame.
# MAGIC
# MAGIC - **A. DataFrame:**  
# MAGIC   - ❌ Cannot be contained within a column  
# MAGIC   - DataFrames are distributed tables, not row-level values
# MAGIC
# MAGIC - **B. String:**  
# MAGIC   - ✅ Allowed (basic data type)
# MAGIC
# MAGIC - **C. Array:**  
# MAGIC   - ✅ Allowed (ArrayType supported)
# MAGIC
# MAGIC - **D. null:**  
# MAGIC   - ✅ Allowed (represents missing values)
# MAGIC
# MAGIC - **E. Vector:**  
# MAGIC   - ✅ Allowed (e.g., MLlib Vector type)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Key takeaway:**  
# MAGIC Columns store values, not DataFrames
# MAGIC
# MAGIC **⚡ Memory Trick:**  
# MAGIC - ❌ DataFrame inside DataFrame → NOT allowed  
# MAGIC - ✅ Primitive + complex types (array, struct, vector) → allowed

# COMMAND ----------

# DBTITLE 1,Cell 21
# MAGIC %md
# MAGIC Question #:18<br>**Which of the following operations can be used to create a DataFrame with a subset of columns from DataFrame storesDF that are specified by name?**<br>A. storesDF.subset()<br>B. storesDF.select()<br>C. storesDF.selectColumn()<br>D. storesDF.filter()<br>E. storesDF.drop()<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC **B. storesDF.select()**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Explanation:**
# MAGIC
# MAGIC - `select()` is used to choose specific columns by name.
# MAGIC - Returns a new DataFrame with only those columns.
# MAGIC
# MAGIC python:
# MAGIC `storesDF.select("col1", "col2")`
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **❌ Why the other options are incorrect:**
# MAGIC
# MAGIC - **A. subset()**  
# MAGIC   Not a valid Spark DataFrame method.
# MAGIC
# MAGIC - **C. selectColumn()**  
# MAGIC   Not a valid method (incorrect name).
# MAGIC
# MAGIC - **D. filter()**  
# MAGIC   Filters rows, not columns.
# MAGIC
# MAGIC - **E. drop()**  
# MAGIC   Removes columns, but you must specify what to remove (not direct selection).
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Key takeaway:**  
# MAGIC Use `select()` to pick columns by name.
# MAGIC
# MAGIC **⚡ Memory Trick:**  
# MAGIC - `select` → choose columns  
# MAGIC - `filter` → choose rows

# COMMAND ----------

# DBTITLE 1,Cell 22
# MAGIC %md
# MAGIC Question #:19<br>**The code block shown below contains an error. The code block is intended to return a DataFrame containing all columns from DataFrame storesDF except for column sqft and column customerSatisfaction. Identify the error.**<br>Code block: ```storesDF.drop(sqft, customerSatisfaction)```<br>A. 
# MAGIC The drop() operation only works if one column name is called at a time – there should be two calls in succession like storesDF.drop("sqft").drop("customerSatisfaction").<br>
# MAGIC B. The drop() operation only works if column names are wrapped inside the col() function like storesDF.drop(col(sqft), col(customerSatisfaction)).<br>C. There is no drop() operation for storesDF.<br>D. The sqft and customerSatisfaction column names should be quoted like "sqft" and "customerSatisfaction".<br>E. The sqft and customerSatisfaction column names should be subset from the DataFrame storesDF like storesDF."sqft" and storesDF."customerSatisfaction".<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC **D. The sqft and customerSatisfaction column names should be quoted like "sqft" and "customerSatisfaction".**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Explanation:**
# MAGIC
# MAGIC In PySpark, when using `drop()`, column names must be passed as strings.
# MAGIC
# MAGIC - **Incorrect code:**
# MAGIC   python
# MAGIC   storesDF.drop(sqft, customerSatisfaction)
# MAGIC   
# MAGIC   Here, `sqft` and `customerSatisfaction` are treated as variables.  
# MAGIC   Since they are not defined → ❌ error
# MAGIC
# MAGIC - **Correct code:**
# MAGIC   python:
# MAGIC   `storesDF.drop("sqft", "customerSatisfaction")`
# MAGIC   
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **❌ Why other options are incorrect:**
# MAGIC
# MAGIC - **A:** You can drop multiple columns in one call
# MAGIC - **B:** `col()` is not required for `drop()`
# MAGIC - **C:** `drop()` definitely exists
# MAGIC - **E:** Invalid syntax
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Key takeaway:**
# MAGIC
# MAGIC Column names in PySpark functions are usually passed as strings.
# MAGIC
# MAGIC **⚡ Memory Trick:**  
# MAGIC - `"columnName"` ✅  
# MAGIC - `columnName` ❌ (unless using `col()`)

# COMMAND ----------

# DBTITLE 1,Cell 23
# MAGIC %md
# MAGIC Question #:20<br>**Which of the following code blocks returns a DataFrame containing only the rows from DataFrame storesDF where the value in column sqft is less than or equal to 25,000?**<br>A. storesDF.filter("sqft" <= 25000)<br>B. storesDF.filter(sqft > 25000)<br>C. storesDF.where(storesDF[sqft] > 25000)<br>D. storesDF.where(sqft > 25000)<br>E. storesDF.filter(col("sqft") <= 25000)<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC **E. storesDF.filter(col("sqft") <= 25000)**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Explanation:**
# MAGIC
# MAGIC - To filter rows in PySpark, use a Column expression.
# MAGIC - `col("sqft")` correctly references the column.
# MAGIC - Apply the condition `<= 25000`.
# MAGIC
# MAGIC ```python
# MAGIC from pyspark.sql.functions import col
# MAGIC storesDF.filter(col("sqft") <= 25000)
# MAGIC ```
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **❌ Why the other options are incorrect:**
# MAGIC
# MAGIC - **A. storesDF.filter("sqft" <= 25000)**  
# MAGIC   Comparing string `"sqft"` to number → invalid
# MAGIC
# MAGIC - **B. storesDF.filter(sqft > 25000)**  
# MAGIC   `sqft` not defined (missing `col()` or string expression)  
# MAGIC   Also wrong condition (`>` instead of `<=`)
# MAGIC
# MAGIC - **C. storesDF.where(storesDF[sqft] > 25000)**  
# MAGIC   Incorrect syntax (`sqft` not quoted)  
# MAGIC   Wrong condition
# MAGIC
# MAGIC - **D. storesDF.where(sqft > 25000)**  
# MAGIC   Missing `col()`  
# MAGIC   Wrong condition
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Key takeaway:**
# MAGIC
# MAGIC - Use `col("column")` when writing expressions in `filter`/`where`.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **⚡ Alternative correct syntax:**
# MAGIC
# MAGIC python:
# MAGIC `storesDF.filter("sqft <= 25000")`
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **⚡ Memory Trick:**
# MAGIC
# MAGIC - Expression → `col("colName")` ✅  
# MAGIC - String condition → `"colName condition"` ✅

# COMMAND ----------

# DBTITLE 1,Cell 25
# MAGIC %md
# MAGIC Question #:21<br>**Which of the following code blocks returns a DataFrame containing only the rows from DataFrame storesDF where the value in column sqft is less than or equal to 25,000 OR the value in column customerSatisfaction is greater than or equal to 30?**<br>A. storesDF.filter(col("sqft") <= 25000 | col("customerSatisfaction") >= 30)<br>B. storesDF.filter(col("sqft") <= 25000 or col("customerSatisfaction") >= 30)<br>C. storesDF.filter(sqft <= 25000 or customerSatisfaction >= 30)<br>D. storesDF.filter(col(sqft) <= 25000 | col(customerSatisfaction) >= 30)<br>E. storesDF.filter((col("sqft") <= 25000) | (col("customerSatisfaction") >= 30))<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC **E.**
# MAGIC ```python
# MAGIC storesDF.filter((col("sqft") <= 25000) | (col("customerSatisfaction") >= 30))
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Explanation:**
# MAGIC
# MAGIC - In PySpark:
# MAGIC   - Use `|` for **OR** (not `or`)
# MAGIC   - Each condition must be wrapped in parentheses
# MAGIC   - Use `col("columnName")` to reference columns
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **❌ Why the other options are incorrect:**
# MAGIC
# MAGIC - **A:** Missing parentheses → operator precedence issue
# MAGIC - **B:** Uses Python `or` instead of `|`
# MAGIC - **C:** Missing `col()` and uses `or`
# MAGIC - **D:** Column names not quoted (`col(sqft)` is invalid)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Key takeaway:**
# MAGIC
# MAGIC - Use `|` for OR and wrap each condition in parentheses
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **⚡ Correct pattern:**
# MAGIC ```python
# MAGIC df.filter((condition1) | (condition2))
# MAGIC ```
# MAGIC
# MAGIC **⚡ Memory Trick:**
# MAGIC
# MAGIC - `|` → OR ✅
# MAGIC - `&` → AND ✅
# MAGIC - `or` / `and` → ❌ (don’t use in PySpark conditions)

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:22<br>**Which of the following code blocks returns a new DataFrame from DataFrame storesDF where column storeId is of the type string?**<br>
# MAGIC A. storesDF.withColumn("storeId", cast(col("storeId"), StringType()))<br>
# MAGIC B. storesDF.withColumn("storeId", col("storeId").cast(StringType()))<br>
# MAGIC C. storesDF.withColumn("storeId", cast(storeId).as(StringType))<br>
# MAGIC D. storesDF.withColumn("storeId", col(storeId).cast(StringType))<br>
# MAGIC E. storesDF.withColumn("storeId", cast("storeId").as(StringType()))<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC **B. storesDF.withColumn("storeId", col("storeId").cast(StringType()))**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Explanation:**
# MAGIC
# MAGIC - To change a column’s data type in PySpark:
# MAGIC   - Use `withColumn()`
# MAGIC   - Reference column using `col("columnName")`
# MAGIC   - Apply `.cast(DataType())`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **❌ Why the other options are incorrect:**
# MAGIC
# MAGIC - **A:** `cast()` is not used like a standalone function in PySpark
# MAGIC - **C:** Invalid syntax (`cast(storeId).as(...)`)
# MAGIC - **D:** Missing quotes → `storeId` should be `"storeId"`
# MAGIC - **E:** Trying to cast a string literal instead of a column
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Key takeaway:**
# MAGIC
# MAGIC - Correct casting pattern:  
# MAGIC   `col("columnName").cast(DataType())`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **⚡ Alternative (also valid):**
# MAGIC
# MAGIC - `storesDF.withColumn("storeId", col("storeId").cast("string"))`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **⚡ Memory Trick:**
# MAGIC
# MAGIC - Column → `col("name")` ✅  
# MAGIC - Cast → `.cast(type)` ✅

# COMMAND ----------

# DBTITLE 1,Cell 26
# MAGIC %md
# MAGIC Question #:23<br>**Which of the following code blocks returns a new DataFrame with a new column employeesPerSqft that is the quotient of column numberOfEmployees and column sqft, both of which are from DataFrame storesDF? Note that column employeesPerSqft is not in the original DataFrame storesDF.**<br>A. storesDF.withColumn("employeesPerSqft", col("numberOfEmployees") / col("sqft"))<br>B. storesDF.withColumn("employeesPerSqft", "numberOfEmployees" / "sqft")<br>C. storesDF.select("employeesPerSqft", "numberOfEmployees" / "sqft")<br>D. storesDF.select("employeesPerSqft", col("numberOfEmployees") / col("sqft"))<br>E. storesDF.withColumn(col("employeesPerSqft"), col("numberOfEmployees") / col("sqft"))<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC **A.**
# MAGIC ```python
# MAGIC storesDF.withColumn("employeesPerSqft", col("numberOfEmployees") / col("sqft"))
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Explanation:**
# MAGIC
# MAGIC - To create a new column in PySpark:
# MAGIC   - Use `withColumn("newColumnName", expression)`
# MAGIC   - Use `col()` to reference existing columns
# MAGIC   - Apply operations (like division `/`)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **❌ Why the other options are incorrect:**
# MAGIC
# MAGIC - **B:** Cannot divide strings (`"numberOfEmployees" / "sqft"`)
# MAGIC - **C:** `select()` cannot directly create a new column this way (and strings used incorrectly)
# MAGIC - **D:** Missing alias for the computed column
# MAGIC - **E:** Column name should be a string, not `col()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Key takeaway:**
# MAGIC
# MAGIC - Use `withColumn("newName", expression)` to create new columns
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **⚡ Alternative correct syntax:**
# MAGIC ```python
# MAGIC storesDF.select("*", (col("numberOfEmployees") / col("sqft")).alias("employeesPerSqft"))
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **⚡ Memory Trick:**
# MAGIC
# MAGIC - New column → `withColumn()` ✅
# MAGIC - Use `col()` for math operations ✅

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

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC **C.**
# MAGIC 1. withColumn  
# MAGIC 2. "modality"  
# MAGIC 3. lit  
# MAGIC 4. "PHYSICAL"  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Explanation:**
# MAGIC
# MAGIC To add a constant column in PySpark:
# MAGIC
# MAGIC - Use `withColumn()`
# MAGIC - Use `lit()` to create a literal (constant value)
# MAGIC
# MAGIC **✅ Correct code:**
# MAGIC ```python
# MAGIC from pyspark.sql.functions import lit
# MAGIC storesDF.withColumn("modality", lit("PHYSICAL"))
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **❌ Why the other options are incorrect:**
# MAGIC
# MAGIC - **A:** `col("PHYSICAL")` refers to a column, not a constant
# MAGIC - **B:** Missing quotes → PHYSICAL should be `"PHYSICAL"`
# MAGIC - **D:** `StringType` is for casting, not creating constants
# MAGIC - **E:** Invalid syntax and wrong function
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Key takeaway:**
# MAGIC
# MAGIC - Use `lit()` to add constant values to a DataFrame
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **⚡ Memory Trick:**
# MAGIC
# MAGIC - Column value → `col()` ✅  
# MAGIC - Constant value → `lit()` ✅

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

# MAGIC %md
# MAGIC ✅ Correct Answer: **C**
# MAGIC
# MAGIC ```storesDF.withColumn("storeValueCategory", split(col("storeCategory"), "_")[0])
# MAGIC         .withColumn("storeSizeCategory", split(col("storeCategory"), "_")[1])```
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why this is correct:**
# MAGIC
# MAGIC - `split(col("storeCategory"), "_")` creates an array:
# MAGIC   - Example: `"VALUE_MEDIUM"` → `["VALUE", "MEDIUM"]`
# MAGIC - `[0]` → `"VALUE"` ✅
# MAGIC - `[1]` → `"MEDIUM"` ✅
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A & E:** Use `[1]` and `[2]` → index 2 doesn’t exist
# MAGIC - **B:** `col().split()` is invalid syntax
# MAGIC - **D:** `"storeCategory"` passed as string, not column
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key takeaway:**
# MAGIC
# MAGIC - `split()` → array → use `[0]`, `[1]` (0-based indexing)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚡ **Memory Trick:**
# MAGIC
# MAGIC - `"A_B"` →
# MAGIC   - `[0]` = A
# MAGIC   - `[1]` = B

# COMMAND ----------

# DBTITLE 1,Cell 29
# MAGIC %md
# MAGIC Question #:26<br>**Which of the following code blocks returns a new DataFrame where column productCategories only has one word per row, resulting in a DataFrame with many more rows than DataFrame storesDF?**<br>A sample of storesDF is displayed below:<br>![image_1773927252244.png](./image_1773927252244.png "image_1773927252244.png")<br>A. storesDF.withColumn("productCategories", explode(col("productCategories")))<br>B. storesDF.withColumn("productCategories", split(col("productCategories")))<br>C. storesDF.withColumn("productCategories", col("productCategories").explode())<br>D. storesDF.withColumn("productCategories", col("productCategories").split())<br>E. storesDF.select(explode(col("productCategories")).alias("productCategories"))<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC **A.**
# MAGIC ```python
# MAGIC storesDF.withColumn("productCategories", explode(col("productCategories")))
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Explanation:**
# MAGIC
# MAGIC - `productCategories` is an array column.
# MAGIC - `explode()` transforms each array element into a separate row.
# MAGIC
# MAGIC **Example:**
# MAGIC
# MAGIC | storeId | productCategories      |
# MAGIC |---------|-----------------------|
# MAGIC | 0       | ["A", "B", "C"]       |
# MAGIC
# MAGIC **After explode:**
# MAGIC
# MAGIC | storeId | productCategories |
# MAGIC |---------|------------------|
# MAGIC | 0       | A                |
# MAGIC | 0       | B                |
# MAGIC | 0       | C                |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **❌ Why other options are wrong:**
# MAGIC
# MAGIC - **B:** `split()` is for strings, not arrays.
# MAGIC - **C:** `.explode()` is not a method on column objects.
# MAGIC - **D:** `.split()` is invalid on column objects.
# MAGIC - **E:** Works, but drops other columns (not ideal).
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🧠 Key takeaway:**
# MAGIC
# MAGIC - Use `explode()` to convert array elements into multiple rows.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **⚡ Memory Trick:**
# MAGIC
# MAGIC - Array → `explode` → rows 📈

# COMMAND ----------

# DBTITLE 1,Cell 30
# MAGIC %md
# MAGIC Question #:27<br>**Which of the following code blocks returns a new DataFrame with column storeDescription where the pattern "Description: " has been removed from the beginning of column storeDescription in DataFrame storesDF?**<br>A sample of DataFrame storesDF is below:<br>![image_1773927314484.png](./image_1773927314484.png "image_1773927314484.png")<br>A. storesDF.withColumn("storeDescription", regexp_extract(col("storeDescription"), "^Description: (.+)", 1))<br>B. storesDF.withColumn("storeDescription", col("storeDescription").regexp_replace("^Description: ", ""))<br>C. storesDF.withColumn("storeDescription", regexp_extract(col("storeDescription"), "^Description: (.+)", 0))<br>D. storesDF.withColumn("storeDescription", col("storeDescription").regexp_extract("^Description: (.+)", 1))<br>E. storesDF.withColumn("storeDescription", col("storeDescription").regexp_extract("^Description: (.+)", 0))<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ✅ A.
# MAGIC ```python
# MAGIC storesDF.withColumn(
# MAGIC     "storeDescription",
# MAGIC     regexp_extract(col("storeDescription"), "^Description: (.+)", 1)
# MAGIC )
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Explanation:**
# MAGIC
# MAGIC - **Goal:** Remove the prefix `"Description: "` from `storeDescription`.
# MAGIC - `^Description: ` → matches text at the start of the string.
# MAGIC - `(.+)` → captures everything after the prefix.
# MAGIC - `1` → returns the captured group (without prefix).
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **B:** `regexp_replace` is not used as a method on `col()` (wrong syntax).
# MAGIC   - Correct version: `regexp_replace(col("storeDescription"), "^Description: ", "")`
# MAGIC - **C:** Index `0` returns the full match (includes prefix).
# MAGIC - **D & E:** `regexp_extract` is not a method on `col()`.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key takeaway:**
# MAGIC
# MAGIC - Use `regexp_extract()` with group index `1` to remove prefixes.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚡ **Memory Trick:**
# MAGIC - Group `0` → full match ❌
# MAGIC - Group `1` → extracted part ✅

# COMMAND ----------

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

data = [
    (0, "xyz Description: ultra modern store"),
    (1, "xyz Description: spacious and bright"),
    (2, "xyz Description: premium location"),
    (3, "xyz Description: small but efficient"),
    (4, "xyz Description: newly renovated")
]

columns = ["storeId", "storeDescription"]

storesDF = spark.createDataFrame(data, columns)

storesDF.show(truncate=False)

# COMMAND ----------

from pyspark.sql.functions import col, regexp_extract

cleanDF = storesDF.withColumn(
    "storeDescription",
    regexp_extract(col("storeDescription"), "(.*)(Description:)(.*)", 1)
)

cleanDF.show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Cell 31
# MAGIC %md
# MAGIC Question #:28<br>**Which of the following code blocks returns a new DataFrame where column division from DataFrame storesDF has been replaced and renamed to column state and column managerName from DataFrame storesDF has been replaced and renamed to column managerFullName?**<br>A. (storesDF.withColumnRenamed(["division", "state"], ["managerName", "managerFullName"])<br>B. (storesDF.withColumn("state", col("division"))<br>.withColumn("managerFullName", col("managerName")))<br>C. (storesDF.withColumn("state", col("division"))<br>.withColumn("managerFullName", col("managerName"))<br>.drop("division", "managerName"))<br>D. (storesDF.withColumnRenamed("division", "state")<br>.withColumnRenamed("managerName", "managerFullName"))<br>E. (storesDF.withColumn("state", col("division")).drop("division")<br>.withColumn("managerFullName", col("managerName")).drop("managerName"))<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ✅ D.
# MAGIC ```python
# MAGIC storesDF.withColumnRenamed("division", "state") \
# MAGIC         .withColumnRenamed("managerName", "managerFullName")
# MAGIC
# MAGIC ```
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Explanation:**
# MAGIC
# MAGIC - **What the question asks:**  
# MAGIC   Rename column `division` → `state`  
# MAGIC   Rename column `managerName` → `managerFullName`
# MAGIC
# MAGIC - No need to create new columns or drop anything — just rename.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A:** `withColumnRenamed` does NOT take lists
# MAGIC - **B:** Creates new columns but does NOT remove old ones
# MAGIC - **C:** Works logically but not optimal (extra steps)
# MAGIC - **E:** Also works, but unnecessarily complex
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key takeaway:**
# MAGIC
# MAGIC - Use `withColumnRenamed()` when you only need to rename columns
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚡ **Memory Trick:**
# MAGIC
# MAGIC - Rename → `withColumnRenamed()` ✅  
# MAGIC - Modify values → `withColumn()` ✅
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🚀 **Pro Tip:**
# MAGIC
# MAGIC You can chain multiple renames:
# MAGIC python
# MAGIC df.withColumnRenamed("old1", "new1") \
# MAGIC   .withColumnRenamed("old2", "new2")

# COMMAND ----------

# DBTITLE 1,Cell 32
# MAGIC %md
# MAGIC Question #:29<br>**The code block shown contains an error. The code block is intended to return a new DataFrame where column sqft from DataFrame storesDF has had its missing values replaced with the value 30,000. Identify the error.**<br>A sample of DataFrame storesDF is displayed below:<br>![image_1773927626725.png](./image_1773927626725.png "image_1773927626725.png")<br>Code block: storesDF.na.fill(30000, col("sqft"))<br>A. The argument to the subset parameter should be a list like ["sqft"].<br>B. The value and subset arguments should be switched in order.<br>C. The storesDF DataFrame should be wrapped by the col() function.<br>D. Missing values are automatically replaced in Spark – there is no need for this operation.<br>E. The entire operation should be replaced with storesDF.fillna(30000, ["sqft"]).<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ✅ A. The argument to the subset parameter should be a list like ["sqft"].
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Explanation:**
# MAGIC
# MAGIC The issue is in this code:
# MAGIC
# MAGIC python
# MAGIC storesDF.na.fill(30000, col("sqft"))
# MAGIC
# MAGIC
# MAGIC 🔴 **Problem:**  
# MAGIC The second argument (subset) must be a list of column names (strings).  
# MAGIC ❌ `col("sqft")` is a Column object → invalid here
# MAGIC
# MAGIC ✅ **Correct code:**  
# MAGIC python
# MAGIC storesDF.na.fill(30000, ["sqft"])
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **B:** Order is already correct (value, subset)
# MAGIC - **C:** `col()` is not needed for DataFrame itself
# MAGIC - **D:** Spark does NOT auto-fill missing values
# MAGIC - **E:** This is actually correct syntax, but the question asks for the error, not a replacement
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key takeaway:**
# MAGIC
# MAGIC - `na.fill()` expects column names as a list of strings, not `col()` objects
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚡ **Memory Trick:**
# MAGIC
# MAGIC - Column reference in expressions → `col()` ✅  
# MAGIC - Column name in APIs like `fill`/`drop` → `"columnName"` or `["columnName"]` ✅
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🚀 **Bonus:**
# MAGIC
# MAGIC You can fill multiple columns:
# MAGIC
# MAGIC python
# MAGIC storesDF.na.fill(30000, ["sqft", "revenue"])

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

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ❌ **E. DataFrame.drop_duplicates(subset = "all")**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Explanation:**
# MAGIC
# MAGIC - **Goal:** Return a DataFrame with no duplicate rows
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why others work:**
# MAGIC - **A.** `dropDuplicates()` → removes duplicate rows
# MAGIC - **B.** `distinct()` → same as above
# MAGIC - **C.** `drop_duplicates()` → alias of `dropDuplicates()`
# MAGIC - **D.** `drop_duplicates(subset=None)` → considers all columns, removes full duplicates
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why E is incorrect:**
# MAGIC - `DataFrame.drop_duplicates(subset = "all")`
# MAGIC   - `"all"` is not a valid column name or list
# MAGIC   - `subset` must be a list of column names (e.g., `["col1", "col2"]`) or `None`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key takeaway:**
# MAGIC - `subset` must be a list of valid column names, not arbitrary strings
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚡ **Memory Trick:**
# MAGIC - Full duplicate removal → `distinct()` or `dropDuplicates()` ✅
# MAGIC - Partial duplicate removal → `subset=["col"]` ✅
# MAGIC - `"all"` → ❌ invalid

# COMMAND ----------

# DBTITLE 1,Cell 34
# MAGIC %md
# MAGIC Question #:31<br>**Which of the following code blocks will most quickly return an approximation for the number of distinct values in column division in DataFrame storesDF?**<br>A. storesDF.agg(approx_count_distinct(col("division")).alias("divisionDistinct"))<br>B. storesDF.agg(approx_count_distinct(col("division"), 0.01).alias("divisionDistinct"))<br>C. storesDF.agg(count_distinct(col("division")).alias("divisionDistinct"))<br>D. storesDF.agg(approx_count_distinct("division").alias("divisionDistinct"))<br>E. storesDF.select(approx_count_distinct(col("division")).alias("divisionDistinct"))<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ✅ D.
# MAGIC ```python
# MAGIC storesDF.agg(approx_count_distinct("division").alias("divisionDistinct"))
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Explanation:**
# MAGIC
# MAGIC - **What the question asks:**  
# MAGIC   Approximate distinct count  
# MAGIC   Most quickly (i.e., best performance)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚡ **Why D is correct:**
# MAGIC
# MAGIC - Uses `approx_count_distinct` → faster than exact count
# MAGIC - Uses column name directly → clean and efficient
# MAGIC - Uses aggregation (`agg`) → correct pattern
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are not best:**
# MAGIC
# MAGIC - **A:** Slightly more verbose (`col()` unnecessary)
# MAGIC - **B:** Adds precision (`0.01`) → slower (more accurate but less fast)
# MAGIC - **C:** `count_distinct` → exact, much slower ❌
# MAGIC - **E:** `select()` works, but `agg()` is more appropriate for aggregation
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key concept:**
# MAGIC
# MAGIC - `approx_count_distinct` uses HyperLogLog → trades small accuracy for big speed
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚖️ **Speed vs Accuracy:**
# MAGIC
# MAGIC - Faster → `approx_count_distinct()` ✅
# MAGIC - More accurate → `approx_count_distinct(col, rsd)` (lower RSD = more work)
# MAGIC - Exact → `count_distinct()` ❌ (slowest)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚡ **Memory Trick:**
# MAGIC
# MAGIC - `"approx"` = fast 🚀  
# MAGIC - `"count_distinct"` = precise 🐢

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "North"),
    (2, "South"),
    (3, "East"),
    (4, "West"),
    (5, "North"),
    (6, "South"),
    (7, "East"),
    (8, "North"),
    (9, "West"),
    (10, "Central"),
    (11, "Central"),
    (12, "North")
]

columns = ["storeId", "division"]

storesDF = spark.createDataFrame(data, columns)

# storesDF.show()
# storesDF.select(approx_count_distinct(col("division")).alias("divisionDistinct")).show()
# storesDF.agg(approx_count_distinct("division").alias("divisionDistinct")).show()
storesDF.agg(approx_count_distinct(col("division")).alias("divisionDistinct")).show()

# COMMAND ----------

display(storesDF.summary())

# COMMAND ----------

display(storesDF.describe())

# COMMAND ----------

# DBTITLE 1,Cell 35
# MAGIC %md
# MAGIC Question #:32<br>**The code block shown below contains an error. The code block is intended to return a new DataFrame with the mean of column sqft from DataFrame storesDF in column sqftMean. Identify the error.**<br>Code block: storesDF.agg(mean("sqft").alias("sqftMean"))<br>A. The argument to the mean() operation should be wrapped in the col() operation.<br>B. There is no mean() operation – the avg() operation should be used instead.<br>C. The agg() operation should be replaced with the aggregate() operation.<br>D. The agg() operation should be replaced with the select() operation.<br>E. There is no error – this code will run as expected.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ✅ E. There is no error – this code will run as expected.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Explanation:**
# MAGIC
# MAGIC python
# MAGIC storesDF.agg(mean("sqft").alias("sqftMean"))
# MAGIC
# MAGIC
# MAGIC - `mean()` is valid in PySpark ✅ (alias for `avg()`)
# MAGIC - Passing column name as a string `"sqft"` is perfectly fine
# MAGIC - `agg()` is the correct method for aggregation
# MAGIC
# MAGIC 🔄 **Equivalent code:**
# MAGIC
# MAGIC python
# MAGIC from pyspark.sql.functions import avg
# MAGIC storesDF.agg(avg("sqft").alias("sqftMean"))
# MAGIC
# MAGIC
# MAGIC 👉 Both give the same result
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are wrong:**
# MAGIC
# MAGIC - **A:** `col()` is optional, not required
# MAGIC - **B:** `mean()` exists (alias of `avg`)
# MAGIC - **C:** `agg()` is correct method
# MAGIC - **D:** `select()` can work, but `agg()` is standard
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key takeaway:**
# MAGIC
# MAGIC - `mean()` = `avg()` in PySpark
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚡ **Memory Trick:**
# MAGIC
# MAGIC - SQL mindset → `avg()`
# MAGIC - Python mindset → `mean()`
# MAGIC - 👉 Both valid ✅

# COMMAND ----------

# DBTITLE 1,Cell 36
# MAGIC %md
# MAGIC Question #:33<br>**Which of the following operations can be used to return the number of rows in a DataFrame?**<br>A. DataFrame.numberOfRows()<br>B. DataFrame.n()<br>C. DataFrame.sum()<br>D. DataFrame.count()<br>E. DataFrame.countDistinct()<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ✅ **D. DataFrame.count()**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Explanation:**
# MAGIC
# MAGIC - **Purpose:** Get the number of rows in a DataFrame.
# MAGIC - **Correct method:**  
# MAGIC   python
# MAGIC   storesDF.count()
# MAGIC   
# MAGIC   Returns the total number of rows in the DataFrame.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** `numberOfRows()` ❌ does not exist
# MAGIC - **B.** `n()` ❌ does not exist
# MAGIC - **C.** `sum()` ❌ aggregates numeric values, not row count
# MAGIC - **E.** `countDistinct()` ❌ counts unique values in a column, not rows
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key takeaway:**
# MAGIC
# MAGIC - `count()` = total number of rows
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚡ **Memory Trick:**
# MAGIC
# MAGIC - Rows → `count()` ✅
# MAGIC - Unique values → `countDistinct()` ✅
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🚀 **Bonus:**
# MAGIC
# MAGIC If you want row count + performance tip:
# MAGIC python
# MAGIC df.rdd.count()  # sometimes faster for simple counts (advanced use)

# COMMAND ----------

# DBTITLE 1,Cell 37
# MAGIC %md
# MAGIC Question #:34<br>**Which of the following operations returns a GroupedData object?**<br>A. DataFrame.GroupBy()<br>B. DataFrame.cubed()<br>C. DataFrame.group()<br>D. DataFrame.groupBy()<br>E. DataFrame.grouping_id()<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ✅ **D. DataFrame.groupBy()**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Explanation:**
# MAGIC
# MAGIC - `storesDF.groupBy("division")` returns a **GroupedData** object, used for aggregations:
# MAGIC   - `storesDF.groupBy("division").count()`
# MAGIC   - `storesDF.groupBy("division").avg("sqft")`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** `GroupBy()` ❌ incorrect capitalization (case-sensitive)
# MAGIC - **B.** `cubed()` ❌ no such method (`cube()` exists)
# MAGIC - **C.** `group()` ❌ not a valid method
# MAGIC - **E.** `grouping_id()` ❌ used in advanced aggregations, not for grouping
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key takeaway:**
# MAGIC
# MAGIC - `groupBy()` → returns GroupedData → used for aggregations
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚡ **Memory Trick:**
# MAGIC
# MAGIC - `groupBy()` → group + aggregate ✅  
# MAGIC - Then → `.count()`, `.sum()`, `.avg()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🚀 **Bonus:**
# MAGIC
# MAGIC - `df.groupBy("col")`        # standard grouping  
# MAGIC - `df.rollup("col")`         # hierarchical aggregation  
# MAGIC - `df.cube("col")`           # multi-dimensional aggregation

# COMMAND ----------

# DBTITLE 1,Cell 38
# MAGIC %md
# MAGIC Question #:35<br>**Which of the following code blocks returns a collection of summary statistics for all columns in DataFrame storesDF?**<br>A. storesDF.summary("mean")<br>B. storesDF.describe(all = True)<br>C. storesDF.describe("all")<br>D. storesDF.summary("all")<br>E. storesDF.describe()<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ✅ E. `storesDF.describe()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Explanation:**
# MAGIC
# MAGIC - **What the question asks:**  
# MAGIC   Return summary statistics for all columns
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why E is correct:**
# MAGIC
# MAGIC python
# MAGIC storesDF.describe()
# MAGIC
# MAGIC
# MAGIC - Returns statistics like:
# MAGIC   - `count`
# MAGIC   - `mean`
# MAGIC   - `stddev`
# MAGIC   - `min`
# MAGIC   - `max`
# MAGIC - Applies to all numeric (and some string) columns
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 📊 **Example Output:**
# MAGIC
# MAGIC | summary | sqft   | storeId |
# MAGIC |---------|--------|---------|
# MAGIC | count   | 100    | 100     |
# MAGIC | mean    | 25000  | 50      |
# MAGIC | stddev  | 5000   | 29      |
# MAGIC | min     | 10000  | 1       |
# MAGIC | max     | 40000  | 100     |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** `summary("mean")` – only returns mean, not full summary
# MAGIC - **B.** `describe(all=True)` – invalid argument
# MAGIC - **C.** `describe("all")` – invalid usage
# MAGIC - **D.** `summary("all")` – "all" is not a valid parameter
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key takeaway:**
# MAGIC
# MAGIC - `describe()` → quick summary stats for all columns
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚡ **Bonus:**
# MAGIC
# MAGIC For more detailed stats, use:
# MAGIC
# MAGIC python
# MAGIC storesDF.summary()
# MAGIC
# MAGIC
# MAGIC - Includes: `count`, `mean`, `stddev`, `min`, `max`, `25%`, `50%`, `75%` percentiles
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚡ **Memory Trick:**
# MAGIC
# MAGIC - `describe()` → basic stats ✅
# MAGIC - `summary()` → detailed stats 📊

# COMMAND ----------

# DBTITLE 1,Cell 39
# MAGIC %md
# MAGIC Question #:36<br>**Which of the following code blocks fails to return a DataFrame reverse sorted alphabetically based on column division?**<br>A. storesDF.orderBy("division", ascending = False)<br>B. storesDF.orderBy(desc("division"))<br>C. storesDF.orderBy(col("division"), ascending = False)<br>D. storesDF.sort(col("division").desc())<br>E. storesDF.orderBy(col("division").asc())<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ❌ **E. storesDF.orderBy(col("division").asc())**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Explanation:**
# MAGIC
# MAGIC - **What the question asks:**  
# MAGIC   Return DataFrame reverse sorted alphabetically (i.e., descending order)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Valid descending options:**
# MAGIC
# MAGIC - **A.** `storesDF.orderBy("division", ascending=False)`
# MAGIC - **B.** 
# MAGIC   python
# MAGIC   from pyspark.sql.functions import desc
# MAGIC   storesDF.orderBy(desc("division"))
# MAGIC   
# MAGIC - **C.** `storesDF.orderBy(col("division"), ascending=False)`
# MAGIC - **D.** `storesDF.sort(col("division").desc())`
# MAGIC
# MAGIC 👉 All correctly sort descending (Z → A) ✅
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why E is wrong:**
# MAGIC
# MAGIC - `storesDF.orderBy(col("division").asc())`
# MAGIC   - `asc()` = ascending order (A → Z) ❌
# MAGIC   - Opposite of what the question asks
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key takeaway:**
# MAGIC
# MAGIC - Descending sort → `desc()` or `ascending=False`

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "North"),
    (2, "South"),
    (3, "East"),
    (4, "West"),
    (5, "North"),
    (6, "South"),
    (7, "East"),
    (8, "North"),
    (9, "West"),
    (10, "Central"),
    (11, "Central"),
    (12, "North")
]

columns = ["storeId", "division"]

storesDF = spark.createDataFrame(data, columns)
storesDF.orderBy("storeId").desc()

# COMMAND ----------

# DBTITLE 1,Cell 40
# MAGIC %md
# MAGIC Question #:37<br>**Which of the following code blocks returns a 15 percent sample of rows from DataFrame storesDF without replacement?**<br>A. storesDF.sample(fraction = 0.10)<br>B. storesDF.sample(withReplacement = False, fraction = 0.15)<br>C. storesDF.sample(fraction = 0.15)<br>D. storesDF.sample(withReplacement = False, fraction = 1.5)<br>E. storesDF.sample(withReplacement = True, fraction = 0.15)<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ✅ B.
# MAGIC python
# MAGIC storesDF.sample(withReplacement=False, fraction=0.15)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Explanation:**
# MAGIC
# MAGIC - **What the question requires:**  
# MAGIC   15% sample → `fraction=0.15`  
# MAGIC   Without replacement → `withReplacement=False`
# MAGIC
# MAGIC - **Why B is correct:**  
# MAGIC   Explicitly sets:  
# MAGIC   - `fraction=0.15` ✅  
# MAGIC   - `withReplacement=False` ✅
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚠️ **What about C?**
# MAGIC
# MAGIC python
# MAGIC storesDF.sample(fraction=0.15)
# MAGIC
# MAGIC - This also works because default is `withReplacement=False`.
# MAGIC - 👉 BUT the question explicitly says “without replacement”, so B is the most correct/explicit answer.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC - **A:** `fraction=0.10` (10%, not 15%) ❌
# MAGIC - **D:** `fraction=1.5` (invalid → >100%) ❌
# MAGIC - **E:** `withReplacement=True` (wrong condition) ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key takeaway:**
# MAGIC - `sample(fraction, withReplacement)` controls % and duplication behavior
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚡ **Memory Trick:**
# MAGIC - `fraction=0.15` → 15%
# MAGIC - `withReplacement=False` → no duplicates

# COMMAND ----------

# DBTITLE 1,Cell 41
# MAGIC %md
# MAGIC Question #:38<br>**Which of the following code blocks returns all the rows from DataFrame storesDF?**<br>A. storesDF.head()<br>B. storesDF.collect()<br>C. storesDF.count()<br>D. storesDF.take()<br>E. storesDF.show()<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ✅ **B. storesDF.collect()**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Explanation:**
# MAGIC
# MAGIC - **What the question asks:**  
# MAGIC   Return all rows from the DataFrame
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why B is correct:**
# MAGIC
# MAGIC python
# MAGIC storesDF.collect()
# MAGIC
# MAGIC - Returns all rows as a list of Row objects
# MAGIC - Brings data from executors → driver
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** `head()` ❌ returns only first row (or few rows)
# MAGIC - **C.** `count()` ❌ returns number of rows, not the rows
# MAGIC - **D.** `take()` ❌ returns limited rows (you must specify number)
# MAGIC - **E.** `show()` ❌ only displays rows (default 20), doesn’t return all
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚠️ **Important Warning:**
# MAGIC
# MAGIC - `collect()` can be dangerous on large datasets  
# MAGIC   Loads everything into driver memory → may cause OutOfMemory error
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key takeaway:**
# MAGIC
# MAGIC - `collect()` → returns ALL rows to driver
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚡ **Memory Trick:**
# MAGIC
# MAGIC - `collect()` → everything 📦  
# MAGIC - `show()` → preview 👀  
# MAGIC - `take(n)` → limited 📉
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🚀 **Bonus:**
# MAGIC
# MAGIC - Safer alternative:
# MAGIC   python
# MAGIC   storesDF.limit(100).collect()

# COMMAND ----------

# DBTITLE 1,Cell 42
# MAGIC %md
# MAGIC Question #:39<br>**Which of the following code blocks applies the function assessPerformance() to each row of DataFrame storesDF?**<br>A. [assessPerformance(row) for row in storesDF.take(3)]<br>B. [assessPerformance() for row in storesDF]<br>C. storesDF.collect().apply(lambda: assessPerformance)<br>D. [assessPerformance(row) for row in storesDF.collect()]<br>E. [assessPerformance(row) for row in storesDF]<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ✅ **D.**
# MAGIC python
# MAGIC [assessPerformance(row) for row in storesDF.collect()]
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Explanation:**
# MAGIC
# MAGIC - **What the question asks:**  
# MAGIC   Apply a function to each row of a DataFrame
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why D is correct:**
# MAGIC
# MAGIC - `storesDF.collect()` → brings all rows to driver
# MAGIC - List comprehension → iterates over each row
# MAGIC - Applies: `assessPerformance(row)` to every row
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** `storesDF.take(3)`  
# MAGIC   ❌ Only applies to first 3 rows, not all
# MAGIC
# MAGIC - **B.** `[assessPerformance() for row in storesDF]`  
# MAGIC   ❌ No argument passed + DataFrame is not iterable
# MAGIC
# MAGIC - **C.** `storesDF.collect().apply(...)`  
# MAGIC   ❌ `.apply()` is not a method on list
# MAGIC
# MAGIC - **E.** `for row in storesDF`  
# MAGIC   ❌ DataFrame is not directly iterable
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚠️ **Important Note (Real-world practice):**
# MAGIC
# MAGIC - ❗ This approach is **NOT scalable**
# MAGIC - `collect()` pulls all data to driver → risky for large data
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🚀 **Better Spark Approach:**
# MAGIC
# MAGIC Use UDF instead:
# MAGIC
# MAGIC python
# MAGIC from pyspark.sql.functions import udf
# MAGIC
# MAGIC udf_func = udf(assessPerformance)
# MAGIC
# MAGIC storesDF.withColumn("newCol", udf_func(*storesDF.columns))
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key takeaway:**
# MAGIC
# MAGIC - `collect()` + loop works for small data only
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚡ **Memory Trick:**
# MAGIC
# MAGIC - Small data → `collect()` + loop ✅
# MAGIC - Big data → UDF / Spark transformations 🚀

# COMMAND ----------

# DBTITLE 1,Cell 43
# MAGIC %md
# MAGIC Question #:40<br>**The code block shown below contains an error. The code block is intended to print the schema of DataFrame storesDF. Identify the error.**<br>Code block: storesDF.printSchema<br>A. There is no printSchema member of DataFrame – schema and the print() function should be used instead.<br>B. The entire line needs to be a string – it should be wrapped by str().<br>C. There is no printSchema member of DataFrame – the getSchema() operation should be used instead.<br>D. There is no printSchema member of DataFrame – the schema() operation should be used instead.<br>E. The printSchema member of DataFrame is an operation and needs to be followed by parentheses.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ✅ **E. The printSchema member of DataFrame is an operation and needs to be followed by parentheses.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Explanation:**
# MAGIC
# MAGIC - **Problem in the code:**
# MAGIC   python
# MAGIC   storesDF.printSchema
# MAGIC   
# MAGIC   This only references the function, but does **NOT** execute it ❌
# MAGIC
# MAGIC - **Correct code:**
# MAGIC   python
# MAGIC   storesDF.printSchema()
# MAGIC   
# MAGIC   👉 Parentheses `()` are required to call the function
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 📊 **What it does:**
# MAGIC
# MAGIC Prints the schema like:
# MAGIC
# MAGIC
# MAGIC root
# MAGIC  |-- storeId: integer (nullable = true)
# MAGIC  |-- division: string (nullable = true)
# MAGIC  |-- sqft: integer (nullable = true)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A:** `printSchema` **does** exist
# MAGIC - **B:** No need to convert to string
# MAGIC - **C:** `getSchema()` does not exist
# MAGIC - **D:** `schema` exists but behaves differently (`df.schema` returns schema object)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key takeaway:**
# MAGIC
# MAGIC - Methods need `()` to execute
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚡ **Memory Trick:**
# MAGIC
# MAGIC - `df.printSchema` → reference ❌
# MAGIC - `df.printSchema()` → execute ✅
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🚀 **Bonus:**
# MAGIC
# MAGIC - `df.schema`        # returns schema object
# MAGIC - `df.printSchema()` # prints nicely formatted schema

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

# MAGIC %md
# MAGIC ✅ Correct Answer: A
# MAGIC
# MAGIC python
# MAGIC spark.udf.register("ASSESS_PERFORMANCE", assessPerformance)
# MAGIC
# MAGIC spark.sql("""
# MAGIC SELECT customerSatisfaction,
# MAGIC        ASSESS_PERFORMANCE(customerSatisfaction) AS result
# MAGIC FROM stores
# MAGIC """)
# MAGIC
# MAGIC
# MAGIC 🧠 Why A is correct:
# MAGIC
# MAGIC - **Step 1: Register UDF**
# MAGIC   - `spark.udf.register("ASSESS_PERFORMANCE", assessPerformance)`
# MAGIC     - `"ASSESS_PERFORMANCE"` → must be a string ✅
# MAGIC     - `assessPerformance` → Python function (no quotes) ✅
# MAGIC
# MAGIC - **Step 2: Use in SQL**
# MAGIC   - `ASSESS_PERFORMANCE(customerSatisfaction)`
# MAGIC     - Function name is NOT quoted in SQL ✅
# MAGIC
# MAGIC ❌ Why C is wrong:
# MAGIC
# MAGIC - Option C uses `"ASSESS_PERFORMANCE"` quoted in SQL ❌
# MAGIC   - That would be treated as a string literal, not a function
# MAGIC
# MAGIC 🧠 Key takeaway:
# MAGIC
# MAGIC - Register → string name
# MAGIC - Use in SQL → unquoted function name
# MAGIC
# MAGIC ⚡ Memory Trick:
# MAGIC - `"NAME"` when registering
# MAGIC - `NAME()` when using

# COMMAND ----------

# DBTITLE 1,Cell 45
# MAGIC %md
# MAGIC Question #:42<br>**The code block shown below contains an error. The code block is intended to create a Python UDF assessPerformanceUDF() using the integer-returning Python function assessPerformance() and apply it to column customerSatisfaction in DataFrame storesDF. Identify the error.**<br>Code block: assessPerformanceUDF = udf(assessPerformance)<br>storesDF.withColumn("result", assessPerformanceUDF(col("customerSatisfaction")))<br>A. The assessPerformance() operation is not properly registered as a UDF.<br>B. The withColumn() operation is not appropriate here – UDFs should be applied by iterating over rows instead.<br>C. UDFs can only be applied vie SQL and not through the DataFrame API.<br>D. The return type of the assessPerformanceUDF() is not specified in the udf() operation.<br>E. The assessPerformance() operation should be used on column customerSatisfaction rather than the assessPerformanceUDF() operation.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ✅ D. The return type of the assessPerformanceUDF() is not specified in the udf() operation.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Explanation:**
# MAGIC
# MAGIC - **Problem in the code:**
# MAGIC   python
# MAGIC   assessPerformanceUDF = udf(assessPerformance)
# MAGIC   
# MAGIC   ❌ Missing return type  
# MAGIC   Spark needs to know the output data type of the UDF
# MAGIC
# MAGIC - **Correct code:**
# MAGIC   python
# MAGIC   from pyspark.sql.functions import udf
# MAGIC   from pyspark.sql.types import IntegerType
# MAGIC
# MAGIC   assessPerformanceUDF = udf(assessPerformance, IntegerType())
# MAGIC
# MAGIC   storesDF.withColumn(
# MAGIC       "result",
# MAGIC       assessPerformanceUDF(col("customerSatisfaction"))
# MAGIC   )
# MAGIC   
# MAGIC
# MAGIC 🔍 **Why return type is required:**
# MAGIC - Spark uses it for:
# MAGIC   - Schema inference
# MAGIC   - Execution planning
# MAGIC - Without it → may cause errors or unexpected behavior
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **A:** Registration is only needed for SQL UDFs, not DataFrame UDFs
# MAGIC - **B:** `withColumn()` is the correct way to apply UDFs
# MAGIC - **C:** UDFs work in both SQL and DataFrame API
# MAGIC - **E:** You must use the UDF wrapper, not raw function
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key takeaway:**
# MAGIC - Always specify return type when creating PySpark UDFs
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚡ **Memory Trick:**
# MAGIC - `udf(function, returnType)` ✅  
# MAGIC - Missing type → ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🚀 **Bonus:**
# MAGIC python
# MAGIC # String return example
# MAGIC from pyspark.sql.types import StringType
# MAGIC udf_func = udf(myFunc, StringType())

# COMMAND ----------

# DBTITLE 1,Cell 46
# MAGIC %md
# MAGIC Question #:43<br>**The code block shown below contains an error. The code block is intended to use SQL to return a new DataFrame containing column storeId and column managerName from a table created from DataFrame storesDF. Identify the error.**<br>Code block:<br>storesDF.createOrReplaceTempView("stores")<br>storesDF.sql("SELECT storeId, managerName FROM stores")<br>A. The createOrReplaceTempView() operation does not make a Dataframe accessible via SQL.<br>B. The sql() operation should be accessed via the spark variable rather than DataFrame storesDF.<br>C. There is the sql() operation in DataFrame storesDF. The operation query() should be used instead.<br>D. This cannot be accomplished using SQL - the DataFrame API should be used instead.<br>E. The createOrReplaceTemView() operation should be accessed via the spark variable rather than DataFrame storeDF.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ✅ **B. The sql() operation should be accessed via the spark variable rather than DataFrame storesDF.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Explanation:**
# MAGIC
# MAGIC - **Problem in the code:**
# MAGIC   python
# MAGIC   storesDF.sql("SELECT storeId, managerName FROM stores")
# MAGIC   
# MAGIC   ❌ `sql()` is NOT a method of DataFrame  
# MAGIC   It belongs to the SparkSession (`spark`)
# MAGIC
# MAGIC - **Correct code:**
# MAGIC   python
# MAGIC   storesDF.createOrReplaceTempView("stores")
# MAGIC   spark.sql("SELECT storeId, managerName FROM stores")
# MAGIC   
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **How it works:**
# MAGIC
# MAGIC - **Register DataFrame as a temp view:**
# MAGIC   python
# MAGIC   storesDF.createOrReplaceTempView("stores")
# MAGIC   
# MAGIC - **Query using Spark SQL:**
# MAGIC   python
# MAGIC   spark.sql("SELECT ...")
# MAGIC   
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A:** Temp view DOES make DataFrame accessible via SQL
# MAGIC - **C:** No `query()` method exists
# MAGIC - **D:** SQL can absolutely be used here
# MAGIC - **E:** `createOrReplaceTempView()` is correctly used on DataFrame
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key takeaway:**
# MAGIC
# MAGIC - SQL queries in Spark are executed via `spark.sql()`, not DataFrame
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚡ **Memory Trick:**
# MAGIC
# MAGIC - DataFrame → `.select()`, `.filter()`
# MAGIC - SQL → `spark.sql()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🚀 **Bonus:**
# MAGIC
# MAGIC - You can chain:
# MAGIC   python
# MAGIC   spark.sql("SELECT * FROM stores").show()

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

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ✅ E
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Filled Code:**
# MAGIC python
# MAGIC spark.createDataFrame(years, IntegerType())
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Explanation:**
# MAGIC
# MAGIC - **What the question asks:**  
# MAGIC   Create a single-column DataFrame from a Python list of integers
# MAGIC
# MAGIC - **Why E is correct:**  
# MAGIC   - `spark.createDataFrame()` → correct method ✅  
# MAGIC   - `years` → list of integers ✅  
# MAGIC   - `IntegerType()` → schema definition (must be instantiated) ✅
# MAGIC
# MAGIC ⚠️ **Important Detail:**  
# MAGIC Must use: `IntegerType()`  
# MAGIC ❌ NOT `IntegerType` (class only)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are wrong:**
# MAGIC - **A:** Missing parentheses → `IntegerType` ❌
# MAGIC - **B:** Invalid syntax (`DataFrame.create`)
# MAGIC - **C:** Typo + missing `()`
# MAGIC - **D:** Typo: `IntegertType()` ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key takeaway:**  
# MAGIC Schema types must be instantiated → `IntegerType()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚡ **Memory Trick:**  
# MAGIC Type class → `IntegerType` ❌  
# MAGIC Type object → `IntegerType()` ✅
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🚀 **Bonus:**  
# MAGIC Better (explicit schema):
# MAGIC
# MAGIC python
# MAGIC from pyspark.sql.types import StructType, StructField, IntegerType
# MAGIC years = [2001, 2002, 2203]
# MAGIC schema = StructType([StructField("year", IntegerType(), True)])
# MAGIC spark.createDataFrame([(y,) for y in years], schema)

# COMMAND ----------

# DBTITLE 1,Cell 48
# MAGIC %md
# MAGIC Question #:45<br>**The code block shown below contains an error. The code block is intended to cache DataFrame storesDF only in Spark's memory and then return the number of rows in the cached DataFrame. Identify the error.**<br>Code block: storesDF.cache().count()<br>A. The cache() operation caches DataFrames at the MEMORY_AND_DISK level by default – the storage level must be specified to MEMORY_ONLY as an argument to cache().<br>B. The cache() operation caches DataFrames at the MEMORY_AND_DISK level by default – the storage level must be set via storesDF.storageLevel prior to calling cache().<br>C. The storesDF DataFrame has not been checkpointed – it must have a checkpoint in order to be cached.<br>D. DataFrames themselves cannot be cached – DataFrame storesDF must be cached as a table.<br>E. The cache() operation can only cache DataFrames at the MEMORY_AND_DISK_ONLY storage level. The persist() operation should be used instead to cache only in memory.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ✅ **E**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation**
# MAGIC
# MAGIC The code:
# MAGIC
# MAGIC python
# MAGIC storesDF.cache().count()
# MAGIC
# MAGIC
# MAGIC looks fine at first glance, but the question is testing your understanding of how caching works in Apache Spark.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Key Concept**
# MAGIC
# MAGIC - `cache()` in Spark is just a shortcut for `persist()` with default storage level.
# MAGIC - The default storage level is:
# MAGIC
# MAGIC   👉 **MEMORY_AND_DISK**
# MAGIC
# MAGIC   That means:
# MAGIC   - Spark will try to store data in memory
# MAGIC   - If memory is insufficient, it will spill to disk
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **What’s the problem?**
# MAGIC
# MAGIC The question says:
# MAGIC
# MAGIC > “cache DataFrame storesDF only in Spark's memory”
# MAGIC
# MAGIC But:
# MAGIC
# MAGIC - `cache()` does **NOT** guarantee memory-only storage
# MAGIC - It may use disk as well
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct Approach**
# MAGIC
# MAGIC If you want memory-only caching, you must explicitly use:
# MAGIC
# MAGIC python
# MAGIC from pyspark.storagelevel import StorageLevel
# MAGIC storesDF.persist(StorageLevel.MEMORY_ONLY)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Why Option E is correct**
# MAGIC
# MAGIC > The cache() operation can only cache DataFrames at the MEMORY_AND_DISK_ONLY storage level. The persist() operation should be used instead to cache only in memory.
# MAGIC
# MAGIC ✔ This is essentially correct because:
# MAGIC
# MAGIC - `cache()` ≈ `persist(MEMORY_AND_DISK)`
# MAGIC - To force memory-only → use `persist(MEMORY_ONLY)`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are wrong**
# MAGIC
# MAGIC - **A & B:** You cannot pass storage level to `cache()`
# MAGIC - **C:** Checkpointing is unrelated to caching
# MAGIC - **D:** DataFrames can absolutely be cached directly
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Final Takeaway**
# MAGIC
# MAGIC - `cache()` = convenience method (**MEMORY_AND_DISK**)
# MAGIC - `persist()` = full control over storage level

# COMMAND ----------

# DBTITLE 1,Cell 49
# MAGIC %md
# MAGIC Question #:46<br>**Which of the following operations can be used to return a new DataFrame from DataFrame storesDF without inducing a shuffle?**<br>A. storesDF.intersect()<br>B. storesDF.repartition(1)<br>C. storesDF.union()<br>D. storesDF.coalesce(1)<br>E. storesDF.rdd.getNumPartitions()<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ✅ **D. storesDF.coalesce(1)**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Explanation
# MAGIC
# MAGIC The question asks:  
# MAGIC **Which operation returns a new DataFrame from storesDF _without_ inducing a shuffle?**
# MAGIC
# MAGIC A **shuffle** happens when data is redistributed across partitions (expensive operation 🚨).
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### 🔍 Option-by-option analysis
# MAGIC
# MAGIC - **A. storesDF.intersect()**  
# MAGIC   ❌ Requires comparing data across partitions  
# MAGIC   👉 Causes shuffle
# MAGIC
# MAGIC - **B. storesDF.repartition(1)**  
# MAGIC   ❌ Explicitly redistributes data evenly  
# MAGIC   👉 Always causes shuffle
# MAGIC
# MAGIC - **C. storesDF.union()**  
# MAGIC   ❌ Combines two DataFrames  
# MAGIC   May require alignment of partitions  
# MAGIC   👉 Typically can involve shuffle
# MAGIC
# MAGIC - **D. storesDF.coalesce(1)**  
# MAGIC   ✅ Reduces number of partitions without full shuffle  
# MAGIC   Merges existing partitions locally  
# MAGIC   👉 Does **NOT** cause shuffle (narrow transformation)  
# MAGIC   ✔ **This is the correct answer**
# MAGIC
# MAGIC - **E. storesDF.rdd.getNumPartitions()**  
# MAGIC   ❌ Returns an integer, not a DataFrame  
# MAGIC   👉 Doesn’t even satisfy the question requirement
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Key Concept to Remember
# MAGIC
# MAGIC - `repartition()` → shuffle (**wide transformation**)
# MAGIC - `coalesce()` → no shuffle (**narrow transformation**, when reducing partitions)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ⚡ Quick Memory Trick
# MAGIC
# MAGIC - “Repartition = Redistribute = Shuffle”
# MAGIC - “Coalesce = Combine = No Shuffle”

# COMMAND ----------

# DBTITLE 1,Cell 50
# MAGIC %md
# MAGIC Question #:47<br>**The code block shown below contains an error. The code block is intended to return a new 12-partition DataFrame from the 8-partition DataFrame storesDF by inducing a shuffle. Identify the error.**<br>Code block: storesDF.coalesce(12)<br>A. The coalesce() operation cannot guarantee the number of target partitions – the repartition() operation should be used instead.<br>B. The coalesce() operation does not induce a shuffle and cannot increase the number of partitions – the repartition() operation should be used instead.<br>C. The coalesce() operation will only work if the DataFrame has been cached to memory – the repartition() operation should be used instead.<br>D. The coalesce() operation will only work if the number of target partitions is lower than the number of current partitions.<br>E. The coalesce() operation does not induce a shuffle and cannot increase the number of partitions. The shuffle() operation should be used instead.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is: B
# MAGIC
# MAGIC ✅ Why B is correct
# MAGIC
# MAGIC The code:
# MAGIC
# MAGIC storesDF.coalesce(12)
# MAGIC
# MAGIC **Goal:**  
# MAGIC Increase partitions: 8 → 12  
# MAGIC Induce a shuffle
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🚨 **What’s wrong here?**
# MAGIC
# MAGIC - **coalesce() does NOT shuffle**  
# MAGIC   It is a narrow transformation and avoids data movement.
# MAGIC
# MAGIC - **coalesce() cannot increase partitions**  
# MAGIC   If you request more partitions than exist, Spark will NOT actually increase them.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct way:**
# MAGIC
# MAGIC python
# MAGIC storesDF.repartition(12)
# MAGIC
# MAGIC - Increases partitions
# MAGIC - Forces a shuffle
# MAGIC - Distributes data evenly
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Why Option B is perfect**
# MAGIC
# MAGIC > B. The coalesce() operation does not induce a shuffle and cannot increase the number of partitions – the repartition() operation should be used instead.
# MAGIC
# MAGIC ✔ Matches both problems exactly:
# MAGIC - No shuffle ❌
# MAGIC - Cannot increase partitions ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong**
# MAGIC - **A:** Talks about guarantee — not the main issue
# MAGIC - **C:** Caching is irrelevant
# MAGIC - **D:** Partially true, but incomplete (doesn’t mention shuffle)
# MAGIC - **E:** shuffle() is not a real Spark API method
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Final takeaway**
# MAGIC - Increase partitions → use `repartition()`
# MAGIC - Decrease partitions → use `coalesce()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚡ **Memory Trick**
# MAGIC - “Repartition = Redistribute (shuffle)”
# MAGIC - “Coalesce = Compress (no shuffle)”

# COMMAND ----------

# DBTITLE 1,Cell 51
# MAGIC %md
# MAGIC Question #:48<br>**Which of the following Spark properties is used to configure whether DataFrame partitions that do not meet a minimum size threshold are automatically coalesced into larger partitions during a shuffle?**<br>A. spark.sql.shuffle.partitions<br>B. spark.sql.autoBroadcastJoinThreshold<br>C. spark.sql.adaptive.skewJoin.enabled<br>D. spark.sql.inMemoryColumnarStorage.batchSize<br>E. spark.sql.adaptive.coalescePartitions.enabled<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ✅ **E. spark.sql.adaptive.coalescePartitions.enabled**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Simple Explanation
# MAGIC
# MAGIC **What does this property do?**  
# MAGIC Lets Spark automatically merge small partitions into bigger ones during a shuffle (Adaptive Query Execution, AQE).
# MAGIC
# MAGIC - During a shuffle, Spark may create many small partitions  
# MAGIC - Small partitions = inefficient (too many tiny tasks 🐢)
# MAGIC - This property enables Spark to automatically combine (coalesce) them
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Why E is correct
# MAGIC
# MAGIC - `spark.sql.adaptive.coalescePartitions.enabled`
# MAGIC   - Turns ON/OFF automatic merging
# MAGIC   - Works during shuffle stage
# MAGIC   - Improves performance
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ❌ Why other options are wrong
# MAGIC
# MAGIC - **A. spark.sql.shuffle.partitions**  
# MAGIC   Sets the initial number of shuffle partitions  
# MAGIC   ❌ Does NOT auto-merge them
# MAGIC
# MAGIC - **B. spark.sql.autoBroadcastJoinThreshold**  
# MAGIC   Controls broadcast join size  
# MAGIC   ❌ Unrelated
# MAGIC
# MAGIC - **C. spark.sql.adaptive.skewJoin.enabled**  
# MAGIC   Handles skewed data (uneven partitions)  
# MAGIC   ❌ Different optimization
# MAGIC
# MAGIC - **D. spark.sql.inMemoryColumnarStorage.batchSize**  
# MAGIC   Controls caching batch size  
# MAGIC   ❌ Not about shuffle
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 One-line takeaway
# MAGIC
# MAGIC > AQE can shrink small shuffle partitions automatically — controlled by this property
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ⚡ Memory Trick
# MAGIC
# MAGIC > “adaptive + coalescePartitions = auto merge small partitions”

# COMMAND ----------

# DBTITLE 1,Cell 52
# MAGIC %md
# MAGIC Question #:49<br>**The code block shown below contains an error. The code block is intended to return a DataFrame containing a column openDateString, a string representation of Java's SimpleDateFormat. Identify the error.**<br>Note that column openDate is of type integer and represents a date in the UNIX epoch format – the number of seconds since midnight on January 1st, 1970.<br>An example of Java's SimpleDateFormat is "Sunday, Dec 4, 2008 1:05 PM".<br>A sample of storesDF is displayed below:<br>![image_1773928852784.png](./image_1773928852784.png "image_1773928852784.png")<br>Code block:<br>storesDF.withColumn("openDateString", from_unixtime(col("openDate"), "EEE, MMM d, yyyy h:mm a", TimestampType()))<br>A. The from_unixtime() operation can only accept one or two arguments – the third argument TimestampType() should be removed.<br>B. The from_unixtime() operation requires column openDate to be wrapped in the col() function like col(col("openDate")).<br>C. The from_unixtime() operation returns a timestamp and needs to be cast as a string.<br>D. The from_unixtime() operation does not exist – the to_timestamp() operation should be used instead.<br>E. The from_unixtime() operation requires the column name openDate to be in quotes like from_unixtime("openDate", "EEE, MMM d, yyyy h:mm a").<br>

# COMMAND ----------

# MAGIC %md
# MAGIC ✅ Correct Answer: A
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Explanation**
# MAGIC
# MAGIC **Given code:**
# MAGIC python
# MAGIC storesDF.withColumn(
# MAGIC     "openDateString",
# MAGIC     from_unixtime(col("openDate"), "EEE, MMM d, yyyy h:mm a", TimestampType())
# MAGIC )
# MAGIC
# MAGIC
# MAGIC ❗ **What’s wrong?**
# MAGIC
# MAGIC The function `from_unixtime()` in PySpark has the signature:
# MAGIC
# MAGIC python
# MAGIC from_unixtime(timestamp, format=None)
# MAGIC
# MAGIC
# MAGIC 👉 It accepts **ONLY 1 or 2 arguments**:
# MAGIC - Column (UNIX timestamp)
# MAGIC - Format string (optional)
# MAGIC
# MAGIC 🚫 **Problem in the code:**
# MAGIC A third argument is passed: `TimestampType()`
# MAGIC This is **invalid syntax**.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct code:**
# MAGIC python
# MAGIC from pyspark.sql.functions import from_unixtime, col
# MAGIC
# MAGIC storesDF.withColumn(
# MAGIC     "openDateString",
# MAGIC     from_unixtime(col("openDate"), "EEE, MMM d, yyyy h:mm a")
# MAGIC )
# MAGIC
# MAGIC
# MAGIC ✔ This already returns a string, so no casting needed.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are wrong:**
# MAGIC - **B:** `col(col("openDate"))` is invalid
# MAGIC - **C:** `from_unixtime()` already returns string
# MAGIC - **D:** `from_unixtime()` definitely exists
# MAGIC - **E:** Using `col("openDate")` is perfectly valid
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Final takeaway**
# MAGIC
# MAGIC | Function         | Output  |
# MAGIC |------------------|---------|
# MAGIC | from_unixtime()  | String  |
# MAGIC
# MAGIC - Accepts max **2 arguments** only

# COMMAND ----------

# DBTITLE 1,Cell 53
# MAGIC %md
# MAGIC Question #:50<br>**Which of the following code blocks returns a DataFrame containing a column dayOfYear, an integer representation of the day of the year from column openDate from DataFrame storesDF?**<br>Note that column openDate is of type integer and represents a date in the UNIX epoch format – the number of seconds since midnight on January 1st, 1970.<br>A sample of storesDF is displayed below:<br>![image_1773928908521.png](./image_1773928908521.png "image_1773928908521.png")<br>A. (storesDF.withColumn("openTimestamp", col("openDate").cast("Timestamp"))<br>. withColumn("dayOfYear", dayofyear(col("openTimestamp"))))<br>B. storesDF.withColumn("dayOfYear", get dayofyear(col("openDate")))<br>C. storesDF.withColumn("dayOfYear", dayofyear("openDate"))<br>D. storesDF.withColumn("dayOfYear", dayofyear(col("openDate")))<br>E. (storesDF.withColumn("openTimestamp", col("openDate").cast(TimestampType()))<br>.withColumn("dayOfYear", dayofyear(col("openTimestamp"))))<br>

# COMMAND ----------

# MAGIC %md
# MAGIC ✅ Correct Answer: A
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Key Concept**
# MAGIC
# MAGIC - `openDate` is a UNIX timestamp (integer)
# MAGIC - To use `dayofyear()`, Spark needs a timestamp/date column
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why A is correct**
# MAGIC
# MAGIC python
# MAGIC storesDF.withColumn("openTimestamp", col("openDate").cast("Timestamp")) \
# MAGIC         .withColumn("dayOfYear", dayofyear(col("openTimestamp")))
# MAGIC
# MAGIC
# MAGIC - Converts integer → timestamp using `"Timestamp"`
# MAGIC - Applies `dayofyear()` correctly
# MAGIC - Fully valid PySpark syntax
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❗ **Important Note**
# MAGIC
# MAGIC In PySpark, both are valid:
# MAGIC
# MAGIC - `col("openDate").cast("Timestamp")`       # string
# MAGIC - `col("openDate").cast(TimestampType())`   # object
# MAGIC
# MAGIC 👉 So A and E are logically equivalent, but:
# MAGIC
# MAGIC - Exams typically prefer string-based cast (`"Timestamp"`)
# MAGIC - Hence A is the expected answer
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong**
# MAGIC
# MAGIC - **B** → Invalid syntax (`get dayofyear`)
# MAGIC - **C** → No conversion → still integer
# MAGIC - **D** → Same issue → cannot apply `dayofyear` directly on int
# MAGIC - **E** → Technically correct, but A is preferred/expected
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Final takeaway**
# MAGIC
# MAGIC | Step | Operation                        |
# MAGIC |------|----------------------------------|
# MAGIC | 1    | Cast UNIX int → Timestamp        |
# MAGIC | 2    | Apply `dayofyear()`              |
# MAGIC
# MAGIC 👉 **Exam tip:**  
# MAGIC If multiple correct answers exist, choose:
# MAGIC - Simpler syntax
# MAGIC - More commonly used form → usually string-based cast

# COMMAND ----------

# DBTITLE 1,Cell 54
# MAGIC %md
# MAGIC Question #:51<br>**The code block shown below contains an error. The code block intended to return a new DataFrame that is the result of an inner join between DataFrame storesDF and DataFrame employeesDF on column storeId. Identify the error.**<br>Code block: StoresDF.join(employeesDF, "inner", "storeID")<br>A. The key column storeID needs to be wrapped in the col() operation.<br>B. The key column storeID needs to be in a list like ["storeID"].<br>C. The key column storeID needs to be specified in an expression of both DataFrame columns like storesDF.storeId == employeesDF.storeId.<br>D. There is no DataFrame.join() operation – DataFrame.merge() should be used instead.<br>E. The second and third arguments of the join() operation should be switched in order.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC ✅ Correct Answer: E
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **What’s wrong in the code?**
# MAGIC
# MAGIC **Given code:**
# MAGIC python
# MAGIC StoresDF.join(employeesDF, "inner", "storeID")
# MAGIC
# MAGIC
# MAGIC ❗ **Issue:**  
# MAGIC The order of arguments in `join()` is incorrect.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Correct syntax of join() in PySpark:**
# MAGIC python
# MAGIC df.join(other, on=None, how=None)
# MAGIC
# MAGIC ✔ **Parameter order:**
# MAGIC - `other` → DataFrame to join
# MAGIC - `on` → join column(s)
# MAGIC - `how` → join type (inner, left, etc.)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **What the code is doing:**
# MAGIC - `.join(employeesDF, "inner", "storeID")`
# MAGIC   - `"inner"` is incorrectly passed as join column
# MAGIC   - `"storeID"` is incorrectly passed as join type
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct code:**
# MAGIC python
# MAGIC storesDF.join(employeesDF, "storeID", "inner")
# MAGIC
# MAGIC ✔ Now:
# MAGIC - `"storeID"` → join key
# MAGIC - `"inner"` → join type
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are wrong:**
# MAGIC - **A:** No need to wrap string column name in `col()`
# MAGIC - **B:** List is optional (used for multiple columns)
# MAGIC - **C:** Valid alternative, but not required
# MAGIC - **D:** `join()` absolutely exists
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Final takeaway**
# MAGIC
# MAGIC | Position | Meaning         |
# MAGIC |----------|----------------|
# MAGIC | 1st      | DataFrame       |
# MAGIC | 2nd      | Join column(s)  |
# MAGIC | 3rd      | Join type       |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🚀 **Exam tip**
# MAGIC
# MAGIC If you see:
# MAGIC python
# MAGIC .join(df2, "inner", "id")
# MAGIC
# MAGIC 👉 Almost always wrong order → fix it to:
# MAGIC python
# MAGIC .join(df2, "id", "inner")

# COMMAND ----------

# DBTITLE 1,Cell 55
# MAGIC %md
# MAGIC Question #:52<br>**Which of the following operations can perform an outer join on two DataFrames?**<br>A. DataFrame.crossJoin()<br>B. Standalone join() function<br>C. DataFrame.outerJoin()<br>D. DataFrame.join()<br>E. DataFrame.merge()<br>

# COMMAND ----------

# MAGIC %md
# MAGIC ✅ Correct Answer: D
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Explanation**
# MAGIC
# MAGIC ✔ In PySpark, outer joins are performed using:
# MAGIC python
# MAGIC df1.join(df2, on="column", how="outer")
# MAGIC
# MAGIC
# MAGIC 👉 The `join()` method supports all join types:
# MAGIC - `"inner"`
# MAGIC - `"left"`
# MAGIC - `"right"`
# MAGIC - `"outer"` ✅
# MAGIC - `"left_outer"`, `"right_outer"`, `"full_outer"`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are wrong**
# MAGIC - **A. crossJoin()** → ❌ Cartesian join (no condition), not outer join
# MAGIC - **B. Standalone join() function** → ❌ No such function in PySpark
# MAGIC - **C. outerJoin()** → ❌ No such method exists
# MAGIC - **E. merge()** → ❌ Used in Pandas, not PySpark
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Final takeaway**
# MAGIC
# MAGIC | Operation           | Supports Outer Join? |
# MAGIC |---------------------|---------------------|
# MAGIC | DataFrame.join()    | ✅ YES              |
# MAGIC | crossJoin()         | ❌ NO               |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🚀 **Example**
# MAGIC python
# MAGIC df1.join(df2, "id", "outer")
# MAGIC
# MAGIC
# MAGIC 👉 **Exam tip:**  
# MAGIC If you see any join type in Spark → answer is almost always `DataFrame.join()`

# COMMAND ----------

# DBTITLE 1,Cell 56
# MAGIC %md
# MAGIC Question #:53<br>**Which of the following pairs of arguments cannot be used in DataFrame.join() to perform an inner join on two DataFrames, named and aliased with "a" and "b" respectively, to specify two key columns?**<br>A. on = [a.column1 == b.column1, a.column2 == b.column2]<br>B. on = [col("column1"), col("column2")]<br>C. on = [col("a.column1") == col("b.column1"), col("a.column2") == col("b.column2")]<br>D. All of these options can be used to perform an inner join with two key columns.<br>E. on = ["column1", "column2"]<br>

# COMMAND ----------

# MAGIC %md
# MAGIC ✅ Correct Answer: B
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Understanding the question**
# MAGIC
# MAGIC We need to find:
# MAGIC
# MAGIC ❗ Which option CANNOT be used to perform an inner join on two key columns
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Valid join formats in PySpark**
# MAGIC
# MAGIC | Format                                 | Valid? |
# MAGIC |-----------------------------------------|--------|
# MAGIC | ["col1", "col2"]                       | ✅     |
# MAGIC | [df1.col == df2.col, df1.col2 == df2.col2] | ✅     |
# MAGIC | [col("a.col1") == col("b.col1"), col("a.col2") == col("b.col2")] | ✅     |
# MAGIC | [col("col1"), col("col2")]              | ❌     |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option A — Valid**
# MAGIC on = [a.column1 == b.column1, a.column2 == b.column2]
# MAGIC
# MAGIC ✔ Explicit join condition
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Option B — INVALID (Correct Answer)**
# MAGIC on = [col("column1"), col("column2")]
# MAGIC
# MAGIC 🚫 Problem:  
# MAGIC This is just a list of Column objects, not conditions.  
# MAGIC Spark expects either column names (strings) or boolean expressions.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option C — Valid**
# MAGIC on = [col("a.column1") == col("b.column1"),
# MAGIC       col("a.column2") == col("b.column2")]
# MAGIC
# MAGIC ✔ Fully valid condition-based join
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option E — Valid**
# MAGIC on = ["column1", "column2"]
# MAGIC
# MAGIC ✔ Standard way for joining on multiple columns (same names)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Option D — Incorrect**
# MAGIC Because B is invalid, so not all options work
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Final takeaway**
# MAGIC
# MAGIC - Strings → OK
# MAGIC - Boolean conditions → OK
# MAGIC - Plain Column objects → ❌ WRONG

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

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ✅ A. The larger DataFrame employeesDF is being broadcasted rather than the smaller DataFrame storesDF.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC - In a broadcast join, the smaller DataFrame should be broadcasted to all worker nodes to avoid shuffling the larger DataFrame.
# MAGIC - The given code:
# MAGIC   
# MAGIC   python
# MAGIC   storesDF.join(broadcast(employeesDF), "storeId")
# MAGIC   
# MAGIC   broadcasts the much larger `employeesDF`, which is inefficient.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Correct approach:**
# MAGIC
# MAGIC - Broadcast the smaller DataFrame:
# MAGIC
# MAGIC   python
# MAGIC   broadcast(storesDF).join(employeesDF, "storeId")
# MAGIC   
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Why other options are incorrect:**
# MAGIC
# MAGIC - **B:** `DataFrame.join()` is valid in Spark; no need for `merge()`.
# MAGIC - **C:** You can use `broadcast()` directly; no need to rely on config.
# MAGIC - **D:** Spark supports broadcast joins.
# MAGIC - **E:** `broadcast()` function exists (`pyspark.sql.functions.broadcast`).
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ The logical error: broadcasting the wrong (larger) DataFrame.

# COMMAND ----------

# DBTITLE 1,Cell 58
# MAGIC %md
# MAGIC

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

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ✅ C. A cross join is not implemented by the DataFrame.join() operation – the DataFrame.crossJoin() operation should be used instead.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Explanation
# MAGIC
# MAGIC The given code:
# MAGIC
# MAGIC python
# MAGIC storesDF.join(employeesDF, "cross")
# MAGIC
# MAGIC
# MAGIC is incorrect because `"cross"` is being passed as the join column, not as a join type.
# MAGIC
# MAGIC - In Spark, a cross join is **not** specified this way.
# MAGIC - The correct way to perform a cross join is:
# MAGIC
# MAGIC   python
# MAGIC   storesDF.crossJoin(employeesDF)
# MAGIC   
# MAGIC
# MAGIC   Or, using `join()` with the `how` argument:
# MAGIC
# MAGIC   python
# MAGIC   storesDF.join(employeesDF, how="cross")
# MAGIC   
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### ❌ Why other options are incorrect
# MAGIC
# MAGIC - **A & E:** No such standalone `CrossJoin()` or alternative `join()` function exists.
# MAGIC - **B:** Spark does support cross joins directly.
# MAGIC - **D:** Cross joins do not require a key column.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Summary:**  
# MAGIC The error is misunderstanding how cross joins are invoked in Spark. Use `crossJoin()` for a cross join.

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

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC ✅ C. The DataFrame.unionByName() operation does not union DataFrames based on column position – it uses column name instead.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC - `storesDF.unionByName(acquiredStoresDF)` aligns columns by **name**, not by position.
# MAGIC - The question intends a **position-wise union**.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Correct approach:**
# MAGIC
# MAGIC - For position-based union, use:
# MAGIC   python
# MAGIC   storesDF.union(acquiredStoresDF)
# MAGIC   
# MAGIC - **Key difference:**
# MAGIC   - `union()` → matches columns by position
# MAGIC   - `unionByName()` → matches columns by name
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Why other options are incorrect:**
# MAGIC - **A:** `unionByName()` exists in Spark.
# MAGIC - **B:** No key columns needed for union.
# MAGIC - **D:** `unionByName()` is a DataFrame method.
# MAGIC - **E:** No explicit column positions needed.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Cell 61
# MAGIC %md
# MAGIC Question #:57<br>**Which of the following code blocks writes DataFrame storesDF to file path filePath as JSON?**<br>A. storesDF.write.option("json").path(filePath)<br>B. storesDF.write.json(filePath)<br>C. storesDF.write.path(filePath)<br>D. storesDF.write(filePath)<br>E. storesDF.write().json(filePath)<br>

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC B. storesDF.write.json(filePath)
# MAGIC
# MAGIC Explanation:
# MAGIC In Spark, writing a DataFrame to JSON is done using the DataFrameWriter API.
# MAGIC
# MAGIC The correct syntax is:
# MAGIC
# MAGIC storesDF.write.json(filePath)
# MAGIC This directly writes the DataFrame in JSON format to the specified path.
# MAGIC
# MAGIC Why other options are incorrect:
# MAGIC A: .option("json") is invalid — format should be specified using .format("json"), not option.
# MAGIC C: .path() is not a valid method for writing.
# MAGIC D: .write(filePath) is not valid syntax.
# MAGIC E: .write() is not callable as a function — it is a property, so parentheses are incorrect.
# MAGIC
# MAGIC ✅ Therefore, Option B is the correct and standard way to write a DataFrame as JSON in Spark.

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

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC C. 4, 6, 2, 3
# MAGIC
# MAGIC ✅ Correct Order Breakdown:
# MAGIC
# MAGIC Let’s map the steps:
# MAGIC
# MAGIC 4 → storesDF  
# MAGIC Start with the DataFrame.  
# MAGIC 6 → write  
# MAGIC Begin the write operation.  
# MAGIC 2 → partitionBy("division")  
# MAGIC Specify that the output files should be partitioned by the division column.  
# MAGIC 3 → parquet(filePath)  
# MAGIC Write the DataFrame in Parquet format to the given path.  
# MAGIC
# MAGIC ✔ Final Correct Code:
# MAGIC storesDF.write \
# MAGIC         .partitionBy("division") \
# MAGIC         .parquet(filePath)
# MAGIC
# MAGIC ❌ Why others are incorrect:
# MAGIC A, B, D, E: Either:
# MAGIC - Use incorrect methods like .write() (should be .write)
# MAGIC - Use invalid .path(filePath, "parquet")
# MAGIC - Miss required steps like correct write chaining
# MAGIC
# MAGIC ✅ So, Option C correctly orders the operations for writing partitioned Parquet data.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC E. There is no source parameter to the load() operation – it can be removed.
# MAGIC
# MAGIC Explanation:
# MAGIC
# MAGIC The given code:
# MAGIC
# MAGIC spark.read.load(filePath, source – "parquet")
# MAGIC
# MAGIC contains an error because:
# MAGIC
# MAGIC The load() method does not use a parameter named source.
# MAGIC To specify the file format, Spark uses the parameter format, not source.
# MAGIC
# MAGIC ✅ Correct ways to read a Parquet file:
# MAGIC
# MAGIC Option 1: Using load() with format
# MAGIC
# MAGIC spark.read.format("parquet").load(filePath)
# MAGIC
# MAGIC Option 2: Using the dedicated method
# MAGIC
# MAGIC spark.read.parquet(filePath)
# MAGIC
# MAGIC Why other options are incorrect:
# MAGIC A: schema is unrelated to specifying file format.
# MAGIC B: load() does exist and is valid.
# MAGIC C: spark.read is a property, not a function—no parentheses needed.
# MAGIC D: filePath may already be a variable, so quoting is not necessarily required.
# MAGIC
# MAGIC ✅ So, the actual issue is the invalid source parameter; use format instead.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC C. 3, 5, 1
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct Order Breakdown:**
# MAGIC
# MAGIC | Step | Code Line                                 | Description                                 |
# MAGIC |------|-------------------------------------------|---------------------------------------------|
# MAGIC | 3    | spark \                                   | Start with the SparkSession.                |
# MAGIC | 5    | .read \                                   | Access the DataFrameReader.                 |
# MAGIC | 1    | .json(filePath, schema = schema)          | Read the JSON file with the specified schema.|
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔ **Final Correct Code:**
# MAGIC python
# MAGIC spark \
# MAGIC   .read \
# MAGIC   .json(filePath, schema=schema)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - 2 (.storesDF): Not relevant for reading data.
# MAGIC - 4 (.read()): Incorrect — read is a property, not a method.
# MAGIC - 6 (.json(filePath, format = schema)): Invalid argument (format is not used this way).

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **D. MEMORY_AND_DISK_2**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC We need a storage level that:
# MAGIC
# MAGIC - Stores as much data as possible in memory
# MAGIC - Spills excess data to disk if it doesn’t fit
# MAGIC - Replicates data across two cluster nodes
# MAGIC
# MAGIC 🔍 **Breakdown of the correct option:**
# MAGIC - `MEMORY_AND_DISK` → Stores data in memory, spills to disk if needed ✅
# MAGIC - `_2` suffix → Replicates data across 2 nodes ✅
# MAGIC
# MAGIC So:
# MAGIC
# MAGIC **MEMORY_AND_DISK_2**
# MAGIC
# MAGIC - ✔ Memory first
# MAGIC - ✔ Disk fallback
# MAGIC - ✔ Replication on 2 nodes
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are incorrect:**
# MAGIC - **A. MEMORY_ONLY_2** → No disk fallback ❌
# MAGIC - **B. MEMORY_AND_DISK_SER** → Uses serialization, but no replication ❌
# MAGIC - **C. MEMORY_AND_DISK** → No replication ❌
# MAGIC - **E. MEMORY_ONLY** → No disk fallback ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ Therefore, MEMORY_AND_DISK_2 perfectly matches all requirements.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **B. spark.sql.autoBroadcastJoinThreshold**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The property `spark.sql.autoBroadcastJoinThreshold` controls the maximum size (in bytes) of a DataFrame that Spark will automatically broadcast during a join.
# MAGIC
# MAGIC If a DataFrame is smaller than this threshold, Spark will broadcast it to all worker nodes to perform a broadcast join, improving performance.
# MAGIC
# MAGIC **Key details:**
# MAGIC - Default value is typically 10 MB (may vary by Spark version).
# MAGIC - Setting it to -1 disables automatic broadcasting.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **A. spark.sql.broadcastTimeout** → Controls how long to wait for a broadcast, not size ❌
# MAGIC - **C. spark.sql.shuffle.partitions** → Controls number of shuffle partitions ❌
# MAGIC - **D. spark.sql.inMemoryColumnarStorage.batchSize** → Related to caching, not joins ❌
# MAGIC - **E. spark.sql.adaptive.skewedJoin.enabled** → Handles skewed joins ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ Therefore, the correct configuration property is `spark.sql.autoBroadcastJoinThreshold`.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **A. spark.sql.adaptive.skewedJoin.enabled**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The property `spark.sql.adaptive.skewedJoin.enabled` is part of Adaptive Query Execution (AQE) in Spark. It enables Spark to:
# MAGIC
# MAGIC - Detect skewed partitions during joins
# MAGIC - Split large (skewed) partitions into smaller ones
# MAGIC - Improve performance by avoiding bottlenecks caused by uneven data distribution
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **B. spark.sql.adaptive.coalescePartitions.enable** → Controls partition coalescing, not skew handling ❌
# MAGIC - **C. spark.sql.adaptive.skewHints.enabled** → Not a valid Spark property ❌
# MAGIC - **D. spark.sql.shuffle.partitions** → Sets number of shuffle partitions ❌
# MAGIC - **E. spark.sql.shuffle.skewHints.enabled** → Not a valid Spark property ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ Therefore, the correct configuration property is `spark.sql.adaptive.skewedJoin.enabled`.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **D. A Spark DataFrame is a tabular data structure that is the most common Structured API in Spark.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC - A Spark DataFrame is a distributed, tabular data structure (like a table with rows and columns).
# MAGIC - It is part of Spark’s Structured APIs.
# MAGIC - It is the most widely used abstraction in Spark for data processing.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **A:** Spark DataFrames are immutable, not mutable.
# MAGIC - **B:** They are used extensively for transformations and analytics, not just I/O.
# MAGIC - **C:** They are distributed across partitions by design.
# MAGIC - **E:** They are similar to Python/R data frames but not exactly the same (distributed, lazy execution, optimized engine).
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ Therefore, Option D is the correct statement.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **C. storesDF.drop()**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The `drop()` method in Spark DataFrames is used to remove one or more columns by name and return a new DataFrame.
# MAGIC
# MAGIC ✅ **Example:**
# MAGIC python
# MAGIC storesDF.drop("column1", "column2")
# MAGIC
# MAGIC This returns a new DataFrame without the specified columns.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **A. filter()** → Used to filter rows, not columns ❌
# MAGIC - **B. select()** → Used to choose columns to keep, not directly remove ❌
# MAGIC - **D. subset()** → Not a valid DataFrame method ❌
# MAGIC - **E. dropColumn()** → Not a valid Spark method ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ Therefore, `drop()` is the correct operation to remove columns by name.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **D. storesDF.filter(col("sqft") <= 25000)**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC To filter rows in a Spark DataFrame based on a condition:
# MAGIC
# MAGIC - You must reference columns properly using `col()` (from `pyspark.sql.functions`) or DataFrame column syntax.
# MAGIC - The condition must correctly reflect ≤ 25,000.
# MAGIC
# MAGIC ✅ **Correct example:**
# MAGIC python
# MAGIC from pyspark.sql.functions import col
# MAGIC
# MAGIC storesDF.filter(col("sqft") <= 25000)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **A.** Uses `>` instead of `<=` and incorrect column reference ❌
# MAGIC - **B.** `sqft` is not defined as a column object ❌
# MAGIC - **C.** `"sqft"` is a string, so comparison is invalid ❌
# MAGIC - **E.** Same issues as A (wrong operator and column reference) ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ Therefore, Option D is the correct way to filter the DataFrame.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **B. storesDF.filter(col("sqft") <= 25000 | col("customerSatisfaction") >= 30)**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC - Use `|` for OR, `&` for AND in Spark DataFrame filters.
# MAGIC - Use `col()` to reference columns.
# MAGIC
# MAGIC ✅ **Correct example:**
# MAGIC python
# MAGIC from pyspark.sql.functions import col
# MAGIC
# MAGIC storesDF.filter(
# MAGIC     (col("sqft") <= 25000) | (col("customerSatisfaction") >= 30)
# MAGIC )
# MAGIC
# MAGIC ❗ **Important note:**  
# MAGIC Wrap each condition in parentheses due to operator precedence.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **A:** Uses Python `and` (not supported for column expressions) ❌
# MAGIC - **C:** Missing quotes around column names + uses `or` ❌
# MAGIC - **D:** Columns not defined properly ❌
# MAGIC - **E:** Uses Python `or` instead of `|` ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key takeaway:**  
# MAGIC - `|` → OR  
# MAGIC - `&` → AND  
# MAGIC - `col("columnName")` → proper column reference
# MAGIC
# MAGIC ✅ Therefore, Option B is correct.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC A. 1. withColumn  
# MAGIC    2. col  
# MAGIC    3. cast  
# MAGIC    4. StringType()
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC To change the data type of a column in a Spark DataFrame, use:
# MAGIC
# MAGIC - `withColumn()` → to replace or create a column  
# MAGIC - `col()` → to reference the column  
# MAGIC - `cast()` → to change the data type  
# MAGIC - `StringType()` → the target data type (must be instantiated)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔ **Final Correct Code:**
# MAGIC python
# MAGIC from pyspark.sql.functions import col
# MAGIC from pyspark.sql.types import StringType
# MAGIC
# MAGIC storesDF.withColumn("storeId", col("storeId").cast(StringType()))
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **B:** Incorrect order (cast and col swapped)  
# MAGIC - **C:** `newColumn` is not a valid method  
# MAGIC - **D:** `StringType` missing parentheses  
# MAGIC - **E:** Same issue — `StringType` must be called as a function  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key takeaway:**
# MAGIC
# MAGIC Always use:
# MAGIC python
# MAGIC col("column").cast(DataType())
# MAGIC
# MAGIC And wrap it inside:
# MAGIC python
# MAGIC withColumn("column", ...)
# MAGIC
# MAGIC
# MAGIC ✅ Therefore, Option A is correct.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **C. storesDF.withColumn("modality", lit("PHYSICAL"))**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC To assign a constant value to a column in a Spark DataFrame:
# MAGIC
# MAGIC - Use `lit()` (from `pyspark.sql.functions`)
# MAGIC - It converts a literal value into a Spark column
# MAGIC
# MAGIC ✔ **Correct code:**
# MAGIC python
# MAGIC from pyspark.sql.functions import lit
# MAGIC
# MAGIC storesDF.withColumn("modality", lit("PHYSICAL"))
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **A:** `PHYSICAL` is not in quotes → treated as a variable ❌
# MAGIC - **B:** `col("PHYSICAL")` refers to a column named PHYSICAL, not a value ❌
# MAGIC - **D:** `StringType()` is for casting, not assigning values ❌
# MAGIC - **E:** `"PHYSICAL"` is not wrapped in `lit()` → invalid ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key takeaway:**
# MAGIC Use `lit("value")` to assign constant values to a column.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC D. The split() operation comes from the imported functions object. It accepts a Column object and split character as arguments. It is not a method of a Column object.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **What’s wrong in the code:**
# MAGIC python
# MAGIC storesDF.withColumn("managerFirstName", col("managerName").split(" ").getItem(0)) \
# MAGIC         .withColumn("managerLastName", col("managerName").split(" ").getItem(1))
# MAGIC
# MAGIC Here, `.split()` is being used as a method on a Column object, which is incorrect in PySpark.  
# MAGIC In Spark, `split()` is a function from `pyspark.sql.functions`, not a Column method.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct approach:**
# MAGIC python
# MAGIC from pyspark.sql.functions import col, split
# MAGIC
# MAGIC storesDF.withColumn("managerFirstName", split(col("managerName"), " ").getItem(0)) \
# MAGIC         .withColumn("managerLastName", split(col("managerName"), " ").getItem(1))
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key points:**
# MAGIC - `split(column, delimiter)` → function, not method
# MAGIC - Returns an array column, so you use `.getItem(index)`
# MAGIC - Indexing starts at 0, so 0 and 1 are correct
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **A:** Indexing starts at 0, so 0 and 1 are correct ❌
# MAGIC - **B:** `split()` does not take index as argument ❌
# MAGIC - **C:** Says it takes a string column name — incorrect ❌
# MAGIC - **E:** You can chain `withColumn()` calls ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ Therefore, the error is misuse of `split()` as a method instead of a function.

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import split, col

# Create Spark session
spark = SparkSession.builder.appName("SplitExample").getOrCreate()

# Sample data
data = [
    ("John Doe",),
    ("Alice Smith",),
    ("Bob Johnson",)
]

# Create DataFrame
storesDF = spark.createDataFrame(data, ["managerName"])

# Apply split logic
resultDF = storesDF \
    .withColumn("managerFirstName", split("managerName", " ").getItem(0)) \
    .withColumn("managerLastName", split("managerName", " ").getItem(1))

# Show result
resultDF.show()

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **D.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC To replace characters in a column, Spark provides:
# MAGIC
# MAGIC - `regexp_replace()` → used to replace matching patterns in a column
# MAGIC
# MAGIC **Syntax:**
# MAGIC
# MAGIC regexp_replace(column, pattern, replacement)
# MAGIC
# MAGIC
# MAGIC ✔ **Correct filled code:**
# MAGIC ```python
# MAGIC from pyspark.sql.functions import col, regexp_replace
# MAGIC
# MAGIC storesDF.withColumn(
# MAGIC     "storeSlogan",
# MAGIC     regexp_replace(col("storeSlogan"), "'", "\"")
# MAGIC )
# MAGIC ```
# MAGIC
# MAGIC
# MAGIC 🔍 **Why Option D is correct:**
# MAGIC - `withColumn` → correct method to modify a column ✅
# MAGIC - `"storeSlogan"` → correct column name ✅
# MAGIC - `regexp_replace` → correct function for replacing text ✅
# MAGIC - `col("storeSlogan")` → correct column reference ✅
# MAGIC - `"'"` → pattern (single quote) ✅
# MAGIC - `"""` → replacement (double quote) ✅
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **A & E:** Use `regexp_extract` (wrong function) ❌
# MAGIC - **B:** Invalid method (`newColumn`) and syntax issues ❌
# MAGIC - **C:** Reverses pattern and replacement ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key takeaway:**
# MAGIC - Use `regexp_replace()` to replace characters
# MAGIC - Pattern comes first, replacement comes second

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
# MAGIC
# MAGIC The correct answer is:
# MAGIC
# MAGIC **A. storesDF.withColumnRenamed("division", "state")  
# MAGIC    .withColumnRenamed("managerName", "managerFullName")**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC To rename columns in a Spark DataFrame, you use:
# MAGIC
# MAGIC - `withColumnRenamed(existingName, newName)`
# MAGIC
# MAGIC This method:
# MAGIC - Renames the column
# MAGIC - Returns a new DataFrame
# MAGIC - Can be chained for multiple renames
# MAGIC
# MAGIC ✔ **Correct code:**
# MAGIC python
# MAGIC storesDF.withColumnRenamed("division", "state") \
# MAGIC         .withColumnRenamed("managerName", "managerFullName")
# MAGIC
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **B:** `withColumn("state", "division")` assigns a string, not a column ❌
# MAGIC - **C:** Creates new columns but does not remove old ones ❌
# MAGIC - **D:** Invalid syntax — `withColumnRenamed` does not take sequences ❌
# MAGIC - **E:** Reverses the rename direction ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key takeaway:**
# MAGIC - Use `withColumnRenamed(oldName, newName)` for renaming
# MAGIC - Chain it to rename multiple columns
# MAGIC
# MAGIC ✅ Therefore, Option A is correct.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **E. storesDF.na.fill(30000, "sqft")**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC To replace null (missing) values in specific columns in Spark:
# MAGIC
# MAGIC - Use `na.fill(value, subset)`
# MAGIC - `subset` can be a column name (string) or a list of column names
# MAGIC
# MAGIC ✔ **Correct code:**
# MAGIC python
# MAGIC storesDF.na.fill(30000, "sqft")
# MAGIC
# MAGIC
# MAGIC 🔍 **Key points:**
# MAGIC - `na` → access missing data functions
# MAGIC - `fill()` → replaces null values
# MAGIC - `"sqft"` → specifies the column to apply the replacement
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **A:** Uses `Seq()` → Scala syntax, not Python ❌
# MAGIC - **B:** `nafill` is not a valid method ❌
# MAGIC - **C:** `col("sqft")` not valid for subset argument ❌
# MAGIC - **D:** `fillna()` exists, but second argument must be string/list, not column ❌
# MAGIC
# MAGIC 🔑 **Alternative valid form:**
# MAGIC python
# MAGIC storesDF.fillna({"sqft": 30000})
# MAGIC
# MAGIC
# MAGIC ✅ Therefore, Option E is correct.

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
# MAGIC
# MAGIC **The correct answer is E. DataFrame.dropDuplicates(), DataFrame.distinct() and DataFrame.drop_duplicates() ✅.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation**
# MAGIC
# MAGIC In the context of Apache Spark (PySpark), all three methods can be used to achieve the same result of returning a DataFrame with no duplicate rows:
# MAGIC
# MAGIC - **DataFrame.distinct():** This is a standard transformation that returns a new DataFrame containing only unique rows.
# MAGIC - **DataFrame.dropDuplicates():** This method also returns a new DataFrame with duplicate rows removed. It is more flexible than distinct() because it allows you to specify a subset of columns to check for duplicates while still retaining the original columns in the output.
# MAGIC - **DataFrame.drop_duplicates():** This is simply an alias for dropDuplicates(), provided for convenience to users coming from other libraries like Pandas.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Why other options are less complete**
# MAGIC
# MAGIC - ❌ **A, C, and D:** These options only list one valid method each, making them incomplete.
# MAGIC - ❌ **B:** This option only lists two of the three valid methods.
# MAGIC - ✅ **E:** This is the most comprehensive answer because it includes the standard Spark methods (distinct and dropDuplicates) as well as the official alias (drop_duplicates).

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **C. storesDF.agg(approx_count_distinct(col("division")).alias("divisionDistinct"))**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC To compute the approximate number of distinct values in a column, Spark provides:
# MAGIC
# MAGIC - `approx_count_distinct()` → an aggregation function
# MAGIC
# MAGIC Since this is an aggregation, you must use:
# MAGIC
# MAGIC - `agg()`, not `withColumn()`
# MAGIC
# MAGIC ✔ **Correct code:**
# MAGIC python
# MAGIC from pyspark.sql.functions import col, approx_count_distinct
# MAGIC
# MAGIC storesDF.agg(
# MAGIC     approx_count_distinct(col("division")).alias("divisionDistinct")
# MAGIC )
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Why Option C is correct:**
# MAGIC - Uses `agg()` → required for aggregation ✅
# MAGIC - Uses `approx_count_distinct()` correctly ✅
# MAGIC - Uses `alias()` to name the output column ✅
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **A:** Uses `withColumn()` → not valid for aggregation ❌
# MAGIC - **B:** Incorrect syntax — `approx_count_distinct` is not a column method ❌
# MAGIC - **D:** Same issue — not a column method ❌
# MAGIC - **E:** Same mistake as B/D ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key takeaway:**
# MAGIC - Aggregations → use `agg()`
# MAGIC - Functions like `approx_count_distinct()` are not column methods

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **A.**
# MAGIC
# MAGIC 1. agg  
# MAGIC 2. mean  
# MAGIC 3. col("sqft")
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC To compute the mean (average) of a column in Spark:
# MAGIC
# MAGIC - Use the aggregation function `mean()`
# MAGIC - Wrap it inside `agg()`
# MAGIC - Reference the column using `col()`
# MAGIC - Use `alias()` to name the result column
# MAGIC
# MAGIC ✔ **Correct code:**
# MAGIC python
# MAGIC from pyspark.sql.functions import mean, col
# MAGIC
# MAGIC storesDF.agg(mean(col("sqft")).alias("sqftMean"))
# MAGIC
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **B:** `withColumn()` is not used for aggregations ❌
# MAGIC - **C:** `average` is not a valid function (correct is `mean`) ❌
# MAGIC - **D:** Incorrect structure and missing aggregation ❌
# MAGIC - **E:** While `"sqft"` can work, the expected canonical form uses `col("sqft")` ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key takeaway:**
# MAGIC - Aggregations → use `agg()`
# MAGIC - Mean → use `mean()`
# MAGIC - Best practice → use `col("columnName")`
# MAGIC
# MAGIC ✅ Therefore, Option A is correct.

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
# MAGIC
# MAGIC **The correct answer is:**
# MAGIC
# MAGIC **E. storesDF.groupBy("division").count()**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC To get the number of rows for each unique value in a column:
# MAGIC
# MAGIC - Use `groupBy("column")`
# MAGIC - Then apply `count()`
# MAGIC
# MAGIC ✔ **Correct code:**
# MAGIC python
# MAGIC storesDF.groupBy("division").count()
# MAGIC
# MAGIC
# MAGIC This returns a DataFrame like:
# MAGIC
# MAGIC | division | count |
# MAGIC |----------|-------|
# MAGIC |   East   |  10   |
# MAGIC |   West   |  15   |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **A:** `count()` inside `agg()` needs a column or `*` ❌
# MAGIC - **B:** Incorrect syntax — `groupBy` is not used inside `agg()` ❌
# MAGIC - **C:** Invalid method chaining ❌
# MAGIC - **D:** `groupBy()` requires a column for grouping ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key takeaway:**
# MAGIC - Grouping → `groupBy("column")`
# MAGIC - Aggregation → `.count()`
# MAGIC
# MAGIC ✅ Therefore, Option E is correct.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **A. storesDF.sort("division")**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC To sort a DataFrame alphabetically (ascending) by a column:
# MAGIC
# MAGIC - Use `sort("column")` or `orderBy("column")`
# MAGIC - Default sorting is ascending
# MAGIC
# MAGIC ✔ **Correct code:**
# MAGIC python
# MAGIC storesDF.sort("division")
# MAGIC
# MAGIC
# MAGIC 🔍 **Why this works:**
# MAGIC - `"division"` is sorted in ascending order (A → Z) by default
# MAGIC - No need to explicitly specify ascending
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **B:** Uses `desc()` → descending order ❌
# MAGIC - **C:** Also descending ❌
# MAGIC - **D:** ❗ This is actually correct in practice, but exams typically expect the simplest canonical form ❌
# MAGIC - **E:** Uses descending ❌
# MAGIC
# MAGIC 🧠 **Important note:**
# MAGIC
# MAGIC Both of these are valid in real Spark:
# MAGIC python
# MAGIC storesDF.sort("division")
# MAGIC storesDF.orderBy("division", ascending=True)
# MAGIC
# MAGIC But Option A is the most direct and expected answer
# MAGIC
# MAGIC 🔑 **Key takeaway:**
# MAGIC - Default sort = ascending
# MAGIC - `sort()` and `orderBy()` are interchangeable
# MAGIC
# MAGIC ✅ Therefore, Option A is the best answer.

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
# MAGIC
# MAGIC **The correct answer is:**
# MAGIC
# MAGIC **B. storesDF.sample(true, fraction = 0.1)**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC The syntax for sampling in Spark is:
# MAGIC
# MAGIC `DataFrame.sample(withReplacement, fraction, seed=None)`
# MAGIC
# MAGIC Where:
# MAGIC
# MAGIC - **withReplacement = True** → allows duplicate rows  
# MAGIC - **fraction = 0.1** → 10% sample  
# MAGIC
# MAGIC ✔ **Correct code:**  
# MAGIC `storesDF.sample(True, fraction=0.1)`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A:** Missing fraction argument ❌  
# MAGIC - **C:** Uses 15% instead of 10% ❌  
# MAGIC - **D:** `sampleBy()` is for stratified sampling, not simple sampling ❌  
# MAGIC - **E:** Uses False → no replacement ❌  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key takeaway:**
# MAGIC
# MAGIC - **True** → with replacement  
# MAGIC - **fraction=0.1** → 10% sample  
# MAGIC
# MAGIC ✅ Therefore, Option B is correct.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **D. storesDF.head(3)**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC To retrieve the first n rows from a Spark DataFrame, you can use:
# MAGIC
# MAGIC - `storesDF.head(3)`  
# MAGIC   - Returns the first 3 rows  
# MAGIC   - Output is a list of Row objects  
# MAGIC
# MAGIC ⚠️ **Important note:**
# MAGIC
# MAGIC Although `take(3)` also works similarly, the most commonly expected answer in exams for “first n rows” is `head(n)`.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **A.** `top_n(3)` → Not a valid Spark method ❌
# MAGIC - **B.** `n(3)` → Not a valid method ❌
# MAGIC - **C.** `take(3)` → ❗ Works in practice, but not the “best” answer here ❌
# MAGIC - **E.** `collect(3)` → `collect()` takes no arguments ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Extra tip:**
# MAGIC
# MAGIC | Method     | Behavior         |
# MAGIC |------------|------------------|
# MAGIC | head(n)    | First n rows     |
# MAGIC | take(n)    | Also first n rows|
# MAGIC | collect()  | All rows         |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Final takeaway:**
# MAGIC - Use `head(n)` for first n rows (exam-preferred answer)
# MAGIC
# MAGIC ✅ Therefore, Option D is correct.

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
# MAGIC
# MAGIC The correct answer is:
# MAGIC
# MAGIC **E. storesDF.collect.foreach(row => assessPerformance(row))**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC - `collect()` → brings all rows from the DataFrame to the driver as a collection (list/array)
# MAGIC - Then you can apply a function to each row using: `foreach()`
# MAGIC
# MAGIC ✔ **Correct logic:**
# MAGIC python
# MAGIC storesDF.collect().foreach(lambda row: assessPerformance(row))
# MAGIC
# MAGIC *(Note: Syntax in options resembles Scala-style, but concept is the same.)*
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Why Option E is correct:**
# MAGIC - Uses collect to retrieve rows ✅
# MAGIC - Uses foreach to iterate over each row ✅
# MAGIC - Applies function to each row correctly ✅
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **A:** Incorrect syntax — function call instead of passing function ❌
# MAGIC - **B:** `apply()` is not valid here ❌
# MAGIC - **C:** `apply` not used this way ❌
# MAGIC - **D:** Incorrect use of `map()` and function call ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚠️ **Important note:**
# MAGIC
# MAGIC Using `collect()`:
# MAGIC - Brings all data to the driver
# MAGIC - Can cause memory issues for large DataFrames
# MAGIC
# MAGIC 👉 **Better alternative (distributed):**
# MAGIC python
# MAGIC storesDF.foreach(lambda row: assessPerformance(row))
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key takeaway:**
# MAGIC - `collect()` + `foreach()` → applies function row by row
# MAGIC - But prefer distributed operations when possible
# MAGIC
# MAGIC ✅ Therefore, Option E is correct.

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
# MAGIC
# MAGIC The correct answer is:
# MAGIC
# MAGIC **D. The printSchema member of DataFrame is an operation that prints the DataFrame – there is no need to call getAs.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC - `printSchema()` is a method that:
# MAGIC   - Directly prints the schema to the console
# MAGIC   - Does not return a DataFrame or value
# MAGIC
# MAGIC ❌ **What’s wrong in the code:**
# MAGIC - `storesDF.printSchema.getAs[String]`
# MAGIC   - `printSchema` is:
# MAGIC     - A method, so it should be called with `()`
# MAGIC     - It does not return anything, so chaining `.getAs[...]` is invalid
# MAGIC
# MAGIC ✔ **Correct usage:**
# MAGIC - `storesDF.printSchema()`
# MAGIC
# MAGIC 🔍 **Key point:**
# MAGIC - `getAs[...]` is used for Row objects, not DataFrames
# MAGIC - `printSchema()` is terminal (just prints, no return)
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **A, B, E:** `printSchema()` does exist ❌
# MAGIC - **C:** Not related to the issue ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Final takeaway:**
# MAGIC - Use `printSchema()` directly — no chaining needed
# MAGIC
# MAGIC ✅ Therefore, Option D is correct.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **A.**
# MAGIC
# MAGIC scala
# MAGIC spark.udf.register("ASSESS_PERFORMANCE", assessPerformance)
# MAGIC spark.sql("SELECT customerSatisfaction, ASSESS_PERFORMANCE(customerSatisfaction) AS result FROM stores")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC To use a UDF in Spark SQL, you must:
# MAGIC
# MAGIC - **Register the UDF**
# MAGIC   scala
# MAGIC   spark.udf.register("ASSESS_PERFORMANCE", assessPerformance)
# MAGIC   
# MAGIC - **Call it inside a SQL query using the registered name**
# MAGIC   
# MAGIC   SELECT ..., ASSESS_PERFORMANCE(column) ...
# MAGIC   
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Why Option A is correct:**
# MAGIC - Registers the UDF with name `"ASSESS_PERFORMANCE"` ✅
# MAGIC - Uses it correctly in SQL query ✅
# MAGIC - Applies it to `customerSatisfaction` column ✅
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **B:** Only registers, does not apply ❌
# MAGIC - **C:** Uses original function name instead of registered UDF name ❌
# MAGIC - **D:** Uses DataFrame API, not SQL UDF ❌
# MAGIC - **E:** UDF cannot be directly used like a Python/Scala function in DataFrame API ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key takeaway:**
# MAGIC - **Register** → `spark.udf.register("NAME", func)`
# MAGIC - **Use in SQL** → `NAME(column)`
# MAGIC
# MAGIC ✅ Therefore, Option A is correct.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC E.
# MAGIC
# MAGIC 1. storesDF  
# MAGIC 2. createOrReplaceTempView  
# MAGIC 3. spark  
# MAGIC 4. sql  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC To query a DataFrame using Spark SQL, you must:
# MAGIC
# MAGIC **Step 1:** Create a temporary view  
# MAGIC `storesDF.createOrReplaceTempView("stores")`  
# MAGIC Registers the DataFrame as a temporary SQL table
# MAGIC
# MAGIC **Step 2:** Run SQL query  
# MAGIC `spark.sql("SELECT storeId, managerName FROM stores")`  
# MAGIC Executes SQL and returns a new DataFrame
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Why Option E is correct:**  
# MAGIC - Uses storesDF to create the temp view ✅  
# MAGIC - Uses createOrReplaceTempView correctly ✅  
# MAGIC - Uses spark.sql to query ✅  
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**  
# MAGIC - **A & D:** createOrReplaceTempView is not a method of spark ❌  
# MAGIC - **B:** createTable is not used this way ❌  
# MAGIC - **C:** query is not a valid Spark method ❌  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key takeaway:**  
# MAGIC - DataFrame → createOrReplaceTempView()  
# MAGIC - Query → spark.sql()
# MAGIC
# MAGIC ✅ Therefore, Option E is correct.

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
# MAGIC import spark.implicits._
# MAGIC
# MAGIC // Step 1: Create a Scala List
# MAGIC val years = List(2020, 2021, 2022, 2023)
# MAGIC
# MAGIC // Step 2: Create Dataset
# MAGIC val ds = spark.createDataset(years)
# MAGIC
# MAGIC // Check type
# MAGIC println(ds.getClass)   // Dataset[Int]
# MAGIC
# MAGIC // Show data
# MAGIC ds.show()
# MAGIC
# MAGIC // Step 3: Convert to DataFrame
# MAGIC val df = ds.toDF("year")
# MAGIC
# MAGIC // Check type
# MAGIC println(df.getClass)   // DataFrame (Dataset[Row])
# MAGIC
# MAGIC // Show DataFrame
# MAGIC df.show()
# MAGIC
# MAGIC // Print schema
# MAGIC df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC The correct answer is:
# MAGIC
# MAGIC **D. The result of the above is a Dataset rather than a DataFrame – the toDF operation must be called at the end.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC In Scala Spark:
# MAGIC
# MAGIC `spark.createDataset(years)`
# MAGIC
# MAGIC creates a `Dataset[Int]`, not a DataFrame.
# MAGIC
# MAGIC A DataFrame in Spark is actually:
# MAGIC - A Dataset of Rows (`Dataset[Row]`)
# MAGIC
# MAGIC ✔ **To convert to a DataFrame:**
# MAGIC `spark.createDataset(years).toDF()`
# MAGIC This converts the Dataset into a single-column DataFrame
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Key point:**
# MAGIC - `createDataset()` → returns typed Dataset
# MAGIC - `toDF()` → converts it into DataFrame
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **A:** Not required ❌
# MAGIC - **B:** Type is inferred automatically ❌
# MAGIC - **C:** `createDataset` does exist ❌
# MAGIC - **E:** Column name is optional ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Final takeaway:**
# MAGIC - Dataset ≠ DataFrame
# MAGIC - Use `.toDF()` when a DataFrame is required
# MAGIC
# MAGIC ✅ Therefore, Option D is correct.

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
# MAGIC The correct answer is:
# MAGIC
# MAGIC **C. storesDF.coalesce(4)**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC To reduce the number of partitions without a shuffle, Spark provides:
# MAGIC
# MAGIC - `coalesce(n)`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Why this works:**
# MAGIC
# MAGIC - `storesDF.coalesce(4)`
# MAGIC   - Reduces partitions from 8 → 4 ✅
# MAGIC   - Avoids shuffle (efficient) ✅
# MAGIC   - Returns a new DataFrame ✅
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚠️ **Important concept:**
# MAGIC
# MAGIC | Operation     | Shuffle? | Use case                                 |
# MAGIC |---------------|----------|------------------------------------------|
# MAGIC | repartition() | ✅ Yes   | Increase/decrease partitions with shuffle |
# MAGIC | coalesce()    | ❌ No    | Reduce partitions efficiently             |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** `repartition(4, "sqft")` → causes shuffle ❌
# MAGIC - **B.** `repartition()` → invalid usage ❌
# MAGIC - **D.** `repartition(4)` → causes shuffle ❌
# MAGIC - **E.** `coalesce` → missing argument ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key takeaway:**
# MAGIC
# MAGIC - Use `coalesce()` to reduce partitions without shuffle
# MAGIC - Use `repartition()` when you need redistribution
# MAGIC
# MAGIC ✅ Therefore, Option C is correct.

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
# MAGIC
# MAGIC The goal is to return a new DataFrame with exactly 12 partitions.
# MAGIC
# MAGIC Let’s evaluate the options:
# MAGIC
# MAGIC - **coalesce(n)** → reduces partitions (usually used to decrease partitions efficiently, not ideal for increasing)
# MAGIC - **repartition(n)** → reshuffles data and creates exactly n partitions
# MAGIC
# MAGIC So to explicitly create 12 partitions, the correct method is:
# MAGIC
# MAGIC 👉 **repartition(12)**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct answer:**
# MAGIC
# MAGIC **D.**
# MAGIC
# MAGIC
# MAGIC storesDF
# MAGIC repartition
# MAGIC 12
# MAGIC
# MAGIC
# MAGIC **Final code:**
# MAGIC scala
# MAGIC storesDF.repartition(12)
# MAGIC
# MAGIC
# MAGIC This guarantees a new DataFrame with exactly 12 partitions.

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
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Let’s break this down clearly so you understand both the correct answer and why the others are wrong.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### 🔍 What the code is trying to do
# MAGIC
# MAGIC
# MAGIC spark.conf.set("spark.default.parallelism", "32")
# MAGIC
# MAGIC
# MAGIC The intention is to set the number of partitions used in wide transformations like:
# MAGIC
# MAGIC - `join()`
# MAGIC - `groupBy()`
# MAGIC - `distinct()`
# MAGIC
# MAGIC These operations involve shuffle, and Spark controls them using:
# MAGIC
# MAGIC > **👉 `spark.sql.shuffle.partitions`**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### ❌ What’s the actual error?
# MAGIC
# MAGIC The code uses:
# MAGIC
# MAGIC
# MAGIC spark.default.parallelism ❌
# MAGIC
# MAGIC
# MAGIC But it should use:
# MAGIC
# MAGIC
# MAGIC spark.sql.shuffle.partitions ✅
# MAGIC
# MAGIC
# MAGIC **✔️ Correct version:**
# MAGIC
# MAGIC spark.conf.set("spark.sql.shuffle.partitions", "32")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **✅ Correct Answer:**
# MAGIC
# MAGIC > **A. spark.default.parallelism is not the right Spark configuration parameter – spark.sql.shuffle.partitions should be used instead.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### 💡 Why this matters
# MAGIC
# MAGIC - `spark.default.parallelism` → Used for RDD operations (low-level API)
# MAGIC - `spark.sql.shuffle.partitions` → Used for DataFrame/Dataset wide transformations
# MAGIC
# MAGIC Since the question explicitly mentions wide transformations like join(), option A is correct.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### ❌ Why the other options are wrong
# MAGIC
# MAGIC **B. There is no way to adjust the number of partitions**
# MAGIC
# MAGIC > ❌ Incorrect  
# MAGIC > You can control it using:  
# MAGIC > - `spark.sql.shuffle.partitions`  
# MAGIC > - or `repartition()`
# MAGIC
# MAGIC **C. Spark configuration parameters cannot be set in runtime**
# MAGIC
# MAGIC > ❌ Incorrect  
# MAGIC > You can set configs at runtime using:  
# MAGIC > - `spark.conf.set(...)`
# MAGIC
# MAGIC **D. Spark configuration parameters are not set with spark.conf.set()**
# MAGIC
# MAGIC > ❌ Incorrect  
# MAGIC > This is exactly the correct method for runtime configuration.
# MAGIC
# MAGIC **E. The second argument should not be a string**
# MAGIC
# MAGIC > ❌ Incorrect  
# MAGIC > Spark accepts both:  
# MAGIC > - `"32"`  
# MAGIC > - `32`  
# MAGIC > So this is not the error.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### 🧠 Final takeaway
# MAGIC
# MAGIC - Use `spark.sql.shuffle.partitions` for joins and aggregations
# MAGIC - `spark.default.parallelism` is not relevant here
# MAGIC
# MAGIC ---

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
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔍 What the code is doing
# MAGIC
# MAGIC `storesDF.withColumn("dayOfYear", dayofyear(col("openDate")))`
# MAGIC
# MAGIC The goal is to extract the day of the year from `openDate`.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🚨 The Problem
# MAGIC
# MAGIC - `openDate` is an integer  
# MAGIC - It represents a UNIX epoch timestamp (seconds since 1970-01-01)
# MAGIC
# MAGIC However:
# MAGIC
# MAGIC 👉 `dayofyear()` does **NOT** work on integers  
# MAGIC It expects a column of type:
# MAGIC
# MAGIC - DateType **OR**
# MAGIC - TimestampType
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ✅ Correct Answer:
# MAGIC
# MAGIC **A. The dayofyear() operation cannot extract the day of year from a column of type integer – column openDate must first be converted to type Timestamp.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ✔️ Correct Approach
# MAGIC
# MAGIC You must first convert the UNIX integer into a timestamp:
# MAGIC
# MAGIC python
# MAGIC from pyspark.sql.functions import col, dayofyear, from_unixtime
# MAGIC
# MAGIC storesDF.withColumn(
# MAGIC     "dayOfYear",
# MAGIC     dayofyear(from_unixtime(col("openDate")))
# MAGIC )
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🤔 Why Timestamp (and not Date)?
# MAGIC
# MAGIC - `from_unixtime()` converts integer → timestamp string  
# MAGIC - Spark can directly apply `dayofyear()` on timestamps  
# MAGIC - This is the standard and safest approach
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ❌ Why the other options are wrong
# MAGIC
# MAGIC **B. Should pass "openDate" instead of col("openDate")**
# MAGIC
# MAGIC > ❌ Incorrect  
# MAGIC > `dayofyear()` expects a Column object, not a string  
# MAGIC > `col("openDate")` is correct usage
# MAGIC
# MAGIC **C. Must convert to Date instead of Timestamp**
# MAGIC
# MAGIC > ❌ Incorrect (subtle trap)  
# MAGIC > While DateType can work, the correct first step from UNIX epoch is:  
# MAGIC > 👉 convert to Timestamp, not directly to Date  
# MAGIC > So this option is not the best answer
# MAGIC
# MAGIC **D. dayofyear() not usable with withColumn()**
# MAGIC
# MAGIC > ❌ Incorrect  
# MAGIC > This is exactly how Spark functions are used:  
# MAGIC > `df.withColumn("newCol", some_function(...))`
# MAGIC
# MAGIC **E. There is no dayofyear() function**
# MAGIC
# MAGIC > ❌ Incorrect  
# MAGIC > `dayofyear()` is a valid built-in Spark SQL function
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Final takeaway
# MAGIC
# MAGIC - UNIX epoch (integer) → must convert before using date functions  
# MAGIC - Use:  
# MAGIC   - `from_unixtime()` → Timestamp  
# MAGIC   - then `dayofyear()`
# MAGIC ---

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
# MAGIC
# MAGIC To solve this, you need to recall the correct syntax for a DataFrame join in PySpark.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔍 Correct join syntax
# MAGIC
# MAGIC `df1.join(df2, on=None, how=None)`
# MAGIC
# MAGIC Where:
# MAGIC
# MAGIC - **df2** → DataFrame to join with  
# MAGIC - **on** → join condition (column name OR expression)  
# MAGIC - **how** → join type ("inner", "left", etc.)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🎯 What the question requires
# MAGIC
# MAGIC - Join `storesDF` with `employeesDF`
# MAGIC - Join column: `storeId`
# MAGIC - Join type: `inner`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ✅ Best way to write it
# MAGIC
# MAGIC python
# MAGIC storesDF.join(employeesDF, "storeId", "inner")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ✅ Correct Answer:
# MAGIC
# MAGIC **B**
# MAGIC
# MAGIC - join
# MAGIC - employeesDF
# MAGIC - "storeId"
# MAGIC - "inner"
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ❌ Why the other options are wrong
# MAGIC
# MAGIC **A.**  
# MAGIC `join(employeesDF, "inner", condition)`
# MAGIC
# MAGIC - ❌ Wrong argument order
# MAGIC - "inner" is placed where the join condition should be
# MAGIC - The condition is placed where join type should be
# MAGIC - 👉 Order matters!
# MAGIC
# MAGIC **C.**  
# MAGIC `merge(...)`
# MAGIC
# MAGIC - ❌ merge is not a valid DataFrame method in PySpark
# MAGIC
# MAGIC **D.**  
# MAGIC `join(employeesDF, "inner", "storeId")`
# MAGIC
# MAGIC - ❌ Wrong order again
# MAGIC - "inner" is incorrectly used as the join condition
# MAGIC
# MAGIC **E.**  
# MAGIC Same as D ❌ (duplicate incorrect option)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Key takeaway
# MAGIC
# MAGIC Two valid ways to join:
# MAGIC
# MAGIC - ✔️ Using column name (simplest):  
# MAGIC   `storesDF.join(employeesDF, "storeId", "inner")`
# MAGIC - ✔️ Using condition:  
# MAGIC   `storesDF.join(employeesDF, storesDF.storeId == employeesDF.storeId, "inner")`

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
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **What the question wants**  
# MAGIC - Join `storesDF` with `employeesDF`  
# MAGIC - Join column: `storeId`  
# MAGIC - Join type: `outer`  
# MAGIC - 🧠 **Key Detail:** `Seq("storeId")`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC The presence of:
# MAGIC
# MAGIC > Seq("storeId")
# MAGIC
# MAGIC means this is **Scala Spark** (not PySpark).
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct Scala syntax**  
# MAGIC `df1.join(df2, Seq("columnName"), "joinType")`
# MAGIC
# MAGIC So the correct code is:
# MAGIC
# MAGIC scala
# MAGIC storesDF.join(employeesDF, Seq("storeId"), "outer")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct Answer:**  
# MAGIC **E**
# MAGIC
# MAGIC - join  
# MAGIC - employeesDF  
# MAGIC - Seq("storeId")  
# MAGIC - "outer"
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why the other options are wrong**
# MAGIC
# MAGIC **A.**  
# MAGIC `join(employeesDF, "outer", Seq("storeId"))`  
# MAGIC - ❌ Wrong argument order  
# MAGIC - "outer" is placed where the join column(s) should be
# MAGIC
# MAGIC **B.**  
# MAGIC `merge(...)`  
# MAGIC - ❌ merge is not a valid DataFrame method in Spark
# MAGIC
# MAGIC **C.**  
# MAGIC `join(employeesDF, "outer", condition)`  
# MAGIC - ❌ Wrong order again  
# MAGIC - "outer" is incorrectly used as the join condition  
# MAGIC - Condition should come before join type
# MAGIC
# MAGIC **D.**  
# MAGIC `merge(...)`  
# MAGIC - ❌ Same issue: merge is invalid
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Final takeaway**  
# MAGIC Scala join patterns:
# MAGIC
# MAGIC - ✔️ Using column name(s):  
# MAGIC   `df1.join(df2, Seq("col"), "outer")`
# MAGIC - ✔️ Using condition:  
# MAGIC   `df1.join(df2, df1("col") === df2("col"), "outer")`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🚀 **Quick exam trick**  
# MAGIC - If you see `Seq(...)` → Scala → column list goes **BEFORE** join type  
# MAGIC - If you see strings only → likely PySpark
# MAGIC
# MAGIC ---

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
# MAGIC
# MAGIC **The correct answer is: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔍 Why A fails
# MAGIC
# MAGIC scala
# MAGIC storesDF.join(employeesDF, Seq(col("storeId"), col("employeeId")))
# MAGIC
# MAGIC
# MAGIC The `Seq(...)` version of join expects column names as `String`, not `Column` objects.  
# MAGIC Here, `col("storeId")` and `col("employeeId")` are of type `Column`, so this results in a type mismatch / compilation error.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ✅ Why the others work
# MAGIC
# MAGIC **B**
# MAGIC
# MAGIC scala
# MAGIC storesDF.join(employeesDF, Seq("storeId", "employeeId"))
# MAGIC
# MAGIC
# MAGIC ✔ Correct — uses column names as strings (defaults to inner join)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **C**
# MAGIC
# MAGIC scala
# MAGIC storesDF.join(employeesDF,
# MAGIC   storesDF("storeId") === employeesDF("storeId") &&
# MAGIC   storesDF("employeeId") === employeesDF("employeeId"))
# MAGIC
# MAGIC
# MAGIC ✔ Correct — valid join condition using Column expressions
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **D**
# MAGIC
# MAGIC scala
# MAGIC storesDF.join(employeesDF, Seq("storeId", "employeeId"), "inner")
# MAGIC
# MAGIC
# MAGIC ✔ Correct — explicitly specifies inner join
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **E**
# MAGIC
# MAGIC scala
# MAGIC storesDF.alias("s").join(employeesDF.alias("e"),
# MAGIC   col("s.storeId") === col("e.storeId") &&
# MAGIC   col("s.employeeId") === col("e.employeeId"))
# MAGIC
# MAGIC
# MAGIC ✔ Correct — valid alias-based join condition
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ✅ Final Answer
# MAGIC
# MAGIC 👉 **A is the only code block that fails to produce the intended inner join.**

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
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **The correct response to fill in the numbered blanks is A.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **The completed code block is:**
# MAGIC
# MAGIC python
# MAGIC employeesDF.join(broadcast(storesDF), "storeId")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Why Option A is Correct
# MAGIC
# MAGIC - **Broadcasting the Smaller Table:**  
# MAGIC   In a broadcast join, the smaller DataFrame is sent (broadcast) to every node in the cluster to avoid a costly shuffle of the larger DataFrame. Since storesDF is described as being much smaller than employeesDF, it is the correct candidate for the broadcast() function.
# MAGIC
# MAGIC - **Syntax:**  
# MAGIC   The standard `pyspark.sql.functions.broadcast` syntax wraps the DataFrame to be broadcasted inside the join() method:  
# MAGIC   `largeDF.join(broadcast(smallDF), "key")`.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Why Other Options are Incorrect
# MAGIC
# MAGIC - **❌ B & C:**  
# MAGIC   These options suggest broadcasting the larger DataFrame (employeesDF) or use incorrect syntax (missing parentheses or calling broadcast on the wrong object). Broadcasting a large table can lead to Out of Memory (OOM) errors.
# MAGIC
# MAGIC - **❌ D & E:**  
# MAGIC   These options place storesDF (the small table) as the primary DataFrame and either broadcast the large one or use incorrect ordering. While technically a broadcast join can work from either side, the blank structure `__1__.join(__2__(__3__), "storeId")` specifically requires a DataFrame for blank 1 and the function broadcast for blank 2.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Final Selection
# MAGIC
# MAGIC | Blank | Value         | Reason                                         |
# MAGIC |-------|--------------|------------------------------------------------|
# MAGIC | 1     | employeesDF   | The large DataFrame that stays partitioned.    |
# MAGIC | 2     | broadcast     | The Spark SQL function used to mark a DataFrame for broadcast. |
# MAGIC | 3     | storesDF      | The small DataFrame to be broadcasted to all executors. |
# MAGIC
# MAGIC **Correct Answer Option: A**
# MAGIC
# MAGIC ---

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
# MAGIC
# MAGIC **The correct answer is: D. DataFrame.crossJoin()**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Explanation**
# MAGIC
# MAGIC A cross join (Cartesian join) returns the Cartesian product of two DataFrames — every row from the first combined with every row from the second.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct Option**
# MAGIC
# MAGIC **D. DataFrame.crossJoin()**
# MAGIC
# MAGIC `df1.crossJoin(df2)`
# MAGIC
# MAGIC - ✔ Explicitly performs a cross (Cartesian) join
# MAGIC - ✔ This is the intended and clear API for cross joins in Spark
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are incorrect**
# MAGIC
# MAGIC - **A. DataFrame.join()**  
# MAGIC   Default is inner join, not cross join  
# MAGIC   Can do cross join only with special config, not by default
# MAGIC
# MAGIC - **B. standalone join()**  
# MAGIC   ❌ Not a valid Spark DataFrame API
# MAGIC
# MAGIC - **C. standalone crossJoin()**  
# MAGIC   ❌ No such standalone function in Spark
# MAGIC
# MAGIC - **E. DataFrame.merge()**  
# MAGIC   ❌ Not a valid Spark DataFrame method
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Final Answer:**
# MAGIC
# MAGIC 👉 **D. DataFrame.crossJoin()**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Tip for exams/interviews:**  
# MAGIC If the question asks explicitly for cross join, always pick:  
# MAGIC - ✔ `crossJoin()` (clear and safe)  
# MAGIC Avoid relying on `join()` unless specified with conditions or configs

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
# MAGIC **The correct answer is: C. storesDF.write.csv(filePath)**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **PySpark Explanation**
# MAGIC
# MAGIC In PySpark, writing a DataFrame to CSV uses the DataFrameWriter API:
# MAGIC
# MAGIC - ✔ **Correct way:**  
# MAGIC   `storesDF.write.csv(filePath)`  
# MAGIC   - `write` is a property (no parentheses)  
# MAGIC   - `.csv(path)` writes the DataFrame in CSV format
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong (in PySpark terms)**
# MAGIC
# MAGIC **A. storesDF.write().csv(filePath)**
# MAGIC
# MAGIC python
# MAGIC # ❌ wrong
# MAGIC storesDF.write().csv(filePath)
# MAGIC
# MAGIC - `write` is not callable
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **B. storesDF.write(filePath)**
# MAGIC
# MAGIC python
# MAGIC # ❌ wrong
# MAGIC storesDF.write(filePath)
# MAGIC
# MAGIC - Missing format method
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **D. storesDF.write.option("csv").path(filePath)**
# MAGIC
# MAGIC python
# MAGIC # ❌ wrong
# MAGIC storesDF.write.option("csv").path(filePath)
# MAGIC
# MAGIC - `option()` needs key-value pairs, and `.path()` is invalid
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **E. storesDF.write.path(filePath)**
# MAGIC
# MAGIC python
# MAGIC # ❌ wrong
# MAGIC storesDF.write.path(filePath)
# MAGIC
# MAGIC - No such method
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Recommended (real-world usage)**
# MAGIC
# MAGIC python
# MAGIC storesDF.write \
# MAGIC     .option("header", True) \
# MAGIC     .mode("overwrite") \
# MAGIC     .csv(filePath)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Final Answer:**
# MAGIC
# MAGIC 👉 **C**

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
# MAGIC ✅ **Correct Answer:**  
# MAGIC **D. storesDF.write.partitionBy("division").parquet(filePath)**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **PySpark Explanation**
# MAGIC
# MAGIC To write a DataFrame in Parquet format and partition by a column, the correct pattern is:
# MAGIC
# MAGIC python
# MAGIC storesDF.write.partitionBy("division").parquet(filePath)
# MAGIC
# MAGIC
# MAGIC - `partitionBy("division")` → takes column name as string  
# MAGIC - `.parquet(path)` → writes in Parquet format  
# MAGIC - `write` → is a property (no parentheses)  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are wrong**
# MAGIC
# MAGIC **A**
# MAGIC
# MAGIC python
# MAGIC storesDF.write.partitionBy(col("division")).path(filePath)
# MAGIC
# MAGIC - ❌ `partitionBy()` expects string, not `col()`
# MAGIC - ❌ `.path()` is not valid
# MAGIC
# MAGIC **B**
# MAGIC
# MAGIC python
# MAGIC storesDF.write.option("parquet").partitionBy("division").path(filePath)
# MAGIC
# MAGIC - ❌ `option("parquet")` is invalid (needs key-value)
# MAGIC - ❌ `.path()` is not valid
# MAGIC
# MAGIC **C**
# MAGIC
# MAGIC python
# MAGIC storesDF.write.option("parquet").partitionBy(col("division")).path(filePath)
# MAGIC
# MAGIC - ❌ Same issues: wrong `option()` and `col()` usage
# MAGIC - ❌ `.path()` invalid
# MAGIC
# MAGIC **E**
# MAGIC
# MAGIC python
# MAGIC storesDF.write().partitionBy("division").parquet(filePath)
# MAGIC
# MAGIC - ❌ `write` is not callable
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Best Practice (real-world)**
# MAGIC
# MAGIC python
# MAGIC storesDF.write \
# MAGIC     .mode("overwrite") \
# MAGIC     .partitionBy("division") \
# MAGIC     .parquet(filePath)

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
# MAGIC
# MAGIC ✅ **Correct Answer:** B. Job
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **PySpark / Spark Concept Explanation**
# MAGIC
# MAGIC In Spark, the execution hierarchy (from largest → smallest) is:
# MAGIC
# MAGIC **Job → Stage → Task**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 📊 **Breakdown**
# MAGIC
# MAGIC - **Job** ✅ *(Coarsest level)*
# MAGIC   - Created when you run an action (e.g., `.show()`, `.collect()`, `.write()`)
# MAGIC   - Represents the entire computation
# MAGIC
# MAGIC - **Stage**
# MAGIC   - A Job is divided into stages based on shuffle boundaries
# MAGIC
# MAGIC - **Task**
# MAGIC   - Smallest unit of work
# MAGIC   - Runs on a single partition
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are incorrect**
# MAGIC
# MAGIC - **A. Slot**
# MAGIC   - ❌ Not part of core Spark execution hierarchy
# MAGIC
# MAGIC - **C. Task**
# MAGIC   - ❌ Finest (smallest), not coarsest
# MAGIC
# MAGIC - **D. Stage**
# MAGIC   - ❌ Intermediate level
# MAGIC
# MAGIC - **E. Executor**
# MAGIC   - ❌ Resource/process, not a hierarchy level
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Quick Memory Trick**
# MAGIC
# MAGIC 👉 J → S → T  
# MAGIC *(Job → Stage → Task)*

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
# MAGIC
# MAGIC ✅ **Correct Answer:**  
# MAGIC A. Slots are the most granular level of execution in the Spark execution hierarchy.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Explanation (PySpark / Spark Concepts)**
# MAGIC
# MAGIC Let’s clarify the roles:
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key Concepts**
# MAGIC
# MAGIC | Component  | Role                                 |
# MAGIC |------------|--------------------------------------|
# MAGIC | Task       | Smallest unit of execution ✅         |
# MAGIC | Slot       | CPU core; resource used to run a task|
# MAGIC | Executor   | JVM process that contains slots (cores)|
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why A is incorrect**
# MAGIC
# MAGIC > “Slots are the most granular level of execution…”
# MAGIC
# MAGIC - ❌ Wrong because **Tasks** are the smallest execution units
# MAGIC - Slots are just resources (CPU cores) used to execute tasks
# MAGIC - So, slots are not part of the execution hierarchy
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why other options are correct**
# MAGIC
# MAGIC - **B. Slots are resources for parallelization within an executor**  
# MAGIC   ✔ True — slots = CPU cores
# MAGIC
# MAGIC - **C. Tasks are assigned to slots for computation**  
# MAGIC   ✔ True — each task runs in one slot
# MAGIC
# MAGIC - **D. There can be more slots than tasks**  
# MAGIC   ✔ True — extra cores can remain idle
# MAGIC
# MAGIC - **E. There must be at least as many slots as there are executors**  
# MAGIC   ✔ True — each executor has at least one core (slot)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Quick Summary**
# MAGIC
# MAGIC | Component | Role                    |
# MAGIC |-----------|------------------------|
# MAGIC | Job       | Highest level          |
# MAGIC | Stage     | Split by shuffle       |
# MAGIC | Task      | Smallest execution unit ✅ |
# MAGIC | Slot      | CPU core (resource)    |

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
# MAGIC
# MAGIC ✅ **Correct Answer:** E. `storesDF.dropDuplicates()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **PySpark Explanation**
# MAGIC
# MAGIC To remove duplicate rows from a DataFrame in PySpark, you use:
# MAGIC
# MAGIC python
# MAGIC storesDF.dropDuplicates()
# MAGIC
# MAGIC
# MAGIC - ✔ Returns a new DataFrame  
# MAGIC - ✔ Removes duplicate rows  
# MAGIC - ✔ Keeps only unique records
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are wrong**
# MAGIC
# MAGIC - **A. storesDF.removeDuplicates()**  
# MAGIC    ❌ No such method in PySpark
# MAGIC
# MAGIC - **B. storesDF.getDistinct()**  
# MAGIC    ❌ Invalid method
# MAGIC
# MAGIC - **C. storesDF.duplicates.drop()**  
# MAGIC    ❌ Invalid syntax / no such attribute
# MAGIC
# MAGIC - **D. storesDF.duplicates()**  
# MAGIC    ❌ Not a valid PySpark method
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Alternative (also valid in PySpark)**
# MAGIC
# MAGIC python
# MAGIC storesDF.distinct()
# MAGIC
# MAGIC - Also removes duplicates  
# MAGIC - Slightly different use case (no subset option)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Final Answer:**
# MAGIC
# MAGIC 👉 **E. storesDF.dropDuplicates()**

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
# MAGIC
# MAGIC ✅ **Correct Answer:**  
# MAGIC E. The approx_count_distinct() operation cannot determine an exact number of distinct values in a column.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **PySpark Explanation**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Your code:**
# MAGIC
# MAGIC python
# MAGIC storesDF.agg(approx_count_distinct(col("division")).alias("divisionDistinct"))
# MAGIC
# MAGIC
# MAGIC - `approx_count_distinct()` is designed for approximate distinct counts  
# MAGIC - It uses probabilistic algorithms (like HyperLogLog)  
# MAGIC - ✔ Faster and memory efficient  
# MAGIC - ❌ Not exact  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❗ **What’s the error?**
# MAGIC
# MAGIC The question clearly says:
# MAGIC
# MAGIC > “return the exact number of distinct values”
# MAGIC
# MAGIC But:
# MAGIC
# MAGIC - `approx_count_distinct(...)`  
# MAGIC   👉 only gives an estimate, not the exact value
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct way for exact count**
# MAGIC
# MAGIC python
# MAGIC from pyspark.sql.functions import countDistinct
# MAGIC
# MAGIC storesDF.agg(countDistinct("division").alias("divisionDistinct"))
# MAGIC
# MAGIC
# MAGIC - ✔ Returns exact distinct count
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are wrong**
# MAGIC
# MAGIC - **A**  
# MAGIC   Adding rsd only controls accuracy, still not exact
# MAGIC
# MAGIC - **B**  
# MAGIC   `.alias()` is valid ✔
# MAGIC
# MAGIC - **C**  
# MAGIC   Spark can compute exact distinct counts ✔
# MAGIC
# MAGIC - **D**  
# MAGIC   `approx_count_distinct()` is a valid standalone function ✔
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key Takeaway**
# MAGIC
# MAGIC | Function                | Result                |
# MAGIC |-------------------------|-----------------------|
# MAGIC | approx_count_distinct() | Fast, approximate ❌  |
# MAGIC | countDistinct()         | Exact ✔              |

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
# MAGIC ✅ **Correct Answer:** C
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### PySpark
# MAGIC python
# MAGIC storesDF.groupBy("division", "storeCategory").count()
# MAGIC
# MAGIC
# MAGIC ### Scala
# MAGIC scala
# MAGIC storesDF.groupBy("division", "storeCategory").count()
# MAGIC
# MAGIC
# MAGIC - ✔ Works in both Python and Scala
# MAGIC - ✔ Groups by both columns together
# MAGIC - ✔ Returns count per unique combination
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔍 Why not others (considering both languages)
# MAGIC
# MAGIC **A**
# MAGIC scala
# MAGIC storesDF.groupBy(Seq(col("division"), col("storeCategory"))).count()
# MAGIC
# MAGIC - ❌ In Scala: `groupBy()` does not take `Seq[Column]`
# MAGIC - It expects: `groupBy("col1", "col2")` OR `groupBy(col("col1"), col("col2"))`
# MAGIC
# MAGIC **B**
# MAGIC scala
# MAGIC storesDF.groupBy(division, storeCategory).count()
# MAGIC
# MAGIC - ❌ Invalid in Python (variables undefined)
# MAGIC - ✔ Could work in Scala only if variables exist, but not standard usage
# MAGIC - 👉 Not a safe/correct answer
# MAGIC
# MAGIC **D**
# MAGIC scala
# MAGIC storesDF.groupBy("division").groupBy("storeCategory").count()
# MAGIC
# MAGIC - ❌ Wrong in both: Second `groupBy` overrides the first
# MAGIC
# MAGIC **E**
# MAGIC scala
# MAGIC storesDF.groupBy(Seq("division", "storeCategory")).count()
# MAGIC
# MAGIC - ❌ In Scala: `Seq("col1", "col2")` is not accepted directly in `groupBy`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Key Takeaway (Works in BOTH)
# MAGIC
# MAGIC | Syntax                        | Works in PySpark | Works in Scala |
# MAGIC |-------------------------------|:---------------:|:-------------:|
# MAGIC | groupBy("col1", "col2")       |       ✔         |      ✔        |
# MAGIC | groupBy(col("col1"), col("col2")) |    ✔         |      ✔        |
# MAGIC | groupBy(Seq(...))             |       ❌        |      ❌       |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Final Answer:**  
# MAGIC 👉 C

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
# MAGIC
# MAGIC ✅ **Correct Answer:**  
# MAGIC E. The describe() operation does not accept a Column object as an argument — the column name string "sqft" should be specified instead.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **What’s wrong in the code?**
# MAGIC
# MAGIC **Given code:**
# MAGIC
# MAGIC storesDF.describes(col("sgft"))
# MAGIC
# MAGIC
# MAGIC There are actually two issues, but the exam-focused error is:
# MAGIC
# MAGIC - ❌ describe() expects column names as strings, NOT col() objects
# MAGIC - ❌ Typo: "sgft" instead of "sqft"
# MAGIC - ❌ Method name typo: describes → should be describe
# MAGIC
# MAGIC 👉 Among the options, only E correctly identifies the API misuse
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct Code (PySpark)**
# MAGIC
# MAGIC storesDF.describe("sqft")
# MAGIC
# MAGIC - ✔ Uses column name as string
# MAGIC - ✔ Returns summary stats: count, mean, stddev, min, max
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct Code (Scala)**
# MAGIC
# MAGIC storesDF.describe("sqft")
# MAGIC
# MAGIC - ✔ Same syntax as PySpark
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 📊 **Example Output**
# MAGIC | summary | sqft  |
# MAGIC |---------|-------|
# MAGIC | count   | 100   |
# MAGIC | mean    | 2500  |
# MAGIC | stddev  | 300   |
# MAGIC | min     | 1000  |
# MAGIC | max     | 5000  |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are wrong**
# MAGIC - **A** ❌ No need to subset column first
# MAGIC - **B** ❌ Seq(col(...)) still invalid
# MAGIC - **C** ❌ describe() works for single column ✔
# MAGIC - **D** ❌ describe() works for numeric columns ✔
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key Takeaway**
# MAGIC
# MAGIC | Wrong ❌                | Correct ✔           |
# MAGIC |------------------------|---------------------|
# MAGIC | describe(col("sqft"))  | describe("sqft")    |

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

from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("TestExample") \
    .getOrCreate()

# Sample data
data = [
    (1, "A", 1200),
    (2, "B", 1500),
    (3, "A", 1800)
]

columns = ["storeId", "division", "sqft"]

# Create DataFrame
storesDF = spark.createDataFrame(data, columns)

# Show DataFrame
storesDF.show()

# ✅ Get sqft from first row
first_sqft = storesDF.first

print("First row sqft value:", first_sqft)

# COMMAND ----------

# MAGIC %md
# MAGIC **Answer : D** 
# MAGIC <br>need more investigation
# MAGIC <br>answer as per chatgpt - A
# MAGIC <br>PDF & exam topic - D

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
# MAGIC
# MAGIC ✅ **Correct Answer:** E. `storesDF.printSchema`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Explanation (PySpark + Scala)**
# MAGIC
# MAGIC To print the schema of a DataFrame:
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC
# MAGIC storesDF.printSchema()
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC
# MAGIC storesDF.printSchema()
# MAGIC
# MAGIC
# MAGIC - ✔ `printSchema()` is the correct method
# MAGIC - ✔ No arguments required
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are wrong**
# MAGIC
# MAGIC **A**
# MAGIC
# MAGIC
# MAGIC storesDF.printSchema("all")
# MAGIC
# MAGIC - ❌ `printSchema()` does not take arguments
# MAGIC
# MAGIC **B**
# MAGIC
# MAGIC
# MAGIC storesDF.schema
# MAGIC
# MAGIC - ⚠️ Returns schema object but does NOT print it nicely
# MAGIC
# MAGIC **C**
# MAGIC
# MAGIC
# MAGIC storesDF.getAs[str]
# MAGIC
# MAGIC - ❌ Invalid method for DataFrame
# MAGIC
# MAGIC **D**
# MAGIC
# MAGIC
# MAGIC storesDF.printSchema(true)
# MAGIC
# MAGIC - ❌ No boolean argument allowed
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key Difference**
# MAGIC
# MAGIC | Method         | Result         |
# MAGIC |----------------|---------------|
# MAGIC | printSchema()  | ✔ Prints nicely|
# MAGIC | schema         | ⚠️ Returns object|

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
# MAGIC
# MAGIC ✅ **Correct Answer:** D. The wrong SQL function is used — it should be ASSESS_PERFORMANCE instead of assessPerformance.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **What’s happening in the code?**
# MAGIC
# MAGIC scala
# MAGIC spark.udf.register("ASSESS_PERFORMANCE", assessPerforance) 
# MAGIC
# MAGIC spark.sql("""
# MAGIC SELECT customerSatisfaction,
# MAGIC        assessPerformance(customerSatisfaction) AS result
# MAGIC FROM stores
# MAGIC """)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❗ **Error Explanation**
# MAGIC
# MAGIC You registered the UDF with the name:
# MAGIC
# MAGIC > "ASSESS_PERFORMANCE"
# MAGIC
# MAGIC But in SQL, you are calling:
# MAGIC
# MAGIC > assessPerformance(customerSatisfaction)
# MAGIC
# MAGIC ❌ These do not match
# MAGIC
# MAGIC 👉 In Spark SQL, you must use the exact registered name of the UDF.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct Code**
# MAGIC
# MAGIC scala
# MAGIC spark.udf.register("ASSESS_PERFORMANCE", assessPerformance)
# MAGIC
# MAGIC spark.sql("""
# MAGIC SELECT customerSatisfaction,
# MAGIC        ASSESS_PERFORMANCE(customerSatisfaction) AS result
# MAGIC FROM stores
# MAGIC """)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🐍 **Equivalent in PySpark**
# MAGIC
# MAGIC python
# MAGIC spark.udf.register("ASSESS_PERFORMANCE", assessPerformance)
# MAGIC
# MAGIC spark.sql("""
# MAGIC SELECT customerSatisfaction,
# MAGIC        ASSESS_PERFORMANCE(customerSatisfaction) AS result
# MAGIC FROM stores
# MAGIC """)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are wrong**
# MAGIC
# MAGIC - **A** ❌ You can use the same column multiple times
# MAGIC - **B** ❌ UDFs can be used in SQL ✔
# MAGIC - **C** ❌ Argument order is correct (name, function)
# MAGIC - **E** ❌ spark.sql() is valid ✔
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚠️ **Bonus: Hidden typo (not in options)**
# MAGIC
# MAGIC - assessPerforance   // ❌ typo
# MAGIC - assessPerformance  // ✔ correct
# MAGIC
# MAGIC But since it's not an option, ignore it for the answer.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Final Answer:**
# MAGIC
# MAGIC 👉 D

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
# MAGIC **The correct answer is B. The return type of assessPerformanceUDF() must be specified.**
# MAGIC
# MAGIC In Scala, when creating a User-Defined Function (UDF) using the `udf()` method, the return type must be explicitly defined if it cannot be inferred from the function signature provided. While Scala can sometimes infer types for anonymous functions, Spark's `udf()` operation generally requires the return type to be specified (e.g., `IntegerType` or `StringType`) to correctly map the output to a DataFrame column.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Explanation of Answer Options
# MAGIC
# MAGIC ✅ **Option B (Correct):**  
# MAGIC To properly register a function as a UDF in Spark, the return type is a mandatory parameter in the `udf()` registration to ensure Spark's Catalyst optimizer knows how to handle the resulting data.
# MAGIC
# MAGIC ❌ **Option A:**  
# MAGIC The input type of the column is usually handled by the column's existing schema within the DataFrame; it does not need to be specified again within the `udf()` call itself.
# MAGIC
# MAGIC ❌ **Option C:**  
# MAGIC Using `withColumn()` is the standard and recommended way to apply a UDF to a column in the DataFrame API. Iterating over rows manually is inefficient and against Spark's distributed processing model.
# MAGIC
# MAGIC ❌ **Option D:**  
# MAGIC While you can define a Scala function first, you can also define it inline within the `udf()` call using an anonymous function.
# MAGIC
# MAGIC ❌ **Option E:**  
# MAGIC UDFs are fully supported in the DataFrame API and are not limited to SQL.

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
# MAGIC
# MAGIC To create a single-column DataFrame from a Scala list of integers, the clean and idiomatic Spark approach is:
# MAGIC
# MAGIC
# MAGIC spark.createDataset(years).toDF()
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Now check the options:**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **A.**
# MAGIC
# MAGIC
# MAGIC spark.createDataFrame(years).IntegerType
# MAGIC
# MAGIC - ❌ createDataFrame does not take a plain Scala list directly like this.
# MAGIC - ❌ .IntegerType is not a method you can call here.
# MAGIC - ❌ Missing schema handling if using createDataFrame.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **B.**
# MAGIC
# MAGIC
# MAGIC spark.createDataset(years).IntegerType
# MAGIC
# MAGIC - ❌ createDataset(years) is valid.
# MAGIC - ❌ But .IntegerType is meaningless here—no such method in this context.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **C.**
# MAGIC
# MAGIC
# MAGIC spark.createDataset(List(years)).toDF
# MAGIC
# MAGIC - ❌ List(years) creates a list containing the entire list (nested list), not what you want.
# MAGIC - ❌ Also missing parentheses on toDF().
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **D.**
# MAGIC
# MAGIC
# MAGIC spark.createDataFrame(List(years)).IntegerType
# MAGIC
# MAGIC - ❌ Same issue as A: createDataFrame doesn’t work like this for raw lists.
# MAGIC - ❌ .IntegerType is invalid here.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **So what’s the issue?**
# MAGIC
# MAGIC None of the options exactly match the correct and idiomatic solution:
# MAGIC
# MAGIC
# MAGIC spark.createDataset(years).toDF()
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Best intended answer:**
# MAGIC
# MAGIC C is the closest, because it uses:
# MAGIC - createDataset ✔
# MAGIC - toDF ✔
# MAGIC
# MAGIC …but it’s still technically incorrect due to:
# MAGIC - List(years) ❌ (should just be years)
# MAGIC - missing () in toDF() ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Final takeaway:**
# MAGIC
# MAGIC - Correct concept: use `createDataset(years).toDF()`
# MAGIC - Among given choices: C is the intended answer, even though it’s slightly flawed.

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
# MAGIC
# MAGIC ✅ **Correct Answer:** E
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Correct Code**
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC storesDF.persist(StorageLevel.MEMORY_ONLY).count()
# MAGIC
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC from pyspark import StorageLevel
# MAGIC storesDF.persist(StorageLevel.MEMORY_ONLY).count()
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Explanation**
# MAGIC
# MAGIC - `persist(StorageLevel.MEMORY_ONLY)` → explicitly caches DataFrame only in memory
# MAGIC - `.count()` → action to trigger caching
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❗ **Important Concept**
# MAGIC
# MAGIC - `cache()` is just a shortcut for:
# MAGIC   python
# MAGIC   persist(StorageLevel.MEMORY_ONLY)
# MAGIC   
# MAGIC - BUT in this question:
# MAGIC   - The code requires a parameter (__3__)
# MAGIC   - So `persist()` must be used
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are wrong**
# MAGIC
# MAGIC **A**
# MAGIC python
# MAGIC storesDF.cache(StorageLevel.MEMORY_ONLY)
# MAGIC
# MAGIC - ❌ `cache()` does NOT take arguments
# MAGIC
# MAGIC **B**
# MAGIC python
# MAGIC storesDF.storageLevel(cache)
# MAGIC
# MAGIC - ❌ Invalid API
# MAGIC
# MAGIC **C**
# MAGIC python
# MAGIC storesDF.cache(Nothing)
# MAGIC
# MAGIC - ❌ Invalid syntax
# MAGIC
# MAGIC **D**
# MAGIC python
# MAGIC storesDF.persist(Nothing)
# MAGIC
# MAGIC - ❌ Missing storage level
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Final Answer:**
# MAGIC
# MAGIC 👉 E

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
# MAGIC
# MAGIC ✅ **Correct Answer:** D
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Correct Code (PySpark)**
# MAGIC
# MAGIC python
# MAGIC from pyspark.sql.functions import col, month
# MAGIC
# MAGIC storesDF.withColumn("openTimestamp", col("openDate").cast("timestamp")) \
# MAGIC         .withColumn("month", month(col("openTimestamp")))
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Explanation**
# MAGIC
# MAGIC **Step-by-step:**
# MAGIC
# MAGIC - **Convert UNIX epoch (integer) → timestamp**
# MAGIC   - `col("openDate").cast("timestamp")`
# MAGIC   - ✔ Required before extracting date parts
# MAGIC
# MAGIC - **Extract month**
# MAGIC   - `month(col("openTimestamp"))`
# MAGIC   - ✔ `month()` is a built-in Spark function
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔎 **Fill in the blanks**
# MAGIC
# MAGIC | Blank   | Value                |
# MAGIC |---------|----------------------|
# MAGIC | __1__   | "Timestamp"          |
# MAGIC | __2__   | "month"              |
# MAGIC | __3__   | month                |
# MAGIC | __4__   | col("openTimestamp") |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are wrong**
# MAGIC
# MAGIC **A**
# MAGIC - ❌ "Data" is invalid type
# MAGIC - ❌ "month" as string instead of function
# MAGIC
# MAGIC **B**
# MAGIC - ❌ "month" used as string, not function
# MAGIC
# MAGIC **C**
# MAGIC - ❌ getMonth is not a Spark function
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key Takeaway**
# MAGIC
# MAGIC | Task                    | Function           |
# MAGIC |-------------------------|--------------------|
# MAGIC | Convert epoch → timestamp| cast("timestamp")  |
# MAGIC | Extract month           | month()            |

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
# MAGIC
# MAGIC ✅ **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **What’s the issue in the code?**
# MAGIC
# MAGIC `StoresDF.join(employeesDF, Seq("storeId")`
# MAGIC
# MAGIC ❌ The code has a syntax error — missing closing parenthesis `)`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **The intended correct usage is:**
# MAGIC
# MAGIC `storesDF.join(employeesDF, Seq("storeId"))`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why option A is the best match**
# MAGIC
# MAGIC A. The key column storeId needs to be a string like "storeId". ✔
# MAGIC
# MAGIC Spark expects column names as strings when using `Seq(...)`
# MAGIC
# MAGIC This is the correct form:
# MAGIC
# MAGIC `Seq("storeId")`
# MAGIC
# MAGIC Even though the code already shows "storeId", A is the closest valid explanation among given choices (exam-style question).
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong**
# MAGIC
# MAGIC - **B** ❌ Not required — `Seq("storeId")` is already valid for join
# MAGIC - **C** ❌ Default join is already inner
# MAGIC - **D** ❌ `join()` is valid (no need for `merge()`)
# MAGIC - **E** ❌ `col()` not needed when using `Seq("column")`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🐍 **Equivalent in PySpark**
# MAGIC
# MAGIC `storesDF.join(employeesDF, ["storeId"])`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key Takeaway**
# MAGIC
# MAGIC | Syntax         | Use case                |
# MAGIC |----------------|------------------------|
# MAGIC | Seq("col")     | Join using column name  |
# MAGIC | col("col")     | Used in expressions     |

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
# MAGIC
# MAGIC ✅ **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Explanation (Scala + PySpark concepts)**
# MAGIC
# MAGIC In Spark, DataFrame.join() supports two ways to specify join columns:
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **1. Using column names (USING-style join)**  
# MAGIC `df1.join(df2, Seq("column1", "column2"))`  
# MAGIC ✔ Valid → matches Option E
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **2. Using join expressions**  
# MAGIC scala
# MAGIC df1.join(df2,
# MAGIC   col("a.column1") === col("b.column1") &&
# MAGIC   col("a.column2") === col("b.column2")
# MAGIC )
# MAGIC
# MAGIC ✔ Valid → matches Option A
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Also:**  
# MAGIC `storesDF("column1") === employeesDF("column1")`  
# MAGIC ✔ Valid → matches Option D
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why B is incorrect**  
# MAGIC `usingColumns = Seq(col("column1"), col("column2"))`  
# MAGIC ❌ Seq() for usingColumns must contain strings, not Column objects
# MAGIC
# MAGIC ✔ **Correct form:**  
# MAGIC `Seq("column1", "column2")`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🐍 **Equivalent in PySpark**  
# MAGIC python
# MAGIC # ✔ using column names
# MAGIC df1.join(df2, ["column1", "column2"])
# MAGIC
# MAGIC # ✔ using expressions
# MAGIC df1.join(df2,
# MAGIC     (df1.column1 == df2.column1) &
# MAGIC     (df1.column2 == df2.column2)
# MAGIC )
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key Takeaway**
# MAGIC
# MAGIC | Method      | Accepts         |
# MAGIC |-------------|-----------------|
# MAGIC | Seq(...)    | ✔ Strings only  |
# MAGIC | Expressions | ✔ Column objects|
# MAGIC | Invalid     | Seq(col("column1"), col("column2")) // ❌ |

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
# MAGIC **The correct option is E.**  
# MAGIC `storesDF.union(acquiredStoresDF)`
# MAGIC
# MAGIC In Apache Spark, a position-wise union (also known as a positional union) matches columns based on their index or order in the schema, regardless of their names. The `pyspark.sql.DataFrame.union` method is the standard way to perform this operation.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Explanation of Options
# MAGIC
# MAGIC - ✅ **E.** `storesDF.union(acquiredStoresDF)`: This is the correct method for a position-wise union. It appends rows from the second DataFrame to the first based on column order.
# MAGIC - ❌ **B.** `storesDF.unionByName(acquiredStoresDF)`: This performs a name-wise union, matching columns by their labels rather than their positions.
# MAGIC - ❌ **D.** `unionAll(storesDF, acquiredStoresDF)`: While `unionAll` is a valid method in Spark, it is an alias for `union` and must be called as a method on a DataFrame (e.g., `storesDF.unionAll(...)`), not as a standalone function.
# MAGIC - ❌ **A & C:** `concat()` and `union()` used as standalone functions are not standard PySpark DataFrame methods for this task.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Key Differences
# MAGIC
# MAGIC | Feature         | union()                  | unionByName()           |
# MAGIC |-----------------|-------------------------|-------------------------|
# MAGIC | Matching Logic  | By Position (Index)      | By Column Name          |
# MAGIC | Requirement     | Same number of columns   | Column names must match |
# MAGIC | Deduplication   | Keeps duplicates         | Keeps duplicates        |
# MAGIC | API Source      | Spark DataFrame.union    | Spark DataFrame.unionByName |

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
# MAGIC ✅ **Correct Answer:** C. `storesDF.write.mode("overwrite").parquet(filePath)`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **PySpark Explanation**
# MAGIC
# MAGIC To write a DataFrame as Parquet and overwrite existing data, use:
# MAGIC
# MAGIC python
# MAGIC storesDF.write.mode("overwrite").parquet(filePath)
# MAGIC
# MAGIC
# MAGIC - ✔ `mode("overwrite")` → replaces existing data
# MAGIC - ✔ `.parquet(filePath)` → writes in Parquet format
# MAGIC - ✔ `write` is a property (no parentheses)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are wrong**
# MAGIC
# MAGIC **A**
# MAGIC
# MAGIC python
# MAGIC storesDF.write(filePath, mode="overwrite")
# MAGIC
# MAGIC - ❌ Invalid API (write is not a function like this)
# MAGIC
# MAGIC **B**
# MAGIC
# MAGIC python
# MAGIC storesDF.write().mode("overwrite").parquet(filePath)
# MAGIC
# MAGIC - ❌ `write()` is incorrect (should not use parentheses)
# MAGIC
# MAGIC **D**
# MAGIC
# MAGIC python
# MAGIC storesDF.write.option("parquet", "overwrite").path(filePath)
# MAGIC
# MAGIC - ❌ Wrong use of `option()`
# MAGIC - ❌ `.path()` is not valid here
# MAGIC
# MAGIC **E**
# MAGIC
# MAGIC python
# MAGIC storesDF.write.mode("overwrite").path(filePath)
# MAGIC
# MAGIC - ❌ Missing format (parquet, csv, etc.)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Best Practice**
# MAGIC
# MAGIC python
# MAGIC storesDF.write \
# MAGIC     .mode("overwrite") \
# MAGIC     .format("parquet") \
# MAGIC     .save(filePath)

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
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct Answer:** C. `spark.read.schema(schema).csv(filePath)`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **PySpark Explanation**
# MAGIC
# MAGIC To read a CSV file with a predefined schema, use:
# MAGIC
# MAGIC python
# MAGIC spark.read.schema(schema).csv(filePath)
# MAGIC
# MAGIC
# MAGIC - ✔ `schema(schema)` → pass a StructType object, not a string
# MAGIC - ✔ `.csv(filePath)` → reads CSV into DataFrame
# MAGIC - ✔ `read` is a property (no parentheses)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are wrong**
# MAGIC
# MAGIC **A**
# MAGIC
# MAGIC python
# MAGIC spark.read().csv(filePath)
# MAGIC
# MAGIC - ❌ No schema specified
# MAGIC - ❌ `read()` is incorrect (no parentheses)
# MAGIC
# MAGIC **B**
# MAGIC
# MAGIC python
# MAGIC spark.read().schema("schema").csv(filePath)
# MAGIC
# MAGIC - ❌ "schema" is a string, not a schema object
# MAGIC - ❌ `read()` incorrect
# MAGIC
# MAGIC **D**
# MAGIC
# MAGIC python
# MAGIC spark.read.schema("schema").csv(filePath)
# MAGIC
# MAGIC - ❌ Schema passed as string (invalid)
# MAGIC
# MAGIC **E**
# MAGIC
# MAGIC python
# MAGIC spark.read().schema(schema).csv(filePath)
# MAGIC
# MAGIC - ❌ `read()` should not have parentheses
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Example Schema (PySpark)**
# MAGIC
# MAGIC python
# MAGIC from pyspark.sql.types import StructType, StructField, IntegerType, StringType
# MAGIC
# MAGIC schema = StructType([
# MAGIC     StructField("id", IntegerType(), True),
# MAGIC     StructField("name", StringType(), True)
# MAGIC ])

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
# MAGIC
# MAGIC ✅ **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **PySpark Explanation**
# MAGIC
# MAGIC In PySpark, when combining multiple conditions inside `filter()`:
# MAGIC
# MAGIC - Use `&` for AND
# MAGIC - Use parentheses around each condition
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct Code**
# MAGIC
# MAGIC python
# MAGIC from pyspark.sql.functions import col
# MAGIC
# MAGIC storesDF.filter(
# MAGIC     (col("sqft") <= 25000) & (col("customerSatisfaction") >= 30)
# MAGIC )
# MAGIC
# MAGIC
# MAGIC - ✔ `&` → logical AND
# MAGIC - ✔ `col()` → column reference
# MAGIC - ✔ Parentheses required for each condition
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are wrong**
# MAGIC
# MAGIC **A**
# MAGIC
# MAGIC python
# MAGIC col("sqft") <= 25000 and col("customerSatisfaction") >= 30
# MAGIC
# MAGIC - ❌ `and` does NOT work with Column objects
# MAGIC
# MAGIC **B**
# MAGIC
# MAGIC python
# MAGIC ... or ...
# MAGIC
# MAGIC - ❌ Uses OR instead of AND
# MAGIC
# MAGIC **C**
# MAGIC
# MAGIC python
# MAGIC storesDF.filter(sqft) <= 25000 ...
# MAGIC
# MAGIC - ❌ Invalid syntax
# MAGIC
# MAGIC **E**
# MAGIC
# MAGIC python
# MAGIC storesDF.filter(sqft <= 25000) & customerSatisfaction >= 30
# MAGIC
# MAGIC - ❌ Condition split incorrectly
# MAGIC - ❌ Missing `col()` and parentheses
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key Takeaway**
# MAGIC
# MAGIC | Operator | Use in PySpark |
# MAGIC |----------|---------------|
# MAGIC | AND      | `&`           |
# MAGIC | OR       | `|`           |
# MAGIC | NOT      | `~`           |

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
# MAGIC
# MAGIC ✅ **Correct Answer:** C. `filter(), where()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Explanation (Works in BOTH PySpark & Scala)**
# MAGIC
# MAGIC Both `filter()` and `where()` are used to return rows based on a condition.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Example**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC
# MAGIC storesDF.filter(col("sqft") > 1000)
# MAGIC storesDF.where(col("sqft") > 1000)
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC
# MAGIC storesDF.filter(col("sqft") > 1000)
# MAGIC storesDF.where(col("sqft") > 1000)
# MAGIC
# MAGIC
# MAGIC ✔ Both return a new DataFrame  
# MAGIC ✔ Both apply row-level filtering  
# MAGIC ✔ `where()` is just an alias of `filter()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are wrong**
# MAGIC
# MAGIC - **A.** `drop(), where()`  
# MAGIC   ❌ `drop()` removes columns, not rows
# MAGIC
# MAGIC - **B.** `filter(), select()`  
# MAGIC   ❌ `select()` selects columns, not rows
# MAGIC
# MAGIC - **D.** `select(), where()`  
# MAGIC   ❌ `select()` is column operation
# MAGIC
# MAGIC - **E.** `filter(), drop()`  
# MAGIC   ❌ `drop()` is not for row filtering
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key Takeaway**
# MAGIC
# MAGIC | Method   | Purpose              |
# MAGIC |----------|----------------------|
# MAGIC | filter() | Row filtering ✔      |
# MAGIC | where()  | Row filtering ✔      |
# MAGIC | select() | Column selection ❌  |
# MAGIC | drop()   | Remove columns ❌    |

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
# MAGIC
# MAGIC ✅ **Correct Answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Correct Code (Works in BOTH PySpark & Scala)**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC storesDF.drop("sqft", "customerSatisfaction")
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC storesDF.drop("sqft", "customerSatisfaction")
# MAGIC
# MAGIC
# MAGIC - ✔ Removes specified columns
# MAGIC - ✔ Returns a new DataFrame
# MAGIC - ✔ Accepts column names as strings
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔎 **Fill in the blanks**
# MAGIC
# MAGIC | Blank  | Value                      |
# MAGIC |--------|----------------------------|
# MAGIC | __1__  | storesDF                   |
# MAGIC | __2__  | drop                      |
# MAGIC | __3__  | "sqft", "customerSatisfaction" |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are wrong**
# MAGIC
# MAGIC **A**
# MAGIC
# MAGIC python
# MAGIC drop(storesDF, col("sqft"), ...)
# MAGIC
# MAGIC - ❌ Wrong order + invalid syntax
# MAGIC
# MAGIC **B**
# MAGIC
# MAGIC python
# MAGIC storesDF.drop(sqft, customerSatisfaction)
# MAGIC
# MAGIC - ❌ Missing quotes → treated as variables
# MAGIC
# MAGIC **D**
# MAGIC
# MAGIC python
# MAGIC col(sqft)
# MAGIC
# MAGIC - ❌ Missing quotes inside col()
# MAGIC
# MAGIC **E**
# MAGIC
# MAGIC python
# MAGIC drop(storesDF, ...)
# MAGIC
# MAGIC - ❌ drop is not a standalone function
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key Takeaway**
# MAGIC
# MAGIC | Correct           | Incorrect         |
# MAGIC |-------------------|------------------|
# MAGIC | "columnName"      | columnName        |
# MAGIC | drop("col1", "col2") | drop(col(col1)) |

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
# MAGIC
# MAGIC ✅ **Correct Answer:** A
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Explanation (PySpark + Scala)**
# MAGIC
# MAGIC **🔹 `repartition(n)`**
# MAGIC - ✔ Creates exactly n partitions
# MAGIC - ✔ Performs a full shuffle
# MAGIC - ✔ Distributes data evenly across partitions
# MAGIC - ❌ More expensive (due to shuffle)
# MAGIC
# MAGIC python
# MAGIC storesDF.repartition(4)
# MAGIC
# MAGIC
# MAGIC **🔹 `coalesce(n)`**
# MAGIC - ✔ Reduces number of partitions (best for shrinking)
# MAGIC - ✔ Avoids full shuffle (more efficient)
# MAGIC - ❌ May lead to uneven data distribution
# MAGIC
# MAGIC python
# MAGIC storesDF.coalesce(4)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key Differences**
# MAGIC
# MAGIC | Feature      | repartition()      | coalesce()         |
# MAGIC |--------------|--------------------|--------------------|
# MAGIC | Shuffle      | ✔ Full shuffle     | ❌ Minimal/no shuffle |
# MAGIC | Performance  | ❌ Slower          | ✔ Faster           |
# MAGIC | Distribution | ✔ Even             | ❌ Uneven possible |
# MAGIC | Use case     | Increase/decrease partitions | Mainly decrease partitions |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are wrong**
# MAGIC
# MAGIC - **B / D**  
# MAGIC   ❌ Efficiency reasoning is incorrect
# MAGIC
# MAGIC - **C**  
# MAGIC   ❌ Reversed behavior (wrong)
# MAGIC
# MAGIC - **E**  
# MAGIC   ❌ Completely incorrect descriptions
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 Use:
# MAGIC - `repartition()` → when you need balanced partitions
# MAGIC - `coalesce()` → when you want faster reduction

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
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct Answer:** D. Scenario #1
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Key Concept: Garbage Collection (GC) in Spark**
# MAGIC
# MAGIC GC issues happen when:
# MAGIC - Executors have very large memory
# MAGIC - Fewer executors → large heap size per executor
# MAGIC - Large DataFrames sit in memory → long GC pauses
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 📊 **Scenario Analysis**
# MAGIC
# MAGIC | Scenario | Executors | Memory per Executor | GC Risk     |
# MAGIC |----------|-----------|---------------------|-------------|
# MAGIC | #1       | 1         | 100 GB              | 🔴 Very High |
# MAGIC | #4       | 2         | 50 GB               | 🟠 Medium    |
# MAGIC | #5       | 4         | 25 GB               | 🟡 Lower     |
# MAGIC | #6       | 8         | 12.5 GB             | 🟢 Lowest    |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Scenario #1 is Worst**
# MAGIC
# MAGIC - Only 1 executor
# MAGIC - Entire 100GB heap in one JVM
# MAGIC
# MAGIC Leads to:
# MAGIC - ❌ Long GC pauses
# MAGIC - ❌ Memory pressure
# MAGIC - ❌ Slow processing
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 **Spark best practice:**
# MAGIC
# MAGIC Use more smaller executors instead of one huge executor
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔁 **Better Approach**
# MAGIC
# MAGIC Instead of:
# MAGIC
# MAGIC - 1 executor × 100GB
# MAGIC
# MAGIC Prefer:
# MAGIC
# MAGIC - 4 executors × 25GB  
# MAGIC - OR  
# MAGIC - 8 executors × 12.5GB
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC - ❗ Bigger executor = higher GC risk
# MAGIC - ❗ More executors = better parallelism + less GC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Final Answer:**
# MAGIC
# MAGIC 👉 D. Scenario #1
# MAGIC
# MAGIC ---

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
# MAGIC
# MAGIC ✅ **Correct Answer:** A. `DataFrame.select()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Transformation vs Action (Spark Core Concept)**
# MAGIC
# MAGIC **🔹 Transformations**
# MAGIC - Return a new DataFrame
# MAGIC - Are lazy (not executed immediately)
# MAGIC
# MAGIC **🔹 Actions**
# MAGIC - Trigger execution
# MAGIC - Return results (value, rows, etc.)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Example (Transformation)**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC storesDF.select("sqft", "division")
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC storesDF.select("sqft", "division")
# MAGIC
# MAGIC
# MAGIC - ✔ Returns a new DataFrame
# MAGIC - ✔ Does NOT execute immediately
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are Actions**
# MAGIC
# MAGIC | Option   | Type     | Reason                        |
# MAGIC |----------|----------|------------------------------|
# MAGIC | count()  | ❌ Action| Returns number of rows        |
# MAGIC | show()   | ❌ Action| Displays data                 |
# MAGIC | first()  | ❌ Action| Returns first row             |
# MAGIC | collect()| ❌ Action| Brings data to driver         |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Quick Rule**
# MAGIC
# MAGIC | Category        | Examples                  |
# MAGIC |-----------------|--------------------------|
# MAGIC | Transformations | select, filter, groupBy   |
# MAGIC | Actions         | count, show, collect      |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 If it returns DataFrame → Transformation  
# MAGIC 👉 If it returns value/output → Action

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
# MAGIC
# MAGIC ✅ **Correct Answer:** D. `DataFrame.join()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Key Concept: Lazy Evaluation in Spark**
# MAGIC
# MAGIC - **Transformations** → ❌ Do NOT trigger execution  
# MAGIC - **Actions** → ✅ Trigger execution
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Classification**
# MAGIC
# MAGIC | Operation   | Type           | Triggers Execution? |
# MAGIC |-------------|---------------|---------------------|
# MAGIC | collect()   | Action         | ✅ Yes              |
# MAGIC | count()     | Action         | ✅ Yes              |
# MAGIC | first()     | Action         | ✅ Yes              |
# MAGIC | take()      | Action         | ✅ Yes              |
# MAGIC | join()      | Transformation | ❌ No               |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Example**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC df1.join(df2, "id")           # No execution yet
# MAGIC df1.join(df2, "id").count()   # Execution triggered here
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC df1.join(df2, "id")           // Lazy (no execution)
# MAGIC df1.join(df2, "id").count()   // Action triggers execution
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why join() is Correct**
# MAGIC
# MAGIC - Returns a new DataFrame
# MAGIC - Part of execution plan only
# MAGIC - Runs only when an action is called
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 If it returns DataFrame → no execution  
# MAGIC 👉 If it returns value/data → execution happens

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
# MAGIC
# MAGIC ✅ **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Correct Code (Works in BOTH PySpark & Scala)**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC spark.read.schema(schema).load(filePath)
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC spark.read.schema(schema).load(filePath)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔎 **Fill in the blanks**
# MAGIC
# MAGIC | Blank  | Value     |
# MAGIC |--------|-----------|
# MAGIC | __1__  | spark     |
# MAGIC | __2__  | read      |
# MAGIC | __3__  | schema    |
# MAGIC | __4__  | schema    |
# MAGIC | __5__  | load      |
# MAGIC | __6__  | filePath  |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚠️ **Important Note**
# MAGIC
# MAGIC The question says JSON, but the code uses:
# MAGIC
# MAGIC `format("csv")`
# MAGIC
# MAGIC 👉 This is inconsistent, but among the options, only D forms a valid and correct Spark read pattern with schema.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong**
# MAGIC
# MAGIC - **A / B**  
# MAGIC   ❌ Incorrect chaining and method usage
# MAGIC
# MAGIC - **C**  
# MAGIC   ❌ Uses `read()` instead of `read`
# MAGIC
# MAGIC - **E**  
# MAGIC   ❌ Missing `.schema(schema)` → schema not applied
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Correct Pattern to Remember**
# MAGIC
# MAGIC python
# MAGIC spark.read.schema(schema).format("json").load(path)
# MAGIC
# MAGIC
# MAGIC OR simply:
# MAGIC
# MAGIC python
# MAGIC spark.read.schema(schema).json(path)

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
# MAGIC ✅ **Correct Answer:** A
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Correct Code**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC from pyspark.sql.functions import col, abs
# MAGIC
# MAGIC storesDF.withColumn("customerSatisfactionAbs", abs(col("customerSatisfaction")))
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC import org.apache.spark.sql.functions._
# MAGIC
# MAGIC storesDF.withColumn("customerSatisfactionAbs", abs(col("customerSatisfaction")))
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Option A is Correct**
# MAGIC
# MAGIC - `withColumn()` → used to create a new column
# MAGIC - `abs()` → computes absolute value
# MAGIC - `col("customerSatisfaction")` → correct column reference
# MAGIC
# MAGIC ✔ Returns a new DataFrame  
# MAGIC ✔ Adds new column `customerSatisfactionAbs`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Others Are Wrong**
# MAGIC
# MAGIC | Option | Issue                                      |
# MAGIC |--------|--------------------------------------------|
# MAGIC | B      | `withColumnRenamed()` is for renaming, not creating |
# MAGIC | C      | ❌ Syntax error (missing quotes & brackets) |
# MAGIC | D      | ❌ Column name not in quotes                |
# MAGIC | E      | ❌ `abs()` needs a Column, not a string     |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 Always use:  
# MAGIC `withColumn("newCol", function(col("existingCol")))`

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
# MAGIC ✅ **Correct Answer:** D
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Explanation**
# MAGIC
# MAGIC The Spark Driver is the central coordinator of a Spark application.
# MAGIC
# MAGIC 👉 **It is responsible for:**
# MAGIC - Creating the execution plan (DAG)
# MAGIC - Splitting jobs into stages & tasks
# MAGIC - Scheduling tasks on executors (worker nodes)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Option D is Correct**
# MAGIC
# MAGIC > “Spark driver is responsible for scheduling the execution of data by various worker nodes in cluster mode.”
# MAGIC
# MAGIC ✔ This is exactly what the driver does  
# MAGIC ✔ Works in both local and cluster modes
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Other Options Are Wrong**
# MAGIC
# MAGIC | Option | Reason |
# MAGIC |--------|--------|
# MAGIC | A | ❌ Driver is NOT horizontally scaled (single process) |
# MAGIC | B | ❌ Coarsest level is Job, not driver |
# MAGIC | C | ❌ Driver is NOT fault tolerant (if it fails → app fails) |
# MAGIC | E | ❌ Spark supports multiple cluster managers (YARN, Mesos, Kubernetes) |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Quick Summary**
# MAGIC
# MAGIC | Component      | Role                |
# MAGIC |----------------|---------------------|
# MAGIC | Driver         | Orchestrates execution |
# MAGIC | Executors      | Execute tasks          |
# MAGIC | Cluster Manager| Allocates resources    |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 Driver = Brain of Spark Application  
# MAGIC 👉 Not fault tolerant + Not distributed

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
# MAGIC ✅ **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Correct Code**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC storesDF.write.partitionBy("division").parquet(filePath)
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC storesDF.write.partitionBy("division").parquet(filePath)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔎 **Fill in the blanks**
# MAGIC
# MAGIC | Blank  | Value         |
# MAGIC |--------|--------------|
# MAGIC | __1__  | write        |
# MAGIC | __2__  | partitionBy  |
# MAGIC | __3__  | "division"   |
# MAGIC | __4__  | parquet      |
# MAGIC | __5__  | filePath     |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Option B is Correct**
# MAGIC
# MAGIC - `write` → DataFrameWriter
# MAGIC - `partitionBy("division")` → partitions data by column
# MAGIC - `parquet(filePath)` → writes in parquet format
# MAGIC
# MAGIC ✔ Correct syntax  
# MAGIC ✔ Works in both PySpark & Scala
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Others Are Wrong**
# MAGIC
# MAGIC | Option | Issue                                 |
# MAGIC |--------|---------------------------------------|
# MAGIC | A      | ❌ Invalid syntax (path + wrong argument) |
# MAGIC | C      | ❌ partitionBy expects string, not col() |
# MAGIC | D      | ❌ write() is incorrect (no parentheses) |
# MAGIC | E      | ❌ repartition is not used for writing format |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 Always remember:
# MAGIC
# MAGIC python
# MAGIC df.write.partitionBy("colName").format(filePath)
# MAGIC
# MAGIC or
# MAGIC python
# MAGIC df.write.partitionBy("colName").parquet(path)

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
# MAGIC
# MAGIC ✅ **Correct Answer:** A. Shuffle
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Key Concept: Stage Boundaries in Spark**
# MAGIC
# MAGIC A stage boundary is created when Spark needs to reorganize data across partitions.
# MAGIC
# MAGIC 👉 This happens during a shuffle operation.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Shuffle Creates Stage Boundary**
# MAGIC
# MAGIC - Shuffle = data moves across executors
# MAGIC - Requires:
# MAGIC   - Writing intermediate data
# MAGIC   - Redistributing data
# MAGIC - Spark splits execution into multiple stages
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔁 **Examples of Shuffle Operations**
# MAGIC
# MAGIC - `groupBy()`
# MAGIC - `reduceByKey()`
# MAGIC - `join()`
# MAGIC - `distinct()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Others Are Wrong**
# MAGIC
# MAGIC | Option | Reason                                      |
# MAGIC |--------|---------------------------------------------|
# MAGIC | B. Caching           | ❌ Just stores data, no stage boundary      |
# MAGIC | C. Executor failure  | ❌ Runtime issue, not execution planning    |
# MAGIC | D. Job delegation    | ❌ Not a Spark concept                     |
# MAGIC | E. Application failure| ❌ Stops execution, not stage creation     |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Quick Visualization**
# MAGIC
# MAGIC Stage 1  --->  **SHUFFLE**  --->  Stage 2
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 Narrow transformations → Same stage  
# MAGIC 👉 Wide transformations (Shuffle) → New stage

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
# MAGIC
# MAGIC ✅ **Correct Answer:** C. Scenario 1
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Key Concept: Shuffle & Network Traffic**
# MAGIC
# MAGIC During a shuffle, data is:
# MAGIC - Moved across executors
# MAGIC - Sent over the network
# MAGIC
# MAGIC 👉 More executors = more cross-node communication = more network traffic
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 📊 **Scenario Comparison**
# MAGIC
# MAGIC | Scenario | Executors     | Network Traffic |
# MAGIC |----------|--------------|----------------|
# MAGIC | #1       | 1 executor   | 🟢 Lowest      |
# MAGIC | #4       | 2 executors  | 🟡 Medium      |
# MAGIC | #5       | 4 executors  | 🟠 Higher      |
# MAGIC | #6       | 8 executors  | 🔴 Highest     |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Scenario #1 is Best**
# MAGIC - Only one executor
# MAGIC - Shuffle happens within same node
# MAGIC - ❌ No inter-node data transfer
# MAGIC
# MAGIC 👉 **Result:** Minimal network usage
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Trade-off Insight**
# MAGIC
# MAGIC | Scenario | GC Risk | Network Traffic |
# MAGIC |----------|--------|----------------|
# MAGIC | #1       | 🔴 High| 🟢 Low         |
# MAGIC | #6       | 🟢 Low | 🔴 High        |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC - ❗ More nodes → more network shuffle
# MAGIC - ❗ Single node → minimal network traffic

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
# MAGIC ✅ **Correct Answer:** E
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **What is a Partition in Spark?**
# MAGIC
# MAGIC A partition is:
# MAGIC - 👉 A chunk of data (rows)
# MAGIC - 👉 That is distributed across machines (executors)
# MAGIC - 👉 And processed in parallel
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Option E is Correct**
# MAGIC
# MAGIC > “A partition is a collection of rows of data that fit on a single machine in a cluster.”
# MAGIC
# MAGIC ✔ Matches Spark’s definition  
# MAGIC ✔ Each partition is processed by one task on one executor
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 📊 **Simple Visualization**
# MAGIC
# MAGIC DataFrame  
# MAGIC    ↓  
# MAGIC [Partition 1] → Executor 1  
# MAGIC [Partition 2] → Executor 2  
# MAGIC [Partition 3] → Executor 3  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Others Are Wrong**
# MAGIC
# MAGIC | Option | Issue                        |
# MAGIC |--------|------------------------------|
# MAGIC | A      | ❌ Partition ≠ executor capacity |
# MAGIC | B      | ❌ Not about logical plans        |
# MAGIC | C      | ❌ Too vague (not “fits on node”)|
# MAGIC | D      | ❌ Describes jobs/stages, not partitions |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key Characteristics**
# MAGIC
# MAGIC - Smallest unit of parallelism
# MAGIC - Each partition → 1 task
# MAGIC - Can be reshuffled / repartitioned
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 Partition = data chunk processed independently

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
# MAGIC
# MAGIC ✅ **Correct Answer:** C. Stage
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Key Concept: Spark Execution Hierarchy**
# MAGIC
# MAGIC Spark execution is organized as:
# MAGIC
# MAGIC
# MAGIC Job → Stage → Task
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **What is a Stage?**
# MAGIC
# MAGIC A Stage is:
# MAGIC - 👉 A group of tasks
# MAGIC - 👉 Created from multiple narrow transformations
# MAGIC - 👉 Executed without shuffle
# MAGIC
# MAGIC ✔ Narrow transformations are pipelined together in one stage  
# MAGIC ✔ A new stage is created only when a shuffle occurs
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 📊 **Example**
# MAGIC
# MAGIC python
# MAGIC storesDF.filter(...).select(...).map(...)
# MAGIC
# MAGIC
# MAGIC ✔ All are narrow operations  
# MAGIC ✔ Executed in one Stage
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Others Are Wrong**
# MAGIC
# MAGIC | Option   | Reason                        |
# MAGIC |----------|------------------------------|
# MAGIC | A. Slot  | ❌ Not a Spark execution unit |
# MAGIC | B. Job   | ❌ Contains multiple stages   |
# MAGIC | D. Task  | ❌ Smallest unit, not sequence|
# MAGIC | E. Executor | ❌ Worker process          |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Quick Summary**
# MAGIC
# MAGIC | Level | Description                |
# MAGIC |-------|----------------------------|
# MAGIC | Job   | Entire Spark action        |
# MAGIC | Stage | Group of narrow ops ✔      |
# MAGIC | Task  | Work on one partition      |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 No shuffle → same stage  
# MAGIC 👉 Shuffle → new stage

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
# MAGIC
# MAGIC ✅ **Correct Answer:** C. Standard mode
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Explanation**
# MAGIC
# MAGIC Spark supports the following execution/deployment modes:
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ✅ Valid Modes
# MAGIC
# MAGIC | Mode         | Description                          |
# MAGIC |--------------|--------------------------------------|
# MAGIC | Client mode  | Driver runs on the client machine    |
# MAGIC | Cluster mode | Driver runs inside the cluster       |
# MAGIC | Local mode   | Runs locally (no cluster, for testing)|
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ❌ Invalid Mode
# MAGIC
# MAGIC | Mode         | Status   |
# MAGIC |--------------|----------|
# MAGIC | Standard mode| ❌ Not valid |
# MAGIC
# MAGIC 👉 This is not a valid Spark deployment mode
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Quick Summary**
# MAGIC
# MAGIC - Valid → Client, Cluster, Local
# MAGIC - Invalid → Standard
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 Only remember 3 modes:
# MAGIC - Local
# MAGIC - Client
# MAGIC - Cluster

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
# MAGIC
# MAGIC ✅ **Correct Answer:** E. A failed driver node
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Explanation**
# MAGIC
# MAGIC The Spark Driver is the central coordinator of the application.
# MAGIC
# MAGIC 👉 If the driver fails:
# MAGIC
# MAGIC - ❌ Entire Spark application stops
# MAGIC - ❌ No task scheduling possible
# MAGIC - ❌ Job cannot recover
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Other Options Are NOT Failures**
# MAGIC
# MAGIC | Option | What Happens           | Result                        |
# MAGIC |--------|-----------------------|-------------------------------|
# MAGIC | A      | No data to driver     | ✔ Normal                      |
# MAGIC | B      | Cache > memory        | ✔ Partial caching / recompute |
# MAGIC | C      | Spill to disk         | ✔ Normal Spark behavior       |
# MAGIC | D      | Worker fails          | ✔ Spark recovers (re-executes tasks) |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔁 **Fault Tolerance in Spark**
# MAGIC
# MAGIC - Executors (workers) → ✅ Fault tolerant
# MAGIC - Driver → ❌ Single point of failure
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Example**
# MAGIC
# MAGIC python
# MAGIC df.collect()  # Driver crash here → job fails completely
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 Driver failure = Job failure  
# MAGIC 👉 Executor failure = Recoverable

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
# MAGIC
# MAGIC ✅ **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Key Concept: Spark Storage Levels**
# MAGIC
# MAGIC Spark provides different persistence/storage levels to cache data.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 MEMORY_ONLY
# MAGIC
# MAGIC - Stores data only in memory (RAM)
# MAGIC - If data does not fit:
# MAGIC   - ❌ It is NOT stored
# MAGIC   - 🔁 It is recomputed when needed
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 MEMORY_AND_DISK
# MAGIC
# MAGIC - Stores data in memory first
# MAGIC - If data does not fit:
# MAGIC   - 💾 Remaining data is stored on disk
# MAGIC   - 📥 Read from disk when required (no recomputation)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 📊 **Comparison**
# MAGIC
# MAGIC | Feature         | MEMORY_ONLY      | MEMORY_AND_DISK   |
# MAGIC |-----------------|------------------|-------------------|
# MAGIC | Storage         | Memory only      | Memory + Disk     |
# MAGIC | If memory full  | Recompute        | Store on disk     |
# MAGIC | Performance     | Faster (if fits) | Slightly slower (disk I/O) |
# MAGIC | Reliability     | Lower            | Higher            |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Option D is Correct**
# MAGIC
# MAGIC ✔ Correctly states:
# MAGIC
# MAGIC - MEMORY_ONLY → recompute missing data
# MAGIC - MEMORY_AND_DISK → spill to disk
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Others Are Wrong**
# MAGIC
# MAGIC - A → ❌ Reversed definitions
# MAGIC - B/C → ❌ Mention replication (not relevant here)
# MAGIC - E → ❌ Incorrect “half memory half disk” concept
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 MEMORY_ONLY → recompute  
# MAGIC 👉 MEMORY_AND_DISK → spill to disk

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
# MAGIC ✅ **Correct Answer:** B. `spark.sql.autoBroadcastJoinThreshold`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Explanation**
# MAGIC
# MAGIC This Spark configuration controls:
# MAGIC
# MAGIC 👉 Automatic broadcasting of small DataFrames during joins
# MAGIC
# MAGIC If a DataFrame size is below the threshold  
# MAGIC → Spark will automatically broadcast it  
# MAGIC Helps optimize join performance
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Default Behavior**
# MAGIC
# MAGIC - Default value: 10 MB
# MAGIC - If DataFrame size ≤ threshold → broadcast join used
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🐍 Example (PySpark)**
# MAGIC python
# MAGIC spark.conf.set("spark.sql.autoBroadcastJoinThreshold", 10485760)  # 10 MB
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC spark.conf.set("spark.sql.autoBroadcastJoinThreshold", 10485760)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Others Are Wrong**
# MAGIC
# MAGIC | Option | Purpose                                 |
# MAGIC |--------|-----------------------------------------|
# MAGIC | A      | Broadcast timeout duration              |
# MAGIC | C      | Number of shuffle partitions            |
# MAGIC | D      | Columnar storage batch size             |
# MAGIC | E      | Adaptive query execution optimization   |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 “autoBroadcast” = automatic broadcast join threshold

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
# MAGIC
# MAGIC ✅ **Correct Answer:** E
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Explanation**
# MAGIC
# MAGIC The error is in how `cast()` is used.
# MAGIC
# MAGIC 👉 In Spark:
# MAGIC
# MAGIC - `cast()` is **NOT** a standalone function
# MAGIC - It is a method of the Column object
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Incorrect Code (Given)**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC storesDF.withColumn("storeId", cast(col("storeId"), StringType()))
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct Code**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC from pyspark.sql.functions import col
# MAGIC from pyspark.sql.types import StringType
# MAGIC
# MAGIC storesDF.withColumn("storeId", col("storeId").cast(StringType()))
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC import org.apache.spark.sql.functions._
# MAGIC import org.apache.spark.sql.types._
# MAGIC
# MAGIC storesDF.withColumn("storeId", col("storeId").cast(StringType))
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Option E is Correct**
# MAGIC
# MAGIC ✔ `cast()` must be called like:
# MAGIC
# MAGIC python
# MAGIC col("columnName").cast(DataType)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Others Are Wrong**
# MAGIC
# MAGIC | Option | Reason |
# MAGIC |--------|--------|
# MAGIC | A | ❌ You CAN overwrite same column using withColumn() |
# MAGIC | B | ❌ Type conversion is valid inside withColumn() |
# MAGIC | C | ❌ Parentheses are correct in PySpark |
# MAGIC | D | ❌ Column names MUST be in quotes |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 Always remember:
# MAGIC
# MAGIC python
# MAGIC col("colName").cast(Type)

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
# MAGIC
# MAGIC ✅ **Correct Answer: E**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Key Concept: substr() in Spark**
# MAGIC
# MAGIC In Spark (both PySpark & Scala):
# MAGIC
# MAGIC - `substr(startPos, length)`
# MAGIC - ⚠️ Index starts from 1 (NOT 0)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct Code**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC from pyspark.sql.functions import col
# MAGIC
# MAGIC storesDF.withColumn("division", col("division").substr(1, 2))
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC import org.apache.spark.sql.functions._
# MAGIC
# MAGIC storesDF.withColumn("division", col("division").substr(1, 2))
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Option E is Correct**
# MAGIC
# MAGIC - `substr(1, 2)` → starts at position 1
# MAGIC - Extracts first 2 characters
# MAGIC
# MAGIC ✔ Matches requirement exactly
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Others Are Wrong**
# MAGIC
# MAGIC | Option | Issue                  |
# MAGIC |--------|------------------------|
# MAGIC | A      | ❌ Uses 0 index (invalid in Spark) |
# MAGIC | B      | ❌ Typo (susbtr)        |
# MAGIC | C      | ❌ Extracts 3 characters|
# MAGIC | D      | ❌ Starts at 0 (invalid)|
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 Spark string functions use 1-based indexing

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
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct Answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Correct Code**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC storesDF.withColumnRenamed("division", "state") \
# MAGIC         .withColumnRenamed("managerName", "managerFullName")
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC storesDF.withColumnRenamed("division", "state")
# MAGIC         .withColumnRenamed("managerName", "managerFullName")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔎 **Fill in the blanks**
# MAGIC
# MAGIC - __1__ = withColumnRenamed  
# MAGIC - __2__ = "division"  
# MAGIC - __3__ = "state"  
# MAGIC - __4__ = withColumnRenamed  
# MAGIC - __5__ = "managerName"  
# MAGIC - __6__ = "managerFullName"
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Option C is Correct**
# MAGIC
# MAGIC - `withColumnRenamed(oldName, newName)`
# MAGIC - Correct order: 👉 existing column → new column name
# MAGIC - ✔ Proper chaining
# MAGIC - ✔ Correct syntax (case-sensitive)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Others Are Wrong**
# MAGIC
# MAGIC | Option | Issue |
# MAGIC |--------|-------|
# MAGIC | A      | ❌ Parameters reversed |
# MAGIC | B      | ❌ Uses col() instead of string |
# MAGIC | C      | ✅ Correct (only valid one) |
# MAGIC | D/E    | ❌ withColumn is for creating/modifying, not renaming |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 Always remember:  
# MAGIC `withColumnRenamed("oldName", "newName")`

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
# MAGIC
# MAGIC ✅ **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Requirement**
# MAGIC
# MAGIC 👉 Drop rows where **ALL** columns have missing values
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct Code**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC storesDF.na.drop(how="all")
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC storesDF.na.drop("all")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔎 **Fill in the blanks**
# MAGIC
# MAGIC - __1__ = na  
# MAGIC - __2__ = drop  
# MAGIC - __3__ = how  
# MAGIC - __4__ = "all"
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Option D is Correct**
# MAGIC
# MAGIC - `na.drop()` → handles null values
# MAGIC - `how="all"` → drops rows where all columns are null
# MAGIC
# MAGIC ✔ Matches requirement exactly
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Others Are Wrong**
# MAGIC
# MAGIC | Option | Issue                                 |
# MAGIC |--------|---------------------------------------|
# MAGIC | A      | ❌ "any" drops rows with ANY null (too aggressive) |
# MAGIC | B/C    | ❌ subset is for specific columns only |
# MAGIC | E      | ❌ Incorrect method chaining           |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC | Condition         | Usage         |
# MAGIC |-------------------|--------------|
# MAGIC | Drop if ANY null  | how="any"    |
# MAGIC | Drop if ALL null  | how="all" ✅ |

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
# MAGIC
# MAGIC ✅ **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Correct Code**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC storesDF.describe("sqft")
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC storesDF.describe("sqft")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Option D is Correct**
# MAGIC
# MAGIC - `describe()` returns summary statistics like:
# MAGIC   - count
# MAGIC   - mean
# MAGIC   - stddev
# MAGIC   - min
# MAGIC   - max
# MAGIC - It expects column names as strings, not `col()` objects
# MAGIC
# MAGIC ✔ Correct syntax  
# MAGIC ✔ Matches requirement exactly
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Others Are Wrong**
# MAGIC
# MAGIC | Option | Issue                                 |
# MAGIC |--------|---------------------------------------|
# MAGIC | A      | ❌ `summary()` expects string, not `col()` |
# MAGIC | B      | ❌ `describe()` does NOT take `col()`      |
# MAGIC | C      | ⚠️ `summary("sqft")` works, but question typically expects `describe()` |
# MAGIC | E      | ❌ `"all"` is not a column                 |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **describe() vs summary()**
# MAGIC
# MAGIC | Function  | Notes                                 |
# MAGIC |-----------|---------------------------------------|
# MAGIC | describe()| Standard stats (common use) ✅         |
# MAGIC | summary() | Extended stats (more flexible)         |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 Use:
# MAGIC python
# MAGIC df.describe("column")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC | Key Differences | describe(*cols) | summary(*statistics) |
# MAGIC |-----------------|-----------------|----------------------|
# MAGIC | Default Statistics | Count, mean, stddev, min, max. | Count, mean, stddev, min, approx. percentiles (25%, 50%, 75%), max. |
# MAGIC | Arguments | Takes column names to describe specific features. | Takes statistic names (e.g., "count", "75%") to filter what is computed. |
# MAGIC | Percentiles | Does not include percentiles by default. | Includes 25%, 50%, and 75% percentiles by default. |
# MAGIC | Flexibility | Limited to basic predefined statistics. | Highly customizable; you can specify arbitrary percentiles like "10%" or "99%". |

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
# MAGIC
# MAGIC ✅ **Correct Answer:** B
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Requirement**
# MAGIC
# MAGIC - Sample 15% of rows  
# MAGIC - Without replacement
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct Code**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC storesDF.sample(fraction=0.15)
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC storesDF.sample(0.15)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Option B is Correct**
# MAGIC
# MAGIC - `fraction=0.15` → 15% sample
# MAGIC - `withReplacement` default = False  
# MAGIC   ✔ So this is without replacement
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Others Are Wrong**
# MAGIC
# MAGIC | Option | Issue                                 |
# MAGIC |--------|---------------------------------------|
# MAGIC | A      | ❌ True → with replacement             |
# MAGIC | C      | ❌ sampleBy() requires column + fractions |
# MAGIC | D      | ❌ 10%, not 15%                       |
# MAGIC | E      | ❌ Missing fraction                   |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 If `withReplacement` is not provided → default is False

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
# MAGIC
# MAGIC ✅ **Correct Answer: E**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Correct Code**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC
# MAGIC storesDF.first().sqft
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC
# MAGIC storesDF.first().getAs[Int]("sqft")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Option E is Correct**
# MAGIC
# MAGIC - `first()` → returns the first Row
# MAGIC - `.sqft` → accesses the column value
# MAGIC
# MAGIC ✔ Clean and valid in PySpark  
# MAGIC ✔ Commonly used pattern
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Others Are Wrong**
# MAGIC
# MAGIC | Option | Issue                                 |
# MAGIC |--------|---------------------------------------|
# MAGIC | A      | ❌ Cannot use col() inside Row access  |
# MAGIC | B      | ❌ DataFrame is not indexable like list|
# MAGIC | C      | ⚠️ Works but inefficient (collects all data)|
# MAGIC | D      | ❌ Missing parentheses in first()      |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Better vs Allowed**
# MAGIC
# MAGIC | Code                  | Status                |
# MAGIC |-----------------------|-----------------------|
# MAGIC | first().sqft          | ✅ Best               |
# MAGIC | collect()[0]["sqft"]  | ⚠️ Works but bad practice|
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 Prefer:
# MAGIC
# MAGIC df.first().columnName

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
# MAGIC
# MAGIC ✅ **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Correct Code**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC storesDF.createOrReplaceTempView("stores")
# MAGIC spark.sql("SELECT storeId, managerName FROM stores")
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC storesDF.createOrReplaceTempView("stores")
# MAGIC spark.sql("SELECT storeId, managerName FROM stores")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Option D is Correct**
# MAGIC
# MAGIC - `createOrReplaceTempView("stores")`
# MAGIC   - 👉 Registers DataFrame as a temporary SQL table
# MAGIC - `spark.sql(...)`
# MAGIC   - 👉 Runs SQL query on that table
# MAGIC
# MAGIC ✔ Proper workflow  
# MAGIC ✔ Valid in both PySpark & Scala
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Others Are Wrong**
# MAGIC
# MAGIC | Option | Issue |
# MAGIC |--------|-------|
# MAGIC | A      | ❌ Missing table name in createOrReplaceTempView() |
# MAGIC | B      | ❌ query() is not a Spark DataFrame method |
# MAGIC | C      | ❌ Wrong object calling createOrReplaceTempView() |
# MAGIC | E      | ❌ query() method does not exist |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 Always follow:
# MAGIC
# MAGIC python
# MAGIC df.createOrReplaceTempView("tableName")
# MAGIC spark.sql("SELECT ... FROM tableName")

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
# MAGIC
# MAGIC ✅ **Correct Answer: E**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Correct Code**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC spark.conf.set("spark.sql.shuffle.partitions", "32")
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC spark.conf.set("spark.sql.shuffle.partitions", "32")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Option E is Correct**
# MAGIC
# MAGIC - `spark.sql.shuffle.partitions`
# MAGIC   - 👉 Controls number of partitions used in shuffle operations (like join, groupBy)
# MAGIC - `spark.conf.set()`
# MAGIC   - 👉 Used to set configuration
# MAGIC
# MAGIC ✔ Exactly matches requirement: wide transformations → shuffle → partitions = 32
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Others Are Wrong**
# MAGIC
# MAGIC | Option | Issue                                 |
# MAGIC |--------|---------------------------------------|
# MAGIC | A      | ❌ get retrieves value, doesn’t set    |
# MAGIC | B      | ❌ Wrong config (spark.default.parallelism) |
# MAGIC | C      | ❌ text is invalid method              |
# MAGIC | D      | ❌ Wrong config again                  |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key Difference**
# MAGIC
# MAGIC | Config                     | Purpose                        |
# MAGIC |----------------------------|-------------------------------|
# MAGIC | spark.sql.shuffle.partitions| ✅ For joins, aggregations     |
# MAGIC | spark.default.parallelism   | For RDD operations            |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 Shuffle = spark.sql.shuffle.partitions

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
# MAGIC ✅ **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Correct Code**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC from pyspark.sql.functions import col, from_unixtime
# MAGIC
# MAGIC storesDF.withColumn(
# MAGIC     "openDateString",
# MAGIC     from_unixtime(col("openDate"), "EEEE, MMM d, yyyy h:mm a")
# MAGIC )
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC import org.apache.spark.sql.functions._
# MAGIC
# MAGIC storesDF.withColumn(
# MAGIC   "openDateString",
# MAGIC   from_unixtime(col("openDate"), "EEEE, MMM d, yyyy h:mm a")
# MAGIC )
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Option A is Correct**
# MAGIC
# MAGIC - `from_unixtime()` converts:
# MAGIC   - 👉 UNIX timestamp → formatted string
# MAGIC
# MAGIC - Format:
# MAGIC   - `"EEEE, MMM d, yyyy h:mm a"`
# MAGIC
# MAGIC ✔ Matches Java’s SimpleDateFormat
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Others Are Wrong**
# MAGIC
# MAGIC | Option | Issue                                      |
# MAGIC |--------|--------------------------------------------|
# MAGIC | B      | ❌ from_unixtime does not take TimestampType|
# MAGIC | C      | ❌ date() is not valid for formatting like this|
# MAGIC | D      | ❌ newColumn() does not exist               |
# MAGIC | E      | ❌ Wrong function + invalid arguments       |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key Function**
# MAGIC
# MAGIC | Function         | Purpose                          |
# MAGIC |------------------|----------------------------------|
# MAGIC | from_unixtime()  | Convert epoch → formatted string ✅|
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 UNIX timestamp → readable date = `from_unixtime()`

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
# MAGIC
# MAGIC **The correct answer is A.**  
# MAGIC `storesDF.crossJoin(employeesDF)`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation**
# MAGIC
# MAGIC - Option A is correct because in PySpark, the dedicated method for performing a Cartesian product (cross join) between two DataFrames is `crossJoin()`. This method takes the right-side DataFrame as its only required argument.
# MAGIC
# MAGIC - Option B is incorrect because it specifies a join key ("storeId"). A cross join is a Cartesian product that combines every row from the left DataFrame with every row from the right DataFrame without a join condition.
# MAGIC
# MAGIC - Option C and D are incorrect because `crossJoin` and `join` are methods of the DataFrame class (e.g., `df.crossJoin()`), not standalone functions that you call by passing both DataFrames as arguments in that specific syntax.
# MAGIC
# MAGIC - Option E is incorrect because, while some documentation indicates Spark can perform different join types via the `join()` method (like "inner" or "outer"), the standard and intended way to execute a cross join in the Spark DataFrame API is through the specific `.crossJoin()` method. Using `.join(df, "cross")` without a join condition is not the standard implementation for a Cartesian product in this context.

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
# MAGIC
# MAGIC ✅ **Correct Answer: E**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Correct Code**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC storesDF.union(acquiredStoresDF)
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC storesDF.union(acquiredStoresDF)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Option E is Correct**
# MAGIC
# MAGIC - `union()` performs a position-wise union
# MAGIC - It combines rows based on column order, not column names
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 **Requirements:**
# MAGIC - Same number of columns
# MAGIC - Same column data types
# MAGIC - Same column order
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔄 **Position-wise vs Name-wise**
# MAGIC
# MAGIC | Method         | Behavior                        |
# MAGIC |----------------|---------------------------------|
# MAGIC | union()        | ✅ Matches columns by position   |
# MAGIC | unionByName()  | ✅ Matches columns by column name|
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Other Options Are Wrong**
# MAGIC
# MAGIC | Option | Issue                                 |
# MAGIC |--------|---------------------------------------|
# MAGIC | A      | ❌ unionByName() → name-based, not position-based |
# MAGIC | B      | ❌ unionAll() is deprecated            |
# MAGIC | C      | ❌ Not a valid standalone function     |
# MAGIC | D      | ❌ concat() is for columns, not DataFrames |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 Position-wise → `union()`
# MAGIC 👉 Column name-wise → `unionByName()`

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
# MAGIC Answer: C (According to Pdf and ExamTopic)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **The correct order for the lines of code to read a Parquet file into a DataFrame is 4, 5, 6 (Option D).**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 1. Analysis of the Code Structure
# MAGIC
# MAGIC To read a file in Spark, you typically use the SparkSession (represented as `spark`) to access the DataFrameReader through the `read` property or method.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Based on the provided lines:**
# MAGIC
# MAGIC - **Line 4 (`spark \`)**: This is the starting point. It references the SparkSession object.
# MAGIC - **Line 5 (`.read() \`)**: In Spark’s Java/Scala APIs, `read()` returns a DataFrameReader. While PySpark often uses the property `read` without parentheses, the exam question structure specifically includes `.read()` as a step to obtain the reader.
# MAGIC - **Line 6 (`.parquet(filePath)`)**: This is the final method called on the DataFrameReader to load the file at the specified path as a Parquet format.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **The completed command becomes:**
# MAGIC python
# MAGIC spark \
# MAGIC .read() \
# MAGIC .parquet(filePath)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 2. Explanation of Incorrect Options
# MAGIC
# MAGIC - **Option A (1, 5, 2):** Starts with `storesDF`, which is an existing DataFrame, not the reader object needed to load a new file.
# MAGIC - **Option B (4, 5, 2):** This would result in `spark.read().load(filePath, source = "parquet")`. While functionally similar in some contexts, the standard exam-targeted `parquet` method is line 6.
# MAGIC - **Option C (4, 3, 6):** This would result in `spark.read \.parquet(filePath)`. In many Spark APIs, `read` is a property, but the question lists `.read()` as line 5, making 4, 5, 6 a more complete chain.
# MAGIC - **Option E (4, 3, 2):** Uses line 3 (`.read \`), which is often a property access in Python, but line 2 (`.load(...)`) is less direct than the specialized `parquet()` method when specifically asked to "read a parquet".

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
# MAGIC ✅ **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 What are Slots in Spark?
# MAGIC
# MAGIC - Slots = CPU cores (or threads) available on an executor  
# MAGIC - Each slot can run one task at a time
# MAGIC
# MAGIC 👉 So, more slots = more parallelism
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔍 Why Option B is Correct
# MAGIC
# MAGIC Slots are resource threads that can be used for parallelization within a Spark application.
# MAGIC
# MAGIC ✔ Exactly matches Spark’s execution model:
# MAGIC
# MAGIC - 1 task runs per slot
# MAGIC - Slots come from executor cores
# MAGIC - Enable parallel execution of tasks
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ❌ Why Other Options Are Wrong
# MAGIC
# MAGIC | Option | Issue |
# MAGIC |--------|-------|
# MAGIC | A      | ❌ Most coarse level is Application, not slots |
# MAGIC | C      | ❌ Describes cluster resource sharing, not slots |
# MAGIC | D      | ❌ Most granular level is Task, not slot |
# MAGIC | E      | ❌ Describes partition, not slot |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Quick Hierarchy (Exam Gold 🔥)
# MAGIC
# MAGIC
# MAGIC Application
# MAGIC   → Job
# MAGIC     → Stage
# MAGIC       → Task (runs on a slot)
# MAGIC
# MAGIC
# MAGIC 👉 Slot is NOT part of hierarchy, but supports execution
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Exam Tip
# MAGIC
# MAGIC - Task = unit of work
# MAGIC - Slot = resource that runs the task

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
# MAGIC
# MAGIC ✅ **Correct Answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Spark Execution Hierarchy (Largest → Smallest)
# MAGIC
# MAGIC **Job → Stage → Task**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔍 Explanation
# MAGIC
# MAGIC **Job**
# MAGIC - Triggered by an action (e.g., `count()`, `collect()`)
# MAGIC - Represents the entire computation
# MAGIC
# MAGIC **Stage**
# MAGIC - A set of tasks
# MAGIC - Created based on shuffle boundaries
# MAGIC
# MAGIC **Task**
# MAGIC - The smallest unit of work
# MAGIC - Operates on one partition
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ❌ Why Other Options Are Wrong
# MAGIC
# MAGIC | Option | Issue                                 |
# MAGIC |--------|---------------------------------------|
# MAGIC | A      | ❌ Reverse order                      |
# MAGIC | B      | ❌ Starts with Stage instead of Job    |
# MAGIC | D      | ❌ Incorrect hierarchy                |
# MAGIC | E      | ❌ Task cannot be larger than Stage    |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Exam Tip
# MAGIC
# MAGIC 👉 Action → Job → Stage → Task → (runs on Slot)

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

# MAGIC %md
# MAGIC ✅ **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Why?
# MAGIC
# MAGIC `DataFrame.filter()` is a **narrow transformation**:
# MAGIC
# MAGIC - Operates within each partition
# MAGIC - No data movement across nodes
# MAGIC - 👉 Therefore, **no shuffle**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔍 Compare with Other Options
# MAGIC
# MAGIC | Operation   | Shuffle? | Reason                                 |
# MAGIC |-------------|----------|----------------------------------------|
# MAGIC | join()      | ❌ Yes    | Needs data alignment across partitions |
# MAGIC | filter()    | ✅ No     | Works row-wise within partition        |
# MAGIC | orderBy()   | ❌ Yes    | Requires global sorting                |
# MAGIC | distinct()  | ❌ Yes    | Needs grouping across partitions       |
# MAGIC | intersect() | ❌ Yes    | Requires comparison across partitions  |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Key Concept
# MAGIC
# MAGIC - **Narrow Transformation** → No shuffle
# MAGIC - **Wide Transformation** → Shuffle required
# MAGIC
# MAGIC 👉 `filter()` is narrow, others are wide
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Exam Tip
# MAGIC
# MAGIC 👉 If operation does **not** require data from other partitions → **no shuffle**

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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct Answer: E (Scenario #6)**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Key Concept: Garbage Collection (GC) in Spark
# MAGIC
# MAGIC GC issues happen when:
# MAGIC - Executors have large memory heaps
# MAGIC - JVM struggles to clean up large objects
# MAGIC
# MAGIC 👉 Smaller executors = less GC pressure
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔍 Understanding the Scenarios
# MAGIC
# MAGIC **Scenario #1 (Worst for GC ❌)**
# MAGIC - 1 executor with 100 GB
# MAGIC - Very large heap → high GC pauses
# MAGIC
# MAGIC **Scenario #6 (Best for GC ✅)**
# MAGIC - 8 executors with 12.5 GB each
# MAGIC - Smaller heaps → faster GC
# MAGIC - Better distribution → less memory pressure per executor
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Why Scenario #6 is Best
# MAGIC
# MAGIC - Memory split across many executors
# MAGIC - GC happens on smaller heaps
# MAGIC - Reduces:
# MAGIC   - GC pause time
# MAGIC   - Risk of memory fragmentation
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 📊 Rule of Thumb
# MAGIC
# MAGIC | Executor Size | GC Impact      |
# MAGIC |---------------|---------------|
# MAGIC | Large         | ❌ High GC delay |
# MAGIC | Small         | ✅ Low GC delay  |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Exam Tip
# MAGIC
# MAGIC 👉 More executors with smaller memory = better for GC

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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct Answer: E**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Correct Code**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC from pyspark.sql.functions import col, explode
# MAGIC
# MAGIC storesDF.withColumn(
# MAGIC     "productCategories",
# MAGIC     explode(col("productCategories"))
# MAGIC )
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why E is Correct**
# MAGIC
# MAGIC - The column `productCategories` is already an array (as shown in the image)
# MAGIC - We need:
# MAGIC   - One word per row
# MAGIC   - More rows than original DataFrame
# MAGIC
# MAGIC 👉 `explode()` does exactly this:
# MAGIC - Takes each element of the array
# MAGIC - Creates a new row per element
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔄 **Transformation**
# MAGIC
# MAGIC | Original         | After explode |
# MAGIC |------------------|--------------|
# MAGIC | [netus, pellentesque] | netus<br>pellentesque |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Others Are Wrong**
# MAGIC
# MAGIC | Option | Issue                        |
# MAGIC |--------|------------------------------|
# MAGIC | A      | ❌ `newColumn` doesn’t exist  |
# MAGIC | B      | ❌ Missing `explode()`        |
# MAGIC | C      | ❌ Changes column name unnecessarily (question doesn’t require rename) |
# MAGIC | D      | ❌ `newColumn` invalid        |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Trap 🚨**
# MAGIC
# MAGIC - Use `split()` only if column is string
# MAGIC - Use `explode()` if column is array ✅
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **One-Line Rule**
# MAGIC
# MAGIC 👉 Array → `explode()` → more rows

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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Correct Code**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC from pyspark.sql.functions import col, regexp_replace
# MAGIC
# MAGIC storesDF.withColumn(
# MAGIC     "storeReview",
# MAGIC     regexp_replace(col("storeReview"), " End$", "")
# MAGIC )
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC import org.apache.spark.sql.functions._
# MAGIC
# MAGIC storesDF.withColumn(
# MAGIC   "storeReview",
# MAGIC   regexp_replace(col("storeReview"), " End$", "")
# MAGIC )
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Option B is Correct**
# MAGIC
# MAGIC - `regexp_replace()` is used to replace/remove patterns
# MAGIC - `" End$"` means: " End" at the end of the string (`$` = end anchor)
# MAGIC - `""` replaces it with nothing → effectively removes it
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Others Are Wrong**
# MAGIC
# MAGIC | Option | Issue                                      |
# MAGIC |--------|--------------------------------------------|
# MAGIC | A      | ❌ regexp_replace is not a column method    |
# MAGIC | C      | ❌ Missing replacement argument             |
# MAGIC | D      | ⚠️ Works in PySpark sometimes, but not standard/expected |
# MAGIC | E      | ❌ regexp_extract extracts, doesn’t replace |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key Regex Concept**
# MAGIC
# MAGIC | Pattern   | Meaning                        |
# MAGIC |-----------|-------------------------------|
# MAGIC | " End$"   | Matches "End" only at end of string |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 Remove pattern → `regexp_replace(col, pattern, "")`

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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔍 Correct Code
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC storesDF.na.drop(how="any")
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC storesDF.na.drop("any")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Why Option D is Correct
# MAGIC
# MAGIC - `na.drop()` → removes rows with null values
# MAGIC - `how="any"` → drop rows if any column has a null
# MAGIC
# MAGIC 👉 Exactly matches requirement:
# MAGIC
# MAGIC > “rows containing at least one missing value”
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ❌ Why Others Are Wrong
# MAGIC
# MAGIC | Option | Issue                                      |
# MAGIC |--------|--------------------------------------------|
# MAGIC | A      | ❌ subset is for specific columns, not condition |
# MAGIC | B      | ❌ "all" drops rows only if all values are null |
# MAGIC | C      | ❌ Same issue with subset                   |
# MAGIC | E      | ❌ Wrong method chaining (drop.na)          |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Key Difference
# MAGIC
# MAGIC | Parameter   | Meaning                        |
# MAGIC |-------------|-------------------------------|
# MAGIC | how="any"   | Drop if any column is null ✅  |
# MAGIC | how="all"   | Drop if all columns are null   |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Exam Tip
# MAGIC
# MAGIC 👉 “at least one null” → use `"any"`  
# MAGIC 👉 “all nulls” → use `"all"`

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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔍 Correct Usage
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC from pyspark.sql.functions import mean
# MAGIC
# MAGIC df.select(mean("columnName"))
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC import org.apache.spark.sql.functions._
# MAGIC
# MAGIC df.select(mean("columnName"))
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Why Option B is Correct
# MAGIC
# MAGIC - `mean()` calculates the average (arithmetic mean) of a column
# MAGIC - It’s a built-in Spark SQL function
# MAGIC
# MAGIC 👉 Equivalent to SQL:  
# MAGIC `AVG(columnName)`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ❌ Why Others Are Wrong
# MAGIC
# MAGIC | Option | Issue                                 |
# MAGIC |--------|---------------------------------------|
# MAGIC | A      | ❌ simpleAvg() does not exist          |
# MAGIC | C      | ⚠️ agg() is generic, not specific to average |
# MAGIC | D      | ❌ average() not a valid Spark function|
# MAGIC | E      | ❌ approxMean() does not exist         |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Exam Tip
# MAGIC
# MAGIC 👉 Average = `mean()` or `avg()`

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

# MAGIC %md
# MAGIC ✅ **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Why Option B Fails
# MAGIC
# MAGIC python
# MAGIC storesDF.groupBy("division").groupBy("storeCategory").count()
# MAGIC
# MAGIC
# MAGIC **❌ Problem:**
# MAGIC - You cannot chain `groupBy()` twice.
# MAGIC - The second `groupBy()` overrides the first one.
# MAGIC
# MAGIC **👉 Result:**
# MAGIC - It groups only by `storeCategory`, ignoring `division`.
# MAGIC - ❌ Does NOT return counts for combination of both columns.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ✅ Correct Ways (Working Options)
# MAGIC
# MAGIC All these correctly group by both columns:
# MAGIC
# MAGIC - **✔️ Multiple column arguments**
# MAGIC   python
# MAGIC   storesDF.groupBy("division", "storeCategory").count()
# MAGIC   
# MAGIC - **✔️ Using list**
# MAGIC   python
# MAGIC   storesDF.groupBy(["division", "storeCategory"]).count()
# MAGIC   
# MAGIC - **✔️ Using col()**
# MAGIC   python
# MAGIC   storesDF.groupBy(col("division"), col("storeCategory")).count()
# MAGIC   
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ⚠️ About Option A
# MAGIC
# MAGIC python
# MAGIC storesDF.groupBy((col("division"), col("storeCategory")]).count()
# MAGIC
# MAGIC - ❌ Syntax issue (mismatched brackets)
# MAGIC - Conceptually correct, but written incorrectly
# MAGIC
# MAGIC **👉 Exam intent focuses on logical failure, not syntax typo**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Exam Tip
# MAGIC
# MAGIC 👉 Group multiple columns in ONE `groupBy()` call
# MAGIC
# MAGIC **❌ Wrong:**
# MAGIC python
# MAGIC groupBy("col1").groupBy("col2")
# MAGIC
# MAGIC
# MAGIC **✅ Correct:**
# MAGIC python
# MAGIC groupBy("col1", "col2")

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

# MAGIC %md
# MAGIC ✅ **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔍 Given Code
# MAGIC
# MAGIC python
# MAGIC storesDF.describes(col("sgft"))
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 What’s the Error?
# MAGIC
# MAGIC There are actually two issues, but the key conceptual error tested here is:
# MAGIC
# MAGIC 👉 `describe()` expects column names as strings, **NOT** Column objects
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### ❌ Problem Explained
# MAGIC
# MAGIC - `col("sqft")` → returns a Column object
# MAGIC - `describe()` expects:
# MAGIC   - `"sqft"`   # string
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ✅ Correct Code
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC storesDF.describe("sqft")
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC storesDF.describe("sqft")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚠️ **Additional Minor Error (Ignored in Options)**
# MAGIC
# MAGIC - `"sgft"` ❌ typo → should be `"sqft"`
# MAGIC - 👉 But this is not the main concept being tested
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ❌ Why Other Options Are Wrong
# MAGIC
# MAGIC | Option | Issue                                 |
# MAGIC |--------|---------------------------------------|
# MAGIC | A      | ❌ `describe()` works fine for single column |
# MAGIC | B      | ❌ No need to subset column first      |
# MAGIC | C      | ❌ List of Column objects still not valid |
# MAGIC | E      | ❌ `describe()` works for numeric columns |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Exam Tip
# MAGIC
# MAGIC | Function   | Input Type           |
# MAGIC |------------|----------------------|
# MAGIC | describe() | ✅ column name string |
# MAGIC | col()      | ❌ NOT used here      |

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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct Answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Correct Code**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC storesDF.sample(fraction=0.25, seed=1234)
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC storesDF.sample(fraction = 0.25, seed = 1234)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Option C is Correct**
# MAGIC
# MAGIC - `fraction=0.25` → returns 25% of rows
# MAGIC - `seed=1234` → ensures reproducible results
# MAGIC
# MAGIC 👉 This exactly matches the requirement:
# MAGIC
# MAGIC > “25 percent sample with reproducible results”
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Other Options Are Wrong**
# MAGIC
# MAGIC | Option | Issue                                      |
# MAGIC |--------|--------------------------------------------|
# MAGIC | A      | ❌ seed must be a number, not True          |
# MAGIC | B      | ❌ Missing fraction                        |
# MAGIC | D      | ❌ Uses 15%, not 25%                       |
# MAGIC | E      | ❌ Missing fraction, unnecessary withReplacement |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Key Parameters**
# MAGIC
# MAGIC | Parameter       | Purpose                  |
# MAGIC |-----------------|-------------------------|
# MAGIC | fraction        | Percentage of data       |
# MAGIC | seed            | Reproducibility          |
# MAGIC | withReplacement | Sampling with/without duplicates |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 Reproducible sample = always use seed

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

# MAGIC %md
# MAGIC ✅ **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔍 Correct Code
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC from pyspark.sql.functions import udf, col
# MAGIC from pyspark.sql.types import IntegerType
# MAGIC
# MAGIC assessPerformanceUDF = udf(assessPerformance, IntegerType())
# MAGIC
# MAGIC storesDF.withColumn(
# MAGIC     "result",
# MAGIC     assessPerformanceUDF(col("customerSatisfaction"))
# MAGIC )
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Why Option B is Correct
# MAGIC
# MAGIC - `udf(function, returnType)` → correct way to define a UDF
# MAGIC - `IntegerType()` → must be instantiated (with parentheses)
# MAGIC - Then apply:  
# MAGIC   `assessPerformanceUDF(col("customerSatisfaction"))`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ❌ Why Other Options Are Wrong
# MAGIC
# MAGIC | Option | Issue                                      |
# MAGIC |--------|--------------------------------------------|
# MAGIC | A      | ❌ IntegerType missing ()                  |
# MAGIC | C      | ❌ UDF not used when applying              |
# MAGIC | D      | ❌ Missing return type (bad practice / may fail in strict cases) |
# MAGIC | E      | ❌ Calling original function instead of UDF|
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Key Concept
# MAGIC
# MAGIC | Step | Action                       |
# MAGIC |------|------------------------------|
# MAGIC | 1    | Create UDF with return type  |
# MAGIC | 2    | Apply UDF to column          |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Exam Tip
# MAGIC
# MAGIC 👉 Always use:  
# MAGIC `udf(function, ReturnType())`

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

# MAGIC %md
# MAGIC ✅ **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔍 Given Code
# MAGIC
# MAGIC python
# MAGIC spark.createDataFrame(years, IntegerType)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 What’s the Error?
# MAGIC
# MAGIC 👉 `IntegerType` is a class, and it must be instantiated
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### ❌ Wrong:
# MAGIC
# MAGIC python
# MAGIC IntegerType
# MAGIC
# MAGIC
# MAGIC #### ✅ Correct:
# MAGIC
# MAGIC python
# MAGIC IntegerType()
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ✅ Correct Code
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC from pyspark.sql.types import IntegerType
# MAGIC
# MAGIC spark.createDataFrame(years, IntegerType())
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚠️ **Important Note**
# MAGIC
# MAGIC - Spark allows passing a data type as schema for single-column DataFrames
# MAGIC - But it must be an instance, not the class itself
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ❌ Why Other Options Are Wrong
# MAGIC
# MAGIC | Option | Issue                                      |
# MAGIC |--------|--------------------------------------------|
# MAGIC | A      | ❌ Column name is optional (auto-generated) |
# MAGIC | B      | ❌ Wrapping not required                    |
# MAGIC | C      | ❌ createDataFrame exists                   |
# MAGIC | E      | ❌ Explicit schema is allowed and often preferred |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Exam Tip
# MAGIC
# MAGIC 👉 Always instantiate data types:
# MAGIC
# MAGIC python
# MAGIC IntegerType()   # ✅
# MAGIC StringType()    # ✅

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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔍 Correct Code
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC from pyspark.sql.functions import col, from_unixtime
# MAGIC
# MAGIC storesDF.withColumn(
# MAGIC     "openDateString",
# MAGIC     from_unixtime(col("openDate"), "EEEE, MMM d, yyyy h:mm a")
# MAGIC )
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC import org.apache.spark.sql.functions._
# MAGIC
# MAGIC storesDF.withColumn(
# MAGIC   "openDateString",
# MAGIC   from_unixtime(col("openDate"), "EEEE, MMM d, yyyy h:mm a")
# MAGIC )
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Why Option A is Correct
# MAGIC
# MAGIC - `withColumn()` → creates new column
# MAGIC - `from_unixtime()` → converts UNIX epoch → formatted string
# MAGIC
# MAGIC **Format:**
# MAGIC
# MAGIC
# MAGIC "EEEE, MMM d, yyyy h:mm a"
# MAGIC
# MAGIC
# MAGIC ✔ Matches Java SimpleDateFormat
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ❌ Why Other Options Are Wrong
# MAGIC
# MAGIC | Option | Issue                        |
# MAGIC |--------|------------------------------|
# MAGIC | B      | ❌ mmm should be MMM (case-sensitive) |
# MAGIC | C      | ❌ newColumn doesn’t exist    |
# MAGIC | D      | ❌ SimpleDateFormat is not passed like this |
# MAGIC | E      | ❌ Invalid format (dw)        |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Key Concept
# MAGIC
# MAGIC | Function         | Use                        |
# MAGIC |------------------|---------------------------|
# MAGIC | from_unixtime()  | Epoch → formatted string ✅|
# MAGIC | date_format()    | Works on timestamp, not raw integer |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Exam Tip
# MAGIC
# MAGIC 👉 Epoch (int) → string = from_unixtime()

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

# MAGIC %md
# MAGIC ✅ **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Correct Usage**
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC storesDF.join(employeesDF, on="storeId", how="left")
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC storesDF.join(employeesDF, Seq("storeId"), "left")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Why Option A is Correct**
# MAGIC
# MAGIC - `DataFrame.join()` is the standard method for all join types
# MAGIC - Supports:
# MAGIC   - `"inner"`
# MAGIC   - `"left"` ✅
# MAGIC   - `"right"`
# MAGIC   - `"outer"`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why Other Options Are Wrong**
# MAGIC
# MAGIC | Option | Issue                                      |
# MAGIC |--------|--------------------------------------------|
# MAGIC | B      | ❌ `crossJoin()` → Cartesian join, not left join |
# MAGIC | C      | ❌ `merge()` not a Spark DataFrame method   |
# MAGIC | D      | ❌ `leftJoin()` does not exist              |
# MAGIC | E      | ❌ No standalone `join()` function          |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip**
# MAGIC
# MAGIC 👉 All joins in Spark use:
# MAGIC
# MAGIC python
# MAGIC df.join(otherDF, condition, "joinType")

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

# MAGIC %md
# MAGIC ✅ **Correct Answer: E**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔍 Correct Code
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC storesDF.join(
# MAGIC     employeesDF,
# MAGIC     [
# MAGIC         storesDF.storeId == employeesDF.storeId,
# MAGIC         storesDF.employeeId == employeesDF.employeeId
# MAGIC     ]
# MAGIC )
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC storesDF.join(
# MAGIC   employeesDF,
# MAGIC   Seq(
# MAGIC     storesDF("storeId") === employeesDF("storeId"),
# MAGIC     storesDF("employeeId") === employeesDF("employeeId")
# MAGIC   )
# MAGIC )
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Why Option E is Correct
# MAGIC
# MAGIC Correctly matches:
# MAGIC - `storesDF.storeId == employeesDF.storeId`
# MAGIC - `storesDF.employeeId == employeesDF.employeeId`
# MAGIC
# MAGIC 👉 Ensures:
# MAGIC - Proper column disambiguation
# MAGIC - Correct join condition across two DataFrames
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ❌ Why Other Options Are Wrong
# MAGIC
# MAGIC | Option | Issue                                 |
# MAGIC |--------|---------------------------------------|
# MAGIC | A      | ❌ Compares columns within same DataFrame |
# MAGIC | B      | ❌ Ambiguous — no DataFrame reference  |
# MAGIC | C      | ❌ Invalid syntax                      |
# MAGIC | D      | ❌ Incorrect column pairing            |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Key Concept
# MAGIC
# MAGIC 👉 When joining on multiple columns:
# MAGIC - `df1.col == df2.col`
# MAGIC - ✔ Always specify DataFrame reference
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Exam Tip
# MAGIC
# MAGIC 👉 Use:
# MAGIC - `df1.colName == df2.colName`
# MAGIC - Avoid ambiguity with `col("colName")`

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

# MAGIC %md
# MAGIC ✅ **Correct Answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔍 Correct Code
# MAGIC
# MAGIC **🐍 PySpark**
# MAGIC python
# MAGIC storesDF.union(acquiredStoresDF)
# MAGIC
# MAGIC
# MAGIC **☕ Scala**
# MAGIC scala
# MAGIC storesDF.union(acquiredStoresDF)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Why Option C is Correct
# MAGIC
# MAGIC - `union()` performs a position-wise union
# MAGIC - Combines rows based on column order (not names)
# MAGIC
# MAGIC 👉 Exactly matches requirement:  
# MAGIC **position-wise union**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔄 Position-wise vs Name-wise
# MAGIC
# MAGIC | Method         | Behavior                       |
# MAGIC |----------------|-------------------------------|
# MAGIC | union()        | ✅ Matches columns by position |
# MAGIC | unionByName()  | ❌ Matches by column name      |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ❌ Why Other Options Are Wrong
# MAGIC
# MAGIC | Option | Issue                        |
# MAGIC |--------|------------------------------|
# MAGIC | A      | ❌ Not a valid static call    |
# MAGIC | B      | ❌ concat() not for DataFrames|
# MAGIC | D      | ❌ unionByName() is name-based|
# MAGIC | E      | ❌ unionAll() deprecated      |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🧠 Exam Tip
# MAGIC
# MAGIC 👉 Position-based → `union()`  
# MAGIC 👉 Name-based → `unionByName()`

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

# MAGIC %md
# MAGIC ---
# MAGIC
# MAGIC **The correct answer is:**
# MAGIC
# MAGIC **B.** `storesDF.write.mode("overwrite").text(filePath)`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC - `write` → returns a DataFrameWriter  
# MAGIC - `.mode("overwrite")` → ensures existing files are replaced  
# MAGIC - `.text(filePath)` → writes the DataFrame as text files to the given path  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are incorrect:**
# MAGIC
# MAGIC - **A** → Invalid syntax; `write()` does not take arguments like that  
# MAGIC - **C** → `.path()` is not a valid write method  
# MAGIC - **D** → Incorrect use of `.option()`  
# MAGIC - **E** → `write()` should not be called as a function with parentheses  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Final Correct Code:**
# MAGIC
# MAGIC python
# MAGIC storesDF.write.mode("overwrite").text(filePath)
# MAGIC
# MAGIC
# MAGIC ---

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

# MAGIC %md
# MAGIC ---
# MAGIC
# MAGIC **The correct answer is:**
# MAGIC
# MAGIC **A.** The schema operation from read takes a schema object rather than a string — the argument should be schema.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC - In PySpark, `.schema()` expects a StructType schema object, not a string.
# MAGIC - In the code:  
# MAGIC   `spark.read.schema("schema").format("json").load(filePath)`  
# MAGIC   `"schema"` is passed as a string, which is incorrect.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Correct Code:**
# MAGIC
# MAGIC python
# MAGIC spark.read.schema(schema).format("json").load(filePath)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are incorrect:**
# MAGIC
# MAGIC - **B** → `.load()` is valid and commonly used with `.format()`
# MAGIC - **C** → `spark.read` is a property, not a method (no parentheses needed)
# MAGIC - **D** → `spark.read` is valid in SparkSession
# MAGIC - **E** → `.schema()` expects a schema object, not a column
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key Point:**
# MAGIC
# MAGIC Always pass a defined schema object (StructType), not a string, to `.schema()`.
# MAGIC
# MAGIC ---

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

# MAGIC %md
# MAGIC
# MAGIC **The correct answer is:**
# MAGIC
# MAGIC **E. Executors are processing engine instances for performing data computations which run on a worker node.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC In Apache Spark:
# MAGIC
# MAGIC - Executors are JVM processes launched on worker nodes.
# MAGIC - They are responsible for:
# MAGIC   - Executing tasks
# MAGIC   - Storing data in memory or disk (caching)
# MAGIC   - Returning results to the driver
# MAGIC
# MAGIC So essentially, executors are the actual workers that perform computations.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A** → Describes communication, not executors
# MAGIC - **B** → The most granular unit is a task, not an executor
# MAGIC - **C** → A worker node can have multiple executors
# MAGIC - **D** → Executors run on worker nodes but are not the same
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key Point:**
# MAGIC
# MAGIC - Driver → coordinates
# MAGIC - Executors → execute tasks
# MAGIC - Tasks → smallest unit of work

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

# MAGIC %md
# MAGIC
# MAGIC **The correct answer is:**
# MAGIC
# MAGIC **A.**
# MAGIC
# MAGIC python
# MAGIC storesDF.filter((col("sqft") <= 25000) & (col("customerSatisfaction") >= 30))
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC - `.filter()` is the correct method to apply row-level conditions.
# MAGIC - In PySpark:
# MAGIC   - Use `&` for AND (not `and`)
# MAGIC   - Each condition must be wrapped in parentheses
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are incorrect:**
# MAGIC - **B** → Missing parentheses around the full condition (syntax error)
# MAGIC - **C** → Uses `and` instead of `&` (invalid in PySpark column expressions)
# MAGIC - **D** → `.drop()` removes columns, not rows
# MAGIC - **E** → Missing parentheses + uses `and` instead of `&`

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

# MAGIC %md
# MAGIC ---
# MAGIC **The correct code block to replace single quotes with double quotes in a PySpark DataFrame column is:**
# MAGIC
# MAGIC **C.**  
# MAGIC `storesDF.withColumn("storeSlogan", regexp_replace(col("storeSlogan"), "'", "\""))`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC - `withColumn("storeSlogan", ...)`: Updates or adds the column `"storeSlogan"`.
# MAGIC - `regexp_replace(col("storeSlogan"), "'", "\"")`:  
# MAGIC   - Column to process: `col("storeSlogan")`  
# MAGIC   - Pattern to match: `'` (single quote)  
# MAGIC   - Replacement string: `"` (double quote, escaped as `\"` in Python string literals, but commonly written as `"` in this context).
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Alternative:**  
# MAGIC `regexp_replace("storeSlogan", "'", "\"")` (Option D) can also work, but specifying the column using `col()` is generally preferred for clarity.  
# MAGIC However, based on typical Spark certification, `regexp_replace(col("storeSlogan"), "'", "\"")` is the standard syntax.
# MAGIC ---

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

# MAGIC %md
# MAGIC ---
# MAGIC **The correct answer is:**
# MAGIC
# MAGIC **B. DataFrame.withColumnRenamed()**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC - `withColumnRenamed(existingName, newName)` is used to rename an existing column in a DataFrame.
# MAGIC
# MAGIC ✔️ **Example:**
# MAGIC python
# MAGIC df = df.withColumnRenamed("oldColumnName", "newColumnName")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are incorrect:**
# MAGIC - **A** → `renamedColumn()` does not exist
# MAGIC - **C** → Typo (`wlthColumn`) and also not valid
# MAGIC - **D** → `col()` is used to reference a column, not rename it
# MAGIC - **E** → `newColumn()` does not exist
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key Point:**
# MAGIC - Use `withColumnRenamed()` specifically for renaming columns
# MAGIC - Use `withColumn()` if you want to create or replace column values
# MAGIC
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

# MAGIC %md
# MAGIC ---
# MAGIC **The correct answer is:**
# MAGIC
# MAGIC **D.**
# MAGIC
# MAGIC python
# MAGIC storesDF.printSchema()
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC - `printSchema()` is the correct method to display the schema of a DataFrame.
# MAGIC - It does not take any arguments, so we pass nothing.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are incorrect:**
# MAGIC - **A** → `.schema` returns the schema object but does not print it
# MAGIC - **B** → `.str` is not a valid DataFrame method
# MAGIC - **C** → `printSchema()` does not take `True`
# MAGIC - **E** → `"all"` is not a valid argument
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key Point:**
# MAGIC - Use `printSchema()` to print schema
# MAGIC - Use `.schema` only if you want to programmatically access it
# MAGIC
# MAGIC ---

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

# MAGIC %md
# MAGIC
# MAGIC **The correct answer is:**
# MAGIC
# MAGIC **E. The wrong SQL function is used to compute column result — it should be ASSESS_PERFORMANCE instead of assessPerformance.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC The UDF is registered with the name:
# MAGIC
# MAGIC `spark.udf.register("ASSESS_PERFORMANCE", assessPerformance)`
# MAGIC
# MAGIC When using it in SQL, you must call it using the registered name, not the Python function name.
# MAGIC
# MAGIC ✔️ **Correct SQL:**
# MAGIC sql
# MAGIC SELECT customerSatisfaction, ASSESS_PERFORMANCE(customerSatisfaction) AS result 
# MAGIC FROM stores
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are incorrect:**
# MAGIC - **A** → `spark.sql()` is valid for applying UDFs
# MAGIC - **B** → Argument order is correct: (name, function)
# MAGIC - **C** → You can reference a column multiple times
# MAGIC - **D** → UDFs can absolutely be used in SQL queries
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key Point:**
# MAGIC - Register name = SQL function name
# MAGIC - Python function name is not used in SQL

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

# MAGIC %md
# MAGIC ---
# MAGIC
# MAGIC **The correct answer is:**
# MAGIC
# MAGIC **D.**
# MAGIC
# MAGIC python
# MAGIC storesDF.persist(StorageLevel.MEMORY_ONLY).count()
# MAGIC
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC - `persist(StorageLevel.MEMORY_ONLY)` explicitly tells Spark to cache data only in memory.
# MAGIC - `.count()` is used to trigger execution, so caching actually happens.
# MAGIC
# MAGIC ❌ **Why others are incorrect:**
# MAGIC - **A** → `cache()` does not take arguments
# MAGIC - **B** → `persist()` defaults to MEMORY_AND_DISK, not memory-only
# MAGIC - **C** → `cache()` is equivalent to MEMORY_AND_DISK (not strictly memory-only)
# MAGIC - **E** → `persist()` expects a StorageLevel object, not a string
# MAGIC
# MAGIC 🔑 **Key Point:**
# MAGIC - Memory only → `persist(StorageLevel.MEMORY_ONLY)`
# MAGIC - Default cache → `cache()` or `persist()` = MEMORY_AND_DISK
# MAGIC
# MAGIC ---

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

# MAGIC %md
# MAGIC ---
# MAGIC **The correct answer is:**
# MAGIC
# MAGIC **C. storesDF.repartition()**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC - `repartition()` always triggers a shuffle to redistribute data evenly across partitions.
# MAGIC - It returns a new DataFrame with updated partitions.
# MAGIC
# MAGIC ❌ **Why others are incorrect:**
# MAGIC - **A** → `coalesce()` avoids shuffle (used to reduce partitions efficiently)
# MAGIC - **B** → `getNumPartitions()` only returns a number, no transformation
# MAGIC - **D** → `union()` combines DataFrames, not specifically for repartitioning
# MAGIC - **E** → `intersect()` filters common rows, not related to partition reshuffling
# MAGIC
# MAGIC 🔑 **Key Point:**
# MAGIC - `repartition()` → shuffle (always)
# MAGIC - `coalesce()` → no shuffle (usually)
# MAGIC
# MAGIC ---

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

# MAGIC %md
# MAGIC
# MAGIC **The correct answer is:**
# MAGIC
# MAGIC **D.**
# MAGIC
# MAGIC python
# MAGIC (storesDF.withColumn("openTimestamp", from_unixtime(col("openDate")))
# MAGIC  .withColumn("month", month(col("openTimestamp"))))
# MAGIC
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC - `openDate` is in UNIX epoch (seconds) → must be converted first
# MAGIC - `from_unixtime()` converts it to a timestamp
# MAGIC - `month()` extracts the month as an integer (1–12)
# MAGIC
# MAGIC ❌ **Why others are incorrect:**
# MAGIC - **A** → `getMonth()` is not a valid PySpark function
# MAGIC - **B** → `substr()` treats data as string, not proper date handling
# MAGIC - **C** → Direct cast from integer → date is invalid for UNIX epoch
# MAGIC - **E** → `date_part()` is not standard in PySpark
# MAGIC
# MAGIC 🔑 **Key Point:**
# MAGIC
# MAGIC For UNIX timestamps in PySpark:
# MAGIC - Convert using `from_unixtime()`
# MAGIC - Extract parts using functions like `month()`, `year()`, etc.

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

# MAGIC %md
# MAGIC ---
# MAGIC
# MAGIC **The correct answer is:**
# MAGIC
# MAGIC **E.**
# MAGIC
# MAGIC python
# MAGIC spark.read.load(filePath)
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC - `spark.read` → correct (DataFrameReader, no parentheses)
# MAGIC - `.load(filePath)` → valid method to read data
# MAGIC - Default format is Parquet, so this correctly reads a parquet file
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are incorrect:**
# MAGIC
# MAGIC - **A** → `read()` is invalid (should be `read`, not a method)
# MAGIC - **B** → same issue: `read()` is incorrect
# MAGIC - **C** → `load()` does not support source parameter
# MAGIC - **D** → `storesDF` is already a DataFrame, cannot be used to read
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key Point:**
# MAGIC
# MAGIC - Default behavior:  
# MAGIC   `spark.read.load(path)`  # assumes parquet
# MAGIC
# MAGIC - Explicit way:  
# MAGIC   `spark.read.format("parquet").load(path)`
# MAGIC
# MAGIC ---

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

# MAGIC %md
# MAGIC **The correct answer is:**
# MAGIC
# MAGIC **C. Transformations work on DataFrames/Datasets while actions are reserved for native language objects.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why this is incorrect:**
# MAGIC - Both transformations and actions operate on DataFrames/Datasets
# MAGIC - Actions are not reserved for native language objects
# MAGIC - Actions simply trigger execution and may optionally return results (e.g., `collect()` returns data to driver)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Why other options are correct:**
# MAGIC - **A** → Correct: only transformations are categorized as wide/narrow
# MAGIC - **B** → Correct: transformations are lazy, actions trigger execution
# MAGIC - **D** → Correct: actions like `collect()` return native objects (e.g., list in Python)
# MAGIC - **E** → Correct: transformations = logic, actions = results
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key Point:**
# MAGIC - Transformations → Lazy, build execution plan
# MAGIC - Actions → Execute and return results

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

# MAGIC %md
# MAGIC
# MAGIC **The correct answer is:**
# MAGIC
# MAGIC **C. Spark jobs will fail or run slowly if memory is not available for new objects to be created.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC - Garbage Collection (GC) in Spark manages JVM memory by removing unused objects.
# MAGIC - If GC doesn’t free memory:
# MAGIC   - New objects cannot be created
# MAGIC   - Memory pressure increases
# MAGIC   - This leads to slow performance or job failure (OutOfMemory errors)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are incorrect:**
# MAGIC - **A** → GC is about memory, not data correctness
# MAGIC - **B** → “Inaccurate data” is unrelated to GC
# MAGIC - **D** → Too many transformations affects lineage, not GC directly
# MAGIC - **E** → Memory issues affect performance/failure, not result accuracy
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key Point:**
# MAGIC - GC is critical for memory management, not correctness
# MAGIC - Poor GC → slow jobs, frequent pauses, or crashes

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

# MAGIC %md
# MAGIC ---
# MAGIC **The correct answer is:**
# MAGIC
# MAGIC **A.**
# MAGIC
# MAGIC python
# MAGIC storesDF.withColumn("managerNameLength", length(col("managerName")))
# MAGIC
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC - `length()` is the correct PySpark function to get the number of characters in a string column
# MAGIC - `col("managerName")` correctly references the column
# MAGIC - `withColumn()` creates a new column or replaces an existing one
# MAGIC
# MAGIC ❌ **Why others are incorrect:**
# MAGIC - **B** → `"managerName"` is treated as a string literal, not a column
# MAGIC - **C** → `.length()` is not a valid method on a Column object
# MAGIC - **D** → `stringLength()` does not exist in PySpark
# MAGIC - **E** → `managerName` is not defined as a variable (should use `col()`)
# MAGIC
# MAGIC 🔑 **Key Point:**
# MAGIC - Always use `col("columnName")` to reference columns
# MAGIC - Built-in functions like `length()` for transformations
# MAGIC ---

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

# MAGIC %md
# MAGIC ---
# MAGIC **The correct answer is:**
# MAGIC
# MAGIC **D.**
# MAGIC
# MAGIC python
# MAGIC storesDF.na.drop("all")
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC - `.na.drop("all")` removes rows only when all columns are null
# MAGIC - This matches the requirement: “missing values in every column”
# MAGIC
# MAGIC ❌ **Why others are incorrect:**
# MAGIC - **A** → Drops rows if any column has null (default = "any")
# MAGIC - **B** → Same as A (`dropna()` defaults to "any")
# MAGIC - **C** → Applies condition only to a specific column (subset)
# MAGIC - **E** → Invalid method (`nadrop` does not exist)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key Point:**
# MAGIC - `"any"` → drop if any column is null
# MAGIC - `"all"` → drop only if all columns are null
# MAGIC
# MAGIC ---

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

# MAGIC %md
# MAGIC ---
# MAGIC **The correct answer is:**
# MAGIC
# MAGIC **D. The default argument to the how parameter is "inner" – an additional argument of "left" must be specified.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC
# MAGIC The given code:
# MAGIC
# MAGIC `storesDF.join(employeesDF, "storeId")`
# MAGIC
# MAGIC performs an **INNER JOIN** by default.
# MAGIC
# MAGIC But the requirement is a **LEFT JOIN**, so we must explicitly specify:
# MAGIC
# MAGIC `storesDF.join(employeesDF, "storeId", "left")`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are incorrect:**
# MAGIC
# MAGIC - **A** → Passing "storeId" as a string is valid (no need for list)
# MAGIC - **B** → `col()` is not required when passing column name as string
# MAGIC - **C** → `DataFrame.join()` is valid in Spark
# MAGIC - **E** → Expression syntax is optional; string column name works fine
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key Point:**
# MAGIC
# MAGIC - Default join = inner
# MAGIC - Always specify "left" (or other types) when required
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Correct version:**
# MAGIC
# MAGIC `storesDF.join(employeesDF, "storeId", "left")`
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

# MAGIC %md
# MAGIC ---
# MAGIC
# MAGIC **The correct answer is:**
# MAGIC
# MAGIC **D. The split() operation does not accomplish the requested task. The explode() operation should be used instead.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Explanation:**
# MAGIC - The goal is to:
# MAGIC   - Split a column with multiple values (e.g., "A,B,C")
# MAGIC   - Create multiple rows (one value per row)
# MAGIC - `split()` only converts a string into an array, but does not increase rows
# MAGIC - To create multiple rows, you must use `explode()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Correct Code:**
# MAGIC python
# MAGIC from pyspark.sql.functions import split, explode, col
# MAGIC
# MAGIC storesDF.withColumn(
# MAGIC     "productCategories",
# MAGIC     explode(split(col("productCategories"), ","))
# MAGIC )
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are incorrect:**
# MAGIC - **A** → Alias is unrelated to row expansion
# MAGIC - **B** → `broadcast()` is for joins, not splitting rows
# MAGIC - **C** → `split()` usage is fine, but insufficient alone
# MAGIC - **E** → `array_distinct()` removes duplicates, not expand rows
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key Point:**
# MAGIC - `split()` → string → array
# MAGIC - `explode()` → array → multiple rows
# MAGIC
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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct answer: A**
# MAGIC
# MAGIC **Why A is the best choice (exam-intended)**  
# MAGIC `storesDF.withColumn("managerFirstName", split(col("managerName"), " ")[0]) \
# MAGIC         .withColumn("managerLastName", split(col("managerName"), " ")[1])`  
# MAGIC It correctly uses:  
# MAGIC - `split(col("managerName"), " ")` ✔️ (valid PySpark function)  
# MAGIC It attempts to extract:  
# MAGIC - first name → `[0]`  
# MAGIC - last name → `[1]`  
# MAGIC
# MAGIC Even though the indexing style is not the best practice in PySpark, this is the only option using correct split syntax, so it is the expected answer in most certification exams.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚠️ **Important correction (real PySpark best practice)**
# MAGIC
# MAGIC In actual PySpark, you should NOT use `[0]` like this. Instead:
# MAGIC
# MAGIC python
# MAGIC from pyspark.sql.functions import split, col
# MAGIC
# MAGIC storesDF.withColumn("managerFirstName", split(col("managerName"), " ").getItem(0)) \
# MAGIC         .withColumn("managerLastName", split(col("managerName"), " ").getItem(1))
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong**  
# MAGIC - B, D → `col("managerName").split()` ❌ invalid API  
# MAGIC - C → wrong indexing + wrong positions  
# MAGIC - E → incorrect `split()` syntax  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 📌 **Final takeaway**  
# MAGIC - Exam answer: **A**  
# MAGIC - Real-world Spark: use `.getItem()` instead of `[ ]`

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

# MAGIC %md
# MAGIC The key idea here is fault tolerance in Spark depends on having multiple worker nodes. If a node fails, Spark can recompute lost tasks only if other nodes are available.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Let’s break it down:**
# MAGIC
# MAGIC - **Scenario #1** → ❌ Only 1 worker node  
# MAGIC   - If that node fails → entire cluster is gone  
# MAGIC   - No executors left to recompute tasks  
# MAGIC   - 👉 Application cannot complete
# MAGIC
# MAGIC - **Scenario #4, #5, #6** → ✅ Multiple worker nodes  
# MAGIC   - If one node fails → others still run tasks  
# MAGIC   - Spark recomputes lost partitions using lineage  
# MAGIC   - 👉 Application can still complete
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC Option E is incorrect because Spark is fault-tolerant only when there are redundant resources (multiple nodes)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **✅ Final Answer:**  
# MAGIC **D. Scenario #1**

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

# MAGIC %md
# MAGIC ---
# MAGIC **Correct answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Why A is correct:**
# MAGIC
# MAGIC `storesDF.na.fill("No Manager", "managerName")`
# MAGIC
# MAGIC In PySpark:
# MAGIC
# MAGIC - `na.fill()` is the correct API for handling missing (null) values.
# MAGIC - You can specify:
# MAGIC   - a value → `"No Manager"`
# MAGIC   - a column name → `"managerName"`
# MAGIC
# MAGIC So this replaces nulls only in `managerName`.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Why others are wrong:**
# MAGIC
# MAGIC - **B.** `storesDF.nafill(...)` ❌  
# MAGIC   → Method does not exist (`nafill` is invalid)
# MAGIC
# MAGIC - **C.** `storesDF.na.fill("No Manager", col("managerName"))` ❌  
# MAGIC   → `na.fill()` does not accept Column objects, only string column names or subset list
# MAGIC
# MAGIC - **D.** `storesDF.fillna("No Manager", col("managerName"))` ❌  
# MAGIC   → Same issue: `fillna` expects string or dict, not `col()`
# MAGIC
# MAGIC - **E.** `storesDF.nafill(...)` ❌  
# MAGIC   → Invalid method again
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

# MAGIC %md
# MAGIC ✅ **Correct answer: B. storesDF.printSchema()**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Why B is correct:**
# MAGIC - `storesDF.printSchema()`
# MAGIC - This is the standard PySpark method to display the DataFrame schema.
# MAGIC - It prints a tree-like structure showing column names, types, and nullability.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why the others are wrong:**
# MAGIC - **A.** `print(storesDF)`  
# MAGIC   → Prints object reference, not schema
# MAGIC
# MAGIC - **C.** `storesDF.schema()`  
# MAGIC   → ❌ schema is not a function
# MAGIC
# MAGIC - **D.** `storesDF.schema`  
# MAGIC   → Returns schema object, but does not print it
# MAGIC
# MAGIC - **E.** `storesDF.schema()`  
# MAGIC   → ❌ invalid (same issue as C)

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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct answer: D**
# MAGIC
# MAGIC python
# MAGIC storesDF.filter((col("sqft") <= 25000) & (col("customerSatisfaction") >= 30))
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Why D is correct:**
# MAGIC
# MAGIC - PySpark uses bitwise operators for column conditions:
# MAGIC   - `&` = AND
# MAGIC   - `|` = OR
# MAGIC - Each condition must be wrapped in parentheses:
# MAGIC   - `(col("sqft") <= 25000) & (col("customerSatisfaction") >= 30)`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A ❌**
# MAGIC   - `col("sqft") <= 25000 and col("customerSatisfaction") >= 30`
# MAGIC   - Python `and` cannot be used with PySpark Column objects
# MAGIC
# MAGIC - **B ❌**
# MAGIC   - Missing parentheses → operator precedence error
# MAGIC
# MAGIC - **C ❌**
# MAGIC   - Uses `or` instead of required AND condition
# MAGIC
# MAGIC - **E ❌**
# MAGIC   - Columns not referenced using `col()`
# MAGIC   - Also invalid Python syntax in DataFrame context

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

# MAGIC %md
# MAGIC
# MAGIC ❌ **Incorrect statement:**  
# MAGIC **A. Spark DataFrames are the same as a data frame in Python or R.** ❌  
# MAGIC → This is incorrect.  
# MAGIC Spark DataFrames are similar in concept, but not the same.
# MAGIC
# MAGIC **Key differences:**  
# MAGIC - Spark DataFrames are distributed across a cluster  
# MAGIC - They are lazy-evaluated  
# MAGIC - Built for big data processing, unlike local Pandas/R data frames  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Why others are correct:**  
# MAGIC - **B. Built on top of RDDs** ✔️  
# MAGIC   → Spark DataFrames internally rely on RDDs  
# MAGIC - **C. Immutable** ✔️  
# MAGIC   → You cannot modify a DataFrame directly; transformations create new ones  
# MAGIC - **D. Distributed** ✔️  
# MAGIC   → Data is spread across multiple nodes in a cluster  
# MAGIC - **E. Have Structured APIs** ✔️  
# MAGIC   → Support SQL, DataFrame, and Dataset APIs  
# MAGIC **Final Answer: A**

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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct answer: B**  
# MAGIC `storesDF.coalesce(4)`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Why this is correct:**  
# MAGIC - `coalesce(n)` is used to reduce the number of partitions  
# MAGIC - It does **NOT** cause a shuffle (unlike `repartition`)  
# MAGIC - Since we want to go from 8 → 4 partitions, this is the correct method
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**  
# MAGIC - **A.** `coalesce()` with no argument ❌  
# MAGIC   → Missing required number of partitions  
# MAGIC - **C.** `coalesce(4, "storeId")` ❌  
# MAGIC   → `coalesce` does not accept column arguments  
# MAGIC - **D.** `coalesce("storeId")` ❌  
# MAGIC   → Invalid parameter (expects integer, not column name)

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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC `storesDF.join(employeesDF, "storeId")`
# MAGIC
# MAGIC This code does not produce an outer join.
# MAGIC
# MAGIC By default, PySpark `join()` uses:
# MAGIC
# MAGIC - `how = "inner"`
# MAGIC
# MAGIC So the error is that the join type is missing.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct version:**
# MAGIC
# MAGIC `storesDF.join(employeesDF, "storeId", "outer")`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are wrong:**
# MAGIC
# MAGIC - **B ❌**
# MAGIC   - You can pass column name as a string; `col()` is not required
# MAGIC
# MAGIC - **C ❌**
# MAGIC   - This is optional syntax, not required when using column name directly
# MAGIC
# MAGIC - **D ❌**
# MAGIC   - List is optional; string works fine
# MAGIC
# MAGIC - **E ❌**
# MAGIC   - `DataFrame.join()` is valid in PySpark (`merge()` is Pandas)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🟢 **Final Answer: A**

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

# MAGIC %md
# MAGIC ---
# MAGIC **Correct answer: D. `storesDF.agg(mean(col("sqft")).alias("sqftMean"))`**
# MAGIC
# MAGIC This code block successfully calculates the mean of a column and renames it using standard Apache Spark DataFrame aggregation methods.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Why Option D is Correct ✅
# MAGIC
# MAGIC - **Methodology:** The `agg()` function is the standard way to perform aggregate calculations on a whole PySpark DataFrame.
# MAGIC - **Expression:** `mean(col("sqft"))` correctly uses the `pyspark.sql.functions.mean` function on a column object.
# MAGIC - **Aliasing:** The `.alias("sqftMean")` method correctly renames the resulting aggregate column from its default (typically `avg(sqft)`) to the requested name.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Why Other Options are Incorrect ❌
# MAGIC
# MAGIC - **Option A:** `withColumn` requires a string name for the new column as the first argument; it cannot take an aliased column expression as its sole argument.
# MAGIC - **Option B:** While Spark has a `mean` function, it is not a method of the Column object (e.g., `col("sqft").mean()` is invalid).
# MAGIC - **Option C:** While some Spark versions allow strings in aggregate functions, standard exam contexts often consider `mean("sqft")` incorrect because the function strictly expects a Column object created via `col()`.
# MAGIC - **Option E:** `withColumn("sqftMean", mean(col("sqft")))` is technically incorrect for a simple aggregate because `mean` is an aggregate function. Using it in `withColumn` without a window function would typically result in an error or unexpected behavior, as `withColumn` is intended for row-wise transformations rather than summary aggregations.
# MAGIC
# MAGIC ---

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

# MAGIC %md
# MAGIC ✅ **Correct answer: B. RDDs**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC - RDDs (Resilient Distributed Datasets) are the core abstraction in Apache Spark that enable:
# MAGIC   - Distributed data processing
# MAGIC   - Parallel execution across cluster nodes
# MAGIC - Spark DataFrames are actually built on top of RDDs, so they inherit this parallelism capability.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A. Delta Tables** ❌  
# MAGIC   → Storage layer feature (ACID transactions), not responsible for parallel execution
# MAGIC
# MAGIC - **C. Multiprocessing** ❌  
# MAGIC   → Python concept, not how Spark achieves distributed execution
# MAGIC
# MAGIC - **D. Multithreading** ❌  
# MAGIC   → Local parallelism, not cluster-level distributed execution used by Spark
# MAGIC
# MAGIC - **E. Vectors** ❌  
# MAGIC   → Data structure, unrelated to execution model

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

# MAGIC %md
# MAGIC
# MAGIC ❌ **Incorrect (ineffective) strategy:** **C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC **C. Use fewer transformations and more actions** ❌  
# MAGIC → This is ineffective and misleading  
# MAGIC In Spark, actions trigger execution, which can increase memory pressure and GC overhead  
# MAGIC The goal is usually to optimize transformations, not arbitrarily increase actions  
# MAGIC More actions can actually worsen performance and GC behavior
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Why others are effective:**
# MAGIC
# MAGIC - **A. Use G1GC** ✔️  
# MAGIC   → Helps reduce GC pause times
# MAGIC
# MAGIC - **B. Use Structured APIs** ✔️  
# MAGIC   → Optimized execution (Catalyst + Tungsten) reduces memory usage
# MAGIC
# MAGIC - **D. Check GC frequency** ✔️  
# MAGIC   → Essential for diagnosing GC issues
# MAGIC
# MAGIC - **E. Allow more memory** ✔️  
# MAGIC   → Reduces frequency of major GC cycles
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🟢 **Final Answer: C**

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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct answer: E. 1, 4**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **✔️ Step-by-step reasoning:**
# MAGIC
# MAGIC We are given:
# MAGIC
# MAGIC - openDate is an integer (UNIX epoch time)
# MAGIC - We need to compute day of year
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **✅ Correct sequence:**
# MAGIC
# MAGIC **Step 1:** Convert UNIX integer → Timestamp  
# MAGIC `storesDF.withColumn("openTimestamp", col("openDate").cast("Timestamp"))`
# MAGIC
# MAGIC **Step 2:** Extract day of year  
# MAGIC `storesDF.withColumn("dayOfYear", dayofyear(col("openTimestamp")))`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **✔️ Why this works:**
# MAGIC
# MAGIC - `dayofyear()` requires a date or timestamp column
# MAGIC - Since openDate is an integer, it must first be converted
# MAGIC - Casting to Timestamp is the correct approach for UNIX epoch values
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **❌ Why others are wrong:**
# MAGIC
# MAGIC - **2 ❌**  
# MAGIC   → Uses openDate directly (still integer)
# MAGIC
# MAGIC - **3, 5 ❌**  
# MAGIC   → Casting directly to Date from integer is not appropriate for UNIX epoch
# MAGIC
# MAGIC - **6 ❌**  
# MAGIC   → get_dayofyear is not a valid PySpark function

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

# MAGIC %md
# MAGIC ✅ **Correct answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC **A. A task is the smallest unit of work that can fit on a single executor.** ✔️  
# MAGIC → This is the correct definition  
# MAGIC In Spark, a task operates on a single partition  
# MAGIC Each task runs on one executor core  
# MAGIC It is the smallest unit of execution
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **B ❌**  
# MAGIC   → Describes executor resources (slots/cores), not a task
# MAGIC
# MAGIC - **C ❌**  
# MAGIC   → Tasks can exist before and after shuffles; shuffle does not define task boundaries
# MAGIC
# MAGIC - **D ❌**  
# MAGIC   → Task is the finest (smallest) level, not the most coarse
# MAGIC
# MAGIC - **E ❌**  
# MAGIC   → Partially descriptive but not the standard definition; wording is inaccurate

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

# MAGIC %md
# MAGIC
# MAGIC ❌ **Correct answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC We are asked which code block fails to sort alphabetically (ascending).
# MAGIC
# MAGIC **Alphabetical order = ascending order**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Option analysis:**
# MAGIC
# MAGIC - **A. `storesDF.sort(asc("division"))`** ✔️  
# MAGIC   → Explicit ascending sort → correct
# MAGIC
# MAGIC - **B. `storesDF.orderBy(["division"], ascending = [1])`** ✔️  
# MAGIC   → 1 means ascending → correct
# MAGIC
# MAGIC - **C. `storesDF.orderBy(col("division").desc())`** ❌  
# MAGIC   → Sorts in descending order, not alphabetical (ascending) → fails
# MAGIC
# MAGIC - **D. `storesDF.orderBy("division")`** ✔️  
# MAGIC   → Default is ascending → correct
# MAGIC
# MAGIC - **E. `storesDF.sort("division")`** ✔️  
# MAGIC   → Default ascending → correct

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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC **A. Spark jobs can be better optimized because all of the transformations in the job are visible prior to evaluation** ✔️  
# MAGIC → This is the key advantage of lazy evaluation in Spark  
# MAGIC - Transformations are not executed immediately  
# MAGIC - Spark builds a logical plan (DAG)  
# MAGIC - The optimizer (Catalyst Optimizer) can:  
# MAGIC   - Reorder operations  
# MAGIC   - Eliminate unnecessary steps  
# MAGIC   - Combine transformations  
# MAGIC → **Result:** more efficient execution
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **B ❌**  
# MAGIC   → Jobs still execute all operations when an action is called
# MAGIC
# MAGIC - **C ❌**  
# MAGIC   → Lazy evaluation does not reduce task distribution like this
# MAGIC
# MAGIC - **D ❌**  
# MAGIC   → Lazy evaluation does not inherently reduce failure probability
# MAGIC
# MAGIC - **E ❌**  
# MAGIC   → Spark actually tries to minimize communication, not increase it

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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct answer: D**  
# MAGIC `storesDF.distinct()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**  
# MAGIC - `distinct()` returns a new DataFrame with only unique rows  
# MAGIC - It removes all duplicate records across all columns  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**  
# MAGIC - **A. getDistinct()** ❌  
# MAGIC   → Not a valid PySpark method  
# MAGIC - **B. duplicates.drop()** ❌  
# MAGIC   → Invalid syntax / method does not exist  
# MAGIC - **C. removeDuplicates()** ❌  
# MAGIC   → Not a valid method (correct one is `dropDuplicates()`)  
# MAGIC - **E. duplicates()** ❌  
# MAGIC   → Not a valid method

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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC In PySpark, you can sort a DataFrame using both:
# MAGIC
# MAGIC - `storesDF.sort("columnName")`
# MAGIC - `storesDF.orderBy("columnName")`
# MAGIC
# MAGIC `sort()` and `orderBy()` are functionally equivalent.  
# MAGIC Both return a new DataFrame sorted by specified columns.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **B. orderBy()** ❌  
# MAGIC   → Correct, but not complete (question asks all valid operations)
# MAGIC
# MAGIC - **C. sort()** ❌  
# MAGIC   → Same issue, incomplete
# MAGIC
# MAGIC - **D. orderby()** ❌  
# MAGIC   → Incorrect casing (PySpark is case-sensitive)
# MAGIC
# MAGIC - **E. orderby()** ❌  
# MAGIC   → Invalid method name

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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC **DataFrame.collect()** ✔️  
# MAGIC → Returns all rows from the DataFrame to the driver as a list  
# MAGIC → This is the only option that retrieves the entire dataset  
# MAGIC `storesDF.collect()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A. count()** ❌  
# MAGIC   → Returns only the number of rows, not the data
# MAGIC
# MAGIC - **B. head()** ❌  
# MAGIC   → Returns only the first row (or few rows if specified)
# MAGIC
# MAGIC - **D. show()** ❌  
# MAGIC   → Displays rows but does not return them
# MAGIC
# MAGIC - **E. take()** ❌  
# MAGIC   → Returns only a limited number of rows
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚠️ **Note:**  
# MAGIC collect() should be used carefully on large DataFrames  
# MAGIC → It can cause memory issues on the driver

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

# MAGIC %md
# MAGIC ✅ **Correct answer: A**  
# MAGIC `storesDF.withColumn("numberOfManagers", lit(1))`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**  
# MAGIC - `withColumn()` → used to add or replace a column  
# MAGIC - `"numberOfManagers"` → new column name  
# MAGIC - `lit(1)` → creates a constant column with integer value 1  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**  
# MAGIC - **B. IntegerType** ❌  
# MAGIC   → Used for schema definition, not for assigning values  
# MAGIC - **C. newColumn** ❌  
# MAGIC   → Not a valid DataFrame method  
# MAGIC - **D. col(1)** ❌  
# MAGIC   → col() expects a column name, not a literal value  
# MAGIC - **E. lit("1")** ❌  
# MAGIC   → Creates a string, not an integer

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

# MAGIC %md
# MAGIC ---
# MAGIC
# MAGIC ❌ **Incorrect statement:** **E**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC - **E. There is a single node that contains the Spark driver and the executors.** ❌  
# MAGIC   → This describes local mode, not cluster mode  
# MAGIC   → In cluster mode, the driver and executors run on different nodes  
# MAGIC   → Execution is distributed across multiple machines
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Why others are correct:**
# MAGIC
# MAGIC - **A. Driver runs on its own node** ✔️  
# MAGIC   → In cluster mode, driver runs separately from executors
# MAGIC
# MAGIC - **B. Executors run inside worker nodes** ✔️  
# MAGIC   → Each executor is a process on a worker node
# MAGIC
# MAGIC - **C. Executors vs nodes count can vary** ✔️  
# MAGIC   → Multiple executors can run on one node or across many nodes
# MAGIC
# MAGIC - **D. Always more than one node** ✔️  
# MAGIC   → Cluster mode implies distributed setup (multiple nodes)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🟢 **Final Answer:** **E**

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

# MAGIC %md
# MAGIC
# MAGIC ❌ **Correct answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC We need to find which code fails to perform a valid inner join on two columns.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Option analysis:**
# MAGIC
# MAGIC **A. storesDF.join(employeesDF, [col("storeId"), col("employeeId")])** ❌  
# MAGIC → Incorrect usage  
# MAGIC Passing a list of col() objects without join conditions is invalid  
# MAGIC Spark expects either:  
# MAGIC - column names as strings → `["storeId", "employeeId"]`  
# MAGIC - or boolean conditions → `storesDF.storeId == employeesDF.storeId`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Why others are correct:**
# MAGIC
# MAGIC - **B** ✔️  
# MAGIC   → Proper join conditions using equality expressions
# MAGIC
# MAGIC - **C** ✔️  
# MAGIC   → Correct: list of column names
# MAGIC
# MAGIC - **D** ✔️  
# MAGIC   → Correct with aliases and explicit conditions
# MAGIC
# MAGIC - **E** ✔️  
# MAGIC   → Correct with explicit "inner" join (default anyway)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🟢 **Final Answer: A**

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

# MAGIC %md
# MAGIC ✅ **Correct answer: D**  
# MAGIC `employeesDF.join(broadcast(storesDF), "storeId")`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**  
# MAGIC In a broadcast join, you should broadcast the smaller DataFrame.  
# MAGIC Here:  
# MAGIC - `storesDF` = smaller  
# MAGIC - `employeesDF` = much larger  
# MAGIC
# MAGIC So we broadcast `storesDF`:  
# MAGIC `broadcast(storesDF)`  
# MAGIC and join it with the larger DataFrame.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**  
# MAGIC - **A** ❌  
# MAGIC   → Broadcasting the larger DataFrame (`employeesDF`) → inefficient  
# MAGIC - **B** ❌  
# MAGIC   → Invalid syntax; `broadcast()` is not used this way  
# MAGIC - **C** ❌  
# MAGIC   → Broadcasting result of join → incorrect usage  
# MAGIC - **E** ❌  
# MAGIC   → `broadcastJoin()` is not a valid PySpark method

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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct answer: E**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC Both of the following can be used to fill missing values in a specific column:
# MAGIC
# MAGIC - `storesDF.na.fill("value", ["columnName"])`
# MAGIC - `storesDF.fillna("value", subset=["columnName"])`
# MAGIC
# MAGIC - `na.fill()` → part of the DataFrameNaFunctions  
# MAGIC - `fillna()` → convenience method on DataFrame
# MAGIC
# MAGIC Both support:
# MAGIC - specifying a value
# MAGIC - targeting specific columns
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A ❌**  
# MAGIC   → Correct but incomplete (not the only method)
# MAGIC
# MAGIC - **B ❌**  
# MAGIC   → nafill() is not a valid method
# MAGIC
# MAGIC - **C ❌**  
# MAGIC   → Correct but incomplete
# MAGIC
# MAGIC - **D ❌**  
# MAGIC   → Includes invalid method nafill()

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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct answer: D**  
# MAGIC `storesDF.orderBy(col("sqft").asc_nulls_first())`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC **Requirement:**  
# MAGIC - Ascending order  
# MAGIC - Missing values first  
# MAGIC
# MAGIC `asc_nulls_first()` does exactly that:  
# MAGIC - Sorts in ascending order  
# MAGIC - Places null values at the top  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A. asc_nulls_last()** ❌  
# MAGIC   → Puts nulls at the end
# MAGIC
# MAGIC - **B. asc_nulls_first(col("sqft"))** ❌  
# MAGIC   → Invalid syntax (not a standalone function like this)
# MAGIC
# MAGIC - **C. "sqft".asc().nulls_first()** ❌  
# MAGIC   → String does not support .asc()
# MAGIC
# MAGIC - **E. col("sqft").nulls_first()** ❌  
# MAGIC   → Missing .asc() or .desc() → incomplete sort definition

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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC **C. Local mode** ✔️  
# MAGIC → All execution happens on a single machine (single node)  
# MAGIC → There is:  
# MAGIC - One JVM  
# MAGIC - Driver and executors running locally  
# MAGIC → Effectively, all “executors” are on the same node
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A. Standard mode** ❌  
# MAGIC   → Not an official Spark deployment mode
# MAGIC
# MAGIC - **B. Cluster mode** ❌  
# MAGIC   → Executors run across multiple worker nodes
# MAGIC
# MAGIC - **D. All of these** ❌  
# MAGIC   → Incorrect since only local mode fits
# MAGIC
# MAGIC - **E. Client mode** ❌  
# MAGIC   → Driver runs locally, but executors run on cluster nodes

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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC `spark.read.schema("schema").csv(filePath)`
# MAGIC
# MAGIC The error is:  
# MAGIC "schema" is passed as a string  
# MAGIC But `.schema()` expects a StructType schema object, not a string
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct version:**
# MAGIC
# MAGIC `spark.read.schema(schema).csv(filePath)`
# MAGIC
# MAGIC Here, `schema` is a predefined StructType object
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **B ❌**  
# MAGIC   → `.csv()` is a valid method of DataFrameReader
# MAGIC
# MAGIC - **C ❌**  
# MAGIC   → `spark.read` is correct
# MAGIC
# MAGIC - **D ❌**  
# MAGIC   → `.schema()` does not take a `col()` object
# MAGIC
# MAGIC - **E ❌**  
# MAGIC   → `spark.read` is a property, not a function

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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct answer: A**
# MAGIC
# MAGIC python
# MAGIC assessPerformanceUDF = udf(assessPerformance)
# MAGIC storesDF.withColumn("result", assessPerformanceUDF(col("customerSatisfaction")))
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC - `udf(assessPerformance)` → wraps the Python function into a Spark UDF  
# MAGIC - `withColumn()` → used to add a new column (`result`)  
# MAGIC - `col("customerSatisfaction")` → correctly references the input column  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **B & C** ❌  
# MAGIC   → Function name passed as string, not callable
# MAGIC
# MAGIC - **D** ❌  
# MAGIC   → `select` would not preserve all existing columns (question implies adding column)
# MAGIC
# MAGIC - **E** ❌  
# MAGIC   → `"customerSatisfaction"` passed as string instead of `col()` inside UDF

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
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct answer: D**  
# MAGIC `storesDF.write.text(filePath)`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC - `write` is a DataFrameWriter property, not a function  
# MAGIC - `.text(path)` is the correct method to write data as text files
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A. storesDF.write(filePath)** ❌  
# MAGIC   → write is not callable
# MAGIC
# MAGIC - **B. storesDF.write.path(filePath)** ❌  
# MAGIC   → path() is not used this way
# MAGIC
# MAGIC - **C. storesDF.write().text(filePath)** ❌  
# MAGIC   → write should not have parentheses
# MAGIC
# MAGIC - **E. storesDF.write.option("text").path(filePath)** ❌  
# MAGIC   → Incorrect usage; format should be specified via .text() or .format("text")
# MAGIC
# MAGIC ---

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
# MAGIC
# MAGIC ✅ **Correct answer: C**  
# MAGIC `storesDF.withColumn("managerName", upper(col("managerName")))`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**  
# MAGIC - `withColumn()` → used to modify or replace a column  
# MAGIC - `upper()` → PySpark function to convert text to uppercase  
# MAGIC - `col("managerName")` → correctly references the column  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**  
# MAGIC - **A. upper(managerName)** ❌  
# MAGIC   → Column not referenced using `col()`  
# MAGIC - **B. toupper()** ❌  
# MAGIC   → Not a valid PySpark function  
# MAGIC - **D. col(...).upper()** ❌  
# MAGIC   → Column object does not have `.upper()` method  
# MAGIC - **E. upper("managerName")** ❌  
# MAGIC   → Treats column name as a string literal, not a column

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
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct answer: B**  
# MAGIC (storesDF  
# MAGIC &nbsp;&nbsp;.withColumn("openTimestamp", col("openDate").cast("Timestamp"))  
# MAGIC &nbsp;&nbsp;.withColumn("month", month(col("openTimestamp")))  
# MAGIC )
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**  
# MAGIC openDate is in UNIX epoch (integer) format  
# MAGIC Functions like month() require a date or timestamp column  
# MAGIC So the correct steps are:  
# MAGIC - Convert integer → Timestamp  
# MAGIC - Extract month using month()
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**  
# MAGIC - **A. getMonth()** ❌  
# MAGIC   → Not a valid PySpark function  
# MAGIC - **C. month(col("openDate"))** ❌  
# MAGIC   → Cannot apply directly on integer  
# MAGIC - **D. substr()** ❌  
# MAGIC   → Works on strings, not epoch integers  
# MAGIC - **E. cast to Date** ⚠️  
# MAGIC   → Direct cast from integer to Date is not reliable for UNIX epoch
# MAGIC
# MAGIC ---

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
# MAGIC
# MAGIC ✅ **Correct answer: C**  
# MAGIC `storesDF.join(employeesDF, "storeId", "left")`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC **Syntax of join():**  
# MAGIC `DataFrame.join(other, on=None, how=None)`  
# MAGIC - `"storeId"` → join key  
# MAGIC - `"left"` → specifies left join
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A. join(employeesDF, "left", col("storeId"))** ❌  
# MAGIC   → Incorrect order of arguments
# MAGIC
# MAGIC - **B. join(employeesDF, "storeId")** ❌  
# MAGIC   → Defaults to inner join, not left
# MAGIC
# MAGIC - **D. merge()** ❌  
# MAGIC   → Not a valid PySpark DataFrame method
# MAGIC
# MAGIC - **E. join(employeesDF, "left", condition)** ❌  
# MAGIC   → Wrong argument order (condition should come before "left")

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
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct answer: B**  
# MAGIC `storesDF.write.mode("overwrite").json(filePath)`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**  
# MAGIC - `write` → DataFrameWriter (no parentheses)  
# MAGIC - `.mode("overwrite")` → overwrite existing data  
# MAGIC - `.json(filePath)` → write in JSON format
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**  
# MAGIC - **A ❌**  
# MAGIC   → Invalid syntax; write() is not used like this  
# MAGIC - **C ❌**  
# MAGIC   → .path() is not used directly for format writing  
# MAGIC - **D ❌**  
# MAGIC   → .option() is not used to set format like this  
# MAGIC - **E ❌**  
# MAGIC   → write() should not have parentheses
# MAGIC
# MAGIC ---

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
# MAGIC
# MAGIC ✅ **Correct answer: A**  
# MAGIC `df_user_non_pii = df_user.drop("first_name", "last_name", "email", "birthdate")`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**  
# MAGIC - `drop()` is the correct PySpark method to remove columns  
# MAGIC - You can pass multiple column names as separate string arguments  
# MAGIC - This results in a DataFrame containing only non-PII columns
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**  
# MAGIC - **B ❌**  
# MAGIC   → Missing quotes around column names → syntax error  
# MAGIC - **C ❌**  
# MAGIC   → `dropfields()` is not a valid PySpark method  
# MAGIC - **D ❌**  
# MAGIC   → Invalid method + incorrect string format

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

# MAGIC %md
# MAGIC
# MAGIC ✅ **Correct answer: B**  
# MAGIC `streaming_df.groupby("Id").count()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**  
# MAGIC In Structured Streaming, only certain operations are supported:  
# MAGIC - Aggregations like `groupBy().count()` ✔️  
# MAGIC   → Supported with proper output modes (append/complete)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**  
# MAGIC - **A. countDistinct()** ❌  
# MAGIC   → Not supported directly in streaming aggregations  
# MAGIC - **C. orderBy().limit()** ❌  
# MAGIC   → Global sorting + limit is not supported on streaming DataFrames  
# MAGIC - **D. .show()** ❌  
# MAGIC   → Streaming DataFrames require `.writeStream`, not actions like show()

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
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC The issue:
# MAGIC
# MAGIC - The model is being loaded inside the UDF for every batch/row call  
# MAGIC - This causes major performance overhead
# MAGIC
# MAGIC ✅ **Best solution: Use Iterator Pandas UDF**
# MAGIC
# MAGIC python
# MAGIC from typing import Iterator
# MAGIC import pandas as pd
# MAGIC
# MAGIC def in_spanish_iter(iterator: Iterator[pd.Series]) -> Iterator[pd.Series]:
# MAGIC     model = get_translation_model(target_lang='es')  # loaded ONCE per partition
# MAGIC     for batch in iterator:
# MAGIC         yield batch.apply(model)
# MAGIC
# MAGIC in_spanish = sf.pandas_udf(in_spanish_iter, StringType())
# MAGIC
# MAGIC
# MAGIC ✔️ **Why this works:**
# MAGIC
# MAGIC - Iterator[Series] → Iterator[Series]
# MAGIC - Model is loaded once per partition
# MAGIC - Reused across multiple batches
# MAGIC - Greatly improves performance and efficiency
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A. Convert to PySpark UDF** ❌  
# MAGIC   → Slower than Pandas UDF (no vectorization)
# MAGIC
# MAGIC - **B. Series → Scalar UDF** ❌  
# MAGIC   → Not valid pattern for this use case
# MAGIC
# MAGIC - **C. mapInPandas()** ❌  
# MAGIC   → Works differently; not the intended fix for reducing model reload frequency
# MAGIC
# MAGIC ---

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
# MAGIC ✅ **Correct answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC With storage level `MEMORY_AND_DISK`:
# MAGIC
# MAGIC - Spark tries to cache data in memory first  
# MAGIC - If memory is not sufficient:  
# MAGIC   Remaining partitions are spilled to disk  
# MAGIC - During processing:  
# MAGIC   - Data in memory → fast access  
# MAGIC   - Data on disk → slower (performance overhead)  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Why C is correct:**
# MAGIC
# MAGIC Spark will store as much data as possible in memory and spill the rest to disk when memory is full
# MAGIC
# MAGIC ✔️ This is exactly how `MEMORY_AND_DISK` works
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A ❌**  
# MAGIC   → Does NOT duplicate entire DataFrame in both memory and disk  
# MAGIC - **B ❌**  
# MAGIC   → No equal split logic exists  
# MAGIC - **D ❌**  
# MAGIC   → Spark does NOT cache based on access frequency (no LRU row-level optimization like this)

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
# MAGIC ---
# MAGIC ✅ **Correct answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC To enable fault tolerance and recovery in Structured Streaming:
# MAGIC
# MAGIC - You must configure a checkpoint location in `writeStream`  
# MAGIC python
# MAGIC streaming_df.writeStream \
# MAGIC     .format("parquet") \
# MAGIC     .option("checkpointLocation", "path/to/checkpoint") \
# MAGIC     .start()
# MAGIC
# MAGIC
# MAGIC ✔️ **Why this works:**
# MAGIC
# MAGIC - Checkpointing stores:
# MAGIC   - Progress information (offsets)
# MAGIC   - State data (for aggregations, joins, etc.)
# MAGIC - On restart, Spark resumes from last checkpoint
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A. checkpointLocation during readStream** ❌  
# MAGIC   → Not applicable; checkpointing is configured on writeStream
# MAGIC
# MAGIC - **B & C. recoveryLocation** ❌  
# MAGIC   → Not a valid Spark option
# MAGIC
# MAGIC ---

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
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC - In Spark, nothing executes until an action is called  
# MAGIC   → Here, `collect()` is the action  
# MAGIC - 🔄 **Execution flow:**  
# MAGIC   - Action (`collect()`) triggers a job  
# MAGIC   - Spark builds a DAG (Directed Acyclic Graph) of transformations  
# MAGIC   - DAG is split into stages based on shuffle boundaries  
# MAGIC   - Each stage is divided into tasks  
# MAGIC   - Each task operates on a single data partition  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Why C is correct:**
# MAGIC
# MAGIC The `collect()` action triggers a job, which is divided into stages at shuffle boundaries, and each stage is split into tasks
# MAGIC
# MAGIC ✔️ Perfectly describes Spark execution hierarchy
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A ❌**  
# MAGIC   → Script is not divided into multiple applications  
# MAGIC - **B ❌**  
# MAGIC   → Entire script is not always a single job (each action triggers a job)  
# MAGIC - **D ❌**  
# MAGIC   → Tasks are not created per transformation/action directly
# MAGIC
# MAGIC ---

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
# MAGIC ✅ **Correct answer: A**  
# MAGIC python
# MAGIC fact_df = purch_df.join(
# MAGIC     cust_df,
# MAGIC     F.col("customer_id") == F.col("cust_id"),
# MAGIC     "left"
# MAGIC )
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**  
# MAGIC **Current behavior:**  
# MAGIC - Default join = inner join  
# MAGIC - So rows in purchases_fct without matching customer_dim records are dropped  
# MAGIC
# MAGIC ✅ **Solution:**  
# MAGIC - Use a left join  
# MAGIC - Keeps all rows from purch_df  
# MAGIC - Adds matching data from cust_df (or null if no match)  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**  
# MAGIC - **B ❌**  
# MAGIC   → Still an inner join (default), just reversed order → same issue  
# MAGIC - **C ❌**  
# MAGIC   → Same as original logic (inner join), just condition order swapped  
# MAGIC - **D ❌**  
# MAGIC   → Right join keeps all rows from cust_df, not purch_df

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
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct answers: B and E**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC - **B. Only actions trigger the execution of the transformation pipeline** ✔️  
# MAGIC   Spark does not execute transformations immediately  
# MAGIC   Execution starts only when an action is called (e.g., collect(), count())
# MAGIC
# MAGIC - **E. Transformations are evaluated lazily** ✔️  
# MAGIC   Transformations are lazy  
# MAGIC   Spark builds a logical plan (DAG) instead of executing right away
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A ❌**  
# MAGIC   → No manual intervention required; actions automatically trigger execution
# MAGIC
# MAGIC - **C ❌**  
# MAGIC   → Transformations are not executed immediately
# MAGIC
# MAGIC - **D ❌**  
# MAGIC   → Optimization happens, but it’s not the reason for delayed execution  
# MAGIC   → Lazy evaluation is the core reason
# MAGIC
# MAGIC ---

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
# MAGIC ✅ **Correct answer: A**  
# MAGIC python
# MAGIC regions = dict(
# MAGIC     regions_df
# MAGIC         .select("region", "region_id")
# MAGIC         .sort("region_id")
# MAGIC         .take(3)
# MAGIC )
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC **Requirements:**
# MAGIC - Create a Python dictionary
# MAGIC - Mapping: region → region_id
# MAGIC - Use the smallest 3 region_id values
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Why A is correct:**
# MAGIC - `.select("region", "region_id")` → correct key-value order
# MAGIC - `.sort("region_id")` → ascending → smallest values first
# MAGIC - `.take(3)` → gets top 3 rows
# MAGIC - `dict(...)` → converts list of tuples into dictionary
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC - **B ❌**  
# MAGIC   → Reversed order → creates mapping region_id → region
# MAGIC - **C ❌**  
# MAGIC   → Uses .limit(3) without sorting → may not return smallest values
# MAGIC - **D ❌**  
# MAGIC   → Uses desc() → largest values, not smallest

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
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct answer: C**  
# MAGIC python
# MAGIC spark.read.orc("/file/test_data.orc").select("col1", "col2")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC - Spark uses column pruning optimization
# MAGIC - Even though `.select()` comes after `.read()`, Spark:
# MAGIC   - Pushes down the column selection to the data source (ORC)
# MAGIC   - Reads only required columns → efficient memory usage
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A ❌**  
# MAGIC   → Applies filter + selects only col2 → not both columns
# MAGIC
# MAGIC - **B ❌**  
# MAGIC   → `.select()` cannot be used before `.load()` (invalid syntax)
# MAGIC
# MAGIC - **D ❌**  
# MAGIC   → Works correctly, but exam-wise C is the standard/simple expected answer
# MAGIC
# MAGIC ---

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
# MAGIC ✅ **Correct answer: A**  
# MAGIC `psdf.to_spark()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**  
# MAGIC - pyspark.pandas (Pandas API on Spark) provides:  
# MAGIC   - `to_spark()` → converts to PySpark DataFrame
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**  
# MAGIC - **B. to_pyspark()** ❌  
# MAGIC   → Not a valid method  
# MAGIC - **C. to_pandas()** ❌  
# MAGIC   → Converts to Pandas DataFrame, not PySpark  
# MAGIC - **D. to_dataframe()** ❌  
# MAGIC   → Not a valid method

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
# MAGIC ✅ **Correct answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC - "GC overhead limit exceeded" means:
# MAGIC   - JVM is spending too much time doing garbage collection
# MAGIC   - Very little memory is being reclaimed → memory pressure is too high
# MAGIC
# MAGIC ✅ **Best solution:**
# MAGIC - Increase memory for the Spark Driver
# MAGIC - `--driver-memory 4g` (or higher)
# MAGIC
# MAGIC ✔️ **This gives more heap space → reduces GC pressure**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A. Repartition DataFrame** ❌  
# MAGIC   → May help distribution, but doesn’t directly fix driver GC issue
# MAGIC
# MAGIC - **B. Disable garbage collection** ❌  
# MAGIC   → Not possible / would crash JVM
# MAGIC
# MAGIC - **D. Cache large DataFrames** ❌  
# MAGIC   → Makes memory usage worse → increases GC pressure

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
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct answer: D**  
# MAGIC `df.orderBy("age", "salary", ascending=[True, False]).show()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC **Requirement:**
# MAGIC
# MAGIC - age → ascending ✅
# MAGIC - salary → descending ✅
# MAGIC
# MAGIC So:
# MAGIC
# MAGIC - ascending=[True, False]
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A ❌**  
# MAGIC   → Both columns sorted ascending
# MAGIC
# MAGIC - **B ❌**  
# MAGIC   → Both ascending again
# MAGIC
# MAGIC - **C ❌**  
# MAGIC   → age descending, salary ascending (reversed requirement)
# MAGIC
# MAGIC ---

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
# MAGIC ✅ **Correct answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC **cache():**
# MAGIC
# MAGIC - Shortcut for:
# MAGIC   - `df.persist(StorageLevel.MEMORY_AND_DISK)`
# MAGIC - Uses default storage level
# MAGIC
# MAGIC **persist():**
# MAGIC
# MAGIC - More flexible
# MAGIC - Allows specifying custom storage levels:
# MAGIC   - `df.persist(StorageLevel.DISK_ONLY)`
# MAGIC   - `df.persist(StorageLevel.MEMORY_ONLY)`
# MAGIC
# MAGIC 🔍 **Key Difference:**
# MAGIC
# MAGIC | Method    | Storage Level                  |
# MAGIC |-----------|-------------------------------|
# MAGIC | cache()   | Default only (MEMORY_AND_DISK) |
# MAGIC | persist() | Customizable                   |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A ❌**
# MAGIC   - → cache() cannot set storage level
# MAGIC - **B ❌**
# MAGIC   - → Default for persist() is NOT DISK_ONLY
# MAGIC - **C ❌**
# MAGIC   - → Reversed definition

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
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC - groupBy causes a shuffle ✔️
# MAGIC - Data must be redistributed across partitions
# MAGIC - Required to group same keys together
# MAGIC - This triggers a shuffle operation
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **B. filter** ❌  
# MAGIC   → Narrow transformation → no shuffle
# MAGIC - **C. select** ❌  
# MAGIC   → Only column projection → no shuffle
# MAGIC - **D. coalesce** ❌  
# MAGIC   → Reduces partitions without shuffle (unless explicitly forced)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip:**
# MAGIC
# MAGIC 👉 **Wide transformations = shuffle**  
# MAGIC - groupBy, join, distinct
# MAGIC
# MAGIC 👉 **Narrow transformations = no shuffle**  
# MAGIC - filter, select, map
# MAGIC
# MAGIC ---

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
# MAGIC ✅ **Correct answer: D**  
# MAGIC `df = spark.read.parquet("/path/events/data/")`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**  
# MAGIC - Spark automatically reads all nested directories when using a base path  
# MAGIC - Parquet supports partition discovery  
# MAGIC
# MAGIC **Given structure:**  
# MAGIC - `/path/events/data/year/month/day`  
# MAGIC
# MAGIC → Spark will recursively read all files under this path
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**  
# MAGIC - **A ❌**  
# MAGIC   → Typo in path (evets instead of events)  
# MAGIC - **B ❌**  
# MAGIC   → recursiveFileLookup is unnecessary for standard partitioned data  
# MAGIC - **C ❌**  
# MAGIC   → * only matches one level, not deeply nested structure  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip:**  
# MAGIC 👉 For partitioned data:  
# MAGIC `spark.read.parquet("base_path/")`  
# MAGIC ✔️ Automatically reads all subdirectories

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
# MAGIC ✅ **Correct answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC - `coalesce(n)` is used to reduce the number of partitions, not increase them efficiently
# MAGIC - If you try to increase partitions:
# MAGIC   - `df.coalesce(20)`
# MAGIC   - → Spark will **NOT** increase partitions
# MAGIC   - → It keeps the original number
# MAGIC
# MAGIC 📌 **Given:**
# MAGIC - Original partitions = 10
# MAGIC - Requested = 20
# MAGIC
# MAGIC 👉 **Result = 10 partitions**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **B ❌**
# MAGIC   - → Partitions are not tied directly to executors
# MAGIC - **C ❌**
# MAGIC   - → Only if `coalesce(1)` is used
# MAGIC - **D ❌**
# MAGIC   - → `coalesce()` does not increase partitions
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip:**
# MAGIC
# MAGIC | Method        | Can Increase? | Causes Shuffle |
# MAGIC |---------------|---------------|---------------|
# MAGIC | coalesce()    | ❌ No         | ❌ No         |
# MAGIC | repartition() | ✅ Yes        | ✅ Yes        |

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
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC The driver node is the brain of the Spark application
# MAGIC
# MAGIC 👉 **Its responsibilities:**
# MAGIC - Converts actions (like show()) into a job
# MAGIC - Breaks job into stages and tasks
# MAGIC - Schedules and distributes tasks to executors (worker nodes)
# MAGIC - Tracks execution and collects results
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **B ❌**
# MAGIC   - UI is only a small part (Spark UI), not the main role
# MAGIC - **C ❌**
# MAGIC   - Data is distributed across executors, not stored/processed only on driver
# MAGIC - **D ❌**
# MAGIC   - Driver may collect results, but does not “store” all results as its main role
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Quick Memory:**
# MAGIC
# MAGIC 👉 Driver = Orchestrator / Coordinator  
# MAGIC 👉 Executors = Workers (do actual computation)
# MAGIC
# MAGIC ---

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
# MAGIC ✅ **Correct answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **def shake_256(df: pd.Series) -> pd.Series:**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC - Pandas UDF (vectorized UDF) expects:
# MAGIC   - **Input:** pd.Series
# MAGIC   - **Output:** pd.Series
# MAGIC
# MAGIC 👉 Because it processes data in batches, not row-by-row
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Correct implementation:**
# MAGIC python
# MAGIC import pandas as pd
# MAGIC import hashlib
# MAGIC import pyspark.sql.functions as sf
# MAGIC from pyspark.sql.types import StringType
# MAGIC
# MAGIC def shake_256(df: pd.Series) -> pd.Series:
# MAGIC     return df.apply(lambda raw: hashlib.shake_256(raw.encode()).hexdigest(20))
# MAGIC
# MAGIC shake_256_udf = sf.pandas_udf(shake_256, StringType())
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A. -> str ❌**
# MAGIC   - Return type must be pd.Series, not single value
# MAGIC - **B. Iterator version ⚠️**
# MAGIC   - Valid for a different Pandas UDF type, but not the default expected here
# MAGIC - **C. (raw: str) -> str ❌**
# MAGIC   - This is regular Python UDF signature (causes the error)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip:**
# MAGIC
# MAGIC 👉 Pandas UDF = Series → Series (most common)

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
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC **The requirement:**
# MAGIC
# MAGIC - Execute groupBy operation in parallel using Pandas DataFrame logic across Spark workers
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why A is correct:**
# MAGIC
# MAGIC - `df.groupBy('user_id').applyInPandas(mean_func, schema="user_id long, value double")`
# MAGIC - `applyInPandas()` is specifically designed for:
# MAGIC   - grouped operations
# MAGIC   - Running Pandas logic per group
# MAGIC   - Executing in parallel across partitions/workers
# MAGIC
# MAGIC ✔️ Each group (`user_id`) is processed as a Pandas DataFrame  
# MAGIC ✔️ Fully distributed and parallel
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **B. mapInPandas()** ❌  
# MAGIC   → Works on partitions, not grouped data  
# MAGIC   → No guarantee grouping is correct across partitions
# MAGIC
# MAGIC - **C. Spark built-in mean()** ❌  
# MAGIC   → Not using Pandas; question focuses on Pandas DataFrame usage
# MAGIC
# MAGIC - **D. Pandas UDF (scalar agg)** ❌  
# MAGIC   → Not group-aware in the same way; less flexible than applyInPandas
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip:**
# MAGIC
# MAGIC | API            | Use Case                      |
# MAGIC |----------------|------------------------------|
# MAGIC | applyInPandas()| ✅ GroupBy + Pandas logic     |
# MAGIC | mapInPandas()  | Partition-level processing    |
# MAGIC | pandas_udf()   | Column-level vectorized ops   |
# MAGIC
# MAGIC ---

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
# MAGIC ✅ **Correct answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC Valid Spark log levels (Log4j) include:
# MAGIC
# MAGIC - ALL
# MAGIC - TRACE
# MAGIC - DEBUG
# MAGIC - INFO
# MAGIC - WARN
# MAGIC - ERROR
# MAGIC - FATAL
# MAGIC - OFF
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Why B is correct:**
# MAGIC
# MAGIC - ERROR, WARN, TRACE, OFF ✔️
# MAGIC   → All are valid Spark log levels
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A ❌**
# MAGIC   → FAIL is not a valid log level
# MAGIC - **C ❌**
# MAGIC   → NONE is not valid
# MAGIC - **D ❌**
# MAGIC   → NONE is invalid
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip:**
# MAGIC
# MAGIC 👉 Remember common levels:  
# MAGIC TRACE < DEBUG < INFO < WARN < ERROR < FATAL < OFF

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
# MAGIC ✅ **Correct answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC python
# MAGIC result = df1.join(df2, df1.employee_id == df2.emp_id, how="inner")
# MAGIC
# MAGIC
# MAGIC The join condition is explicitly defined:
# MAGIC
# MAGIC - `df1.employee_id == df2.emp_id`
# MAGIC
# MAGIC So Spark does not require column names to match  
# MAGIC It correctly performs an inner join based on the condition
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A ❌**  
# MAGIC   → Column names do not need to match if condition is provided
# MAGIC
# MAGIC - **B ❌**  
# MAGIC   → `on='employee_id'` only works when column names are the same
# MAGIC
# MAGIC - **C ❌**  
# MAGIC   → Spark supports joining DataFrames with different schemas
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip:**
# MAGIC
# MAGIC 👉 Two ways to join:
# MAGIC
# MAGIC - **Same column name:**  
# MAGIC   `df1.join(df2, "id")`
# MAGIC
# MAGIC - **Different column names:**  
# MAGIC   `df1.join(df2, df1.id1 == df2.id2)`

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
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct answer: C**
# MAGIC
# MAGIC python
# MAGIC final_df \
# MAGIC   .sort("market_time") \
# MAGIC   .coalesce(1) \
# MAGIC   .write \
# MAGIC   .format("parquet") \
# MAGIC   .mode("overwrite") \
# MAGIC   .saveAsTable("output.market_events")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC **Requirement:**
# MAGIC
# MAGIC - All records must be globally sorted by `market_time`
# MAGIC - Data is written to Parquet daily (overwrite)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔑 **Key Point:**
# MAGIC
# MAGIC - `sort()` / `orderBy()` → performs global sort
# MAGIC - **BUT:**  
# MAGIC   Data is still distributed across multiple partitions  
# MAGIC   So final output files are not globally ordered across files
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why coalesce(1) is needed:**
# MAGIC
# MAGIC - Forces single partition
# MAGIC - Ensures:
# MAGIC   - Only one output file
# MAGIC   - Data is fully globally sorted
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A & B ❌**  
# MAGIC   → Sorting happens, but multiple output files → not globally ordered
# MAGIC
# MAGIC - **D ❌**  
# MAGIC   → `sortWithinPartitions()` only sorts within each partition, not globally
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip:**
# MAGIC
# MAGIC 👉 Global ordering guarantee = orderBy/sort + single partition
# MAGIC
# MAGIC ---

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
# MAGIC ✅ **Correct answer: A**  
# MAGIC `.outputMode("complete")`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC **Structured Streaming output modes:**
# MAGIC
# MAGIC - **complete** ✔️  
# MAGIC   → Writes the entire result table on every trigger  
# MAGIC   → Required for aggregations when you want full output each time
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **append** ❌  
# MAGIC   → Writes only new rows (not full table)
# MAGIC - **replace** ❌  
# MAGIC   → Not a valid output mode
# MAGIC - **aggregate** ❌  
# MAGIC   → Not a valid output mode
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Quick Cheat Sheet:**
# MAGIC
# MAGIC | Mode     | Behavior            |
# MAGIC |----------|---------------------|
# MAGIC | append   | Only new rows       |
# MAGIC | update   | Only updated rows   |
# MAGIC | complete | Full result table   |

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
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC **The issue:**
# MAGIC
# MAGIC - Too few partitions
# MAGIC - Not enough parallelism → CPUs are underutilized
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Best practice:**
# MAGIC
# MAGIC 👉 Partition based on data size, not cluster size
# MAGIC
# MAGIC - Number of partitions = Total data size / Ideal partition size
# MAGIC - Recommended partition size: ~128 MB (or 128–256 MB)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 📌 **Calculation:**
# MAGIC
# MAGIC - Data size = 1 TB = 1024 GB
# MAGIC - Partition size ≈ 128 MB
# MAGIC - 1024 GB / 0.125 GB ≈ 8192 partitions
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **This creates enough tasks to:**
# MAGIC
# MAGIC - Fully utilize all cores
# MAGIC - Improve parallelism
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A ❌**
# MAGIC   - Too few partitions (~160 cores) → underutilization
# MAGIC - **B ❌**
# MAGIC   - Fixed number (200) is arbitrary and too small for 1 TB
# MAGIC - **C ❌**
# MAGIC   - Partitions = nodes (10) → extremely low parallelism
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip:**
# MAGIC
# MAGIC 👉 Always size partitions by data volume, not hardware count
# MAGIC
# MAGIC ---

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
# MAGIC ✅ **Correct answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC - `date_sub(start, days)` normally subtracts days from start
# MAGIC
# MAGIC 🔁 **When days is negative:**
# MAGIC - `date_sub(start, -n)`  
# MAGIC   → This becomes:  
# MAGIC   `start - (-n) = start + n`
# MAGIC
# MAGIC ✔️ **So it adds days instead of subtracting**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 📌 **Example:**
# MAGIC - `date_sub("2024-01-10", -5)`  
# MAGIC   → Result: `"2024-01-15"`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A ❌**  
# MAGIC   → Date does change
# MAGIC - **B ❌**  
# MAGIC   → No error; negative values are allowed
# MAGIC - **D ❌**  
# MAGIC   → That’s normal behavior for positive values
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip:**
# MAGIC
# MAGIC 👉 Negative input flips the operation

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
# MAGIC ✅ **Correct answer: B**
# MAGIC
# MAGIC python
# MAGIC query = streaming_df.writeStream \
# MAGIC     .format("console") \
# MAGIC     .outputMode("append") \
# MAGIC     .option("checkpointLocation", "/path/to/checkpoint") \
# MAGIC     .start()
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC To enable fault tolerance and recovery in Structured Streaming:
# MAGIC
# MAGIC You must specify:
# MAGIC `.option("checkpointLocation", "path")`
# MAGIC
# MAGIC ✔️ **This stores:**
# MAGIC - Offsets (progress)
# MAGIC - State (for aggregations, joins, etc.)
# MAGIC
# MAGIC 👉 On failure, Spark resumes from the last checkpoint
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are wrong:**
# MAGIC
# MAGIC - **A ❌**
# MAGIC   - Incorrect option name (`checkpoint` is invalid)
# MAGIC - **C ❌**
# MAGIC   - No checkpointing → cannot recover
# MAGIC - **D ❌**
# MAGIC   - Missing checkpoint → no fault tolerance
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🧠 **Exam Tip:**
# MAGIC
# MAGIC 👉 Always remember:  
# MAGIC `checkpointLocation` → `writeStream` only

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
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Explanation:**
# MAGIC
# MAGIC **Given:**
# MAGIC
# MAGIC - 10 worker nodes
# MAGIC - 4 executors per node
# MAGIC - Each executor uses 4 cores
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 📌 **Step-by-step calculation:**
# MAGIC
# MAGIC - **Total executors:**  
# MAGIC   10 nodes × 4 executors = 40 executors
# MAGIC
# MAGIC - **Total cores:**  
# MAGIC   40 executors × 4 cores = 160 cores
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🟢 **Final Answer:** A (160)
# MAGIC
# MAGIC ---

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
# MAGIC **The key issue:**  
# MAGIC Very low number of tasks per stage, which indicates insufficient parallelism. Even with many executors available, Spark cannot utilize them if there aren’t enough partitions/tasks to distribute work.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **In Spark SQL, the number of tasks in shuffle stages is primarily controlled by:**
# MAGIC
# MAGIC `spark.sql.shuffle.partitions`
# MAGIC
# MAGIC This setting defines how many partitions (and thus tasks) are created during shuffle operations (joins, aggregations, etc.).
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **What should be done?**
# MAGIC
# MAGIC To improve cluster utilization, you should increase the number of shuffle partitions, which creates more tasks and allows better parallel execution across executors.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Correct answer:**  
# MAGIC A. Increase the value of spark.sql.shuffle.partitions
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Why others are incorrect:**
# MAGIC - B. Reduce spark.sql.shuffle.partitions → makes parallelism worse
# MAGIC - C. Increase dataset size → not a valid tuning strategy for utilization
# MAGIC - D. Enable dynamic resource allocation → helps scale executors, but won’t fix lack of tasks per stage
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Final:** A

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
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **When converting a large Pandas API on Spark DataFrame back to a Pandas DataFrame, the key risk is related to driver memory limitations.**
# MAGIC
# MAGIC In Spark, data is distributed across worker nodes. However, Pandas operates on a single machine (driver).
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **So when you convert:**
# MAGIC
# MAGIC - All distributed data is collected back to the driver node
# MAGIC - This can cause out-of-memory errors if the dataset is large
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Correct answer:**
# MAGIC
# MAGIC D. The operation will load all data into the driver's memory, potentially causing memory overflow.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Why others are incorrect:**
# MAGIC
# MAGIC - **A → Wrong:** conversion does NOT distribute data; it does the opposite
# MAGIC - **B → Wrong:** no 1000-row limit exists
# MAGIC - **C → Wrong:** data loss is not expected, but memory overflow is
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Final:** D
# MAGIC
# MAGIC ---

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
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Correct Answer:** B
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC In Adaptive Query Execution (AQE), Spark can dynamically choose an optimal join strategy based on runtime statistics such as partition sizes.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **The configuration:**
# MAGIC
# MAGIC `spark.sql.adaptive.maxShuffledHashJoinLocalMapThreshold`
# MAGIC
# MAGIC controls whether Spark can build a local hash map for shuffled hash joins.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key rule:**
# MAGIC
# MAGIC If all post-shuffle partitions are smaller than this threshold, Spark can safely:
# MAGIC
# MAGIC - Load each partition into memory
# MAGIC - Build an in-memory hash map locally
# MAGIC - Perform a shuffled hash join efficiently
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Therefore:**
# MAGIC
# MAGIC Spark will choose a **Shuffled Hash Join** because the partitions are small enough to fit into memory for hash table creation.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Why other options are incorrect:**
# MAGIC
# MAGIC - **A. Cartesian join ❌**  
# MAGIC   Not used for optimization; only when no join condition exists
# MAGIC
# MAGIC - **C. Broadcast nested loop join ❌**  
# MAGIC   Used when one side is very small (broadcastable), not based on shuffle partition threshold
# MAGIC
# MAGIC - **D. Sort-merge join ❌**  
# MAGIC   Default fallback for large datasets, not for small partitions
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✔️ **Final Answer:** B. A shuffled hash join
# MAGIC
# MAGIC ---

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
# MAGIC
# MAGIC **Correct Answer: B.**
# MAGIC
# MAGIC python
# MAGIC spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC Apache Arrow is used in PySpark to optimize data transfer between Pandas and Spark DataFrames by enabling columnar in-memory data exchange, which is much faster than traditional serialization.
# MAGIC
# MAGIC The correct configuration key is:
# MAGIC
# MAGIC - `spark.sql.execution.arrow.pyspark.enabled`
# MAGIC
# MAGIC When set to `"true"`, it enables Arrow optimization for:
# MAGIC - `toPandas()`
# MAGIC - `createDataFrame(pandas_df)`
# MAGIC - Pandas UDFs
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Why other options are incorrect:**
# MAGIC
# MAGIC - **A. `spark.pandas.arrow.enabled` ❌**  
# MAGIC   → Not a valid Spark configuration.
# MAGIC
# MAGIC - **C. `spark.sql.execution.arrow.enabled` ❌**  
# MAGIC   → Incomplete / incorrect key (missing `.pyspark`).
# MAGIC
# MAGIC - **D. `spark.sql.arrow.pandas.enabled` ❌**  
# MAGIC   → Incorrect key structure.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Quick Tip:**
# MAGIC
# MAGIC Always remember the full key:
# MAGIC
# MAGIC - `spark.sql.execution.arrow.pyspark.enabled`

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
# MAGIC ---
# MAGIC
# MAGIC **Correct Answer: B.**  
# MAGIC Broadcast join, as df2 is smaller than the default broadcast threshold.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC Spark automatically uses a broadcast join when one of the DataFrames is smaller than the threshold defined by:
# MAGIC
# MAGIC - `spark.sql.autoBroadcastJoinThreshold` (default: 10 MB)
# MAGIC
# MAGIC **In this case:**
# MAGIC - dfl ≈ 10 GB (large)
# MAGIC - df2 ≈ 8 MB (small)
# MAGIC
# MAGIC Since 8 MB < 10 MB, Spark will:
# MAGIC - Broadcast df2 to all worker nodes
# MAGIC - Avoid shuffling the large dataset (dfl)
# MAGIC - Perform a Broadcast Hash Join, which is much faster
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Why other options are incorrect:**
# MAGIC
# MAGIC - **A. Shuffle join, because AQE is not enabled ❌**  
# MAGIC   → Even without AQE, Spark can still perform broadcast joins using static planning.
# MAGIC
# MAGIC - **C. Shuffle join due to large size difference ❌**  
# MAGIC   → Size difference actually favors broadcast joins.
# MAGIC
# MAGIC - **D. Shuffle join because no broadcast hints were provided ❌**  
# MAGIC   → Spark automatically decides to broadcast based on size; hints are optional.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key Takeaway:**
# MAGIC
# MAGIC If one table is small enough (< 10 MB by default), Spark will automatically use a broadcast join for better performance.
# MAGIC
# MAGIC ---

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
# MAGIC ---
# MAGIC **Correct Answer: A.**
# MAGIC
# MAGIC python
# MAGIC df = spark.read.option("mergeSchema", "true").parquet("/data/parquet_files")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC When reading multiple Parquet files with different but compatible schemas, Spark by default:
# MAGIC
# MAGIC - Uses the schema from one file (not all)
# MAGIC - May ignore columns present in other files
# MAGIC
# MAGIC To ensure all columns from all files are included, you must enable schema merging:
# MAGIC
# MAGIC python
# MAGIC df = spark.read.option("mergeSchema", "true").parquet("/data/parquet_files")
# MAGIC
# MAGIC
# MAGIC - `"mergeSchema" = true` tells Spark to:
# MAGIC   - Combine schemas across all files
# MAGIC   - Include missing columns with null values where applicable
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Why other options are incorrect:**
# MAGIC
# MAGIC - **B. `.mergeAllcolumns()` ❌**
# MAGIC   - Not a valid Spark API method.
# MAGIC - **C. `.schema("merge")` ❌**
# MAGIC   - Incorrect usage; `schema()` expects a defined schema, not a keyword.
# MAGIC - **D. `.format("parquet").load(...)` ❌**
# MAGIC   - Reads files but does not enable schema merging, so some columns may be missing.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key Takeaway:**
# MAGIC
# MAGIC Use:
# MAGIC
# MAGIC python
# MAGIC option("mergeSchema", "true")
# MAGIC
# MAGIC when working with evolving Parquet schemas to avoid losing columns.

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
# MAGIC **Correct Answers: B and C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **B. Execute their pyspark shell with the option `--remote "sc://localhost"`**  
# MAGIC This starts the PySpark shell using Spark Connect  
# MAGIC Connects to a local Spark Connect server using the correct protocol:  
# MAGIC `sc://`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **C. Set the environment variable `SPARK_REMOTE="sc://localhost"` before starting the pyspark shell**  
# MAGIC This allows enabling Spark Connect without modifying application code  
# MAGIC Useful for testing existing applications transparently
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A. `--remote "https://localhost"` ❌**  
# MAGIC   → Spark Connect uses gRPC (`sc://`), not HTTP/HTTPS
# MAGIC
# MAGIC - **D. `.remote("sc://localhost")` in code ❌**  
# MAGIC   → Requires code change, which the question explicitly avoids
# MAGIC
# MAGIC - **E. Setting `spark.connect.grpc.binding.port` in code ❌**  
# MAGIC   → Also requires modifying application code
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Key Takeaway:**
# MAGIC
# MAGIC To test Spark Connect without changing existing code, use:
# MAGIC
# MAGIC - CLI option: `--remote "sc://localhost"`
# MAGIC - Environment variable: `SPARK_REMOTE`

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
# MAGIC ---
# MAGIC **Correct Answer:** B.  
# MAGIC Use an accumulator to record the maximum time on the driver.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Explanation:**
# MAGIC
# MAGIC - The requirement is to:
# MAGIC   - Track task-level metrics (processing time) across executors
# MAGIC   - Aggregate the result (maximum time)
# MAGIC   - Make it available on the driver
# MAGIC
# MAGIC 👉 This is exactly what an Accumulator is designed for:
# MAGIC - Executors update values
# MAGIC - Driver reads the final aggregated result
# MAGIC
# MAGIC For this case, a developer can use a custom accumulator (AccumulatorV2) to track the maximum value instead of just sum/count.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A. reduce() ❌**  
# MAGIC   → Works on RDD data, not suitable for tracking task execution metrics across workers
# MAGIC
# MAGIC - **C. Broadcast variable ❌**  
# MAGIC   → Used for read-only sharing, not for aggregation
# MAGIC
# MAGIC - **D. Spark UI ❌**  
# MAGIC   → Useful for monitoring, but not programmatically accessible for application logic
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Key Takeaway:**
# MAGIC
# MAGIC 👉 Use Accumulators (especially custom ones) when you need to:
# MAGIC - Collect metrics from executors
# MAGIC - Aggregate them
# MAGIC - Access the result on the driver
# MAGIC
# MAGIC **Perfect for monitoring and performance tracking**
# MAGIC

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
# MAGIC
# MAGIC **Correct Answer: A.**  
# MAGIC `DataFrame.groupBy().agg()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Explanation:**
# MAGIC
# MAGIC In Apache Spark, a shuffle occurs when data needs to be redistributed across partitions.
# MAGIC
# MAGIC **👉 `groupBy().agg()`:**
# MAGIC - Groups data by key
# MAGIC - Requires all records with the same key to be brought together
# MAGIC - Causes data movement across nodes (shuffle)
# MAGIC - Creates a new stage boundary
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **B. `filter()` ❌**
# MAGIC   - Narrow transformation
# MAGIC   - No data movement across partitions
# MAGIC
# MAGIC - **C. `withColumn()` ❌**
# MAGIC   - Column-level transformation
# MAGIC   - Operates within the same partition
# MAGIC
# MAGIC - **D. `select()` ❌**
# MAGIC   - Projection only
# MAGIC   - No shuffle involved
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Key Concept: Narrow vs Wide Transformations**
# MAGIC
# MAGIC | Type                | Example           | Shuffle | New Stage |
# MAGIC |---------------------|-------------------|---------|-----------|
# MAGIC | Narrow Transformation| filter, select    | ❌ No   | ❌ No     |
# MAGIC | Wide Transformation  | groupBy, join     | ✅ Yes  | ✅ Yes    |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Key Takeaway:**
# MAGIC
# MAGIC 👉 Any operation that requires data redistribution (like `groupBy`) will trigger a shuffle and a new stage.

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
# MAGIC ---
# MAGIC **Correct Answer:** D. `df.withColumn("length", udf(lambda s: len(s), StringType()))`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation of Answer Options:**
# MAGIC
# MAGIC - ✅ **Option D:**  
# MAGIC   Correctly defines a User-Defined Function (UDF) using a Python lambda that calls `len(s)` and wraps it with the `pyspark.sql.functions.udf` wrapper, specifying the return type. It then applies this UDF to create a new column via `withColumn`.
# MAGIC
# MAGIC - ❌ **Option A:**  
# MAGIC   Uses invalid syntax; `spark.udf` is used for registering UDFs for SQL use, but the call `spark.udf("len", StringType())` is not a valid way to create or apply a UDF in this context.
# MAGIC
# MAGIC - ❌ **Option B:**  
# MAGIC   Uses the built-in `pyspark.sql.functions.length` function. While this is the most efficient way to calculate string length in Spark, it is not a UDF implementation.
# MAGIC
# MAGIC - ❌ **Option C:**  
# MAGIC   Registers a UDF with the SparkSession for use in SQL queries, but it does not actually apply the function to the DataFrame in the code provided.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key Takeaways for UDFs:**
# MAGIC
# MAGIC - **Performance:**  
# MAGIC   Built-in functions (like Option B) are highly optimized and should be preferred over UDFs whenever possible.
# MAGIC
# MAGIC - **Flexibility:**  
# MAGIC   UDFs (like Option D) allow you to use custom Python logic but incur overhead due to data movement between the JVM and Python processes.
# MAGIC
# MAGIC - **Usage:**  
# MAGIC   To use a Python function in a DataFrame transformation, it must be wrapped with the `udf()` function or the `@udf` decorator.

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
# MAGIC
# MAGIC **Correct Answer: B.**  
# MAGIC It removes duplicates that arrive within the 30-minute window specified by the watermark.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Explanation:**
# MAGIC
# MAGIC In Apache Spark Structured Streaming, deduplication with a watermark works as follows:
# MAGIC
# MAGIC - The watermark defines how late data can arrive
# MAGIC - `dropDuplicatesWithinWatermark()`:
# MAGIC   - Keeps track of seen records within the watermark window
# MAGIC   - Removes duplicates only within that time boundary
# MAGIC
# MAGIC 🔹 **In this scenario:**
# MAGIC - Duplicate records differ by at most 30 minutes
# MAGIC - Watermark is set to "30 minutes"
# MAGIC
# MAGIC 👉 **Result:**
# MAGIC - Spark will identify and remove duplicates within that 30-minute window
# MAGIC - Older state (beyond watermark) is dropped to save memory
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A. Not able to handle deduplication ❌**  
# MAGIC   → This is exactly what watermark-based deduplication is designed for
# MAGIC
# MAGIC - **C. Removes all duplicates regardless of time ❌**  
# MAGIC   → Only works within watermark window, not globally forever
# MAGIC
# MAGIC - **D. Accepts only seconds ❌**  
# MAGIC   → Spark supports time formats like "30 minutes", "1 hour", etc.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Key Takeaway:**
# MAGIC
# MAGIC 👉 `dropDuplicatesWithinWatermark()` =  
# MAGIC Deduplication + bounded state using watermark
# MAGIC
# MAGIC - ✔ Removes duplicates within time window  
# MAGIC - ❌ Does not guarantee global deduplication forever

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
# MAGIC **Correct Answer: A.**  
# MAGIC `employees_df.filter(employees_df.tenure >= 5).show()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Explanation:**
# MAGIC
# MAGIC The requirement is to:
# MAGIC
# MAGIC - Filter employees with tenure ≥ 5
# MAGIC - Display the result
# MAGIC
# MAGIC 👉 Option A does both:
# MAGIC
# MAGIC - `filter(...)` → applies the condition
# MAGIC - `.show()` → displays the result
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **B. `where(...)` ❌**  
# MAGIC   → Correct filtering, but does NOT display the result
# MAGIC
# MAGIC - **C. `filter(...)` ❌**  
# MAGIC   → Invalid usage (missing DataFrame reference)
# MAGIC
# MAGIC - **D. `.collect()` ❌**  
# MAGIC   → Returns data to driver (not just display)  
# MAGIC   → Can cause memory issues for large datasets
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Key Takeaway (in Apache Spark):**
# MAGIC
# MAGIC 👉 Use:
# MAGIC - `.show()` → to display results
# MAGIC - `.collect()` → only when you truly need data on the driver

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
# MAGIC ---
# MAGIC **Correct Answer: C.**  
# MAGIC [Row(name='bambi', age=None), Row(name='alladin', age=20)]
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Explanation:**
# MAGIC
# MAGIC In Apache Spark, when you provide a schema while reading a CSV:
# MAGIC
# MAGIC python
# MAGIC schema = StructType([
# MAGIC     StructField("name", StringType()),
# MAGIC     StructField("age", IntegerType())
# MAGIC ])
# MAGIC
# MAGIC
# MAGIC Spark will:
# MAGIC
# MAGIC - Try to cast each column to the specified type
# MAGIC - If conversion fails, it sets the value to null (None in Python) instead of throwing an error (by default)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Input Data:**
# MAGIC
# MAGIC bambi, hello
# MAGIC alladin, 20
# MAGIC
# MAGIC
# MAGIC 🔹 **Row-wise Result:**
# MAGIC - `"bambi, hello"`
# MAGIC   - name = "bambi" ✅
# MAGIC   - age = "hello" → cannot convert to Integer ❌ → becomes None
# MAGIC - `"alladin, 20"`
# MAGIC   - name = "alladin" ✅
# MAGIC   - age = 20 ✅
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Final Output:**
# MAGIC
# MAGIC [
# MAGIC   Row(name='bambi', age=None),
# MAGIC   Row(name='alladin', age=20)
# MAGIC ]
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Why other options are incorrect:**
# MAGIC - **A. Missing age in first row ❌**  
# MAGIC   → Age column still exists, just becomes None
# MAGIC - **B. Drops invalid row ❌**  
# MAGIC   → Spark does not drop rows by default
# MAGIC - **D. Throws error ❌**  
# MAGIC   → Spark is tolerant and sets invalid casts to null
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Key Takeaway:**
# MAGIC
# MAGIC 👉 Spark uses permissive mode by default:
# MAGIC
# MAGIC - Invalid type conversions → NULL, not error
# MAGIC - Makes ingestion robust for messy data

# COMMAND ----------

# MAGIC %md
# MAGIC 🔹 **Default Behavior (Permissive)**
# MAGIC
# MAGIC By default:
# MAGIC
# MAGIC
# MAGIC spark.read.schema(schema).csv(path)
# MAGIC
# MAGIC - Invalid values → converted to NULL  
# MAGIC - No errors thrown ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Enforcing Strict Schema ✅**
# MAGIC
# MAGIC ✅ **Option 1: Use `mode("FAILFAST")` (Most Important)**
# MAGIC
# MAGIC python
# MAGIC df = spark.read \
# MAGIC     .schema(schema) \
# MAGIC     .option("mode", "FAILFAST") \
# MAGIC     .csv(path)
# MAGIC
# MAGIC
# MAGIC 🔥 **What it does:**
# MAGIC - Immediately throws an error if:
# MAGIC   - Type mismatch (e.g., "hello" → Integer)
# MAGIC   - Corrupt records
# MAGIC - Stops job execution
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Other Modes (for understanding)**
# MAGIC
# MAGIC | Mode         | Behavior                |
# MAGIC |--------------|------------------------|
# MAGIC | PERMISSIVE   | Invalid → NULL         |
# MAGIC | DROPMALFORMED| Drops bad rows         |
# MAGIC | FAILFAST     | ❌ Throws error         |

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
# MAGIC
# MAGIC **The correct code fragment to return the desired DataFrame is Option B.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Correct Answer: Option B**
# MAGIC python
# MAGIC exploded_df = sensor_df.withColumn("record_exploded", explode("record"))
# MAGIC exploded_df = exploded_df.select("record_datetime", "record_exploded.sensor_id", "record_exploded.status", "record_exploded.health")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation**
# MAGIC
# MAGIC **Step 1: Exploding the Array:**  
# MAGIC The `explode()` function in PySpark takes an array column and returns a new row for each element in that array. Using `withColumn("record_exploded", explode("record"))` creates a new column `record_exploded` where each row contains a single struct from the original `record` array.
# MAGIC
# MAGIC **Step 2: Accessing Struct Fields:**  
# MAGIC To split the struct into separate columns, you use dot notation (e.g., `record_exploded.sensor_id`). This allows you to select individual fields from the exploded struct and promote them to top-level columns in the DataFrame.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Why other options are incorrect:**
# MAGIC
# MAGIC - ❌ **Option A:**  
# MAGIC   It attempts to select columns like `sensor_id` directly after the explode. However, these fields are still nested inside the `record_exploded` struct. Without the `record_exploded.` prefix, Spark will not find these columns.
# MAGIC
# MAGIC - ❌ **Option C:**  
# MAGIC   This option is often identical to B in some exam versions but might contain subtle syntax errors (like incorrect ordering or duplicated variable assignments) depending on the specific source text.
# MAGIC
# MAGIC - ❌ **Option D:**  
# MAGIC   This only selects the `record_datetime` and the single struct column `record_exploded` without splitting the struct into its constituent `sensor_id`, `status`, and `health` columns.

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
# MAGIC **Correct Answer: C.**  
# MAGIC **Switch the deployment mode to cluster mode.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Explanation:**
# MAGIC
# MAGIC In Apache Spark, the difference between deployment modes is key:
# MAGIC
# MAGIC - **Client Mode:**
# MAGIC   - Driver runs on the client machine
# MAGIC   - If the client machine has limited resources → performance bottleneck
# MAGIC
# MAGIC - **Cluster Mode:**
# MAGIC   - Driver runs inside the cluster (worker node)
# MAGIC   - Gets better resources and scalability
# MAGIC
# MAGIC 👉 Since the issue is driver resource constraint in client mode, moving the driver to the cluster resolves it.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A. Add more executor instances ❌**
# MAGIC   - Helps task execution, but does NOT fix driver bottleneck
# MAGIC
# MAGIC - **B. Increase driver memory on client machine ❌**
# MAGIC   - May help temporarily, but still limited by client machine capacity
# MAGIC
# MAGIC - **D. Switch to local mode ❌**
# MAGIC   - Worse performance (runs everything on one machine)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Key Takeaway:**
# MAGIC
# MAGIC 👉 If the driver is the bottleneck in client mode, the best solution is:
# MAGIC
# MAGIC - ✔ Move to cluster mode
# MAGIC - ✔ Let the cluster handle driver workload

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
# MAGIC **Correct Answer: D.**  
# MAGIC `.option("path", "path/to/destination/dir")`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Explanation:**
# MAGIC
# MAGIC In Apache Spark Structured Streaming, when writing a streaming DataFrame to files (like Parquet), you must specify:
# MAGIC
# MAGIC 👉 The output path using:
# MAGIC
# MAGIC `.option("path", "destination_path")`
# MAGIC
# MAGIC ✅ **Correct Code:**
# MAGIC python
# MAGIC .writeStream \
# MAGIC     .format("parquet") \
# MAGIC     .option("path", "path/to/destination/dir") \
# MAGIC     .option("checkpointLocation", "path/to/checkpoint/dir") \
# MAGIC     .start()
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A. `.option("location", ...)` ❌**  
# MAGIC   → Not a valid option for file sink
# MAGIC
# MAGIC - **B. `.option("destination", ...)` ❌**  
# MAGIC   → Invalid key
# MAGIC
# MAGIC - **C. `.option("location", ...)` ❌**  
# MAGIC   → Same as A, incorrect
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Key Takeaway:**
# MAGIC
# MAGIC 👉 For file-based streaming sinks (Parquet, CSV, JSON):
# MAGIC
# MAGIC - ✔ Use `.option("path", "...")` for output
# MAGIC - ✔ Use `.option("checkpointLocation", "...")` for fault tolerance

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
# MAGIC **Correct Answer: A.**  
# MAGIC Dynamically switching join strategies
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Explanation:**
# MAGIC
# MAGIC In Apache Spark, Adaptive Query Execution (AQE) improves performance by modifying the execution plan at runtime based on actual data characteristics.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔥 **Key capability of AQE:**
# MAGIC
# MAGIC 👉 **Dynamic Join Strategy Switching**
# MAGIC
# MAGIC - Spark can change:  
# MAGIC   Sort-Merge Join → Broadcast Hash Join  
# MAGIC - Happens when runtime stats show one side is small enough  
# MAGIC - Reduces shuffle → improves performance significantly  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **B. Collecting persistent table statistics ❌**  
# MAGIC   → Done via ANALYZE TABLE, not AQE
# MAGIC
# MAGIC - **C. Improving single-stage jobs ❌**  
# MAGIC   → AQE mainly optimizes multi-stage queries involving shuffle
# MAGIC
# MAGIC - **D. Optimizing Delta file layout ❌**  
# MAGIC   → Related to Delta Lake optimizations, not AQE
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Key Takeaway:**
# MAGIC
# MAGIC 👉 AQE = runtime intelligence for Spark queries
# MAGIC
# MAGIC - ✔ Adjusts joins dynamically  
# MAGIC - ✔ Optimizes shuffle partitions  
# MAGIC - ✔ Handles skew

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
# MAGIC **Correct Answer: A.**  
# MAGIC `saveAsTable` with mode `ErrorIfExists`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Explanation:**
# MAGIC
# MAGIC **The requirement is:**
# MAGIC - Create a managed table
# MAGIC - If the table already exists → fail the job
# MAGIC - Do not modify existing data
# MAGIC
# MAGIC ✅ **Correct approach in Apache Spark:**
# MAGIC python
# MAGIC df.write \
# MAGIC   .mode("error") \
# MAGIC   .saveAsTable("finance_table")
# MAGIC
# MAGIC - `saveAsTable` → creates a managed table
# MAGIC - `ErrorIfExists` (default for `"error"`) →
# MAGIC   - ❌ Throws error if table already exists
# MAGIC   - ✔ Ensures no data is overwritten
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **B. Overwrite ❌**  
# MAGIC   → Replaces existing data (violates requirement)
# MAGIC - **C. save with Ignore ❌**  
# MAGIC   → Does nothing if exists (does NOT fail)
# MAGIC - **D. save with ErrorIfExists ❌**  
# MAGIC   → `save()` writes files, not a managed table
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Key Takeaway:**
# MAGIC
# MAGIC 👉 Use:
# MAGIC - `saveAsTable` → for managed tables
# MAGIC - `mode("error")` / `ErrorIfExists` → to fail safely

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
# MAGIC **Correct Answer: A.**  
# MAGIC `.trigger(processingTime='1 second')`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Explanation:**
# MAGIC
# MAGIC **The requirement is:**
# MAGIC
# MAGIC - ✅ Low latency
# MAGIC - ✅ Exactly-once processing
# MAGIC
# MAGIC 🔹 **In Apache Spark Structured Streaming:**
# MAGIC
# MAGIC - ✅ **Processing Time Trigger**
# MAGIC   - `.trigger(processingTime="1 second")`
# MAGIC   - Runs micro-batches every 1 second
# MAGIC   - Provides low latency
# MAGIC   - Supports exactly-once guarantees (with checkpointing)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **B. `.trigger(continuous=True)` ❌**
# MAGIC - **C. `.trigger(continuous='1 second')` ❌**
# MAGIC   - Continuous processing mode:
# MAGIC     - ❌ Does NOT support exactly-once guarantees
# MAGIC     - At best provides at-least-once semantics
# MAGIC     - Also limited operation support
# MAGIC
# MAGIC - **D. `.trigger(availableNow=True)` ❌**
# MAGIC   - Batch-like processing (not continuous streaming)
# MAGIC   - Not suitable for low-latency streaming
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Key Takeaway:**
# MAGIC
# MAGIC 👉 For low latency + exactly-once:
# MAGIC
# MAGIC - ✔ Use micro-batch with small processingTime
# MAGIC - ❌ Avoid continuous mode for strict guarantees

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
# MAGIC **Correct Answer: D.**  
# MAGIC Increase the value of the accuracy parameter in order to increase the memory usage but also improve the accuracy
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Explanation:**
# MAGIC
# MAGIC In Apache Spark, the function:
# MAGIC
# MAGIC `approx_percentile(col, percentage, accuracy)`
# MAGIC
# MAGIC uses an approximation algorithm where:
# MAGIC
# MAGIC - **accuracy** controls the precision of the result  
# MAGIC - Higher accuracy →  
# MAGIC   ✔ Better approximation (closer to true percentile)  
# MAGIC   ❌ More memory usage and slightly slower  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Current Issue:**  
# MAGIC - Accuracy = 1000  
# MAGIC - Result → Faster runtime ✅  
# MAGIC - But percentiles drifting too far ❌
# MAGIC
# MAGIC 👉 This means accuracy is too low
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Solution:**
# MAGIC
# MAGIC Increase accuracy:
# MAGIC
# MAGIC `F.approx_percentile("price", [0.25, 0.5, 0.75], 10000)`
# MAGIC
# MAGIC - ✔ Improves precision  
# MAGIC - ✔ Reduces drift  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A. Decrease percentage value ❌**  
# MAGIC   → Changes percentile points (not accuracy)
# MAGIC - **B. Decrease accuracy ❌**  
# MAGIC   → Makes results less accurate
# MAGIC - **C. Increase percentage value ❌**  
# MAGIC   → Changes percentile range, not precision
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Key Takeaway:**
# MAGIC
# MAGIC 👉 In `approx_percentile()`:
# MAGIC
# MAGIC - accuracy ↑ → precision ↑ → memory ↑  
# MAGIC - accuracy ↓ → faster but less accurate

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
# MAGIC **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC In a broadcast join in Apache Spark:
# MAGIC
# MAGIC - The smaller DataFrame is broadcasted to all worker nodes.
# MAGIC - This allows Spark to avoid shuffling the larger DataFrame, which is the main performance benefit.
# MAGIC
# MAGIC **In this case:**
# MAGIC - DataFrame A = 128 GB (very large)
# MAGIC - DataFrame B = 1 GB (small enough to broadcast)
# MAGIC
# MAGIC **So:**
# MAGIC
# MAGIC - Broadcasting DataFrame B sends it to all executors.
# MAGIC - Each executor can then join it locally with partitions of DataFrame A.
# MAGIC - This eliminates the need to shuffle DataFrame A, which is expensive.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Why Option B is correct:**
# MAGIC
# MAGIC - Broadcasting B avoids shuffling A → major performance gain
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Why others are wrong:**
# MAGIC
# MAGIC - **A:** Incorrect focus — broadcasting avoids shuffling the other DataFrame, not itself.
# MAGIC - **C/D:** Broadcasting a large dataset (128 GB) is inefficient and not feasible.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Always broadcast the smaller DataFrame to avoid shuffling the larger one.

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
# MAGIC
# MAGIC **Correct Answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC Spark Connect is a feature introduced to enable a client-server architecture for Apache Spark.
# MAGIC
# MAGIC **Key idea:**
# MAGIC - The client (e.g., Python, Scala, or other interfaces) connects to a remote Spark cluster.
# MAGIC - The actual execution of Spark jobs happens remotely on the cluster, not on the client.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Why Option C is correct:**
# MAGIC
# MAGIC - It allows for remote execution of Spark jobs
# MAGIC
# MAGIC ✔ **Spark Connect lets users:**
# MAGIC - Submit queries from a client
# MAGIC - Execute them remotely on the Spark cluster
# MAGIC - Receive results back
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Why other options are incorrect:**
# MAGIC
# MAGIC - **A. ❌ Misleading** — Spark Connect supports specific APIs (like DataFrame API), not any programming language.
# MAGIC - **B. ❌ Incorrect** — Spark Connect does not rely on REST APIs; it uses a structured protocol (like gRPC).
# MAGIC - **D. ❌ Incorrect** — It is not designed for data ingestion; it's about remote interaction and execution.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Spark Connect = remote client → remote Spark execution (cluster-side processing)

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
# MAGIC **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC Broadcast variables in Spark are intended for small datasets that can fit comfortably in memory on each executor.
# MAGIC
# MAGIC **What happens in this scenario:**  
# MAGIC The engineer is trying to broadcast a DataFrame with millions of rows (i.e., large dataset).  
# MAGIC Spark will attempt to:
# MAGIC - Serialize the DataFrame on the driver
# MAGIC - Send it to every executor
# MAGIC - Store it in memory on each executor
# MAGIC
# MAGIC **Why Option A is correct:**
# MAGIC
# MAGIC If the dataset is too large, executors may not have enough memory, causing the job to fail (e.g., OutOfMemory errors).
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Why other options are incorrect:**
# MAGIC
# MAGIC - **B. ❌** CPU cores are not the limiting factor here — memory is.
# MAGIC - **C. ❌** Spark may slow down or fail, but it won’t typically hang indefinitely.
# MAGIC - **D. ❌** Serialization is more about memory, not CPU cores on the driver.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Only broadcast small datasets; broadcasting large datasets can cause executor memory failures.

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
# MAGIC **The correct answer is A. It supports DataStreamReader, DataStreamWriter, StreamingQuery Streaming APIs.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Below is an analysis of why this option is correct and why the others are not:**
# MAGIC
# MAGIC - ✅ **Option A is correct:**  
# MAGIC   Spark Connect supports the majority of the Structured Streaming API, which includes essential interfaces such as DataStreamReader, DataStreamWriter, and StreamingQuery.
# MAGIC
# MAGIC - ❌ **Option B is incorrect:**  
# MAGIC   While Spark Connect supports DataFrame, Functions, and Column APIs, it does not support SparkContext or the RDD API. These are intentionally unavailable because the client-server architecture isolates the client from the Spark driver JVM.
# MAGIC
# MAGIC - ❌ **Option C is incorrect:**  
# MAGIC   Spark Connect is designed to be language-agnostic. While it initially focused on PySpark, it also supports Scala (starting in Spark 3.5) and has foundations for other languages like Go and Rust.
# MAGIC
# MAGIC - ❌ **Option D is incorrect:**  
# MAGIC   Spark Connect does not have built-in authentication. Instead, its gRPC interface is designed to work with existing infrastructure, such as authenticating proxies, to secure connections.

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
# MAGIC **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement is to compute the average temperature per sensor over the last 5 minutes in a streaming DataFrame. This is a time-based windowed aggregation, which is handled in Spark Structured Streaming using window + watermark.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option D is correct:**
# MAGIC python
# MAGIC df.withWatermark("timestamp", "5 minutes")
# MAGIC   .groupBy("sensor_id", window("timestamp", "5 minutes"))
# MAGIC   .agg(avg("temperature").alias("avg_temp"))
# MAGIC
# MAGIC - `window("timestamp", "5 minutes")` → creates 5-minute time windows  
# MAGIC - `groupBy("sensor_id", window(...))` → calculates per sensor per window  
# MAGIC - `withWatermark()` → manages late-arriving data in streaming  
# MAGIC - `avg()` → computes the required aggregation  
# MAGIC
# MAGIC ✔ This is the standard and correct approach for streaming time-window aggregations.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A. Uses over(Window...)**  
# MAGIC   → Not supported for streaming aggregations like this; also not proper for time-windowed streaming
# MAGIC
# MAGIC - **B. Groups by exact timestamp**  
# MAGIC   → No 5-minute window → produces per-second aggregation instead
# MAGIC
# MAGIC - **C. No time window**  
# MAGIC   → Computes overall average, not restricted to last 5 minutes
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 For streaming + time-based calculations → always use  
# MAGIC `window()` + `groupBy()` + optional `withWatermark()`

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
# MAGIC **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement has two parts:
# MAGIC
# MAGIC 1. Get unique values from the Name column  
# MAGIC 2. Return them in alphabetical order  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option B:**  
# MAGIC `df.select("Name").distinct().orderBy(df["Name"])`
# MAGIC
# MAGIC - ✔ `select("Name")` → selects the column  
# MAGIC - ✔ `distinct()` → removes duplicates  
# MAGIC - ✔ `orderBy(df["Name"])` → sorts in ascending (alphabetical) order by default  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are incorrect:**
# MAGIC
# MAGIC **A.**  
# MAGIC `df.select("Name").orderBy(df["Name"].asc())`  
# MAGIC → ❌ Missing distinct() → duplicates will remain
# MAGIC
# MAGIC **C.**  
# MAGIC `df.select("Name").distinct()`  
# MAGIC → ❌ No sorting → results not ordered
# MAGIC
# MAGIC **D.**  
# MAGIC `df.select("Name").distinct().orderBy(df["Name"].desc())`  
# MAGIC → ❌ Sorted in descending order, not alphabetical (ascending)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Use `distinct()` + `orderBy()` to get unique + sorted results in Spark.

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
# MAGIC
# MAGIC The correct sequence of operations is Option A.
# MAGIC
# MAGIC Option A involves:  
# MAGIC df.filter(...): A narrow transformation that does not require a shuffle.  
# MAGIC df.groupBy("user_id").sum(...): A wide transformation that requires a shuffle to group records with the same user_id into the same partition.    
# MAGIC
# MAGIC However, the question asks for a shuffle followed by a transformation that does not. Looking at the logic across all options:  
# MAGIC
# MAGIC - **A:** filter (No Shuffle)  
# MAGIC   groupBy (Shuffle). This is the reverse of what was asked.  
# MAGIC - **B:** withColumn (No Shuffle)  
# MAGIC   select (No Shuffle). Neither requires a shuffle.  
# MAGIC - **C:** withColumn (No Shuffle)  
# MAGIC   where (No Shuffle). Neither requires a shuffle.  
# MAGIC - **D:** groupBy(...).agg(...) (Shuffle)  
# MAGIC   repartition(10) (Shuffle). Both require a shuffle.

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
# MAGIC **Correct Answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC To diagnose performance issues, Executor logs are best accessed through the Spark UI, which provides direct visibility into each executor.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option C is correct:**
# MAGIC
# MAGIC Use the Spark UI to select the stage and view the executor logs directly
# MAGIC
# MAGIC - In the Spark UI, you can:
# MAGIC   - Navigate to Stages → Tasks
# MAGIC   - Click on a specific task
# MAGIC   - Access stdout / stderr logs for each executor
# MAGIC
# MAGIC 👉 This is the standard and easiest way to debug performance issues.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ Logs are not centrally stored on the master node (depends on cluster manager like YARN/K8s)
# MAGIC - **B.** ❌ --verbose only prints submission details, not executor logs
# MAGIC - **D.** ❌ spark-sql CLI is unrelated to fetching executor logs
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Use the Spark UI → Executors / Stages → Logs to inspect executor behavior and debug issues efficiently.

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
# MAGIC
# MAGIC **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC In Spark cluster mode:
# MAGIC
# MAGIC - The driver program runs inside the cluster (on a worker node or cluster manager node)
# MAGIC - This allows the application to:
# MAGIC   - Fully leverage cluster resources
# MAGIC   - Avoid dependency on the client machine
# MAGIC   - Be more fault-tolerant and scalable
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option D is correct:**
# MAGIC
# MAGIC - The driver runs on a worker node, enabling full use of distributed resources
# MAGIC - ✔ This is the core defining feature of cluster mode.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ Resource allocation happens in both client and cluster mode, not unique to cluster mode
# MAGIC - **B.** ❌ Completely incorrect — Spark always distributes tasks across executors
# MAGIC - **C.** ❌ Describes client mode, not cluster mode
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Cluster Mode = Driver runs inside the cluster  
# MAGIC 👉 Client Mode = Driver runs on the client machine
# MAGIC
# MAGIC This is the main difference and advantage of cluster mode.

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
# MAGIC **Correct Answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The method `getOrCreate()` in `SparkSession.builder` works as follows:
# MAGIC
# MAGIC - If a SparkSession already exists, it returns the existing one
# MAGIC - If not, it creates a new SparkSession
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option C is correct:**
# MAGIC
# MAGIC If a SparkSession already exists, this code will return the existing session instead of creating a new one.
# MAGIC
# MAGIC ✔ This is the exact behavior of `getOrCreate()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ It does not destroy an existing session
# MAGIC - **B.** ❌ SparkSession is not tied to appName uniqueness
# MAGIC - **D.** ❌ A new session is not created every time
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 `getOrCreate()` = reuse existing session OR create new if none exists

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
# MAGIC **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The original code has multiple issues:
# MAGIC
# MAGIC - Invalid syntax: `return answer 3.14159`
# MAGIC - Mismatch between:
# MAGIC   - Input type
# MAGIC   - Return type
# MAGIC   - UDF declared return type
# MAGIC
# MAGIC **Key rule in PySpark UDFs:**
# MAGIC
# MAGIC 👉 The declared return type (`T.*Type()`) must match the actual returned value
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option B:**
# MAGIC python
# MAGIC @F.udf(T.DoubleType())
# MAGIC def simple_udf(t: float) -> float:
# MAGIC     return t * 3.14159
# MAGIC
# MAGIC - ✔ `t * 3.14159` produces a floating-point (double) value
# MAGIC - ✔ Return type is correctly declared as `DoubleType`
# MAGIC - ✔ Input and output types are consistent
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why others are incorrect:**
# MAGIC
# MAGIC **A.**
# MAGIC python
# MAGIC @F.udf(T.IntegerType())
# MAGIC def simple_udf(t: int) -> int:
# MAGIC     return t * 3.14159
# MAGIC
# MAGIC - ❌ Returns float but declared as Integer → type mismatch
# MAGIC
# MAGIC **C.**
# MAGIC python
# MAGIC @F.udf(T.DoubleType())
# MAGIC def simple_udf(t: int) -> int:
# MAGIC
# MAGIC - ❌ Function annotation says int return, but actual result is float
# MAGIC
# MAGIC **D.**
# MAGIC python
# MAGIC @F.udf(T.IntegerType())
# MAGIC def simple_udf(t: float) -> float:
# MAGIC
# MAGIC - ❌ Returns float but declared as Integer → mismatch
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Always ensure:
# MAGIC
# MAGIC - Returned value type = Declared Spark SQL type
# MAGIC
# MAGIC Otherwise → runtime errors or incorrect results

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
# MAGIC **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement is to remove duplicate rows across all columns (i.e., rows that are completely identical).
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option A:**  
# MAGIC `df = df.dropDuplicates()`
# MAGIC
# MAGIC - ✔ Removes duplicate rows based on all columns
# MAGIC - ✔ Keeps only unique records across the entire DataFrame
# MAGIC - ✔ This is the correct and simplest approach
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **B.**  
# MAGIC `df.groupBy("transaction_id").agg(...)`
# MAGIC
# MAGIC - ❌ Only deduplicates based on transaction_id
# MAGIC - ❌ May lose data if other columns differ
# MAGIC
# MAGIC **C.**  
# MAGIC `df.filter(F.col("transaction_id").isNotNull())`
# MAGIC
# MAGIC - ❌ Only removes nulls, not duplicates
# MAGIC
# MAGIC **D.**  
# MAGIC `df.dropDuplicates(["transaction_amount"])`
# MAGIC
# MAGIC - ❌ Deduplicates based only on transaction_amount
# MAGIC - ❌ Different transactions with same amount may be incorrectly removed
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Use `dropDuplicates()` with no arguments to remove fully identical rows across all columns

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
# MAGIC **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement includes three key points:
# MAGIC
# MAGIC - Write data in Parquet format  
# MAGIC - Partition by country  
# MAGIC - Overwrite existing data  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option A:**  
# MAGIC `df.write.mode("overwrite").partitionBy("country").parquet("/data/output")`
# MAGIC
# MAGIC - ✔ `mode("overwrite")` → replaces existing data  
# MAGIC - ✔ `partitionBy("country")` → creates partitioned folders by country  
# MAGIC - ✔ `.parquet(...)` → writes in Parquet format  
# MAGIC
# MAGIC 👉 This satisfies all requirements
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **B.**  
# MAGIC `mode("append")`  
# MAGIC → ❌ Appends data instead of overwriting
# MAGIC
# MAGIC **C.**  
# MAGIC `mode("overwrite").parquet(...)`  
# MAGIC → ❌ Missing partitioning
# MAGIC
# MAGIC **D.**  
# MAGIC `partitionBy("country")`  
# MAGIC → ❌ Missing overwrite mode (defaults to error if path exists)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Use:  
# MAGIC - `mode("overwrite")` → replace data  
# MAGIC - `partitionBy()` → optimize storage & queries  
# MAGIC - `.parquet()` → columnar storage format

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
# MAGIC **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**  
# MAGIC The requirement is to:
# MAGIC
# MAGIC - Ensure schema is correctly defined
# MAGIC - Read data efficiently
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option D:**  
# MAGIC `spark.read.schema(predefinedSchema).json("path")`  
# MAGIC - ✔ Uses a predefined StructType schema  
# MAGIC - ✔ Avoids schema inference overhead  
# MAGIC - ✔ Ensures correct data types from the start  
# MAGIC - ✔ Most efficient and production-ready approach
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **A.**  
# MAGIC - Infers schema first, then modifies → ❌ inefficient and error-prone
# MAGIC
# MAGIC **B.**  
# MAGIC - inferSchema = true  
# MAGIC - ❌ Schema inference is slow for large datasets
# MAGIC
# MAGIC **C.**  
# MAGIC - Reads without schema, then casts columns → ❌ inefficient and verbose
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**  
# MAGIC 👉 For large datasets:  
# MAGIC - Always use predefined schema (StructType)  
# MAGIC - Avoid inferSchema for better performance and reliability

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
# MAGIC **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC When reading from Kafka in Spark Structured Streaming, you must specify the topic using the correct option key.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option A:**  
# MAGIC `.option("subscribe", "feed")`
# MAGIC
# MAGIC - ✔ This tells Spark to subscribe to the Kafka topic `feed`
# MAGIC - ✔ This is the standard and correct configuration
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **B.**  
# MAGIC `.option("subscribe.topic", "feed")`  
# MAGIC - ❌ Invalid option key
# MAGIC
# MAGIC **C.**  
# MAGIC `.option("kafka.topic", "feed")`  
# MAGIC - ❌ Not a recognized Kafka option
# MAGIC
# MAGIC **D.**  
# MAGIC `.option("topic", "feed")`  
# MAGIC - ❌ Incorrect key (missing subscribe or assign)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 To read from Kafka in Spark:  
# MAGIC Use `.option("subscribe", "topic_name")` for topic subscription

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
# MAGIC **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirements are:
# MAGIC
# MAGIC - Processing large structured data
# MAGIC - Performing SQL queries
# MAGIC - Applying machine learning algorithms
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option D:**
# MAGIC
# MAGIC **Spark DataFrames, Spark SQL, and MLlib**
# MAGIC
# MAGIC - ✔ Spark DataFrames → efficient structured data processing
# MAGIC - ✔ Spark SQL → run SQL queries on structured data
# MAGIC - ✔ MLlib → machine learning library for Spark
# MAGIC
# MAGIC 👉 This combination perfectly matches all requirements
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ Includes GraphX (graph processing) and Streaming (not required)
# MAGIC - **B.** ❌ Missing MLlib → no machine learning capability
# MAGIC - **C.** ❌ Focuses on streaming and graph processing, not SQL + ML
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 For data processing + SQL + ML:
# MAGIC
# MAGIC Use DataFrames + Spark SQL + MLlib

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
# MAGIC **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**  
# MAGIC The requirement is to split the email column into two parts:
# MAGIC
# MAGIC - **username** (before @)
# MAGIC - **domain** (after @)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option B:**  
# MAGIC python
# MAGIC customerDF.withColumn("username", split(col("email"), "@").getItem(0)) \
# MAGIC           .withColumn("domain", split(col("email"), "@").getItem(1))
# MAGIC
# MAGIC - ✔ `split(col("email"), "@")` → splits email into array [username, domain]
# MAGIC - ✔ `.getItem(0)` → extracts username
# MAGIC - ✔ `.getItem(1)` → extracts domain  
# MAGIC 👉 This is the most standard and correct PySpark approach
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **A.**  
# MAGIC `substr(0, 5)`  
# MAGIC - ❌ Assumes fixed length → emails vary in length
# MAGIC
# MAGIC **C.**  
# MAGIC `substring_index(...)`  
# MAGIC - ❌ Not a standard PySpark function (comes from SQL dialects like MySQL)
# MAGIC
# MAGIC **D.**  
# MAGIC `regexp_replace(...)`  
# MAGIC - ❌ Removes @ but does not split → both columns become identical
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**  
# MAGIC 👉 Use `split()` + `getItem()` to extract parts of a string column in PySpark

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
# MAGIC **Correct Answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirements are:
# MAGIC
# MAGIC - Create an external table
# MAGIC - Read from JSON file (`/data/input.json`)
# MAGIC - Infer schema automatically
# MAGIC - Handle varying schemas (merge them)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option C:**
# MAGIC sql
# MAGIC CREATE EXTERNAL TABLE users
# MAGIC USING json
# MAGIC OPTIONS (path '/data/input.json', mergeSchema 'true')
# MAGIC
# MAGIC - ✔ `USING json` → reads JSON format
# MAGIC - ✔ `path` → points to the data location
# MAGIC - ✔ `mergeSchema 'true'` → handles varying schemas across records/files
# MAGIC - ✔ Schema is inferred automatically
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **A.**
# MAGIC sql
# MAGIC CREATE TABLE users USING json ...
# MAGIC
# MAGIC - ❌ Not explicitly external (though Spark treats it similarly, exam expects explicit external)
# MAGIC
# MAGIC **B.**
# MAGIC sql
# MAGIC CREATE EXTERNAL TABLE users USING json OPTIONS (path ...)
# MAGIC
# MAGIC - ❌ Missing schema merging
# MAGIC
# MAGIC **D.**
# MAGIC - `schemaMerge 'true'`
# MAGIC - ❌ Incorrect option name (should be `mergeSchema`)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Use:
# MAGIC - `USING json`
# MAGIC - `path`
# MAGIC - `mergeSchema = true`
# MAGIC
# MAGIC for external JSON tables with evolving schema

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
# MAGIC **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC In Spark Structured Streaming, a watermark defines how long Spark will wait for late-arriving data.
# MAGIC
# MAGIC python
# MAGIC .withWatermark("event_time", "10 minutes")
# MAGIC
# MAGIC
# MAGIC 👉 This means:
# MAGIC
# MAGIC - Spark will accept late data up to 10 minutes
# MAGIC - After that, data is considered too late and will be dropped
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option B is correct:**
# MAGIC
# MAGIC - Data arriving more than 10 minutes late will be ignored
# MAGIC - ✔ Records older than the watermark threshold are:
# MAGIC   - Discarded
# MAGIC   - Not included in aggregation
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ Late data beyond watermark is not included
# MAGIC - **C.** ❌ Data is not shifted to another window
# MAGIC - **D.** ❌ Partially true but incomplete — doesn’t mention dropping late data
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Watermark = maximum allowed lateness  
# MAGIC - Within threshold → ✅ processed  
# MAGIC - Beyond threshold → ❌ dropped

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
# MAGIC **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The code:
# MAGIC
# MAGIC python
# MAGIC df.write.partitionBy("color", "fruit").parquet("/path/to/output")
# MAGIC
# MAGIC
# MAGIC uses partitioning, which organizes output data into a directory structure based on column values.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **What happens:**
# MAGIC
# MAGIC Spark will create separate directories for each unique combination of color and fruit, like:
# MAGIC
# MAGIC
# MAGIC /path/to/output/
# MAGIC   color=red/fruit=apple/
# MAGIC   color=red/fruit=banana/
# MAGIC   color=green/fruit=apple/
# MAGIC   ...
# MAGIC
# MAGIC
# MAGIC - ✔ Each partition contains corresponding data files
# MAGIC - ✔ Improves query performance via partition pruning
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ Data is split across multiple files and directories, not a single file
# MAGIC - **B.** ❌ Null values do not cause errors (they create color=null folders)
# MAGIC - **C.** ❌ Default mode is error/overwrite, not append (unless specified)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 `partitionBy()` creates a directory structure based on column values, not just files.

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
# MAGIC **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC To overwrite existing data while writing a DataFrame in Spark, you must explicitly set the write mode to "overwrite".
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option A:**  
# MAGIC `df.write.mode("overwrite").json("path/to/file")`
# MAGIC
# MAGIC - ✔ Correct syntax  
# MAGIC - ✔ Uses `.mode("overwrite")` to replace existing data  
# MAGIC - ✔ Writes in JSON format  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **B.**  
# MAGIC `df.write.overwrite.json(...)`  
# MAGIC - ❌ Invalid API — `.overwrite` is not a valid method
# MAGIC
# MAGIC **C.**  
# MAGIC `overwrite=True`  
# MAGIC - ❌ Not a valid parameter in Spark write API
# MAGIC
# MAGIC **D.**  
# MAGIC `df.write.format("json").save("path", mode="overwrite")`  
# MAGIC - ❌ Incorrect — mode is not passed inside `save()` like this
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Always use:  
# MAGIC - `.mode("overwrite")` before writing  
# MAGIC - Works for all formats (JSON, Parquet, etc.)

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
# MAGIC **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC Spark uses lazy evaluation, meaning transformations are not executed immediately. Instead, Spark builds a logical execution plan and only executes it when an action is called.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **In this code:**
# MAGIC
# MAGIC **Transformations (lazy):**
# MAGIC - filter()
# MAGIC - select()
# MAGIC - groupBy().sum()
# MAGIC
# MAGIC 👉 These do NOT trigger execution
# MAGIC
# MAGIC **Actions (trigger execution):**
# MAGIC - reduced_df.count() ✅
# MAGIC - reduced_df.show() ✅
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option B is correct:**
# MAGIC
# MAGIC - Processing begins when the first action (count()) is called
# MAGIC - ✔ This is the first action in the code
# MAGIC - ✔ Spark starts executing the entire DAG here
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ filter() is a transformation (lazy)
# MAGIC - **C.** ❌ groupBy() is also a transformation
# MAGIC - **D.** ❌ show() is an action, but it occurs after count()
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Spark execution starts only when an action is triggered  
# MAGIC 👉 First action in the code = execution start point

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
# MAGIC **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The goal is to remove duplicate records introduced during ingestion.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **Key insight:**  
# MAGIC Original event fields:  
# MAGIC - event_ts  
# MAGIC - sensor_id  
# MAGIC - metric_value  
# MAGIC
# MAGIC Ingestion-added fields:  
# MAGIC - ingest_ts  
# MAGIC - source_file_path  
# MAGIC
# MAGIC 👉 Duplicates occur when the same event is ingested multiple times, but:  
# MAGIC - ingest_ts and source_file_path may differ
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option D is correct:**  
# MAGIC `dedup_df = iot_bronze_df.dropDuplicates(["event_ts", "sensor_id", "metric_value"])`
# MAGIC
# MAGIC - ✔ Removes duplicates based on true event identity  
# MAGIC - ✔ Ignores ingestion-specific fields  
# MAGIC - ✔ Keeps only one record per unique event
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **A.**  
# MAGIC dropDuplicates(["ingest_ts", ...])  
# MAGIC - ❌ Includes ingestion fields → duplicates won’t be removed
# MAGIC
# MAGIC **B.**  
# MAGIC dropDuplicates()  
# MAGIC - ❌ Uses all columns → ingestion differences prevent deduplication
# MAGIC
# MAGIC **C.**  
# MAGIC groupBy(...)  
# MAGIC - ❌ Not a deduplication method (needs aggregation)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**  
# MAGIC 👉 Deduplicate using business keys (true event fields), not ingestion metadata

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
# MAGIC **Correct Answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The `broadcast()` function is used to optimize joins when one DataFrame is significantly smaller than the other.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option C is correct:**
# MAGIC
# MAGIC - It reduces shuffle by replicating the smaller DataFrame to all nodes
# MAGIC - ✔ df1 (small) is broadcasted to all executors
# MAGIC - ✔ Each executor can join its partition of df2 locally
# MAGIC - ✔ No shuffle required for the large DataFrame (df2)
# MAGIC - 👉 This significantly improves performance
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ broadcast() does not filter data
# MAGIC - **B.** ❌ Does not change partition size
# MAGIC - **D.** ❌ Join condition (on='id') handles matching, not broadcast()
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 broadcast() = send small dataset to all nodes → avoid shuffling large dataset

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
# MAGIC **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement is to:
# MAGIC
# MAGIC - Reduce number of partitions
# MAGIC - Avoid a full shuffle
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option B is correct:**  
# MAGIC `df.coalesce(num_partitions)`
# MAGIC
# MAGIC - ✔ Reduces partitions without full shuffle
# MAGIC - ✔ Merges existing partitions efficiently
# MAGIC - ✔ Ideal when decreasing partition count
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **A.**  
# MAGIC `distinct()`
# MAGIC - ❌ Removes duplicates, not partitions
# MAGIC - ❌ Causes a shuffle
# MAGIC
# MAGIC **C.**  
# MAGIC `sortBy()`
# MAGIC - ❌ Triggers shuffle for sorting
# MAGIC - ❌ Not for partition control
# MAGIC
# MAGIC **D.**  
# MAGIC `repartition()`
# MAGIC - ❌ Always causes a full shuffle
# MAGIC - ❌ Expensive operation
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Use:  
# MAGIC - `coalesce()` → reduce partitions (no shuffle)  
# MAGIC - `repartition()` → increase/rebalance partitions (with shuffle)

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
# MAGIC **Correct Answers: D and E**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirements are:
# MAGIC
# MAGIC - Large-scale data processing
# MAGIC - High-level APIs for SQL queries
# MAGIC - Support for batch and streaming workloads
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **D. It provides built-in support for SQL queries through Spark SQL**
# MAGIC
# MAGIC - ✔ Spark SQL allows:
# MAGIC   - Writing SQL queries on large datasets
# MAGIC   - Seamless integration with DataFrames
# MAGIC   - 👉 Directly satisfies the SQL requirement
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **E. It offers mature APIs for DataFrames and Datasets**
# MAGIC
# MAGIC - ✔ Provides:
# MAGIC   - High-level abstractions for data processing
# MAGIC   - Optimized execution via Catalyst optimizer
# MAGIC   - 👉 Essential for efficient large-scale data manipulation
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ Spark is not serverless; it requires cluster/resource management
# MAGIC - **B.** ❌ Not designed for frontend/web development
# MAGIC - **C.** ❌ MLlib exists, but ML is not the core requirement here
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Spark’s strengths:
# MAGIC - Spark SQL (for queries)
# MAGIC - DataFrame/Dataset APIs (for scalable processing)

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
# MAGIC **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC In Apache Spark, execution is organized in a hierarchical manner:
# MAGIC
# MAGIC **Job → Stages → Tasks**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option A is correct:**
# MAGIC
# MAGIC - A job contains multiple stages, and each stage contains multiple tasks
# MAGIC
# MAGIC **✔ Job**
# MAGIC - Triggered by an action (e.g., `count()`, `show()`)
# MAGIC
# MAGIC **✔ Stage**
# MAGIC - A job is divided into stages based on shuffle boundaries
# MAGIC
# MAGIC **✔ Task**
# MAGIC - Each stage is split into tasks
# MAGIC - Each task processes one partition of data
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **B.** Tasks do not contain stages
# MAGIC - **C.** Stages are part of jobs, not the other way around
# MAGIC - **D.** Tasks are the smallest unit, they don’t contain jobs
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Job = full computation  
# MAGIC 👉 Stage = set of parallel operations (no shuffle within)  
# MAGIC 👉 Task = work on a single partition

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
# MAGIC **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC It executes queries faster using all the available cores in the cluster as well as provides Pandas's rich set of features.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation**
# MAGIC
# MAGIC The pandas API on Spark (formerly known as Koalas) was specifically designed to scale the familiar Pandas interface to big data workloads by leveraging Spark's distributed computing engine.
# MAGIC
# MAGIC - **Parallel Execution:** While standard Pandas is limited to single-node, single-core execution, Pandas on Spark utilizes all available cores in a cluster to parallelize computations, often making it significantly faster even on a single machine.
# MAGIC - **Familiar API:** It allows data scientists to use their existing Pandas knowledge and code with minimal changes while benefiting from Spark's query optimization and scalability.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Why the other options are incorrect:**
# MAGIC
# MAGIC - ❌ **A:** While it is a Python API, its primary benefit is scalability rather than just being "Python-only." Standard Pandas is also Python-based, so this does not distinguish the two in terms of learning curve reduction for existing Python users.
# MAGIC - ❌ **B:** Actually, Pandas on Spark uses lazy evaluation, meaning it builds an execution plan and only runs computations when a result is requested. Standard Pandas uses eager execution.
# MAGIC - ❌ **C:** One of the main reasons to use Spark is that it does not run on a single node only. It is designed to scale across multiple machines in a cluster to handle datasets that are much larger than a single machine's memory.

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
# MAGIC **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC By default:
# MAGIC
# MAGIC `spark.read.text(...)`
# MAGIC
# MAGIC 👉 Reads each line as a separate row
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Requirement:**  
# MAGIC Each record should contain:  
# MAGIC - Entire file content (not line-by-line)  
# MAGIC - File path  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option A:**  
# MAGIC `spark.read.option("wholetext", True).text(raw_txt_path)`
# MAGIC
# MAGIC - ✔ Reads entire file as a single record  
# MAGIC - ✔ Each row = one file’s full content  
# MAGIC - ✔ Works perfectly with _metadata.file_path  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **B.**  
# MAGIC `linesep="\n"`  
# MAGIC - ❌ Still processes line-by-line  
# MAGIC
# MAGIC **C.**  
# MAGIC `wholetext=False`  
# MAGIC - ❌ Default behavior → line-based  
# MAGIC
# MAGIC **D.**  
# MAGIC `lineSep=","`  
# MAGIC - ❌ Changes delimiter, not file-level reading  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Use `wholetext=True` to read entire file content as a single row in Spark

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
# MAGIC **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The number of parallel tasks per executor in Spark is determined by:
# MAGIC
# MAGIC ✅ **spark.executor.cores**
# MAGIC
# MAGIC - ✔ Defines how many CPU cores are allocated per executor
# MAGIC - ✔ Each core can run one task at a time
# MAGIC
# MAGIC 👉 **So:**
# MAGIC
# MAGIC Number of parallel tasks per executor = number of executor cores
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **B. spark.task.maxFailures**  
# MAGIC - ❌ Controls retry attempts for failed tasks
# MAGIC
# MAGIC **C. spark.driver.cores**  
# MAGIC - ❌ Refers to driver, not executors
# MAGIC
# MAGIC **D. spark.executor.memory**  
# MAGIC - ❌ Controls memory, not parallel task count
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Parallelism per executor = spark.executor.cores

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
# MAGIC **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC In Local Mode, Spark runs on a single machine and uses threads to simulate parallelism.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option B is correct:**
# MAGIC
# MAGIC Increase the number of local threads based on CPU cores
# MAGIC
# MAGIC - ✔ You can configure:
# MAGIC
# MAGIC   - `spark.master("local[*]")`  
# MAGIC     `*` → uses all available CPU cores
# MAGIC
# MAGIC   - Or specify explicitly:  
# MAGIC     `spark.master("local[4]")`
# MAGIC
# MAGIC 👉 This ensures maximum CPU utilization during testing
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ Cluster mode is not local testing
# MAGIC - **C.** ❌ Dynamic allocation is for cluster environments
# MAGIC - **D.** ❌ Increasing memory alone doesn’t optimize CPU usage
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 In local mode:  
# MAGIC Use `local[*]` to utilize all CPU cores efficiently

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
# MAGIC **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement is to extract the date part from a timestamp column.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option B:**  
# MAGIC `dates_df.withColumn("date", f.to_date("timestamp")).show()`
# MAGIC
# MAGIC - ✔ `to_date()` converts a timestamp → date
# MAGIC - ✔ Output type is `DateType` (correct and clean)
# MAGIC - ✔ Removes time portion
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **A.**  
# MAGIC `unix_timestamp()`
# MAGIC - ❌ Converts to epoch seconds, not a date
# MAGIC
# MAGIC **C.**  
# MAGIC `date_format()`
# MAGIC - ❌ Returns a string, not a date type
# MAGIC
# MAGIC **D.**  
# MAGIC `from_unixtime()`
# MAGIC - ❌ Converts epoch → timestamp string, not applicable here
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Use `to_date()` to extract the date part from a timestamp column

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
# MAGIC **Correct Answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement is:
# MAGIC
# MAGIC - Use micro-batch processing
# MAGIC - Trigger execution every 5 seconds
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option C:**
# MAGIC python
# MAGIC query = df.writeStream \
# MAGIC     .outputMode("append") \
# MAGIC     .trigger(processingTime="5 seconds") \
# MAGIC     .start()
# MAGIC
# MAGIC - ✔ `processingTime="5 seconds"` → runs query every 5 seconds
# MAGIC - ✔ Uses micro-batch mode (default in Structured Streaming)
# MAGIC - ✔ Correct syntax and behavior
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **A.**
# MAGIC python
# MAGIC trigger(continuous="5 seconds")
# MAGIC
# MAGIC - ❌ Continuous processing mode (experimental, not micro-batch)
# MAGIC
# MAGIC **B.**
# MAGIC python
# MAGIC trigger()
# MAGIC
# MAGIC - ❌ Uses default trigger (as fast as possible), not fixed interval
# MAGIC
# MAGIC **D.**
# MAGIC python
# MAGIC processingTime=5000
# MAGIC
# MAGIC - ❌ Incorrect format — must be a string with time unit
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 For fixed micro-batch intervals:  
# MAGIC Use `trigger(processingTime="X seconds")`

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
# MAGIC **Correct Answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement:  
# MAGIC 👉 Remove any record that contains at least one NULL value
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option C:**  
# MAGIC `filtered_df = users_raw_df.na.drop(how='any')`
# MAGIC
# MAGIC - ✔ `how='any'` → drops rows if ANY column has NULL
# MAGIC - ✔ Ensures only fully complete records remain
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **A.**  
# MAGIC `thresh=0`  
# MAGIC - ❌ Keeps all rows (even fully null ones) → ineffective
# MAGIC
# MAGIC **B.**  
# MAGIC `how='all'`  
# MAGIC - ❌ Drops only rows where all columns are NULL
# MAGIC
# MAGIC **D.**  
# MAGIC `how='all', thresh=None`  
# MAGIC - ❌ Same as B → not strict enough
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Use:  
# MAGIC - `how='any'` → drop rows with ANY null  
# MAGIC - `how='all'` → drop rows with ALL nulls

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
# MAGIC **Correct Answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC When using `saveAsTable()`, Spark by default stores data in the warehouse directory unless a custom path is explicitly provided.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option C:**  
# MAGIC `users.write.option("path", "/some/path").saveAsTable("default_table")`
# MAGIC
# MAGIC - ✔ Specifies a custom storage location  
# MAGIC - ✔ Overrides default warehouse path  
# MAGIC - ✔ Correct syntax for setting options before saving
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **A.**  
# MAGIC `write(path=...).saveAsTable()`
# MAGIC
# MAGIC - ❌ Invalid syntax — write() doesn’t accept path directly
# MAGIC
# MAGIC **B.**  
# MAGIC `saveAsTable().option(...)`
# MAGIC
# MAGIC - ❌ Options must be set before saving
# MAGIC
# MAGIC **D.**  
# MAGIC `saveAsTable(..., path=...)`
# MAGIC
# MAGIC - ❌ saveAsTable() does not accept path as a parameter
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 To control table storage location:  
# MAGIC Use `.option("path", "...")` before `saveAsTable()`

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
# MAGIC **Correct Answer: B. Persist the users_vw data as a table.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **In Apache Spark, when you use the command `df.createOrReplaceTempView("users_vw")`, you create a local temporary view.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Understanding the Life Cycle
# MAGIC
# MAGIC - **Session Scope:** The lifetime of a temporary view is strictly tied to the SparkSession that created it.
# MAGIC - **Automatic Deletion:** As soon as the Spark session is terminated (e.g., you close the notebook or the application ends), the view is automatically dropped and is no longer accessible.
# MAGIC - **Persistence Requirement:** To access the data after the session ends, you must move it from a temporary in-memory reference to a permanent storage format, such as a managed or unmanaged table in a metastore like Hive.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Why Other Options Are Incorrect
# MAGIC
# MAGIC - **A. Query the users_vw using Spark:**  
# MAGIC   Once the session is terminated, the view no longer exists in Spark's catalog, making it impossible to query directly.
# MAGIC
# MAGIC - **C. Recreate the users_vw:**  
# MAGIC   While this would technically allow you to query it again, it requires re-running the entire data processing logic from scratch, which is not an "approach to query it after termination" but rather a complete redo of the setup.
# MAGIC
# MAGIC - **D. Save the users_vw definition:**  
# MAGIC   Saving just the SQL definition (the code) does not preserve the data or the view's availability in the catalog. You would still need to execute that definition in a new session to recreate the view.

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
# MAGIC **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The original code:
# MAGIC python
# MAGIC result_df = prices_df \
# MAGIC     .filter(F.col("spot_price") >= F.lit(min_price)) \
# MAGIC     .agg(F.count("*"))
# MAGIC
# MAGIC 👉 It:
# MAGIC
# MAGIC - Filters rows where `spot_price >= min_price`
# MAGIC - Counts the number of such rows
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option B:**
# MAGIC python
# MAGIC result_df = prices_df \
# MAGIC     .agg(F.count_if(F.col("spot_price") >= F.lit(min_price)))
# MAGIC
# MAGIC - ✔ Uses `count_if()` (introduced in newer Spark versions)
# MAGIC - ✔ Combines filter + count into a single operation
# MAGIC - ✔ More efficient and concise
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **A.**  
# MAGIC withColumn + when  
# MAGIC - ❌ Adds a column but does not count
# MAGIC
# MAGIC **C.**  
# MAGIC min, max  
# MAGIC - ❌ Unrelated to requirement
# MAGIC
# MAGIC **D.**  
# MAGIC count + filter  
# MAGIC - ❌ Incorrect logic and syntax (`F.it` typo)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**  
# MAGIC 👉 Use `count_if()` to simplify:
# MAGIC
# MAGIC - filter + count → single aggregation operation

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
# MAGIC **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC Adaptive Query Execution (AQE) is a Spark optimization feature that dynamically adjusts the execution plan at runtime based on actual data statistics.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option B is correct:**
# MAGIC
# MAGIC Adjusts query plan during runtime and improves performance
# MAGIC
# MAGIC - ✔ AQE can:
# MAGIC   - Handle data skew (split skewed partitions)
# MAGIC   - Optimize join strategies (e.g., switch to broadcast join)
# MAGIC   - Coalesce shuffle partitions (reduce small tasks)
# MAGIC
# MAGIC 👉 This leads to better performance and resource utilization
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ AQE works during runtime, not just before execution
# MAGIC - **C.** ❌ AQE does more than parallelism — it adapts strategies
# MAGIC - **D.** ❌ It explicitly does runtime adjustments
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 AQE = runtime optimization of query plans based on real execution data

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
# MAGIC **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The scenario:
# MAGIC
# MAGIC - Large DataFrame → 200 million rows (transactions)
# MAGIC - Small DataFrame → 3000 rows (product info)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option D is correct:**
# MAGIC
# MAGIC **Broadcast the smaller DataFrame**
# MAGIC
# MAGIC - ✔ Small DataFrame is sent to all executors
# MAGIC - ✔ Each executor joins locally with partitions of the large DataFrame
# MAGIC - ✔ Avoids expensive shuffle of large dataset
# MAGIC
# MAGIC 👉 This is the most efficient join strategy
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ Broadcasting large DataFrame is inefficient/impractical
# MAGIC - **B.** ❌ Sort-Merge Join is slower due to sorting + shuffle
# MAGIC - **C.** ❌ Shuffle Hash Join requires shuffling both datasets
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 For joins:
# MAGIC
# MAGIC - Small + Large → Broadcast the SMALL dataset
# MAGIC - Minimizes shuffle and improves performance

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
# MAGIC **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement:
# MAGIC
# MAGIC - Reduce partitions from 1000 → 100
# MAGIC - Avoid shuffle
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option D:**
# MAGIC python
# MAGIC new_df = df.coalesce(100)
# MAGIC
# MAGIC - ✔ Reduces number of partitions
# MAGIC - ✔ Does NOT trigger full shuffle
# MAGIC - ✔ Efficient for decreasing partitions
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **A.**
# MAGIC python
# MAGIC repartition(100)
# MAGIC
# MAGIC - ❌ Causes full shuffle
# MAGIC
# MAGIC **B.**
# MAGIC python
# MAGIC limit(100)
# MAGIC
# MAGIC - ❌ Limits number of rows, not partitions
# MAGIC
# MAGIC **C.**
# MAGIC python
# MAGIC head(100)
# MAGIC
# MAGIC - ❌ Returns local data, not a DataFrame transformation
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Use:
# MAGIC
# MAGIC - `coalesce()` → reduce partitions (no shuffle)
# MAGIC - `repartition()` → redistribute data (with shuffle)

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
# MAGIC **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**  
# MAGIC The question compares `coalesce()` vs `repartition()` when reducing partitions.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option A:**  
# MAGIC `coalesce` minimizes shuffling, `repartition` performs full shuffle
# MAGIC
# MAGIC - **coalesce(n):**
# MAGIC   - Merges existing partitions
# MAGIC   - Avoids full shuffle
# MAGIC   - Efficient for reducing partitions
# MAGIC
# MAGIC - **repartition(n):**
# MAGIC   - Redistributes data evenly
# MAGIC   - Triggers full shuffle
# MAGIC   - Used when you need balanced partitions
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **B.** ❌ Only `repartition()` shuffles, not `coalesce()`
# MAGIC - **C.** ❌ Behavior and resource usage differ significantly
# MAGIC - **D.** ❌ Reversed — incorrect
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**  
# MAGIC 👉 `coalesce()` → reduce partitions (no shuffle)  
# MAGIC 👉 `repartition()` → redistribute (full shuffle)

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
# MAGIC **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC Apache Spark uses lazy evaluation as a core feature of its execution model.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option B is correct:**
# MAGIC
# MAGIC **Lazy evaluation with the Catalyst Optimizer**
# MAGIC
# MAGIC - **Lazy Evaluation:**
# MAGIC   - Transformations (e.g., filter, select) are not executed immediately
# MAGIC   - Spark builds a logical plan (DAG)
# MAGIC
# MAGIC - **Catalyst Optimizer:**
# MAGIC   - Optimizes the query plan before execution
# MAGIC   - Applies techniques like:
# MAGIC     - Predicate pushdown
# MAGIC     - Projection pruning
# MAGIC     - Join optimization
# MAGIC
# MAGIC 👉 Execution happens only when an action (e.g., count(), show()) is triggered
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ Spark does not use immediate execution
# MAGIC - **C.** ❌ Not a real Spark feature
# MAGIC - **D.** ❌ Parallelism is separate from lazy evaluation
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Spark defers execution using lazy evaluation + Catalyst optimization for better performance

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
# MAGIC **Correct Answers: A and D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC Spark execution follows:  
# MAGIC 👉 Job → Stages → Tasks
# MAGIC
# MAGIC Stages are created based on shuffle boundaries.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **A. The groupBy and agg operations may cause a shuffle, resulting in additional stages**
# MAGIC
# MAGIC - **groupBy + agg:**
# MAGIC   - Requires data to be redistributed across partitions
# MAGIC   - Causes a shuffle
# MAGIC   - Creates a new stage
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **D. The join operation causes a shuffle, leading to a new stage**
# MAGIC
# MAGIC - For large DataFrames:
# MAGIC   - Join typically requires shuffling data based on join key
# MAGIC   - Introduces a stage boundary
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **B.** ❌ Not necessarily a single job (depends on actions, though write is an action, but focus here is stages/shuffles)
# MAGIC - **C.** ❌ Spark cannot eliminate all shuffles
# MAGIC - **E.** ❌ Join is not a narrow transformation (it’s wide → causes shuffle)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Wide transformations (join, groupBy) → cause shuffle → new stages  
# MAGIC 👉 Narrow transformations (filter) → stay within same stage

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
# MAGIC **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The dataset is:
# MAGIC
# MAGIC - 50,000 records
# MAGIC - ~20 MB size
# MAGIC
# MAGIC 👉 This is small data, not big data.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option B is correct:**
# MAGIC
# MAGIC **Use pandas in a local Python script**
# MAGIC
# MAGIC - ✔ Easily fits in memory
# MAGIC - ✔ Fast and simple for analysis
# MAGIC - ✔ No need for distributed computing overhead
# MAGIC
# MAGIC 👉 Most efficient and practical solution
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ Streaming is for real-time continuous data, not static files
# MAGIC - **C.** ❌ Spark cluster is overkill for small data
# MAGIC - **D.** ❌ Hadoop ecosystem is unnecessary and complex for this use case
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Use:
# MAGIC
# MAGIC - Pandas → small data (MBs)
# MAGIC - Spark/Hadoop → large-scale data (GBs/TBs)

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
# MAGIC **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement is to replace null values in a specific column (salary) with 0.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option D:**
# MAGIC python
# MAGIC df.fillna({"salary": 0})
# MAGIC
# MAGIC - ✔ Replaces nulls only in the salary column
# MAGIC - ✔ Uses dictionary format → `{column: value}`
# MAGIC - ✔ Correct and standard PySpark syntax
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **A.**
# MAGIC python
# MAGIC df.fillna("salary", 0)
# MAGIC
# MAGIC - ❌ Incorrect argument order
# MAGIC
# MAGIC **B.**
# MAGIC python
# MAGIC replaceNulls()
# MAGIC
# MAGIC - ❌ Not a valid PySpark function
# MAGIC
# MAGIC **C.**
# MAGIC python
# MAGIC dropna(subset=["salary"])
# MAGIC
# MAGIC - ❌ Removes rows instead of replacing nulls
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Use:
# MAGIC - `fillna({"column": value})` to replace nulls in specific columns

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
# MAGIC **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC In client mode:
# MAGIC
# MAGIC - The driver program runs on the client machine (where the application is submitted)
# MAGIC - Executors run on cluster worker nodes
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option D is correct:**
# MAGIC
# MAGIC Driver runs on the client machine, easier to debug but limited resources
# MAGIC
# MAGIC - ✔ Easier debugging (logs available locally)
# MAGIC - ✔ Depends on client machine resources
# MAGIC - ✔ Can be less reliable if client disconnects
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ Tasks are always managed by the driver, not directly from client to workers
# MAGIC - **B.** ❌ Mentions latency but not the defining characteristic
# MAGIC - **C.** ❌ Describes cluster mode, not client mode
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Client Mode = Driver runs on client machine  
# MAGIC 👉 Good for debugging, but less robust for production

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
# MAGIC
# MAGIC **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The code:
# MAGIC
# MAGIC python
# MAGIC div_by_2 = my_df.filter("number % 2 = 0")
# MAGIC print(div_by_2)
# MAGIC
# MAGIC
# MAGIC 👉 Only defines a transformation, not an action.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔍 **What happens here:**
# MAGIC - `filter()` → transformation (lazy)
# MAGIC - `print(div_by_2)` → prints DataFrame schema, not data
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC
# MAGIC DataFrame [number: bigint]
# MAGIC
# MAGIC
# MAGIC ✔ No computation has happened yet  
# MAGIC ✔ Spark has only built a logical plan
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option B is correct:**
# MAGIC
# MAGIC Transformations in Spark are lazy
# MAGIC
# MAGIC - ✔ Spark delays execution until an action is called
# MAGIC - ✔ Examples of actions: `show()`, `count()`, `collect()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ `filter()` does NOT trigger execution
# MAGIC - **C.** ❌ Actions are not triggered automatically after transformations
# MAGIC - **D.** ❌ `filter()` is NOT an action
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Transformations = lazy (no execution)  
# MAGIC 👉 Actions = trigger execution

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

df = spark.read.option("header", "true").csv("/Volumes/pyspark_training/default/test/employee.csv", schema="ID INT, Name STRING, Salary FLOAT")

# COMMAND ----------

df.show()

# COMMAND ----------

# MAGIC %md
# MAGIC **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement is to:
# MAGIC
# MAGIC - Load CSV data
# MAGIC - Explicitly define schema (not infer it)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option D:**
# MAGIC python
# MAGIC schema = StructType([
# MAGIC     StructField("ID", IntegerType(), True),
# MAGIC     StructField("Name", StringType(), True),
# MAGIC     StructField("Salary", FloatType(), True)
# MAGIC ])
# MAGIC
# MAGIC df = spark.read.option("header", "true").csv("employee.csv", schema=schema)
# MAGIC
# MAGIC
# MAGIC - ✔ Defines schema using StructType
# MAGIC - ✔ Applies it directly during read
# MAGIC - ✔ Ensures correct data types
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **A.**
# MAGIC - ❌ Schema is defined but not applied to csv()
# MAGIC
# MAGIC **B.**
# MAGIC - inferSchema = true
# MAGIC - ❌ Infers schema automatically (not explicit)
# MAGIC
# MAGIC **C.**
# MAGIC - schema="ID INT, ..."
# MAGIC - ❌ Invalid way to pass schema in PySpark
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Use:
# MAGIC - StructType + schema= parameter to explicitly define schema while reading data

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
# MAGIC **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement involves:
# MAGIC
# MAGIC - Streaming data
# MAGIC - Deduplication based on `order_id`
# MAGIC - Handling late-arriving data
# MAGIC - Managing state/memory efficiently
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option A is correct:**
# MAGIC
# MAGIC python
# MAGIC df.withWatermark("event_time", "X minutes") \
# MAGIC   .dropDuplicates(["order_id"])
# MAGIC
# MAGIC
# MAGIC - **withWatermark():**
# MAGIC   - Defines how long Spark should keep state for late data
# MAGIC   - Helps clean up old state → prevents memory issues
# MAGIC
# MAGIC - **dropDuplicates(["order_id"]):**
# MAGIC   - Removes duplicate records based on `order_id`
# MAGIC
# MAGIC 👉 **Together:**
# MAGIC - Handles late-arriving data correctly
# MAGIC - Prevents unbounded state growth
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **B.** ❌ Deduplicating on timestamp is incorrect (duplicates defined by `order_id`)
# MAGIC - **C.** ❌ Deduplication is supported with watermarking
# MAGIC - **D.** ❌ Without watermark → state grows indefinitely → memory issues
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 In streaming:
# MAGIC - Use `withWatermark()` + `dropDuplicates()`
# MAGIC - Ensures correctness + bounded state (memory efficiency)

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
# MAGIC **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement:
# MAGIC
# MAGIC - Perform an inner join
# MAGIC - Match on both id AND name columns
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option A:**
# MAGIC `(df1.id == df2.id) & (df1.name == df2.name)`
# MAGIC
# MAGIC - ✔ Joins on both conditions
# MAGIC - ✔ Ensures id AND name must match
# MAGIC - ✔ Correct syntax for multiple join conditions
# MAGIC
# MAGIC **Example:**
# MAGIC
# MAGIC python
# MAGIC joined_df = df1.join(df2, (df1.id == df2.id) & (df1.name == df2.name), "inner")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **B.**
# MAGIC
# MAGIC `df1.id == df2.id`
# MAGIC
# MAGIC - ❌ Only matches id, not name
# MAGIC
# MAGIC **C.**
# MAGIC
# MAGIC `['id', 'dept']`
# MAGIC
# MAGIC - ❌ dept is not common in both DataFrames
# MAGIC
# MAGIC **D.**
# MAGIC
# MAGIC `['id']`
# MAGIC
# MAGIC - ❌ Matches only one column
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 For multiple join conditions:
# MAGIC
# MAGIC - Use boolean expressions with `&`
# MAGIC - Example: `(col1 == col2) & (col3 == col4)`

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
# MAGIC
# MAGIC **Correct Answers: B and C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirements are:
# MAGIC
# MAGIC - Handle large-scale structured data (distributed processing)
# MAGIC - Perform complex aggregations and transformations
# MAGIC - Data does not fit in a single machine’s memory
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **B. Spark SQL**
# MAGIC
# MAGIC - Enables:
# MAGIC   - Running SQL queries on structured data
# MAGIC   - Complex aggregations and transformations
# MAGIC   - Optimized execution using Catalyst optimizer
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **C. DataFrames**
# MAGIC
# MAGIC - Provides:
# MAGIC   - Distributed structured data abstraction
# MAGIC   - High-level APIs for transformations (filter, groupBy, etc.)
# MAGIC   - Works seamlessly with Spark SQL
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A. Structured Streaming** ❌ For real-time streaming, not required here
# MAGIC - **D. GraphX** ❌ For graph processing
# MAGIC - **E. MLlib** ❌ For machine learning tasks
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 For large structured data + transformations + SQL:  
# MAGIC Use DataFrames + Spark SQL

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
# MAGIC **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement:  
# MAGIC 👉 Overwrite existing data at a specific file path
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option B:**
# MAGIC sql
# MAGIC INSERT OVERWRITE DIRECTORY 'path/to/data'
# MAGIC USING delta
# MAGIC OPTIONS (col1 1, col2 2, col3 'test')
# MAGIC SELECT * FROM source_data;
# MAGIC
# MAGIC - ✔ `INSERT OVERWRITE DIRECTORY` → overwrites data at given path
# MAGIC - ✔ `USING delta` → specifies format
# MAGIC - ✔ Correct syntax for writing to a file path (not a table)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **A.**
# MAGIC sql
# MAGIC INSERT 'path/to/data'
# MAGIC
# MAGIC - ❌ Invalid syntax
# MAGIC
# MAGIC **C.**
# MAGIC sql
# MAGIC INSERT OVERWRITE 'path/to/data'
# MAGIC
# MAGIC - ❌ Missing DIRECTORY keyword
# MAGIC
# MAGIC **D.**
# MAGIC sql
# MAGIC OVERWRITE 'path/to/data'
# MAGIC
# MAGIC - ❌ Invalid SQL syntax
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Use:
# MAGIC - `INSERT OVERWRITE DIRECTORY` → overwrite data at a path
# MAGIC - `INSERT OVERWRITE TABLE` → overwrite table data

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
# MAGIC **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC Let’s break down the placeholders:
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **X (in SQL query):**  
# MAGIC `SELECT name, platform FROM X`
# MAGIC
# MAGIC - Must refer to the temporary view name, not DataFrame  
# MAGIC - `devices_df.createOrReplaceTempView("devices")`  
# MAGIC - So, **X = devices**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **Y and Z (write operation):**  
# MAGIC `spark.sql(...).Y.Z("names.parquet", format="parquet")`
# MAGIC
# MAGIC - To write a DataFrame:  
# MAGIC   - Use `.write`  
# MAGIC   - Then `.save(...)`  
# MAGIC - **Correct combination:**
# MAGIC
# MAGIC python
# MAGIC devices_df = spark.read.json("devices.json")
# MAGIC devices_df.createOrReplaceTempView("devices")
# MAGIC
# MAGIC spark.sql("SELECT name, platform FROM devices") \
# MAGIC     .write \
# MAGIC     .save("names.parquet", format="parquet")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** devices_df cannot be used in SQL query
# MAGIC - **B.** Order is wrong (save.write)
# MAGIC - **C.** saveAsTable writes to table, not file path
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC - SQL uses view/table name  
# MAGIC - DataFrame write uses `.write.save()` for files

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
# MAGIC **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The function used:
# MAGIC
# MAGIC `df.createOrReplaceTempView("myView")`
# MAGIC
# MAGIC 👉 The keyword here is **OrReplace**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **What happens:**
# MAGIC - If a view named `myView` already exists  
# MAGIC   It will be replaced by the new DataFrame
# MAGIC
# MAGIC - ✔ No error  
# MAGIC - ✔ No merging  
# MAGIC - ✔ Old view is overwritten
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **A.** ❌ Only one view can exist with a given name
# MAGIC - **B.** ❌ Spark does not merge DataFrames automatically
# MAGIC - **C.** ❌ No exception due to OrReplace behavior
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 `createOrReplaceTempView()` =  
# MAGIC Create if not exists **OR** replace if exists

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
# MAGIC **The correct answer is D. maxFilesPerTrigger.**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation**
# MAGIC
# MAGIC When using the Available-now micro-batch trigger in Spark Structured Streaming, the goal is to process all available data in the source. However, to prevent a single micro-batch from becoming too large and overwhelming your compute resources, you can use admission controls to limit the input rate.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option D (maxFilesPerTrigger):**  
# MAGIC This option explicitly limits the maximum number of new files to be considered in every micro-batch. This is a standard way to throttle data ingestion and ensure predictable micro-batch sizes when running with AvailableNow.
# MAGIC
# MAGIC ❌ **Option A & B (maxExecutorsPerTrigger / maxCoresPerTrigger):**  
# MAGIC These are not valid configuration options for controlling micro-batch size in Structured Streaming. Resources like executors and cores are typically managed at the cluster level, not per trigger.
# MAGIC
# MAGIC ❌ **Option C (maxBytesPerTrigger):**  
# MAGIC While maxBytesPerTrigger is a valid admission control that limits the amount of data processed by size (e.g., 10 GB), it is often considered a "soft max" and may be less commonly used than file counts for basic throttling in some file-based streaming contexts. However, in many exam contexts for Spark Associate Developers, maxFilesPerTrigger is the specifically cited solution for this scenario.

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
# MAGIC **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC In Apache Spark, the Directed Acyclic Graph (DAG) represents the logical execution plan of a job.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option B is correct:**
# MAGIC
# MAGIC Represents a job as interdependent stages, each with parallel tasks
# MAGIC
# MAGIC - ✔ A job is divided into stages
# MAGIC - ✔ Each stage consists of multiple tasks (one per partition)
# MAGIC - ✔ Stages are connected based on dependencies (DAG)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 **DAG shows:**
# MAGIC
# MAGIC - How transformations depend on each other
# MAGIC - Where shuffle boundaries occur
# MAGIC - Execution flow from start to end
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ Ignores stages and tasks → incorrect hierarchy
# MAGIC - **C.** ❌ Incorrect structure (tasks are not jobs)
# MAGIC - **D.** ❌ DAG includes full plan, not just final tasks
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 DAG = Job → Stages → Tasks with dependencies

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
# MAGIC
# MAGIC **Correct Answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement is to:
# MAGIC
# MAGIC - Use Spark SQL
# MAGIC - Improve readability and maintainability
# MAGIC - Work on a large DataFrame (millions of rows)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option C is correct:**
# MAGIC
# MAGIC Register DataFrame as a temp view and use Spark SQL
# MAGIC
# MAGIC - ✔ Convert DataFrame to a temporary view:
# MAGIC
# MAGIC   `sales_data.createOrReplaceTempView("sales")`
# MAGIC
# MAGIC - ✔ Then write SQL:
# MAGIC
# MAGIC   python
# MAGIC   spark.sql("""
# MAGIC   SELECT region, SUM(sales_amount) AS total_sales
# MAGIC   FROM sales
# MAGIC   GROUP BY region
# MAGIC   """)
# MAGIC   
# MAGIC
# MAGIC - ✔ Benefits:
# MAGIC   - Cleaner and more readable SQL syntax
# MAGIC   - Uses Spark’s distributed engine
# MAGIC   - No data movement required
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ Uses DataFrame API, not Spark SQL
# MAGIC - **B.** ❌ Unnecessary data movement → inefficient
# MAGIC - **D.** ❌ Pandas cannot handle millions of rows efficiently
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 For SQL-style processing in Spark:
# MAGIC
# MAGIC Use `createOrReplaceTempView()` + `spark.sql()`

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
# MAGIC **Correct Answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The Spark History Server is used to:
# MAGIC - View completed application logs
# MAGIC - Analyze past jobs via Spark UI after execution
# MAGIC - Help with debugging and performance tuning
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option C is correct:**
# MAGIC
# MAGIC Loss of access to past job logs and reduced debugging capability
# MAGIC
# MAGIC - ✔ Without History Server:
# MAGIC   - Cannot view completed job details
# MAGIC   - No access to:
# MAGIC     - Stages
# MAGIC     - Tasks
# MAGIC     - Execution timelines
# MAGIC - ✔ Makes debugging production issues difficult
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **A.** ❌ History Server does not control log accumulation
# MAGIC - **B.** ❌ No meaningful impact on execution speed
# MAGIC - **D.** ❌ Does not affect executor performance
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Disabling History Server =  
# MAGIC ❌ No visibility into past jobs  
# MAGIC 👉 Keep it enabled for production monitoring & debugging

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
# MAGIC
# MAGIC **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC Parquet is a self-describing format, meaning:
# MAGIC
# MAGIC - It stores schema information along with the data
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **What happens:**
# MAGIC python
# MAGIC df = spark.read.parquet("path/to/file")
# MAGIC
# MAGIC - ✔ Spark reads:
# MAGIC   - Data
# MAGIC   - Schema directly from the Parquet file
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 So the resulting schema will match exactly:
# MAGIC
# MAGIC - `name: String`
# MAGIC - `address: String`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **B.** ❌ c0 is used when schema is unknown (e.g., raw text), not Parquet
# MAGIC - **C.** ❌ Parquet preserves original column names and case
# MAGIC - **D.** ❌ Incorrect column naming
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Parquet = schema is preserved and automatically applied when reading

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
# MAGIC **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement:
# MAGIC
# MAGIC - Convert epoch time (seconds) → timestamp
# MAGIC - Extract the month
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option B:**
# MAGIC python
# MAGIC df_epoch_time = df_epoch_time.withColumn(
# MAGIC     "month",
# MAGIC     month(from_unixtime("epoch_time"))
# MAGIC )
# MAGIC
# MAGIC - ✔ `from_unixtime("epoch_time")` → converts epoch seconds to timestamp
# MAGIC - ✔ `month(...)` → extracts month from timestamp
# MAGIC - ✔ Clean and correct approach
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **A.**
# MAGIC - `substr(4,2)`
# MAGIC - ❌ String manipulation → unreliable and incorrect
# MAGIC
# MAGIC **C.**
# MAGIC - `month("epoch_time")`
# MAGIC - ❌ epoch_time is numeric, not timestamp
# MAGIC
# MAGIC **D.**
# MAGIC - `substr(6,2)`
# MAGIC - ❌ Treats epoch as string → incorrect logic
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 For epoch time:
# MAGIC - Convert using `from_unixtime()`
# MAGIC - Then apply date functions like `month()`

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
# MAGIC **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC Adaptive Query Execution (AQE) can dynamically switch:  
# MAGIC 👉 Sort-Merge Join → Broadcast Join
# MAGIC
# MAGIC But this depends on table size thresholds.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option A is correct:**
# MAGIC
# MAGIC Small table has grown beyond broadcast threshold
# MAGIC
# MAGIC - ✔ AQE uses:  
# MAGIC   `spark.sql.autoBroadcastJoinThreshold`
# MAGIC - ✔ If the smaller table:  
# MAGIC   - Was small before → broadcasted  
# MAGIC   - Grew larger → exceeds threshold → no broadcast
# MAGIC
# MAGIC 👉 **Result:**
# MAGIC
# MAGIC - Falls back to Sort-Merge Join
# MAGIC - Causes extra shuffle → slower performance
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **B.** ❌ AQE uses runtime statistics, not just table stats
# MAGIC - **C.** ❌ AQE is not disabled silently after upgrade
# MAGIC - **D.** ❌ Skew affects performance, but not broadcast decision primarily
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Broadcast join depends on:
# MAGIC
# MAGIC - Size of smaller dataset  
# MAGIC - If it exceeds threshold → AQE won’t convert → performance drop

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
# MAGIC
# MAGIC **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC When reading data using JDBC in Spark, the number of parallel connections to the database is controlled by:
# MAGIC
# MAGIC 👉 **numPartitions**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option A is correct:**
# MAGIC
# MAGIC Reduce numPartitions from 25 to 8
# MAGIC
# MAGIC - ✔ Each partition = one JDBC connection
# MAGIC - ✔ So:
# MAGIC   - numPartitions = 25 → 25 concurrent DB connections
# MAGIC   - Reducing it → fewer connections
# MAGIC
# MAGIC 👉 Directly solves the problem of too many DB connections
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **B.** ❌ Changes data range, not number of connections
# MAGIC - **C.** ❌ spark.sql.shuffle.partitions affects shuffle, not JDBC reads
# MAGIC - **D.** ❌ Index improves performance, not connection count
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 In JDBC reads:
# MAGIC
# MAGIC - numPartitions = number of parallel DB connections
# MAGIC - Reduce it to limit connection load on database

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
# MAGIC
# MAGIC **Correct Answers: B and D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The scenario:
# MAGIC
# MAGIC - Dataset is too large for a single machine
# MAGIC - Need scalability + reliability
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **B. Fault tolerance**
# MAGIC
# MAGIC - ✔ Spark:
# MAGIC   - Uses lineage (DAG) to recompute lost data
# MAGIC   - Automatically recovers from node failures
# MAGIC   - 👉 Critical for large distributed systems
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **D. Distributed processing**
# MAGIC
# MAGIC - ✔ Spark:
# MAGIC   - Distributes data and computation across multiple machines (cluster)
# MAGIC   - Enables horizontal scalability
# MAGIC   - 👉 Can handle datasets far larger than single-machine memory
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ Spark still requires code
# MAGIC - **C.** ❌ Spark is memory-optimized, not disk-only
# MAGIC - **E.** ❌ Runs on commodity hardware, not specialized systems
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Spark advantages over single-machine processing:
# MAGIC
# MAGIC - Distributed computation (scalability)
# MAGIC - Fault tolerance (reliability)

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
# MAGIC **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement:
# MAGIC
# MAGIC - Convert timestamp from UTC → America/New_York
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option A:**
# MAGIC python
# MAGIC raw.withColumn(
# MAGIC     "transaction_datetime",
# MAGIC     from_utc_timestamp(col("transaction_datetime"), "America/New_York")
# MAGIC )
# MAGIC
# MAGIC
# MAGIC - ✔ `from_utc_timestamp()`:
# MAGIC   - Converts UTC timestamp → target timezone
# MAGIC   - ✔ Correct function for this use case
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **B.**
# MAGIC - `date_format(...)`
# MAGIC - ❌ Formats date as string, does NOT change timezone
# MAGIC
# MAGIC **C.**
# MAGIC - `to_utc_timestamp(...)`
# MAGIC - ❌ Converts local → UTC (reverse of requirement)
# MAGIC
# MAGIC **D.**
# MAGIC - `from_utc_timestamp(...)`
# MAGIC - ❌ Missing timezone argument
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Use:
# MAGIC - `from_utc_timestamp()` → UTC → local timezone
# MAGIC - `to_utc_timestamp()` → local → UTC

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
# MAGIC
# MAGIC **Correct Answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The scenario highlights:
# MAGIC
# MAGIC - Huge data volume (2 TB/day)
# MAGIC - Need for real-time processing (fraud detection)
# MAGIC - Traditional DB struggling with scale + speed
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option C is correct:**
# MAGIC
# MAGIC **In-memory computation and parallel processing**
# MAGIC
# MAGIC - ✔ In-memory processing:
# MAGIC   - Faster than disk-based systems
# MAGIC   - Ideal for real-time analytics
# MAGIC
# MAGIC - ✔ Parallel processing:
# MAGIC   - Distributes workload across cluster
# MAGIC   - Handles large-scale data efficiently
# MAGIC
# MAGIC 👉 This directly solves:
# MAGIC
# MAGIC - High data volume
# MAGIC - High processing speed requirements
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ Focuses on small datasets (irrelevant)
# MAGIC - **B.** ❌ SQL support alone doesn’t solve scalability/performance
# MAGIC - **D.** ❌ MLlib is useful, but not the core solution to performance bottleneck
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Spark’s strength:
# MAGIC
# MAGIC - In-memory + distributed processing → high performance at scale

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
# MAGIC **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement:
# MAGIC
# MAGIC - Add a tax column = 10% of salary
# MAGIC - Remove the age column
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option B:**
# MAGIC `employees_df = employees_df.withColumn("tax", employees_df.salary * 0.1).drop("age")`
# MAGIC
# MAGIC - ✔ Correct tax calculation → salary * 0.1 (10%)
# MAGIC - ✔ Correct method to remove column → .drop("age")
# MAGIC - ✔ Valid PySpark syntax
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **A.**
# MAGIC
# MAGIC - salary * 10
# MAGIC - ❌ 1000% instead of 10%
# MAGIC - ❌ dropField() is invalid
# MAGIC
# MAGIC **C.**
# MAGIC
# MAGIC - dropField("age")
# MAGIC - ❌ Invalid function
# MAGIC
# MAGIC **D.**
# MAGIC
# MAGIC - salary * 10
# MAGIC - ❌ Incorrect tax calculation
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Use salary * 0.1 for 10%  
# MAGIC 👉 Use .drop("column") to remove columns

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
# MAGIC **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation (why this is tricky):**
# MAGIC
# MAGIC At first glance, “underutilization” might suggest adding more executors—but the key clues are:
# MAGIC
# MAGIC - Tasks are getting killed due to timeout errors
# MAGIC - Logs show insufficient resources
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option A is correct:**
# MAGIC
# MAGIC **Increase executor memory**
# MAGIC
# MAGIC - ✔ Tasks are likely failing due to memory pressure (e.g., spills, GC pauses)
# MAGIC - ✔ This leads to:
# MAGIC   - Slow execution
# MAGIC   - Timeouts → tasks get killed
# MAGIC   - Fewer tasks completing → underutilization
# MAGIC
# MAGIC 👉 **Increasing memory:**
# MAGIC - Allows tasks to complete successfully
# MAGIC - Reduces retries/timeouts
# MAGIC - Improves overall utilization
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **B. spark.network.timeout**
# MAGIC - ❌ Just increases wait time → hides the issue, doesn’t fix resource problem
# MAGIC
# MAGIC **C. increase executors**
# MAGIC - ❌ If tasks are failing due to memory, adding more executors won’t help
# MAGIC
# MAGIC **D. reduce partition size**
# MAGIC - ❌ Might help slightly, but does not address core resource issue
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key insight:**
# MAGIC
# MAGIC 👉 Underutilization + task failures + resource warnings  
# MAGIC = Resource bottleneck (memory), not lack of parallelism
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Final takeaway:**
# MAGIC If tasks are timing out/failing → fix resources (memory)  
# MAGIC If tasks are queued → increase executors

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
# MAGIC **Correct Answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC Spark Connect is designed to:
# MAGIC
# MAGIC - Provide a client-server architecture
# MAGIC - Enable remote interaction with Spark
# MAGIC - Improve isolation, upgradability, and flexibility
# MAGIC
# MAGIC ❗ **Key limitation:**
# MAGIC
# MAGIC 👉 Spark Connect does **NOT** support the full Spark API, especially:
# MAGIC
# MAGIC - RDD APIs
# MAGIC - Some low-level operations
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option C is correct:**
# MAGIC
# MAGIC - Requires complete Spark API support including RDDs
# MAGIC - ✔ Spark Connect mainly supports:
# MAGIC   - DataFrame API
# MAGIC   - SQL API
# MAGIC - ❌ Does NOT support:
# MAGIC   - RDD-based code
# MAGIC
# MAGIC 👉 So if the organization:
# MAGIC
# MAGIC - Uses RDD-heavy workloads
# MAGIC - Needs full API compatibility
# MAGIC
# MAGIC ➡️ Migration is blocked
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ Debuggability is actually improved with client-side interaction
# MAGIC - **B.** ❌ Isolation is a benefit of Spark Connect
# MAGIC - **D.** ❌ Independent upgrades are a key advantage
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Spark Connect limitation:
# MAGIC
# MAGIC - ❌ No full support for RDD APIs
# MAGIC - 👉 Works best for:
# MAGIC   - ✔ DataFrame / SQL-based applications

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
# MAGIC **Correct Answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The issue:
# MAGIC
# MAGIC - CSV data is being read incorrectly
# MAGIC - Most likely causes:
# MAGIC   - Wrong delimiter
# MAGIC   - Header row treated as data
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option C is correct:**
# MAGIC
# MAGIC `OPTIONS ('path' = '/landing/air_ref_20241001.csv', 'header' = 'true', 'sep' = '|')`
# MAGIC
# MAGIC - ✔ `'header' = 'true'`
# MAGIC   - Ensures first row is treated as column names
# MAGIC - ✔ `'sep' = '|'`
# MAGIC   - Specifies correct delimiter (instead of default comma)
# MAGIC
# MAGIC 👉 Fixes both common CSV parsing issues
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **A.**
# MAGIC
# MAGIC - `'quote' = '|'`
# MAGIC - ❌ Quote character, not delimiter
# MAGIC
# MAGIC **B.**
# MAGIC
# MAGIC - `'inferSchema' = 'true'`
# MAGIC - ❌ Schema already defined
# MAGIC
# MAGIC **D.**
# MAGIC
# MAGIC - `'header' 'true'`
# MAGIC - ❌ Incorrect syntax + missing delimiter
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 For CSV issues:
# MAGIC - Use `header=true` for column names
# MAGIC - Use `sep` to define correct delimiter

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
# MAGIC **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirements:
# MAGIC
# MAGIC - 2 billion rows → very large dataset
# MAGIC - Compute:
# MAGIC   - Approx distinct count of user_id
# MAGIC   - Average of transaction_amount
# MAGIC - Must be done in single transformation step
# MAGIC - Minimize shuffle and cost
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option A is correct:**
# MAGIC
# MAGIC python
# MAGIC from pyspark.sql.functions import approx_count_distinct, avg
# MAGIC
# MAGIC df.agg(
# MAGIC     approx_count_distinct("user_id").alias("approx_count_distinct"),
# MAGIC     avg("transaction_amount").alias("average_transaction")
# MAGIC ).show()
# MAGIC
# MAGIC
# MAGIC - ✔ Uses approx_count_distinct() → efficient for large data
# MAGIC - ✔ Performs both aggregations in one pass
# MAGIC - ✔ Minimizes shuffle and computation cost
# MAGIC - ✔ Best performance for massive datasets
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **B.**
# MAGIC
# MAGIC - countDistinct()
# MAGIC - ❌ Exact count → expensive and heavy shuffle
# MAGIC
# MAGIC **C.**
# MAGIC
# MAGIC - COUNT(DISTINCT ...)
# MAGIC - ❌ Same as above → exact computation → costly
# MAGIC
# MAGIC **D.**
# MAGIC
# MAGIC - separate computations
# MAGIC - ❌ Multiple actions → multiple scans → worst performance
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 For large-scale aggregation:
# MAGIC - Use approx_count_distinct() for scalability
# MAGIC - Combine aggregations in single agg() call

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
# MAGIC
# MAGIC **Correct Answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC Partitioning organizes data based on column values (e.g., country, date) into separate directories.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option C is correct:**
# MAGIC
# MAGIC **Reads only relevant subset of data**
# MAGIC
# MAGIC - ✔ Spark can skip unnecessary partitions
# MAGIC - ✔ This is called partition pruning
# MAGIC - ✔ Reduces:
# MAGIC   - Disk I/O
# MAGIC   - Data scanned
# MAGIC   - Query execution time
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 **Example:**
# MAGIC
# MAGIC If partitioned by country  
# MAGIC Query: `WHERE country = 'US'`  
# MAGIC ➡️ Only US partition is read
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ Partitioning does not auto-clean data
# MAGIC - **B.** ❌ Compression is separate from partitioning
# MAGIC - **D.** ❌ Data is processed lazily, not loaded entirely
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Partitioning improves performance via:
# MAGIC
# MAGIC - Partition pruning → less data read → faster queries

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
# MAGIC **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement:
# MAGIC
# MAGIC - Sort by highest count first (descending)
# MAGIC - Then by Name (optional tie-breaker)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Option A:**
# MAGIC `df.select("Name", "count").orderBy("count", "Name", ascending=False)`
# MAGIC
# MAGIC - ✔ Sorts primarily by count (descending)
# MAGIC - ✔ Then by Name
# MAGIC - ✔ Meets requirement of highest count first
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **B.**
# MAGIC
# MAGIC - `orderBy("count")`
# MAGIC - ❌ Default is ascending → smallest count first
# MAGIC
# MAGIC **C.**
# MAGIC
# MAGIC - `sort("Name", "count")`
# MAGIC - ❌ Sorts by Name first, not count
# MAGIC
# MAGIC **D.**
# MAGIC
# MAGIC - `sort("Name")`
# MAGIC - ❌ Ignores count completely
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚠️ **Note:**
# MAGIC
# MAGIC A more explicit and commonly used version:
# MAGIC
# MAGIC python
# MAGIC from pyspark.sql.functions import col
# MAGIC
# MAGIC df.select("Name", "count") \
# MAGIC   .orderBy(col("count").desc(), col("Name"))
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 To get highest values first:
# MAGIC
# MAGIC - Use `desc()` or `ascending=False` on the target column

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
# MAGIC **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC Let’s break the Spark execution:
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **1. Reading the file**
# MAGIC
# MAGIC - ✔ Spark reads data lazily (no execution yet)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **2. Filter operation**
# MAGIC
# MAGIC - ✔ `filter()` is a narrow transformation
# MAGIC   - Operates within each partition
# MAGIC   - No shuffle required
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **3. GroupBy operation**
# MAGIC
# MAGIC - ✔ `groupBy()` is a wide transformation
# MAGIC   - Requires data to be redistributed across partitions
# MAGIC   - Causes a shuffle
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🔹 **4. Write operation**
# MAGIC
# MAGIC - ✔ Writing data triggers an action
# MAGIC   - Entire DAG gets executed here
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option D is correct:**
# MAGIC
# MAGIC - Lazy read → filter (narrow) → groupBy (wide + shuffle)
# MAGIC - ✔ Matches Spark execution model exactly
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ Spark does NOT load entire data into memory upfront
# MAGIC - **B.** ❌ filter is NOT an action
# MAGIC - **C.** ❌ Filter and groupBy are separate transformations, not one
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Spark execution flow:
# MAGIC
# MAGIC - Lazy evaluation
# MAGIC - Narrow transformations → no shuffle
# MAGIC - Wide transformations → shuffle → new stage

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
# MAGIC **Correct Answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The issue:
# MAGIC
# MAGIC - `au_df` has one extra column
# MAGIC - `nz_df` is missing that column
# MAGIC - `union()` requires:
# MAGIC   - Same number of columns
# MAGIC   - Same order/schema
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option C is correct:**
# MAGIC
# MAGIC `anz_df = au_df.unionByName(nz_df, allowMissingColumns=True)`
# MAGIC
# MAGIC - ✔ Matches columns by name
# MAGIC - ✔ Automatically:
# MAGIC   - Adds missing columns as NULL
# MAGIC - ✔ Handles schema mismatch safely
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **A.**
# MAGIC
# MAGIC - `allowMissingColumns=False`
# MAGIC - ❌ Will still fail due to column mismatch
# MAGIC
# MAGIC **B.**
# MAGIC
# MAGIC - `unionAll()`
# MAGIC - ❌ Deprecated and still requires same schema
# MAGIC
# MAGIC **D.**
# MAGIC
# MAGIC - `join()`
# MAGIC - ❌ Completely different operation (not row append)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 For mismatched schemas:
# MAGIC - Use `unionByName(..., allowMissingColumns=True)`
# MAGIC - 👉 Safely combines DataFrames with different columns

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
# MAGIC **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC In Apache Spark architecture:
# MAGIC
# MAGIC 🔹 **Executors**
# MAGIC - ✔ Run on worker nodes
# MAGIC - ✔ Responsible for:
# MAGIC   - Executing tasks
# MAGIC   - Storing data in memory/disk
# MAGIC - ✔ Each executor uses CPU cores to run tasks
# MAGIC
# MAGIC 👉 Executors are the actual components that carry out the work
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC - **A. CPU Cores** ❌ Just hardware resources, not Spark components
# MAGIC - **B. Driver Nodes** ❌ Coordinates execution, does not run tasks
# MAGIC - **C. Worker Nodes** ❌ Host executors but do not execute tasks directly
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Executors = do the actual computation (task execution)

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
# MAGIC
# MAGIC **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The problem:
# MAGIC
# MAGIC - Queries filter on year AND month
# MAGIC - Current implementation uses bucketBy()
# MAGIC - Users see poor read performance
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❗ **Why current approach is inefficient:**
# MAGIC
# MAGIC - `.bucketBy(42, ["event_year", "event_month"])`
# MAGIC   - ❌ Bucketing:
# MAGIC     - Does NOT support partition pruning
# MAGIC     - Still scans large data portions
# MAGIC     - Better for joins, not filtering
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option B is correct:**
# MAGIC
# MAGIC - `.partitionBy(["event_year", "event_month"])`
# MAGIC   - ✔ Creates directory structure like:
# MAGIC     - `event_year=2024/event_month=10/`
# MAGIC   - ✔ Enables partition pruning:
# MAGIC     - Query with `WHERE year=2024 AND month=10`
# MAGIC     - ➡️ Only relevant partitions are read
# MAGIC   - 👉 Massive improvement in read performance 🚀
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.**
# MAGIC   - `partitionBy("event_year")`
# MAGIC   - ❌ Only partial pruning (month still scanned)
# MAGIC
# MAGIC - **C.**
# MAGIC   - Change bucket count
# MAGIC   - ❌ Doesn’t fix filtering issue
# MAGIC
# MAGIC - **D.**
# MAGIC   - `sortBy()`
# MAGIC   - ❌ Helps ordering, not pruning
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC - 👉 For query filters:
# MAGIC   - Use partitioning on filter columns
# MAGIC - 👉 Bucketing ≠ partitioning
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Final optimized code:**
# MAGIC python
# MAGIC final_df \
# MAGIC     .withColumn("event_year", F.year("event_ts")) \
# MAGIC     .withColumn("event_month", F.month("event_ts")) \
# MAGIC     .write \
# MAGIC     .partitionBy("event_year", "event_month") \
# MAGIC     .format("parquet") \
# MAGIC     .saveAsTable("events.live_latest")

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
# MAGIC **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement:
# MAGIC
# MAGIC - Enable SQL queries on a DataFrame
# MAGIC - View should be session-scoped (not global)
# MAGIC - Should not conflict with existing view names
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option D is correct:**
# MAGIC
# MAGIC `df.createOrReplaceTempView("my_view")`
# MAGIC
# MAGIC - ✔ Creates a temporary (session-scoped) view
# MAGIC - ✔ If the view already exists → replaces it safely
# MAGIC - ✔ Avoids conflicts/errors
# MAGIC - ✔ Ideal for iterative development
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **A.**
# MAGIC
# MAGIC - `createTempView()`
# MAGIC - ❌ Fails if view already exists (no replace)
# MAGIC
# MAGIC **B.**
# MAGIC
# MAGIC - `registerTempTable()`
# MAGIC - ❌ Deprecated
# MAGIC
# MAGIC **C.**
# MAGIC
# MAGIC - `createGlobalTempView()`
# MAGIC - ❌ Available across sessions (not secure for this use case)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Use `createOrReplaceTempView()` for safe, session-scoped SQL access

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
# MAGIC **Correct Answer: B**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement:
# MAGIC
# MAGIC - Read a Parquet file from a path
# MAGIC - Display its schema
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option B is correct:**
# MAGIC
# MAGIC `spark.sql("SELECT * FROM parquet.`" + events_parquet + "`").printSchema()`
# MAGIC
# MAGIC - ✔ Uses Spark SQL parquet datasource syntax
# MAGIC - ✔ Correct way to query a file path in SQL
# MAGIC - ✔ `.printSchema()` → displays schema
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **A.**
# MAGIC
# MAGIC - `SELECT * FROM " + events_parquet`
# MAGIC - ❌ Treats path as table name → invalid
# MAGIC
# MAGIC **C.**
# MAGIC
# MAGIC - `.show()`
# MAGIC - ❌ Displays data, not schema
# MAGIC
# MAGIC **D.**
# MAGIC
# MAGIC - `.show()`
# MAGIC - ❌ Same issue → shows data
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⚠️ **Note:**
# MAGIC
# MAGIC Proper syntax usually includes backticks:
# MAGIC
# MAGIC `spark.sql(f"SELECT * FROM parquet.`{events_parquet}`").printSchema()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC - 👉 To read files in Spark SQL:
# MAGIC   - Use `parquet.\path
# MAGIC   - Use `.printSchema()` to view schema

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
# MAGIC **Correct Answer: A**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The requirement:
# MAGIC
# MAGIC - Register a Python UDF
# MAGIC - Use it as a Spark SQL function (via `selectExpr`)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option A is correct:**
# MAGIC python
# MAGIC spark.udf.register("cubeudf", cubefunc, IntegerType())
# MAGIC num_df.selectExpr("cubeudf(num)")
# MAGIC
# MAGIC - ✔ Registers UDF with a name (`cubeudf`)
# MAGIC - ✔ Specifies return type
# MAGIC - ✔ Uses it in SQL expression via `selectExpr()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC **B.**
# MAGIC python
# MAGIC udf(cubefunc)
# MAGIC
# MAGIC - ❌ Works for DataFrame API, not SQL registration
# MAGIC
# MAGIC **C.**
# MAGIC python
# MAGIC DoubleType()
# MAGIC
# MAGIC - ❌ Incorrect return type (cube of int → int)
# MAGIC
# MAGIC **D.**
# MAGIC python
# MAGIC selectExpr(cubeudf(num)")
# MAGIC
# MAGIC - ❌ Invalid syntax + not registered for SQL
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 To use UDF in Spark SQL:
# MAGIC - Register using `spark.udf.register()`
# MAGIC - Use via SQL expressions (`selectExpr`, SQL queries)

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
# MAGIC **Correct Answer: C**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The code:
# MAGIC
# MAGIC python
# MAGIC joined_df = dfl.join(broadcast(df2), dfl.id == df2.id, "inner") \
# MAGIC                .join(broadcast(df3), df2.id == df3.id, "inner")
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option C is correct:**
# MAGIC
# MAGIC - ✔ Multiple broadcast joins are allowed
# MAGIC - ✔ Spark can:
# MAGIC   - Broadcast df2 (small table)
# MAGIC   - Broadcast df3 (small table)
# MAGIC - ✔ Execution:
# MAGIC   - dfl joins with broadcast(df2)
# MAGIC   - Result joins with broadcast(df3)
# MAGIC - 👉 Both joins avoid shuffle → high performance
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.** ❌ Spark supports multiple broadcast joins
# MAGIC - **B.** ❌ df2.id == df3.id is valid (since both contain id)
# MAGIC - **D.** ❌ broadcast() is already correctly applied inline
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC - 👉 Spark allows:
# MAGIC   - Chained broadcast joins
# MAGIC   - Broadcasting multiple small DataFrames
# MAGIC - 👉 Helps eliminate shuffle and improve performance

# COMMAND ----------

# MAGIC %md
# MAGIC Question #:342<br>
# MAGIC **A developer is creating a Spark application that performs multiple DataFrame transformations and actions. The developer wants to maintain optimal performance by properly managing the SparkSession. How should the developer handle the SparkSession throughout the application?**<br>
# MAGIC A. Stop and restart the SparkSession after each action.<br>
# MAGIC B. Avoid using a SparkSession and rely on SparkContext only.<br>
# MAGIC C. Create a new SparkSession instance before each transformation.<br>
# MAGIC D. Use a single SparkSession instance for the entire application.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC **Correct Answer: D**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC **The requirement:**
# MAGIC
# MAGIC - Maintain optimal performance
# MAGIC - Properly manage SparkSession
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **Why Option D is correct:**
# MAGIC
# MAGIC - Use a single SparkSession instance
# MAGIC
# MAGIC   - ✔ SparkSession is:
# MAGIC     - Expensive to create
# MAGIC     - Manages:
# MAGIC       - Configurations
# MAGIC       - Catalog
# MAGIC       - Execution context
# MAGIC
# MAGIC   - ✔ Best practice:
# MAGIC     - Create once
# MAGIC     - Reuse throughout the application
# MAGIC
# MAGIC   - 👉 Improves:
# MAGIC     - Performance
# MAGIC     - Resource utilization
# MAGIC     - Stability
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ❌ **Why other options are incorrect:**
# MAGIC
# MAGIC - **A.**
# MAGIC   - ❌ Restarting frequently → heavy overhead
# MAGIC - **B.**
# MAGIC   - ❌ SparkSession is the modern entry point (SparkContext alone is outdated)
# MAGIC - **C.**
# MAGIC   - ❌ Creating multiple sessions → inefficient and unnecessary
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Key takeaway:**
# MAGIC
# MAGIC 👉 Always:
# MAGIC - Use one SparkSession per application
# MAGIC - Reuse it across transformations and actions
