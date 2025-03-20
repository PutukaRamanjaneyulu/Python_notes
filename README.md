# Python_notes

Python Basics Summary

1️⃣ Data Types: Python has various built-in data types, including:

- Numeric: int, float, complex

- Sequence: str, list, tuple

- Set & Mapping: set, frozenset, dict

- Boolean: bool (True/False

- NoneType: None

2️⃣ Type Conversion:

- Implicit Conversion: Python automatically converts smaller types to larger ones (e.g., int → float).

- Explicit Conversion: Using functions like int(), float(), str(), list(), tuple(), etc.

3️⃣ String Built-in Functions:

- Case Changes: upper(), lower(), capitalize(), title(), swapcase()

- Search & Check: startswith(), endswith(), find()

- Modification: replace(), strip(), split(), join()

- Formatting: f-strings for dynamic string formatting
---
# String, List, Tuple, Set, and Dictionary in Python

## Overview
This Jupyter Notebook provides an in-depth explanation and examples of fundamental Python data structures: Strings, Lists, Tuples, Sets, and Dictionaries. Each section contains definitions, key operations, and example implementations to enhance understanding. The notebook is designed for beginners as well as intermediate learners who want to strengthen their Python programming skills.

## Content
The notebook covers the following topics:

### 1. Strings
Strings are sequences of characters used for storing text data. The notebook covers:
   - Definition and properties of strings
   - String indexing and slicing
   - Common string manipulation techniques (concatenation, repetition, and modification)
   - Built-in string methods like `upper()`, `lower()`, `strip()`, `replace()`, `split()`, and `join()`
   - String formatting using f-strings and `.format()`

**Example:**
```python
text = "Hello, World!"
print(text.upper())  # Output: "HELLO, WORLD!"
print(text.lower())  # Output: "hello, world!"
print(text.replace("Hello", "Hi"))  # Output: "Hi, World!"
```

### 2. Lists
Lists are ordered, mutable sequences that can store multiple data types. Topics include:
   - List creation and indexing
   - Adding elements (`append()`, `extend()`, `insert()`)
   - Removing elements (`remove()`, `pop()`, `del`)
   - Sorting and reversing lists (`sort()`, `reverse()`)
   - List comprehensions for efficient operations
   - Iterating through lists with loops

**Example:**
```python
numbers = [3, 1, 4, 1, 5, 9]
numbers.append(2)
numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 9]
```

### 3. Tuples
Tuples are immutable sequences used to store a fixed set of values. This section covers:
   - Creating tuples and accessing elements
   - Tuple packing and unpacking
   - Advantages of tuples over lists
   - Use cases of tuples in Python programming

**Example:**
```python
tuple_data = (10, 20, 30)
print(tuple_data[1])  # Output: 20
```

### 4. Sets
Sets are unordered collections of unique elements. The notebook explains:
   - Creating sets and accessing elements
   - Performing set operations like union, intersection, and difference
   - Removing duplicates from lists using sets
   - Checking for set membership
   - Built-in set methods like `add()`, `remove()`, and `discard()`

**Example:**
```python
set_data = {1, 2, 3, 4, 4, 5}
set_data.add(6)
print(set_data)  # Output: {1, 2, 3, 4, 5, 6}
```

### 5. Dictionaries
Dictionaries are key-value pair collections used for fast lookups. This section explores:
   - Creating and accessing dictionaries
   - Adding, modifying, and deleting dictionary elements
   - Dictionary methods like `keys()`, `values()`, `items()`
   - Iterating over dictionaries using loops
   - Nested dictionaries for hierarchical data storage

**Example:**
```python
dict_data = {"name": "Alice", "age": 25, "city": "New York"}
print(dict_data["name"])  # Output: Alice
dict_data["age"] = 26
print(dict_data)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}
```

## Requirements
To run this notebook, you need to have Python installed along with Jupyter Notebook. The required dependencies can be installed using:

```bash
pip install notebook
```

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory containing the notebook.
3. Run the command:

   ```bash
   jupyter notebook String_list_Tuple_set_dict.ipynb
   ```

4. The notebook will open in your default web browser, allowing you to execute and modify the code.

## Contribution
Feel free to contribute by adding more examples, improving explanations, or fixing any errors. If you find any section that requires more clarity, fork the repository, make changes, and submit a pull request.



---

# **"Conditional and Controlling Statements" Notebook**  

This Jupyter Notebook covers the fundamental concepts of **control statements** and **conditional statements** in Python, including `for` loops, `while` loops, `if-else` conditions, and flow control mechanisms like `break` and `pass`.  

---

## **1. Control Statements**  
Control statements help in controlling the flow of execution in loops and conditional structures.

### **a. For Loop**
- Used when the number of iterations is known beforehand.
- Syntax:  
  ```python
  for i in range(start, end):
      # Code block
  ```
- Example:  
  ```python
  for i in range(11, 16):
      print("Good Morning")
  ```

### **b. While Loop**
- Used when the number of iterations is **not known** and depends on a condition.
- Syntax:  
  ```python
  while condition:
      # Code block
  ```
- Example:  
  ```python
  x = 5
  while x > 0:
      print(x)
      x -= 1
  ```

### **c. Iteration**
- **Iteration** refers to repeating a block of code multiple times.
- Can be implemented using `for` and `while` loops.

### **d. Pass Statement**
- `pass` is used as a placeholder when a statement is required syntactically but no operation is needed.
- Example:
  ```python
  for i in range(11, 15):
      pass  # Does nothing, moves to the next iteration
  print("Loop executed but did nothing.")
  ```

---

## **2. Conditional Statements**  
Conditional statements allow decision-making in Python.

### **a. If Statement**
- Executes a block of code only if a given condition is **true**.
- Syntax:  
  ```python
  if condition:
      # Code block
  ```
- Example:
  ```python
  age = 18
  if age >= 18:
      print("You are eligible to vote.")
  ```

### **b. If-Else Statement**
- Used when there are two possible outcomes.
- Syntax:
  ```python
  if condition:
      # Code block (executed if condition is true)
  else:
      # Code block (executed if condition is false)
  ```
- Example:
  ```python
  money = 20000
  iphone_price = 80000

  if money > iphone_price:
      print("I can buy an iPhone.")
  else:
      print("I cannot buy an iPhone.")
  ```

### **c. If-Elif-Else Statement**
- Used when multiple conditions need to be checked.
- Syntax:
  ```python
  if condition1:
      # Code block (executed if condition1 is true)
  elif condition2:
      # Code block (executed if condition2 is true)
  else:
      # Code block (executed if all conditions are false)
  ```
- Example:
  ```python
  marks = 85

  if marks >= 90:
      print("Grade: A")
  elif marks >= 75:
      print("Grade: B")
  else:
      print("Grade: C")
  ```

### **d. Break Statement**
- `break` is used to **exit a loop** immediately when a condition is met.
- Example:
  ```python
  for i in range(10):
      if i == 5:
          break  # Exits the loop when i is 5
      print(i)
  ```

---

## **3. Additional Key Takeaways**
- The notebook includes **multiple examples** demonstrating the use of control and conditional statements.
- Concepts like **looping structures, iteration, and flow control** are well explained.
- The `pass` and `break` statements are introduced to handle scenarios where logic needs to be skipped or stopped.

---

This notebook is an excellent resource for **beginners** looking to understand **Python's control flow** and **decision-making structures**.




---


# **Detailed Breakdown of `Functions.ipynb**




### **Overview of Functions in Python**
The notebook focuses on **functions in Python**, emphasizing **reusability of code**. It categorizes functions into:
1. **Built-in functions** – Predefined functions developed by the Python community.
2. **User-defined functions** – Custom functions created by users for specific tasks.

#### **Types of User-Defined Functions Covered:**
1. **Non-parameter Functions** – Functions that do not accept arguments.
2. **Parameter Functions** – Functions that accept arguments for flexibility.

---

## **Breakdown of Functions in the Notebook**

### **1. Non-Parameter Functions**
- These functions **do not take any arguments**.
- Their parentheses remain **empty** when defining them.
- They execute a fixed task when called.

#### **Example from Notebook:**
```python
# Non-parameter Function
def ram():
  print("Good Morning")

ram()  # Calling the function

def func():
  a = 10
  print(a + 20)

func()  # Calling the function
```
---

### **2. Parameter Functions**
- These functions **accept arguments** to perform operations dynamically.
- The parameters allow **customized execution** based on the inputs.

#### **Example from Notebook:**
```python
# Function with parameters
def kiran(a, b):
  print(a + b)

kiran(10, 20)  # Output: 30
kiran(1, 2)    # Output: 3
kiran(100, 200) # Output: 300
```
---

### **3. Perfect Number Program**
- The notebook includes a **Perfect Number program**, which checks whether a given number is a perfect number.

#### **Example from Notebook:**
```python
# Perfect number Program
n = int(input("Enter a number here: "))
c = 0
for i in range(1, n):
  if i % 2 == 0:
    c = c + i

if c == n:
  print("Perfect number")
else:
  print("Not a perfect number")
```
---

## **Conclusion**
- The notebook primarily discusses **non-parameter and parameter functions**.
- It demonstrates how functions **enhance code reusability**.
- A **Perfect Number program** is also included.




## `lambda_Functions.ipynb`

The Jupyter Notebook primarily covers **Lambda Functions** and their applications in Python. Key topics include:

1. **Introduction to Lambda Functions**  
   - Explanation of anonymous functions (functions without a name).
   - Syntax: `lambda arguments: expression`.
   - Examples demonstrating lambda usage for simple operations.

2. **Comparison with Regular Functions**  
   - Example of defining and using a regular function.
   - Equivalent lambda function performing the same task.

3. **Multiplication Table Using Different Methods**  
   - **Method 1:** Using a simple `for` loop.  
   - **Method 2:** Using a function.  
   - **Method 3:** Using a lambda function inside a loop.

4. **Map Function**  
   - Explanation of `map(function, iterable)`.  
   - Example usage of `map()` with lambda functions.

The notebook includes both **code cells** with practical implementations and **markdown explanations** for better understanding.

# Summary of the File:
The Jupyter Notebook **"Comprehension.ipynb"** covers **list comprehensions** and **dictionary comprehensions** in Python. It explains how comprehensions help reduce lines of code and provides examples with and without comprehension. The notebook is divided into the following sections:

1. **Introduction to Comprehensions**  
   - Explains the concept of comprehensions and their types (List & Dictionary comprehensions).
   - Describes different syntax patterns for comprehensions.

2. **List Comprehension**  
   - Provides three syntax structures for list comprehensions:
     - Basic comprehension
     - Comprehension with conditionals
     - Comprehension with if-else conditions
   - Examples comparing regular loops vs. list comprehensions.

3. **Dictionary Comprehension**  
   - Explains how dictionary comprehensions work.
   - Provides similar examples as list comprehensions but using dictionary structures.

4. **Performance Comparison**  
   - Compares execution speed between using comprehensions and traditional loops.

- The notebook includes multiple **code snippets** and **explanations** demonstrating how comprehensions simplify iteration and filtering in Python.
---


# **Detailed Review of Your Jupyter Notebook on File Handling**

---

## **1. Code Analysis**  
Your notebook contains Python code demonstrating file handling operations, including writing, appending, reading, and working with JSON files. Below is a breakdown:

### **File Writing (`w` mode)**
#### Example:
```python
a = open("student.txt", "w")  # w -> will create file and will open
a.write("I am from India")
a.close()  # close the file
```
✅ **Good Practices:**
- Demonstrates creating a file and writing data.
- Properly closes the file.

🔹 **Suggestions for Improvement:**
- **Use the `with open()` statement** to ensure the file is automatically closed.
  ```python
  with open("student.txt", "w") as a:
      a.write("I am from India")
  ```
- This prevents errors if the script terminates before closing.

---

### **File Appending (`a` mode)**
#### Example:
```python
a = open("student.txt", "a")
a.write(" Data science is the Future in IT")
a.close()
```
✅ **Good Practices:**
- Shows how `a` mode appends data to an existing file.

🔹 **Suggestions for Improvement:**
- **Use `with open()`**:
  ```python
  with open("student.txt", "a") as a:
      a.write(" Data science is the Future in IT")
  ```
- Keeps code cleaner and prevents file corruption.

---

### **File Reading (`r` mode)**
#### Example:
```python
a = open("student.txt", "r")
print(a.read())
a.close()
```
✅ **Good Practices:**
- Demonstrates reading from a file.



---

### **Working with JSON**
#### Example:
```python
import json

Fruits = {'apple': 20, 'banana': 30, 'carrot': 200}

with open("student.json", "w") as f:
    json.dump(Fruits, f)
```
✅ **Good Practices:**
- Uses `json.dump()` to write a dictionary into a JSON file.
- Uses `with open()`, which is best practice.

🔹 **Suggestions for Improvement:**
- Instead of `"student.json"`, dynamically name the file:
  ```python
  filename = "fruits_data.json"
  with open(filename, "w") as f:
      json.dump(Fruits, f)
  ```
- Improves maintainability.

---

### **JSON Serialization (`dumps`) & Deserialization (`loads`)**
#### Example:
```python
Fruits = {'apple': 20, 'banana': 30, 'carrot': 200}

sol = json.dumps(Fruits)
print(sol)
print(type(sol))

p = json.loads(sol)
print(p)
print(type(p))
```
✅ **Good Practices:**
- Demonstrates `json.dumps()` (converts dictionary to string) and `json.loads()` (converts string to dictionary).

🔹 **Suggestions for Improvement:**
- Add indentation for better readability:
  ```python
  sol = json.dumps(Fruits, indent=4)
  print(sol)
  ```

---

## **2. Markdown (Explanations) Analysis**
Your markdown cells provide useful theoretical explanations of file handling modes.

✅ **Good Practices:**
- Clearly defines file handling modes (`w`, `r`, `a`).
- Explains JSON operations (`dump`, `load`, `dumps`, `loads`).

🔹 **Areas for Improvement:**
- Some typos and grammar issues.
- Example:  
  `The file is not close the data will be temporarly store in the file`  
  **Suggested Correction:**  
  `"If the file is not closed, the data remains temporarily stored, which may cause errors."`

- Instead of:
  ```
  If the file is there we can read the data from the file
  The file is not there we can't read the data
  ```
  **Rewrite for clarity:**
  ```
  - If the file exists, we can read its content.
  - If the file does not exist, attempting to read it will raise an error.
  ```

---

## **3. Key Improvements**
### ✅ **Best Practices to Implement:**
1. **Always use `with open()`** instead of manually closing files.
2. **Check if files exist** before reading to prevent errors.
3. **Improve markdown grammar** for better readability.
4. **Use meaningful file names** instead of hardcoding (`"student.txt"`).
5. **Format JSON outputs** for better clarity (`json.dumps(data, indent=4)`).

---

## **Final Thoughts**
Your notebook does a good job of introducing file handling and JSON operations. By implementing the improvements above, it will be **more efficient, readable, and professional**.

---

# Exception Handling in Python

## What is Exception Handling?
Exception handling is a mechanism to detect and handle runtime errors to maintain smooth program execution. It helps to prevent abrupt program termination.

## Common Errors in Python
1. **SyntaxError** - Incorrect syntax in the code.
2. **ZeroDivisionError** - Division by zero is not allowed.
3. **NameError** - Using an undefined variable.
4. **ValueError** - Incorrect value passed to a function.
5. **IndentationError** - Improper indentation in the code.
6. **FileNotFoundError** - Trying to open a file that does not exist.

---

# 1. SyntaxError Example
```python
# Incorrect variable name (SyntaxError)
# 10a = "kamal"  # This will raise a SyntaxError

# Correct syntax
var_name = "kamal"
print(var_name)
```

---

# 2. ZeroDivisionError Example
```python
# Correct division
print(10 / 5)  # Output: 2.0

# Error: Division by zero
# print(5 / 0)  # Uncommenting this will raise ZeroDivisionError
```

---

# 3. NameError Example
```python
# Correct usage
city = "Hyderabad"
print(city)

# Error: Undefined variable
# print(CITY)  # Uncommenting this will raise NameError
```

---

# 4. ValueError Example
```python
# Correct conversion
num = "123"
print(int(num))  # Output: 123

# Error: Cannot convert non-numeric string
# print(int("kamal123"))  # Uncommenting this will raise ValueError
```

---

# 5. IndentationError Example
```python
# Correct indentation
for i in range(11, 15):
    print(i)

# Error: Incorrect indentation
# for i in range(11, 15):
# print(i)  # Uncommenting this will raise IndentationError
```

---

# 6. FileNotFoundError Example
```python
# Error: File not found
# with open("nonexistent_file.txt", "r") as file:
#     print(file.read())  # Uncommenting this will raise FileNotFoundError
```

---

# Handling Errors Using try-except

```python
try:
    a = 10
    b = 0
    print(a / b)  # Division by zero
except ZeroDivisionError as e:
    print("Error:", e)  # Output: Error: division by zero
```

---

# Using try-except-finally

```python
try:
    for i in range(11, 21):
        if i % 2 == 0:
            print(f'Even: {i}')
except Exception as e:
    print("Error:", e)
finally:
    print("This will always execute, regardless of error occurrence.")
```

---

# Accessing Error Type and Line Number

```python
import sys

try:
    for i in range(11, 21):
        if i % 2 == 0:
            print(f'Even: {i / 0}')  # Intentional error
except Exception as e:
    error_type, error_msg, error_lineno = sys.exc_info()
    print(f'Error Type: {error_type}')
    print(f'Error Message: {error_msg}')
    print(f'Error Line Number: {error_lineno.tb_lineno}')
```

---

# Conclusion
- Exception handling helps in writing robust and error-free code. Using `try-except-finally`, we can optimize our code to handle errors efficiently.

---





## 📚 **OOPS -> Object-Oriented Programming System**

### Key Concepts:
- **Class:** Collection of variables and functions.
- **Object:** Instance of a class.
- **Self:** Refers to the object itself.
- **Functions in Class:** Define actions performed by objects.
- **Inheritance:** Mechanism to derive a class from another.
- **Polymorphism:** Ability to take multiple forms.
- **Encapsulation:** Restricting access to methods and variables.

---

## 🏗️ **1. Class Basics**

### 🔹 **Class Definition:**
- Class names should use **capitalized words**.
- Basic syntax:
```python
class ClassName:
    variable_name = value
    def function_name(self):
        # function body
```

---

### ✅ **Example 1: Basic Class and Object**
```python
class CSE:  
  s = 10      
anil = CSE()   
print(anil.s)
```
- `CSE` is the class.
- `s` is a variable.
- `anil` is an object.

---

### ✅ **Example 2: Multiplying Class Variables**
```python
class ECE:
  a = 10
  b = 2

kumar = ECE()
print(kumar.a * kumar.b)
```

---

### ✅ **Example 3: Accessing Class Variables Without Object**
```python
class MECH:
  j = 100
  k = 200

print(MECH.j + MECH.k)
```

---

## 🔄 **2. Methods to Add Data to a Class**

### ✅ **Method 1: Using Object to Create Variables**
```python
class CSE:
  pass
kumar = CSE()
kumar.priya = 10
kumar.liala = 20
print(kumar.priya * kumar.liala)
```

---

### ✅ **Method 2: Using Class Name to Create Variables**
```python
class SEC:
  pass
SEC.priya = 10
SEC.laila = 20
print(SEC.priya + SEC.laila)
```

---

## 🎯 **3. Constructors in OOPS**

### 🔹 **Constructor Basics**
- **Constructor:** Special method that initializes an object.
- Types:
  - **Non-parameterized constructor:** No arguments.
  - **Parameterized constructor:** Takes arguments.

---

### ✅ **Non-parameterized Constructor**
```python
class CSE:
  def __init__(self):
    print("Good Morning")

kumar = CSE()
```

---

### ✅ **Parameterized Constructor**
```python
class CSE:
  def __init__(self, a, b):
    self.a = a
    self.b = b

kimar = CSE(10, 20)
print(kimar.a + kimar.b)
```

---

## ⚡ **4. Functions in Class**

### ✅ **Example with Multiple Functions**
```python
from ast import Raise
class NAME:
  def addition(self):
    p = 50
    g = 80
    print(p + g)
  
  def subtraction(self):
    p = 50
    g = 80
    print(p - g)

ram = NAME()
ram.addition()
ram.subtraction()
```

---

### ✅ **Calling Multiple Methods**
```python
class COL:
  def __init__(self, p, g):
    self.p = p
    self.g = g

  def addition(self):
    print(self.p + self.g)
  
  def Substraction(self):
    print(self.p - self.g)

  def comman(self):
    self.addition()
    self.Substraction()

kumar = COL(50, 80)
kumar.comman()
```

---

## 🔢 **5. Perfect Number Using OOPS**
```python
class PER:
  def __init__(self, n):
    self.n = n
  
  def Col(self):
    self.c = 0
    for i in range(1, self.n):
      if self.n % i == 0:
        self.c += i
    if self.c == self.n:
      print(f'Perfect Number: {self.n}')
    else:
      print(f'Not a Perfect Number: {self.n}')

kumar = PER(8)
kumar.Col()
```

---

## 🧬 **6. Inheritance in OOPS**

### 🔹 **Types of Inheritance:**
1. **Single Inheritance**
2. **Multi-level Inheritance**
3. **Multiple Inheritance**
4. **Hierarchical Inheritance**
5. **Hybrid Inheritance**

---

### ✅ **Single Inheritance**
```python
class PARENT:
  def building(self):
    print("I have Building")
class CHILD(PARENT):
  def job(self):
    print("I have a job")

kumar = PARENT()
anil = CHILD()
kumar.building()
anil.job()
anil.building()
```

---

### ✅ **Multi-level Inheritance**
```python
class FATHER:
  def building(self):
    print("I have a Building")

class CHILD(FATHER):
  def job(self):
    print("I have a job")

class Child2(FATHER):
  def Business(self):
    print("I have the Business")

anil = CHILD()
chandu = Child2()
anil.job()
anil.building()
chandu.Business()
chandu.building()
```

---

### ✅ **Multiple Inheritance**
```python
class FATHER:
  def building(self):
    print("I have Building")

class MOTHER:
  def hari(self):
    print("I have a house")

class CHILD(FATHER, MOTHER):
  def job(self):
    print("I have a job")

son = CHILD()
son.job()
son.hari()
son.building()
```

---

### ✅ **Hierarchical Inheritance**
```python
class FATHER:
  def building(self):
    print("I have a Building")

class CHILD(FATHER):
  def job(self):
    print("I have a job")

class Child2(FATHER):
  def Business(self):
    print("I have the Business")

class Child3(FATHER):
  def company(self):
    print("I have the company")

anil = CHILD()
chandu = Child2()
prasad = Child3()
anil.job()
anil.building()
chandu.Business()
chandu.building()
prasad.company()
prasad.building()
```

---

### ✅ **Hybrid Inheritance**
```python
class Grandparent:
  def building(self):
    print("I have a Building")

class FATHER(Grandparent):
  def job(self):
    print("I have a job")

class MOTHER(Grandparent):
  def Business(self):
    print("I have the Business")

class Child1(FATHER, MOTHER):
  def company(self):
    print("I have the company")

son = Child1()
son.company()
son.job()
son.Business()
```

---

## 🧠 **7. Polymorphism**

### 🔹 **Types of Polymorphism:**
1. **Method Overloading**
2. **Method Overriding**

---

### ✅ **Method Overriding**
```python
def func():
  print("Good Morning")

def func():
  print("Good Afternoon")

func()
```
- Last defined method overrides the previous one.

---

### ✅ **Method Overloading**
```python
def func(a=None, b=None):
  if a == None and b == None:
    print("I am From India")
  elif a == None and b != None:
    print("I am From USA")
  elif a != None and b != None:
    print("I am from UK")
  else:
    print("I am From Canada")

func()
func(a=10)
func(b=20)
func(10, 20)
```

---

## 📝 **Summary of the File**
- The file extensively covers:
  - Basics of OOPS (Class, Object, Self)
  - Constructor types and function implementation
  - All types of inheritance with examples
  - Polymorphism with overloading and overriding
  - Example tasks like perfect number checking using OOPS



# **Production_python**

## 📁 **1. p_python.py**

### 📝 **Description:**
- This script simulates a **sequential execution model** where tasks run one after another.
- **Purpose:**  
    - Show the drawback of normal (sequential) execution without using concurrency or parallelism.

---

### ⚡ **Key Functions:**
1. **india()**
   - Prints "India" with numbers from 1 to 10.
   - Sleeps for 0.5 seconds after each iteration.

2. **uk()**
   - Prints "UK" with numbers from 1 to 10.
   - Sleeps for 0.5 seconds after each iteration.

---

### ⏱️ **Sequential Execution:**
```python
# Drawback of normal level of Code
import time

starting_time=time.time()
def india():
    for i in range(1,11):
        time.sleep(0.5)
        print(f'india : {i}')
def uk():
    for i in range(1,11):
        time.sleep(0.5)
        print(f'uk : {i}')
india()
uk()
print(f'Total Time :{(time.time() - starting_time)}')
```
✅ **Key Point:**
- Tasks are executed one after another, resulting in higher execution time.

---

## 📁 **2. production_python.py**

### 📝 **Description:**
- This script demonstrates **multi-processing** using Python’s `multiprocessing` module.
- **Purpose:**  
    - Run multiple processes in parallel to utilize CPU cores efficiently.

---

### ⚡ **Key Functions:**
1. **india()**
   - Prints "India" with numbers from 1 to 10.
   - Sleeps for 0.5 seconds after each iteration.
   - Displays the process ID (PID) using `os.getpid()`.

2. **uk()**
   - Prints "UK" with numbers from 1 to 10.
   - Displays its process ID.

---

### 🔥 **Multi-processing Implementation:**
```python
import multiprocessing.process
import time
import multiprocessing
import os

starting_time=time.time()
def india():
    print(f'CPU1 processes id: {os.getpid()}')
    for i in range(1,11):
        time.sleep(0.5)
        print(f'india : {i}')
def uk():
    print(f'CPU2 processes id: {os.getpid()}')
    for i in range(1,11):
        time.sleep(0.5)
        print(f'uk : {i}')
if __name__ == "__main__":
    print(f'Main Processor id : {(os.getpid())}')
    cpu1 = multiprocessing.Process(target=india, args=())
    cpu2 = multiprocessing.Process(target=uk, args=())
    cpu1.start()
    cpu2.start()
    cpu1.join()
    cpu2.join()
    print(f'Total Time :{(time.time() - starting_time)}')
    print(f'main Function Exits')
```
✅ **Key Point:**
- `cpu1` and `cpu2` run as separate processes to reduce execution time.
- `join()` ensures that the main process waits for both to complete.

---
## 📁 **3. m_p_2.py**

### 📝 **Description:**
- This script demonstrates **multi-threading** and **multi-processing** concepts in Python.
- It processes tasks concurrently using threads.
- **Purpose:**  
    - Simulate tasks running in parallel, representing different countries (India, UK, Parish, Canada).

---

### ⚡ **Key Functions:**
1. **india()**
   - Prints "India" along with numbers from 1 to 10.
   - Sleeps for 0.5 seconds after each iteration.
   - Displays CPU1 processor ID.

2. **uk()**
   - Prints "UK" along with numbers from 1 to 10.
   - Same sleep time and CPU ID as `india()`.

3. **parish()**
   - Prints "Parish" along with numbers from 1 to 10.
   - Displays CPU2 processor ID.

4. **Canada()**
   - Prints "Canada" along with numbers from 1 to 10.
   - Displays CPU2 processor ID.

---

### 🔥 **Threading Implementation:**
- **Comman_1():** Runs `india()` and `uk()` concurrently using threads.
```python
import time
import os
import multiprocessing
starting_time = time.time()
# Processing work the simultaneously 
# Threading work the Concurrent(line by line)
import threading


def india():
    print(f'Cpu1 Processor id: {(os.getpid())}')
    for i in range(1,11):
        time.sleep(0.5)
        print(f'India : {i}')
def uk():
    print(f'Cpu1 Processor id: {(os.getpid())}')
    for i in range(1,11):
        time.sleep(0.5)
        print(f'uk : {i}')
def parish():
    print(f'Cpu2 Processor id: {(os.getpid())}')
    for i in range(1,11):
        time.sleep(0.5)
        print(f'paridh : {i}')
def Canada():
    print(f'Cpu2 Processor id: {(os.getpid())}')
    for i in range(1,11):
        time.sleep(0.5)
        print(f'canada : {i}')
def Comman_1():
    t1 = threading.Thread(target=india, args=())
    t2 = threading.Thread(target=uk, args=())
    t1.start()
    t2.start()
```
- **Comman_2():** Runs `parish()` and `Canada()` concurrently using threads.
```python
def Comman_2():
    t3 = threading.Thread(target=parish, args=())
    t4 = threading.Thread(target=Canada, args=())
    t3.start()
    t4.start()
```

---

### 🚀 **Main Block:**
```python
if __name__ == "__main__":
    print(f'Main Processor id: {(os.getpid())}')
    cpu1 = threading.Thread(target=Comman_1, args=())
    cpu2 = threading.Thread(target=Comman_2, args=())
    cpu1.start()
    cpu2.start()
    print(f'Total Time : {(time.time() - starting_time)}')
    print(f'Main Processor Exit')
```
✅ **Key Point:**
- `Comman_1()` and `Comman_2()` run concurrently to reduce execution time.

---

## 🎯 **Detailed Comparison**

| Feature                   | m_p_2.py         | p_python.py     | production_python.py |
|---------------------------|------------------|-----------------|----------------------|
| **Execution Model**         | Multi-threading  | Sequential      | Multi-processing     |
| **Concurrency/Parallelism** | Concurrent       | No concurrency  | True parallelism     |
| **Processor Usage**         | Shared           | Single          | Multiple CPUs        |
| **Performance**             | Faster           | Slow            | Fastest              |
| **Thread/Process Control**   | Threads          | None            | Processes            |
| **Execution Time**           | Low              | High            | Low                  |

---

## 🔥 **Performance Insights:**
1. **m_p_2.py:** Best suited for I/O-bound tasks due to threading.
2. **p_python.py:** Slow and inefficient for parallel tasks due to sequential execution.
3. **production_python.py:** Ideal for CPU-bound tasks with heavy computation due to multi-processing.

---

## 📚 **Summary and Recommendations:**
- Use **multi-threading** when tasks involve I/O operations (networking, file I/O).
- Use **multi-processing** for CPU-intensive tasks where tasks need to run in parallel.
- Avoid sequential processing when tasks can be run concurrently to save time.











