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
# MAGIC # Classes Lab
# MAGIC <!-- ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)  -->
# MAGIC
# MAGIC In this lab you:<br>
# MAGIC
# MAGIC Apply concepts learned in the last lesson, including:
# MAGIC - Utilizing instance attributes to define data for new data types
# MAGIC - Using methods to add functionality to new data types

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

# MAGIC %md-sandbox
# MAGIC
# MAGIC
# MAGIC ## Exercise: Simpson
# MAGIC
# MAGIC <img src="https://i.pinimg.com/originals/13/63/37/13633734d116fe188af57fe9da7d095e.jpg" style="height:400">
# MAGIC
# MAGIC Define a class **`Simpson`** representing members of the Simpson's family that has the following attributes and methods:
# MAGIC
# MAGIC * Each Simpson has a **`first_name`**, **`age`**, and **`favorite_food`**. 
# MAGIC   * Define the **`__init__()`** method to initialize these attributes. 
# MAGIC
# MAGIC * Define a method called **`simpson_summary()`** which returns a string in this format: `{first_name} Simpson is {age} years old and their favorite food is {favorite_food}`
# MAGIC   * For example, if `first_name="Homer"`, `age=39`, and `favorite_food="donuts"`, this should return: `Homer Simpson is 39 years old and their favorite food is donuts`
# MAGIC
# MAGIC * Define a method called **`older()`** which takes in another **`Simpson`** object and returns **`True`** if the person that called the method is older than the other one, **`False`** otherwise.

# COMMAND ----------

class Simpson
<ToDo>

# COMMAND ----------

# MAGIC %skip
# MAGIC class Simpson():
# MAGIC     
# MAGIC     def __init__(self, first_name, age, favorite_food):
# MAGIC         self.first_name = first_name
# MAGIC         self.age = age
# MAGIC         self.favorite_food = favorite_food
# MAGIC         
# MAGIC     def simpson_summary(self):
# MAGIC         return f"{self.first_name} Simpson is {self.age} years old and their favorite food is {self.favorite_food}"
# MAGIC         
# MAGIC     def older(self, other_simpson):
# MAGIC         return self.age > other_simpson.age

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Check your work:**

# COMMAND ----------

homer = Simpson("Homer", 39, "Donuts")
bart = Simpson("Bart", 10, "Hamburgers")
assert homer.first_name == "Homer", "first_name is not set properly"
assert homer.favorite_food == "Donuts", "favorite_food is not set properly"
assert bart.age == 10, "Age is not set properly"
assert homer.simpson_summary() == "Homer Simpson is 39 years old and their favorite food is Donuts", "simpson_summary is incorrect"
assert bart.simpson_summary() == "Bart Simpson is 10 years old and their favorite food is Hamburgers", "simpson_summary is incorrect"
assert homer.older(bart) == True, "Homer is older than Bart"
assert bart.older(homer) == False, "Bart is not older than Homer"
print("Test passed!")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Bonus Exercise
# MAGIC
# MAGIC - Create a class called Fraction consisting of the following:
# MAGIC   - Public attributes
# MAGIC     - Numerator
# MAGIC     - Denominator
# MAGIC   - Constructor that initializes the numerator and denominator
# MAGIC   - Method named __to_string__ that returns the Fraction as a string in the format
# MAGIC     Numerator / Denominator
# MAGIC   - Method named __as_decimal__ that returns the value of the fraction as a number (including decimal places)
# MAGIC   - Method named __invert__ that alters the state of the Fraction to it's inverted equivalent.
# MAGIC   - Method named __least_common_denominator__ that computes the least Common Denominator of 2 fractions.
# MAGIC   - A method named __reduce__ that reduces a Fraction to it's least common denominator
# MAGIC   - Method named __is_equal__ that compares a Fraction with another received in its argument list to determine whether or not they are equal
# MAGIC     - Note that 2/4 == 1/2
# MAGIC   - Method named __is_less_than__ that compares a Fraction with another received in its argument list to determine whether the object on which the method is invoked is smaller than the one received in its argument list
# MAGIC     - Note 2/4 is smaller than 5/9
# MAGIC   - A Method named __scale__ that scales a fraction to a designated multiplier
# MAGIC     - e.g. 1/4 scaled by 2 becomes 2/8
# MAGIC   - A method named __clone__ that given a Fraction in its argument list, alters its current state to that of the Fraction received in its argument list

