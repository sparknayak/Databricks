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
# MAGIC # Cloud Computing 101
# MAGIC <!-- ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)  -->
# MAGIC
# MAGIC In this lesson you:
# MAGIC - Contrast local vs on-prem vs cloud computing
# MAGIC - Introduce the basics of cloud computing
# MAGIC - Explore how Databricks works in a cloud based setting with Spark

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
# MAGIC #### Local Execution
# MAGIC
# MAGIC Local execution refers to when you're leveraging only the compute of your local machine to execute code. For example, you're a data scientist running Jupyter notebooks locally on your laptop. 
# MAGIC
# MAGIC <!-- <img src="https://s3.us-west-2.amazonaws.com/files.training.databricks.com/courses/Python/LocalPicture.png" > -->

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### On-Prem
# MAGIC
# MAGIC On-prem is short for on-premise. This refers to the situation where someone manages multiple computers that communicate with each other to store data and run code. This offers significantly more compute power and storage than a single machine. 
# MAGIC
# MAGIC
# MAGIC Here is an illustration showing an on-prem setting:
# MAGIC
# MAGIC <!-- <img src="https://s3.us-west-2.amazonaws.com/files.training.databricks.com/courses/Python/OnPremPicture.png"> -->

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC
# MAGIC
# MAGIC #### Cloud
# MAGIC
# MAGIC Managing an on-prem system is difficult, expensive, and scales poorly. An popular alternative is to rent storage and computer power from cloud providers. 
# MAGIC These providers are typically large technology companies such as Amazon, Microsoft, and Google. 
# MAGIC
# MAGIC In this situation, a user simply accesses data and compute via a web browser or other application, while the actual data and computation are being stored and ran in large warehouses of machines called a data center managed by these companies. This is referred to as a cloud-based setting. 
# MAGIC
# MAGIC It is much less expensive and easier to use cloud storage because you don't have to create or manage your own data center. It also allows for easy scaling: just buy as much storage and compute power as you need at the moment and turn it off when you are finished. 
# MAGIC
# MAGIC <!-- <img src="https://s3.us-west-2.amazonaws.com/files.training.databricks.com/courses/Python/CloudPicture.png" style="width:800px;height:500px;"> -->

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Virtual Machines
# MAGIC
# MAGIC In a cloud based setting we use computers managed by cloud providers to run code and store data. 
# MAGIC
# MAGIC We are able to run code this way by using **virtual machines** on those computers. 
# MAGIC
# MAGIC A virtual machine separates the CPU, memory, networking, and disk storage from other virtual machines on the same computer. 
# MAGIC
# MAGIC By renting virtual machines on cloud computers, we can use the resources those computers provide without worrying about sharing information with other users also renting virtual machines.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Cloud Storage
# MAGIC
# MAGIC Cloud providers offer ways to store data on the cloud easily. These services use computers and software that are specialized for storing data in a reliable way that can scale well.
# MAGIC
# MAGIC One type of storage offered by cloud providers is **object storage**, which can store any type of data including text, images, videos, and other binary data. Some examples of cloud object storage are:
# MAGIC
# MAGIC * [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/)
# MAGIC * Microsoft's [Azure Data Lake Storage Gen2 (ADLS Gen 2)](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction)
# MAGIC * [Google Cloud Storage](https://cloud.google.com/storage)
# MAGIC
# MAGIC Cloud providers also offer services to store and manage relational databases &mdash; such as MySQL, PostgreSQL, and Microsoft SQL Server &mdash; and key-value stores or other "NoSQL" databases &mdash; such as Amazon DynamoDB, Azure Cosmos DB, and Google Cloud Bigtable.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Databricks
# MAGIC
# MAGIC <!-- <img src="https://s3.us-west-2.amazonaws.com/files.training.databricks.com/images/databricks_cloud_overview.png" style="width:800px;height:500px;"> -->
# MAGIC
# MAGIC Databricks provides a unified, cloud-based platform for running and managing a wide variety of data analytics, business intelligence, data science, and machine learning tasks. Databricks runs on multiple cloud providers and can process the data you store in cloud object storage using the virtual machines of that cloud provider.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Apache Spark
# MAGIC
# MAGIC A single computer usually has the memory and computational power to perform calculations on data sets up to the size of a few gigabytes or less. Data sets larger than that either can't fit into the memory of a single computer or take an unacceptably long time for a single computer to process. For these types of "big data" use cases, we need a system that can split a large data set into smaller subsets &mdash; often referred to as **partitions** &mdash; and then distribute the processing of these data partitions across a number of computers.
# MAGIC
# MAGIC [Apache Spark](https://spark.apache.org/) is an open-source data processing engine that manages distributed processing of large data sets.
# MAGIC
# MAGIC For example, let's say that we have a large data set and we want to calculate various statistics for some of its numeric columns. With Apache Spark, our program only needs to specify the data set to read and the statistics that we want calculated. We can then run the program on a set of computers that have been configured to serve as an Apache Spark **cluster**. When we run it, Spark automatically:
# MAGIC
# MAGIC * determines how to divide the data set into partitions,
# MAGIC * assigns those partitions to the various computers of the cluster with instructions for calculating per-partition statistics, and
# MAGIC * finally collects those per-partitions statistics and calculates the final results we requested.
# MAGIC
# MAGIC Spark was created originally as a research project at the University of California Berkeley. In 2013, the project was donated to the Apache Software Foundation. That same year the creators of Spark founded Databricks.
# MAGIC
# MAGIC Databricks, in general, uses Apache Spark as the computation engine for the platform. Databricks provides simple management tools for running Spark clusters composed of cloud-provided virtual machines to process the data you have in cloud object storage and other systems.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Unity Catalog
# MAGIC
# MAGIC Unity Catalog is a unified governance solution for data and AI assets on the Databricks Data Intelligence Platform. It is designed to standardize a security model that is consistent and transparent across all clouds. Unity Catalog supports structured data (tables and views), unstructured data (files and folders), and AI assets. It can be integrated with your own object storage so you can manage access to those objects as if they were directly within your metastore. Unity Catalog also supports external catalogs like Alation, Collibra, Informatica EDC, and others.
# MAGIC
# MAGIC Unity Catalog goes one step beyond the traditional two-level namespace and provides an additional level for organizing your securable objects: **catalogs** and **schemas (databases)**.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Code Versioning and Collaboration with Git
# MAGIC
# MAGIC [Git](https://git-scm.com/) is a free and open source version control system. This means that it tracks the changes to code and allows you to store different versions of a project. You can restore previous versions if needed, and it also allows for branching and merging of a project where you can create different versions of a project focused on developing different features and then combine them back together. 
# MAGIC
# MAGIC Git is a tool that can be run on your local machine or on Databricks to help with version control, but it shines as a collaboration tool when combined with [GitHub](https://github.com/). GitHub is a cloud-based hosting service that lets you manage Git code repositories, and it allows multiple users to download versions of a project, develop for the project, and then push back their changes. These changes can then be merged, so this creates an easy system for collaboration that forms the backbone of code projects. 
# MAGIC
# MAGIC Open Source technology is usually available as a public Github Repository where anyone can download the code and help develop it. For instance, Apache Spark is open source and you can view all its code, download it, and even help create new features all from its GitHub page [here](https://github.com/apache/spark).

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2026 Databricks, Inc. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the <a href="https://www.apache.org/" target="_blank">Apache Software Foundation</a>.<br/><br/><a href="https://databricks.com/privacy-policy" target="_blank">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use" target="_blank">Terms of Use</a> | <a href="https://help.databricks.com/" target="_blank">Support</a>
