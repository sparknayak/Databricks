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
# MAGIC # Data Types and Variables
# MAGIC
# MAGIC <!-- ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)  -->
# MAGIC In this lesson you:
# MAGIC
# MAGIC - Explore fundamental concepts in Python, such as: 
# MAGIC     * Data types
# MAGIC     * Variables
# MAGIC     * Print values
# MAGIC
# MAGIC Recommended Resources:
# MAGIC * <a href="https://www.amazon.com/gp/product/1491957662/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=quantpytho-20&creative=9325&linkCode=as2&creativeASIN=1491957662&linkId=ea8de4253cce96046e8ab0383ac71b33" target="_blank">Python for Data Analysis by Wes McKinney</a>
# MAGIC * <a href="https://www.pythoncheatsheet.org/" target="_blank">Python reference sheet</a>
# MAGIC * <a href="https://docs.python.org/3/tutorial/" target="_blank">Python official tutorial</a>
# MAGIC
# MAGIC Documentation to help with <a href="https://www.markdownguide.org/getting-started/" target="_blank">markdown cells</a>.

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
# MAGIC ### Calculation
# MAGIC
# MAGIC To get started, let's use Python to calculate some mathematical expressions. Can you guess what this will evaluate to?

# COMMAND ----------

1+1

# COMMAND ----------

# MAGIC %md
# MAGIC ### Comments
# MAGIC
# MAGIC In addition to markdown cells, we can annotate our code through [comments](https://www.w3schools.com/python/python_comments.asp). Comments are optional, but can help explain a line of code in context. They are not executed.
# MAGIC
# MAGIC In Python, **`#`** is a reserved keyword to represent a comment. Any characters following it on the line are treated as part of the comment.
# MAGIC
# MAGIC <!-- <img src="https://files.training.databricks.com/images/icon_hint_24.png" alt="Hint:">  -->
# MAGIC
# MAGIC If you have lines of code selected in a notebook cell, you can press `ctrl + /` to comment or uncomment that block of code. Try adding your own comments below.

# COMMAND ----------

# This is our first line of Python code!
1+1

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Data Types
# MAGIC
# MAGIC Python provides basic [**Data Types**](https://www.w3schools.com/python/python_datatypes.asp), each with their own operations. 
# MAGIC
# MAGIC Let's look at a few of them and the operations we can apply to each of them.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### Type 1: Integers
# MAGIC
# MAGIC Integers (or int) are non-decimal whole numbers. 
# MAGIC
# MAGIC **Data**: Integer values (e.g. -2, -1, 0, 1, 2 ...)
# MAGIC
# MAGIC **Example Operations**: +, -, *, /

# COMMAND ----------

# Integer expression
2 * 3 + 5 - 1

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### Type 2: Float
# MAGIC
# MAGIC Float (or floating point) is a number containing a decimal. 
# MAGIC
# MAGIC **Data**: Decimal Values (e.g. -2.342, -1.3, 0.45, 1.1, 2.2 ...)
# MAGIC
# MAGIC **Example Operations**: +, -, *, /

# COMMAND ----------

1.2 * 2.3 + 5.5

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC If you are unsure what type something is, you can pass it into **`type()`**.

# COMMAND ----------

type(1.2)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC Question: Is `1.` a float or an int? Let's test it by checking its type.

# COMMAND ----------

type(1.)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### An Aside on Numeric Precision
# MAGIC
# MAGIC Unlike most programming languages, Python numeric precision is theoretically infinite.

# COMMAND ----------

99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 + 1

# COMMAND ----------

.9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 + .0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### Type 3: Strings
# MAGIC
# MAGIC Strings (or str) are a sequence of characters surrounded by quotation marks (i.e. **`""`** or **`''`**). They are just text, but can contain numbers, punctuation, etc.
# MAGIC
# MAGIC For example, `"Hello World!"` or `'Hello World!'`.
# MAGIC
# MAGIC **Data**: Text (e.g. "Hello", "I love Python", "3.14abc")
# MAGIC
# MAGIC **Example Operations**: Concatenation (+)
# MAGIC
# MAGIC Note that when you use the `+` operator on an integer or float it adds the values, but for strings it concatenates them. The operations differ between types.

# COMMAND ----------

# String expression
"Hello" + "123"

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC Notice that the concatenation operation does **not** insert a space. If we wanted "Hello 123", we would have to add a space in the string.

# COMMAND ----------

# String expression with a space
"Hello" + " " + "123"

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC Question: If you add a float and string together, what is the result? Uncomment then execute the code below to find out.

# COMMAND ----------