# COMMAND ----------

# I have provided a helper standalone function you may wish to invoke as part of your implementation

def greatest_common_factor(a, b):
    gcf = 1
    if a < b:
        limit = a
    else:
        limit = b
    
    for index in range(2, limit + 1):
        if (a % index == 0) and (b % index == 0):
            gcf = index
        
    return gcf

# COMMAND ----------

class Fraction():
<ToDo>

# COMMAND ----------

# MAGIC %skip
# MAGIC class Fraction():
# MAGIC     def __init__(self, numerator, denominator):                     # Constructor
# MAGIC         self.numerator = numerator                                  # Attribute initialization
# MAGIC         self.denominator = denominator
# MAGIC    
# MAGIC     def to_string(self):                                             # Method definitions
# MAGIC         return f"{self.numerator} / {self.denominator}"
# MAGIC   
# MAGIC     def as_decimal(self):
# MAGIC         return self.numerator / self.denominator
# MAGIC   
# MAGIC     def invert(self):
# MAGIC         temp = self.numerator
# MAGIC         self.numerator = self.denominator
# MAGIC         self.denominator = temp
# MAGIC         return None
# MAGIC   
# MAGIC     def least_common_denominator(self, other):
# MAGIC         a = self.denominator
# MAGIC         b = other.denominator
# MAGIC
# MAGIC         lcd = float(a * b)
# MAGIC         lcd /= greatest_common_factor(a, b)
# MAGIC
# MAGIC         return lcd
# MAGIC   
# MAGIC     def reduce(self):
# MAGIC         gcf = greatest_common_factor(self.numerator, self.denominator)
# MAGIC     
# MAGIC         if (self.denominator < 0):
# MAGIC               gcf *= -1
# MAGIC
# MAGIC         self.numerator /= gcf
# MAGIC         self.denominator /= gcf
# MAGIC         return self
# MAGIC   
# MAGIC     def is_equal(self, other):
# MAGIC         return(self.as_decimal() == other.as_decimal())
# MAGIC   
# MAGIC     def is_less_than(self, other):
# MAGIC         return self.as_decimal() < other.as_decimal()
# MAGIC   
# MAGIC     def scale(multiplier):
# MAGIC         self.numerator *= multiplier
# MAGIC         self.denominator *= multiplier
# MAGIC     
# MAGIC     def clone(self):
# MAGIC         return Fraction(self.numerator, self.denominator)

# COMMAND ----------

# Test your work
one_half = Fraction(1,2)
two_fourths = Fraction(2,4)
two_thirds = Fraction(2,3)
six_ninths = Fraction(6,9)

assert one_half.to_string() == "1 / 2", "to_string did not convert the string properly"
assert two_fourths.as_decimal() == .5, "as_decimal did not convert the fraction to a decimal number properly"

four_eighths = Fraction(4, 8)
four_eighths.invert()
assert four_eighths.to_string() == "8 / 4", "invert did not convert the fraction properly"

assert two_thirds.least_common_denominator(six_ninths) == 9.0, "least_common_denominator did not compute the least common denominator properly"

assert one_half.is_equal(two_fourths) == True, "is_equal did not compare two fractions properly"
assert one_half.is_less_than(two_thirds) == True, "is_less_than did not compare two fractions properly"

# COMMAND ----------

# MAGIC %md
# MAGIC ### Bonus Exercise
# MAGIC
# MAGIC Modify the aforementioned class implementation to properly encapsulate the numerator and denominator attributes so that they cannot be accessed directly from an application

