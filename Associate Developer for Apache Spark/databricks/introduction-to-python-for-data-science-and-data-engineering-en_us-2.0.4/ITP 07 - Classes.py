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
# MAGIC # Classes
# MAGIC <!-- ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)  -->
# MAGIC
# MAGIC In this lesson you:
# MAGIC - Explore how to define a new data type called a class
# MAGIC - Utilize instance attributes to define data for classes
# MAGIC - Use methods to add functionality to classes

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
# MAGIC ## Classes
# MAGIC
# MAGIC From [W3Schools](https://www.w3schools.com/python/python_classes.asp): 
# MAGIC ```
# MAGIC Python is an object oriented programming language. Almost everything in Python is an object, with its properties and methods. 
# MAGIC
# MAGIC A Class is like an object constructor, or a "blueprint" for creating objects.
# MAGIC ```
# MAGIC
# MAGIC When we worked with functions, they allowed us to reuse the same code applied to different parameters. **Classes can be thought of as a step beyond functions as they provide a reusable blueprint for both code and data.**
# MAGIC
# MAGIC We've now seen the basic built-in types and some more advanced collection types. We can also define our own custom [**classes**](https://www.w3schools.com/python/python_classes.asp) to fit our needs. 
# MAGIC
# MAGIC To define a class we write:
# MAGIC
# MAGIC ```
# MAGIC class ClassName():
# MAGIC     <code block>
# MAGIC ```
# MAGIC
# MAGIC Up until now, we've typically used the `snake_case` convention. However, when defining a class, [Python style guides](https://peps.python.org/pep-0008/) recommend using `CapWords`, with every word capitalized and no spaces. 
# MAGIC
# MAGIC **Note**: **`pass`** tells Python to not do anything. We're effectively defining a dog that does nothing (not quite what you'd want in a dog!).

# COMMAND ----------

# Create the blueprint
class Dog():
    pass

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC For the built-in types we have seen so far, creating an object from a class has been built-in. If you write **`1`** or **`"hello"`** Python knows what types those are and creates those `int` or `str` objects for you. 
# MAGIC
# MAGIC However, for classes that we define we have to create objects as follows:
# MAGIC
# MAGIC **`object_name = ClassName()`**
# MAGIC
# MAGIC Technically, this is called "instantiating" the class as we create a specific version of the object. Now we have a **`Dog`** class. Let's make a **`Dog`** object, and call it **`my_dog`**.

# COMMAND ----------

# Instantiate the blueprint and save it to the variable
my_dog = Dog()

type(my_dog)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Code Reuse with Methods
# MAGIC
# MAGIC Now that we can make a **`Dog`** that does nothing, let's add some functionality!
# MAGIC
# MAGIC Functionality in classes are defined by [**methods**](https://www.w3schools.com/python/gloss_python_object_methods.asp), which we saw in a previous lesson.
# MAGIC
# MAGIC As a reminder, a **method** is a special function that acts on an object that we call like this: **`object.method(args)`**
# MAGIC
# MAGIC We define a method similarly to how we define a normal function except with two differences:
# MAGIC
# MAGIC 1. We nest the definition of the method within the class definition. 
# MAGIC 1. We must specify a parameter named **`self`**, followed by any additional parameters.
# MAGIC
# MAGIC This looks like this:
# MAGIC
# MAGIC ```
# MAGIC class ClassName():
# MAGIC
# MAGIC     def method_name(self, args):
# MAGIC         method code
# MAGIC ```
# MAGIC
# MAGIC We will ignore the **`self`** parameter for now, but come back to it in a moment.
# MAGIC
# MAGIC Let's look at a very simple example: writing a method that takes in a name and returns it.

# COMMAND ----------

class UpdatedDog():
    
    def return_name(self, name):
        return f"name: {name}"

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Now let's make an object of our updated **`Dog`** class and call the method. Remember we call methods like this: **`object.method(args)`**.
# MAGIC
# MAGIC Note that we do *not* pass an argument for the special **`self`** parameter.

# COMMAND ----------

my_updated_dog = UpdatedDog()

