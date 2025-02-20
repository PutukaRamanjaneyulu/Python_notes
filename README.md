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

## List Python_file.ipynb
##### Key Insights
-> The notebook begins by explaining that lists are mutable, meaning their contents can be changed.

-> It attempts to assign a value to an index beyond the current list size, which leads to an IndexError.

-> It likely covers list indexing, slicing, adding, removing, and modifying elements.

-> There might be some examples demonstrating list methods (e.g., append(), extend(), insert(), remove(), pop(), etc.).

-> Some cells may include incorrect operations to illustrate errors or limitations.

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


