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
# MAGIC # Collection Types and Methods
# MAGIC
# MAGIC <!-- ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)  -->
# MAGIC
# MAGIC In this lesson you:
# MAGIC
# MAGIC - Introduce objects and methods
# MAGIC - Create lists
# MAGIC - Use methods on new collection data types

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
# MAGIC ## Objects
# MAGIC
# MAGIC In this lesson we are first going to look at some new functionality provided by data types, and then see how we can use that in some new data types. But before we do that, we need to look at some terminology.
# MAGIC
# MAGIC An [**object**](https://www.w3schools.com/python/python_classes.asp) is an instance of a specific data type. 
# MAGIC
# MAGIC For example, **`1`** is an Integer, so we would call it an Integer object. **`"Hello"`** is a String, so we would call it a String object.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ## Methods: More Functionality
# MAGIC
# MAGIC As a reminder, data types provide **data** of some kind and **operations** we can do on that kind of data. So far, we have actually only looked at a small fraction of the operations provided by each type. 
# MAGIC
# MAGIC Data types provide special functions called [**methods**](https://www.w3schools.com/python/gloss_python_object_methods.asp) which provide more functionality. Methods are exactly like normal functions except we call them on objects and they can edit the object they are called on. We invoke a method like this:
# MAGIC
# MAGIC **`object.method_name(arguments)`**
# MAGIC
# MAGIC This is a little tricky and we have a whole lesson on these coming up, but right now all you need to know is:
# MAGIC
# MAGIC **Methods are functions provided by a data type that we can call on objects of that type. They act on the object we call them with and allow us to use more functionality provided by that data type**

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### String Methods
# MAGIC
# MAGIC Let's take a look at an example of a method on a type we already know well: Strings. Strings provide a method called [**upper()**](https://www.w3schools.com/python/ref_string_upper.asp) which capitalizes a String.

# COMMAND ----------

greeting = "hello"
print(greeting.upper())
print(greeting)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### In-place methods
# MAGIC
# MAGIC Methods are functions that act on objects, and can either perform operations in-place (modify the underlying object it was called upon) or return a new object.
# MAGIC
# MAGIC Notice that the method **`upper()`** was not a stateful, in-place method as it returned a new string and did not modify the **`greeting`** variable. Take a look at <a href="https://www.w3schools.com/python/python_ref_string.asp" target="_blank">W3Schools</a> provides information on other string methods in Python.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### Tab Completion
# MAGIC
# MAGIC If you want to see a list of methods you can apply to an object, type **`.`** after the object, then hit tab key to see a drop down menu of available methods on that object.
# MAGIC
# MAGIC Try it below on the **`greeting`** string object. Type **`greeting.`** then hit the Tab key.

# COMMAND ----------

# Type . and hit Tab
greeting

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### `help()`
# MAGIC
# MAGIC While using tab completion is extremely helpful, if we use it to look through all possible methods for a given object, we might still not be certain how those methods work.
# MAGIC
# MAGIC We can look up their documentation, or we can use the [**help()**](https://www.geeksforgeeks.org/help-function-in-python/) function we saw in the last lesson.
# MAGIC
# MAGIC As a reminder, the **`help()`** function displays some of the documentation for the item passed into it.
# MAGIC
# MAGIC For example, when using tab completion above, we see the [**capitalize()**](https://www.w3schools.com/python/ref_string_capitalize.asp) string method, but we are not certain how it works.

# COMMAND ----------

help(greeting.capitalize)

# COMMAND ----------

greeting.capitalize()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ## Methods with Collection Types
# MAGIC
# MAGIC Now that we have a brief understanding of methods, let's look at some more advanced data types and the methods they provide.
# MAGIC
# MAGIC We are going to look at **collection data types** next. Like the name suggests, the data in these data types is a collection of other data types.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### Collection Type 1: Lists
# MAGIC
# MAGIC A list is just an ordered sequence of items. 
# MAGIC
# MAGIC It is defined as a sequence of comma separated items inside square brackets like this: **`[item1, item2, item3...]`**
# MAGIC
# MAGIC The items may be of any type, though in practice you'll usually create lists where all of the values are of the same type.
# MAGIC
# MAGIC Let's make a <a href="https://www.w3schools.com/python/python_lists.asp" target="_blank">list</a> of what everyone ate for breakfast this morning.
# MAGIC
# MAGIC <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Scrambed_eggs.jpg/1280px-Scrambed_eggs.jpg" width="20%" height="10%">

# COMMAND ----------

breakfast_list = ["pancakes", "eggs", "waffles"]
breakfast_list

# COMMAND ----------

# Python can tell us breakfast_list's type
type(breakfast_list)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC We'll use our **`breakfast_list`** as the running example, but note that the values in a list can be of any type, as shown below.

# COMMAND ----------