my_updated_dog.return_name("Rex")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC What about `self`?
# MAGIC
# MAGIC A method differs from a function in that it can act on the object it's called on. The method needs to be able to reference the object that called it. That's what **`self`** refers to.
# MAGIC
# MAGIC When we call **`object.method(self, args)`** the object itself is passed to the **`self`** parameter automatically by Python.

# COMMAND ----------

class DogWithSelf():
    
    def print_self(self):
        print(self)
        
dog_with_self = DogWithSelf()

print(dog_with_self)
dog_with_self.print_self() # prints the same object

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Notice that when we print the **`new_dog`** object and call our **`print_self()`** method on **`new_dog`** we see the same object. 
# MAGIC
# MAGIC That's because **`new_dog`** was passed as the argument to **`self`** in **`print_self()`**

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Data Caching with Attributes
# MAGIC
# MAGIC In our class, we need some way to store data. **When a variable is stored in a class, it is called an attribute.** Attributes are just variables that are defined for each instance of an object. Every instance will have the same named attributes but they're normally set to different values.
# MAGIC
# MAGIC ```
# MAGIC class ClassName():
# MAGIC
# MAGIC     def __init__(self, arg):
# MAGIC         self.arg = arg
# MAGIC ```
# MAGIC
# MAGIC Python provides a special method called **`__init__(self)`** that is automatically called when our object is initialized. This is often referred to as the *constructor method* for the class since it constructs the class's attributes.
# MAGIC
# MAGIC Let's say for our **`Dog`** class that we want every dog object to have a name and a color. To do that, we create two attributes for the class **`name`** and **`color`**.
# MAGIC
# MAGIC Then, every **`Dog`** object has a name and color attribute, but they can be set to different values for each object, so that each dog object can have its own name and color.

# COMMAND ----------

class DogWithAttributes():

    def __init__(self, name, color):
        print("This ran automatically!")
        self.name = name
        self.color = color

dog_with_attributes = DogWithAttributes("Rex", "Orange")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC When the `__init__()` method was automatically called, it saved those variables to `self`, which is the instantiation of the object. We can access the attribute similar to how we accessed methods but without the parentheses.

# COMMAND ----------

dog_with_attributes.name

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC In a method definition we can access an attribute using **`self.attribute_name`**, since **`self`** refers to the object that calls the method, regardless of what we named it when we instantiated it.

# COMMAND ----------

class DogWithAttributesAndMethod():
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def return_name(self):
        return self.name
        
my_dog = DogWithAttributesAndMethod("Rex", "Blue")
my_dog.return_name()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC We now have all the tools we need to add functionality! Let's say we want to add the ability to change a dog's name. We can simply update the **`name`** attribute like this.

# COMMAND ----------

class DogWithAttributesAndMethods():
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def return_name(self):
        return self.name
        
    def update_name(self, new_name):
        self.name = new_name
        
my_dog = DogWithAttributesAndMethods("Rex", "Blue")
print(f"Here's my name now: {my_dog.return_name()}")

my_dog.update_name("Brady")
print(f"Here's my name after updating it: {my_dog.return_name()}")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## More Advanced Classes 
# MAGIC
# MAGIC Classes can have many methods and attributes. They can also access the attributes of another class.
# MAGIC
# MAGIC Take a look at the `return_both_names` method to see how a class can use the attributes of another class.

# COMMAND ----------

class DogFinal():
    
    def __init__(self, name_str, color_str):
        self.name = name_str
        self.color = color_str
        
    def return_name(self):
        return self.name
        
    def update_name(self, new_name):
        self.name = new_name
        
    def return_both_names(self, other_dog_object):
        return self.name + " and " + other_dog_object.name
        
dog_1 = DogFinal("Rex", "Blue")
dog_2 = DogFinal("Brady", "Purple")

dog_1.return_both_names(dog_2)

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2026 Databricks, Inc. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the <a href="https://www.apache.org/" target="_blank">Apache Software Foundation</a>.<br/><br/><a href="https://databricks.com/privacy-policy" target="_blank">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use" target="_blank">Terms of Use</a> | <a href="https://help.databricks.com/" target="_blank">Support</a>