# "Hello" + 123

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Multi-line strings
# MAGIC
# MAGIC A [multiline string](https://www.w3schools.com/python/gloss_python_multi_line_strings.asp) is like a container for text that spans across multiple lines of code.
# MAGIC
# MAGIC It allows us to represent text with line breaks, such as paragraphs of text, code blocks, or any content where preserving the line breaks and formatting is important. 
# MAGIC
# MAGIC To create a multi-line string, simply enclose your text within triple quotes (either  **`"""`** or **`'''`**). The triple quotes indicate to Python that the text can span multiple lines without the need for [escape characters](https://www.w3schools.com/python/gloss_python_escape_characters.asp) like **`\n`**.
# MAGIC
# MAGIC Here's an example.

# COMMAND ----------

print('''
This text can go on and on.
You can have as many lines as you need.
Perfect for large paragraphs, code, or anything that's just too long.
''')

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### Type 4: Boolean
# MAGIC
# MAGIC Boolean (or bool) is a binary data type. There are only two boolean values: **`True`** and **`False`**.
# MAGIC
# MAGIC <!-- <img src="https://files.training.databricks.com/images/icon_warn_24.png" alt="Caution"> -->
# MAGIC Python is **case-sensitive**, and these boolean values must be title-case. You will get a Python error if you try to use variants like **`true`** or **`FALSE`**. 
# MAGIC **Data**: True, False
# MAGIC
# MAGIC **Example Operations**: logical operators (i.e. or, and, not)

# COMMAND ----------

True or False

# COMMAND ----------

True and False

# COMMAND ----------

not False

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ## Variables
# MAGIC
# MAGIC We can store the result of an expression in a [variable](https://www.w3schools.com/python/python_variables.asp), which we can then use to refer to the result of that expression. It's very helpful if you plan to re-use the same value multiple times. There should be only one variable assignment per line.
# MAGIC
# MAGIC **`variable_name = expression`**
# MAGIC
# MAGIC A few things to note on Python variable names from <a href="https://www.w3schools.com/python/gloss_python_variable_names.asp#:~:text=Rules%20for%20Python%20variables%3A,0%2D9%2C%20and%20_%20" target="_blank">W3 Schools</a>:
# MAGIC * A variable name must start with a letter or the underscore character
# MAGIC * A variable name cannot start with a number
# MAGIC * A variable name can contain only alpha-numeric characters and underscores (A-z, 0-9, and _ )
# MAGIC * Variable names are case-sensitive (**`age`**, **`Age`** and **`AGE`** are three different variables)

# COMMAND ----------

a = 3
b = 2
c = a*b

c

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC Question: If we update the value of **`b`**, what happens to **`c`**?

# COMMAND ----------

b = 4
c

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### Variable State
# MAGIC
# MAGIC Variables are accessible across cells in the same notebook. If you restart your cluster or detach your notebook from your cluster, you will not lose your code, but you will lose the state of the variables. 
# MAGIC
# MAGIC **Exercise**: Try detaching and reattaching this notebook. Are you still able to run the command above successfully?

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### Weakly Typed Languages
# MAGIC
# MAGIC
# MAGIC Python is a *weakly typed* language. That means any variable can hold any type of value, and you can overwrite a variable to have any type of value. In other words, you can assign a new value to a variable that is of a different type than its original value.
# MAGIC
# MAGIC In contrast, *strongly typed* languages &mdash; such as C and Java &mdash; do not allow this.

# COMMAND ----------

b = "Hello World"
print(type(b))
b = 10
print(type(b))

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### Naming Conventions
# MAGIC
# MAGIC While you can name Python variables almost anything and it will work, the general convention in Python is to use **`snake_case`**. This means all of the characters should be lower case, and spaces are replaced with an `_` character.
# MAGIC
# MAGIC For example, **`my_first_variable`** is a better name than **`MyFirst_variable`**. 
# MAGIC
# MAGIC Try to avoid variable re-use. For example, you would not want to use **`address`** as a variable name referring to a house address, then later use **`address`** again referring to an IP address. You would want to use something like **`house_address`** and **`ip_address`** instead.
# MAGIC
# MAGIC Also try to use variable names that describe their contents to make your Python code easier to read and understand.
# MAGIC
# MAGIC And don't use variable names that are too long. Would you really want to type **`first_appearance_of_the_word_in_this_file`** multiple times in your program?

# COMMAND ----------

my_first_variable = 2

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ## Print Statements
# MAGIC
# MAGIC In Databricks or Jupyter notebooks, the result of last line executed in a cell is printed automatically.
# MAGIC
# MAGIC If you want to see more than just the evaluation of the last line, you need to use a **`print`** statement.
# MAGIC
# MAGIC To use it, write **`print(expression)`** to see the value of the expression displayed.