# any type works
["hello", True, 1, 1.5]

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC #### List Methods
# MAGIC
# MAGIC Now that we understand the **data** a list data type provides, let's look at some of its **functionality**.
# MAGIC
# MAGIC Something you will frequently want to do is add a new item to an existing list. 
# MAGIC
# MAGIC Lists provide a method called [**append()**](https://www.w3schools.com/python/ref_list_append.asp) to do just that. 
# MAGIC
# MAGIC **`append()`** takes in an argument of any type and edits the list it is called on so that the argument is stuck onto the end of the list. 
# MAGIC
# MAGIC Let's say after we ate our pancakes, eggs, and waffles, we also had yogurt.
# MAGIC
# MAGIC Here, we can use **`append()`** to add yogurt to our **`breakfast_list`**.

# COMMAND ----------

breakfast_list.append("yogurt")
breakfast_list

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC **Note:** Notice here that **`append()`** is an in-place method.
# MAGIC The method does not return a new list, but rather edits the original **`breakfast_list`** object. 
# MAGIC
# MAGIC **`+`** is also defined as concatenation for lists as shown below.

# COMMAND ----------

["pancakes", "eggs"] + ["waffles", "yogurt"]

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC While we typically use **`append()`**, it is possible to append elements to a list using **`+`**.

# COMMAND ----------

breakfast_list = ["pancakes", "eggs", "waffles"]
breakfast_list = breakfast_list + ["yogurt"]
breakfast_list

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC A useful shortcut operation for this is **`+=`**.
# MAGIC
# MAGIC **`breakfast_list`** `+=` **`["yogurt"]`** is the same thing as **`breakfast_list`** `=` **`breakfast_list`** `+` **`["yogurt"]`**.
# MAGIC
# MAGIC The **`+=`** operator works for other types as well, using their respective **`+`** operator.

# COMMAND ----------

breakfast_list = ["pancakes", "eggs", "waffles"]
breakfast_list += ["yogurt"]
breakfast_list

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC #### List indexing
# MAGIC
# MAGIC Often, we want to reference a specific item or items in a list. This is called [list indexing](https://www.w3schools.com/python/python_lists_access.asp).
# MAGIC
# MAGIC Lists provide an operation to get the item at a certain index in the list like this:
# MAGIC
# MAGIC       list_name[index]
# MAGIC
# MAGIC In Python indices start from 0, so the first element of the list is 0, the second is 1, etc.

# COMMAND ----------

breakfast_list[0]

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC We can also use negative indexing, which starts counting from right to left, starting from -1. 
# MAGIC
# MAGIC Thus, the last element of the list is -1, the second to last is -2, etc.

# COMMAND ----------

breakfast_list[-1]

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC We can also provide a range of indices we want to access like this:
# MAGIC
# MAGIC **`list_name[start:stop]`**
# MAGIC
# MAGIC This returns a list of the values starting at **`start`** and up to but not including **`stop`**.

# COMMAND ----------

# Note the stop index is exclusive
breakfast_list[0:2]

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC If we don't provide a start index, Python assumes we start at the beginning.
# MAGIC
# MAGIC If we don't provide a stop index, Python assumes we stop at the end.

# COMMAND ----------

print(breakfast_list[:2])
print(breakfast_list[1:])

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC We can also change the value of an index in a list to be something new like this:

# COMMAND ----------

print(breakfast_list)
breakfast_list[0] = "sausage"

print(breakfast_list)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC We can also use **`in`** to check if an element is in a given list. This is a boolean operation:

# COMMAND ----------

"waffles" in breakfast_list

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ####  Filtering Lists
# MAGIC
# MAGIC Sometimes we need to extract specific items from a list based on certain criteria.
# MAGIC
# MAGIC You can achieve this by filtering a list, which allows us to create a new list containing only the elements that meet our defined conditions.
# MAGIC
# MAGIC Let's start with a list of breakfast items that we had this morning.
# MAGIC

# COMMAND ----------

breakfast_list = ["pancakes", "eggs", "waffles", "milk", "yogurt", "bacon", "fruit", "cereal"]

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Now, suppose you want to create a new list containing breakfast items made from dairy products. We'll define a list of milk products that we want to filter for.

# COMMAND ----------

milk_products = []
milk_items = ["milk", "yogurt"]

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Let's get the milk products from the breakfast we just ate.
# MAGIC
# MAGIC We are going to use a loop to do this. Looping is a programming construct that we will cover in more detail in a different discussion. For now, just know that it provides a way to iterate over each item in a list.

# COMMAND ----------

for item in breakfast_list:
    if item in milk_items:
        milk_products.append(item)

print(milk_products)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC This works, but it's not very concise. You can also achieve this using the **`filter()`** method. It is a useful technique for extracting elements from a list based on specific criteria.
# MAGIC
# MAGIC Now, let's get the milk products from the breakfast we just ate, but this time, we'll use the **`filter()`** method.

# COMMAND ----------

milk_products = list(filter(milk_items.count, breakfast_list))

