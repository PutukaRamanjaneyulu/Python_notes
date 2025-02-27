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
## List Python_file.ipynb
##### Key Insights
-> The notebook begins by explaining that lists are mutable, meaning their contents can be changed.

-> It attempts to assign a value to an index beyond the current list size, which leads to an IndexError.

-> It likely covers list indexing, slicing, adding, removing, and modifying elements.

-> There might be some examples demonstrating list methods (e.g., append(), extend(), insert(), remove(), pop(), etc.).

-> Some cells may include incorrect operations to illustrate errors or limitations.
---
#  Tuple.ipynb
* The notebook covers Python Tuples, including their properties, built-in functions, and advantages. Key topics include:

## 1.Introduction to Tuples

-> Tuples are represented with () and can store any data type.

-> They are immutable, meaning their memory allocation cannot be increased or decreased.
## 2.Memory Behavior

-> Code snippets demonstrate that trying to modify tuple elements results in an error.

-> Deleting a tuple completely removes it from memory.

## 3.Built-in Functions

-> count(): Counts occurrences of a value in a tuple.

-> index(): Finds the index of a given value.



## 4.Advantages of Tuples

-> Tuples allow multiple values to be stored in a single variable.

-> Packing and unpacking of tuple values is useful for variable assignment.

---

# Python_set.ipynb
## Overview
The notebook covers the fundamentals of Python sets, including their properties, built-in functions, and operations.

#### Key Topics
* Introduction to Sets

  -> Represented with {} (flower brackets).
  -> Unordered memory allocation.
  -> No indexing, slicing, or skipping concepts.
  -> No duplicate values allowed.
  -> Mutable, but elements inside must be immutable.
## Built-in Functions

### Increasing Functions:

* add(): Adds a single element to a set.
* update(): Adds multiple elements to a set.
### Decreasing Functions:

* pop(): Removes a random element from the set.
* discard(): Removes a specified element without error if the element is absent.
* remove(): Removes a specified element but raises an error if the element is absent.
### Other Specific Functions:

* clear(): Empties the set.
* copy(): Demonstrates deep copy and shallow copy.
* union(): Combines two sets, removing duplicates.
* intersection(): Finds common elements between sets.
### Code Snippets
-> Examples of defining sets.

-> Demonstrations of set operations (add, update, pop, remove, etc.).

-> Explanation of deep copy vs. shallow copy.

-> Set operations like union and intersection.

---



# **Dictionary.ipynb**
This Jupyter Notebook provides a comprehensive guide on Python dictionaries, covering their structure, key characteristics, and built-in functions.

#### **Key Topics Covered:**
1. **Introduction to Dictionaries**  
   - Represented using `{}`  
   - Consists of key-value pairs  
   - No indexing, slicing, or skipping  
   - Can store various data types as values  
   - Requires immutable data types as keys  

2. **Dictionary Properties**  
   - If duplicate keys exist, the last assigned value overrides the previous one  
   - Dictionaries are **mutable**, meaning memory can be increased or decreased dynamically  

3. **Built-in Dictionary Functions**  
   - `get()` – Access values safely  
   - `update()` – Modify existing key-value pairs  
   - `pop()` – Remove a key-value pair  
   - `popitem()` – Remove the last inserted key-value pair  
   - `keys()`, `values()`, `items()` – Retrieve dictionary keys, values, and key-value pairs  
   - `clear()` – Empty the dictionary  
   - `copy()` – Create deep and shallow copies  

#### **Code Examples Included:**
- Creating dictionaries with single and multiple values  
- Accessing dictionary values using keys and indexes  
- Demonstrating dictionary mutability (adding/removing elements)  
- Practical implementation of built-in functions  

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