# COMMAND ----------

a = 1
b = 2

a # This line isn't printed because it's not the last line of code
b

# COMMAND ----------

print(a)
print(b)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC In addition to printing variable values, you can also print strings.

# COMMAND ----------

print(10)
print("Hello world")
print(True)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC You can also inject the value of a variable or expression into the output of a print statement
# MAGIC
# MAGIC In Python 3.5, you would print it like this:

# COMMAND ----------

a = 1
b = 2
print("The sum of {} + {} is {}".format(a, b, a + b))

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### f-string Formatting
# MAGIC
# MAGIC In Python 3.6 a new style for injecting the value of a variable or expression into a string was introduced, called [f-string](https://www.w3schools.com/python/python_string_formatting.asp) formatting. (The __f__ in __f-string__ is short for __formatted__. Put an **`f`** at the beginning of the quotes, and place the variable inside of curly braces. The syntax looks like **`f"optional text {insert_variable_here} optional text"`**.
# MAGIC
# MAGIC In Python 3.6, you would print it like this:

# COMMAND ----------

a = 1
b = 2
print(f"The sum of {a} + {b} is {a + b}")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC You can even use f-string formatting to generate simple columnar output
# MAGIC - The f-string {} placeholder can optionally include a column width following the value being rendered to generate simple, aligned output
# MAGIC   - Numeric values are right justified
# MAGIC   - String values are left justified
# MAGIC - For the record, there are much <a href="https://docs.python.org/3/tutorial/inputoutput.html" target="_blank">better</a>, more powerful ways of doing this in Python

# COMMAND ----------

city1 = "San Francisco"
city2 = "Paris"
city3 = "Mumbai"

temperature1 = 58
temperature2 = 75
temperature3 = 81

humidity1 = .85
humidity2 = .5
humidity3 = .88 

print(f"{'City':15} {'Temperature':15} {'Humidity':15}")
print(f"{city1:15} {temperature1:11} {humidity1:12.2f}")
print(f"{city2:15} {temperature2:11} {humidity2:12.2f}")
print(f"{city3:15} {temperature3:11} {humidity3:12.2f}")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC By default, the print function separates the output for each argument from the next by a space, terminating the entire output with a newline, as illustrated below

# COMMAND ----------

print(1,2,3)
print(4,5,6)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC However, you can override this behavior by specifying custom delimiters as illustrated below

# COMMAND ----------

# Separator: '--' instead of ' '. Terminator: '. ' instead of a newline.
print(1,2,3, sep='--', end='. ') 

# Separator: '###' instead of ' '. Terminator: 'END' instead of a newline. 
# Because the previous output is no longer terminated by a newline, it is printed on the same line as the output produced by line 2.
print(4,5,6, sep='###', end='END') 

# Print a blank line.  This will just be a new line
print("") 

# Separator: '' (none) instead of ' '. Terminator: '$' instead of a newline.
print(1, 2, 3, sep='', end='$')

# Separator: '\t' instead of ' '. Terminator: 'Done' instead of a newline. 
# Because the previous output is no longer terminated by a newline, it is printed on the same line as the output produced by line 11.
print(4, 5, 6, sep='\t', end='Done')

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Ternary Operator
# MAGIC
# MAGIC Ternary operators (also known as conditional expressions) provide a concise way to assign values to variables based on a condition.
# MAGIC
# MAGIC It checks whether a given condition is **`True`** or **`False`** and returns one of two values in a single line of code.
# MAGIC
# MAGIC The syntax of a ternary operator is as follows: **`value_if_true if condition else value_if_false`**
# MAGIC
# MAGIC Let's look at an example.
# MAGIC
# MAGIC In this context, we are going to use **`if`** and **`else`** statements, which are part of Python's control flow. They allow us to make conditional decisions and execute different code blocks based on specific conditions. We will cover them in more detail in another discussion.

# COMMAND ----------

is_tasty = True
food = "Delicious" if is_tasty else "Not Delicious"
print(food)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC As you can see, the **`food`** variable is assigned the value "Delicious" because the condition (**`is_tasty`**) is **`True`**. If **`is_tasty`** were **`False`**, the variable **`food`** would be assigned the value "Not Delicious."

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Congratulations! You have finished your first lesson on Python!**

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2026 Databricks, Inc. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the <a href="https://www.apache.org/" target="_blank">Apache Software Foundation</a>.<br/><br/><a href="https://databricks.com/privacy-policy" target="_blank">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use" target="_blank">Terms of Use</a> | <a href="https://help.databricks.com/" target="_blank">Support</a>