print(milk_products)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC In this example, the **`filter()`** method iterates over each item in the **`breakfast_list`** and includes it in a new list if it matches the specified criteria. In this case, that criteria is the **`milk_items.count()`**, which returns the number of times an element is found in the list. So in otherwords, we're filtering items that can be found in the **`milk_items`** list; otherwise, the item is excluded.
# MAGIC
# MAGIC As you can see, we achieved the same result as the loop-based approach, obtaining a list of milk products from the breakfast list.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### List Comprehensions 
# MAGIC
# MAGIC List comprehensions are a concise pattern for creating new lists by applying an inline expression to each item in an existing list. They are often preferred for transforming or filtering list elements because they offer shorter, more compact, and readable code.
# MAGIC
# MAGIC Now, we already have our breakfast list. Let's use [list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp) to filter milk products from **`breakfast_list`**.

# COMMAND ----------

milk_products = [item for item in breakfast_list if item in milk_items]
print(milk_products)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### Collection Type 2: Dictionaries
# MAGIC
# MAGIC A [Dictionary](https://www.w3schools.com/python/python_dictionaries.asp) is a sequence of key-value pairs. We define a dictionary as follows:
# MAGIC
# MAGIC `{key_1: value_1, key_2: value_2, ...}`
# MAGIC
# MAGIC The keys and values can all be of any type. However, because each key maps to a value, it is important that *all keys are unique*.
# MAGIC
# MAGIC Let's create a breakfast dictionary, where the keys are the type of food and the values are the number of those foods we ate for breakfast.

# COMMAND ----------

breakfast_dict = {"pancakes": 1, "eggs": 2, "waffles": 3}
breakfast_dict

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC #### Dictionary Methods
# MAGIC
# MAGIC Dictionaries provide the method [**dict_object.get()**](https://www.w3schools.com/python/ref_dictionary_get.asp) to get the value in the dictionary for the given argument. 
# MAGIC
# MAGIC Let's see how many waffles we ate.

# COMMAND ----------

breakfast_dict.get("waffles")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC Alternatively, you can use the syntax **`dict_object[key]`**.

# COMMAND ----------

breakfast_dict["waffles"]

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC
# MAGIC You can update a dictionary similarly to a list by assigning **`breakfast_dict[key]`** to be something. 
# MAGIC
# MAGIC If the key is present, it overwrites the current value. If not, it creates a new key-value pair. 
# MAGIC
# MAGIC Let's say we ate another waffle, bringing our total up to 4 waffles, and then ate a yogurt.

# COMMAND ----------

print(breakfast_dict)
breakfast_dict["waffles"] += 1
breakfast_dict["yogurt"] = 1
print(breakfast_dict)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC Notice the use of **`+=`** to increment the count of waffles.
# MAGIC
# MAGIC **Question**: Why did we not use **`+=`** to increment the yogurt count?

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC In order to determine if a key is in a dictionary, we can use the method [**dict_name.keys()**](https://www.w3schools.com/python/ref_dictionary_keys.asp). This returns a list of the keys in the dictionary. 
# MAGIC
# MAGIC Similar to lists, we can use **`in`** to see if our key is in the dictionary. Let's see if we ate bacon for breakfast.

# COMMAND ----------

print(breakfast_dict.keys())
print("bacon" in breakfast_dict.keys())

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Collection Type 3: Tuples
# MAGIC
# MAGIC A tuple is an ordered sequence of items, just like a list.
# MAGIC
# MAGIC [Tuples](https://www.w3schools.com/python/python_tuples.asp), unlike lists and dictionaries, are immutable, meaning they cannot be changed once they are created. We define a tuple as follows: **`(item1, item2, item3, ...)`**.
# MAGIC
# MAGIC Tuples can contain items of various types, and they maintain the order of the elements.
# MAGIC
# MAGIC Let's create a breakfast tuple to keep track of the items we had for breakfast.

# COMMAND ----------

breakfast_tuple = ("pancakes", "eggs", "waffles")
breakfast_tuple

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Tuple Methods 
# MAGIC
# MAGIC Tuples are simple and do not have many built-in methods compared to lists and dictionaries. Tuples don't have methods like **`append()`**, for example, since they are immutable. Once a tuple is created, you cannot change, add, or remove elements from it. However, you can perform operations like indexing, slicing, and checking for the presence of an element, similar to lists. Let's take a look at what we had for breakfast first using indexing.

# COMMAND ----------

breakfast_tuple[0]

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Slicing can also be used with tuples, which allows you to extract a range of elements.

# COMMAND ----------

breakfast_tuple[1:3]

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC You can use the  **`in`** operator to check if an element exists in a tuple. let's see if we had pancakes for breakfast or not.

# COMMAND ----------

print("pancakes" in breakfast_tuple)

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2026 Databricks, Inc. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the <a href="https://www.apache.org/" target="_blank">Apache Software Foundation</a>.<br/><br/><a href="https://databricks.com/privacy-policy" target="_blank">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use" target="_blank">Terms of Use</a> | <a href="https://help.databricks.com/" target="_blank">Support</a>