# COMMAND ----------

class Fraction():
<ToDo>

# COMMAND ----------

# MAGIC %skip
# MAGIC class Fraction():
# MAGIC       def __init__(self, numerator, denominator):                     # Constructor
# MAGIC         self.__numerator = numerator                                  # Attribute initialization
# MAGIC         self.__denominator = denominator
# MAGIC
# MAGIC       def to_string(self):                                             # Method definitions
# MAGIC         return f"{self.__numerator} / {self.__denominator}"
# MAGIC
# MAGIC       def as_decimal(self):
# MAGIC         return self.__numerator / self.__denominator
# MAGIC
# MAGIC       def invert(self):
# MAGIC         temp = self.__numerator
# MAGIC         self.__numerator = self.__denominator
# MAGIC         self.__denominator = temp
# MAGIC         return None
# MAGIC
# MAGIC       def least_common_denominator(self, other):
# MAGIC         a = self.__denominator
# MAGIC         b = other.__denominator
# MAGIC
# MAGIC         lcd = float(a * b)
# MAGIC         lcd /= greatest_common_factor(a, b)
# MAGIC
# MAGIC         return lcd
# MAGIC
# MAGIC       def reduce(self):
# MAGIC         gcf = greatest_common_factor(self.__numerator, self.__denominator)
# MAGIC
# MAGIC         if (self.__denominator < 0):
# MAGIC               gcf *= -1
# MAGIC
# MAGIC         self.__numerator /= gcf
# MAGIC         self.__denominator /= gcf
# MAGIC         return self
# MAGIC
# MAGIC       def is_equal(self, other):
# MAGIC         return(self.as_decimal() == other.as_decimal())
# MAGIC
# MAGIC       def is_less_than(self, other):
# MAGIC         return self.as_decimal() < other.as_decimal()
# MAGIC
# MAGIC       def scale(multiplier):
# MAGIC         self.__numerator *= multiplier
# MAGIC         self.__denominator *= multiplier
# MAGIC
# MAGIC       def clone(self):
# MAGIC         return Fraction(self.__numerator, self.__denominator)
# MAGIC
# MAGIC       def get_numerator(self):
# MAGIC         return self.__numerator
# MAGIC
# MAGIC       def get_denominator(self):
# MAGIC         return self.__denonminator

# COMMAND ----------

# Test your work
one_half = Fraction(1,2)
two_fourths = Fraction(2,4)
two_thirds = Fraction(2,3)
six_ninths = Fraction(6,9)

assert one_half.to_string() == "1 / 2", "to_string did not convert the string properly"
assert two_fourths.as_decimal() == .5, "as_decimal did not convert the fraction to a decimal number properly"

four_eighths = Fraction(4, 8)
four_eighths.invert()
assert four_eighths.to_string() == "8 / 4", "invert did not convert the fraction properly"

assert two_thirds.least_common_denominator(six_ninths) == 9.0, "least_common_denominator did not compute the least common denominator properly"

assert one_half.is_equal(two_fourths) == True, "is_equal did not compare two fractions properly"
assert one_half.is_less_than(two_thirds) == True, "is_less_than did not compare two fractions properly"

nine_fifteenths = Fraction(9, 15)
nine_fifteenths.reduce()
assert nine_fifteenths.is_equal(Fraction(3, 5)), "The reduce function did not reduce its fraction properly"

assert six_ninths.get_numerator() == 6, f"The numerator for {sixNinths.to_string()} has been modified"

try:
    six_ninths.numerator 
    six_ninths.denominator
    print("The fraction has not been encapsulated properly")
except Exception as ex:
    pass

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2026 Databricks, Inc. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the <a href="https://www.apache.org/" target="_blank">Apache Software Foundation</a>.<br/><br/><a href="https://databricks.com/privacy-policy" target="_blank">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use" target="_blank">Terms of Use</a> | <a href="https://help.databricks.com/" target="_blank">Support</a>
