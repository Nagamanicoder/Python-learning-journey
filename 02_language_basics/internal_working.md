# Meomry optimization in Python

### Interview question on memory 
### Is the datatype assigned to the variable?
### Answer:  No, The datatype is not given to the variableand are no datatypes

### Is the moemory doesnot contain the datatype?
### Answer: Yes, It will contain the datatype based on the what memory contains

#### In Python, variables do not have data types; the values (objects) stored in memory do. This is a core concept of Python's dynamic typing. 
Here is a breakdown of how Python handles this:
Everything is an object: In Python, all data values are objects stored in the private heap memory. Every object has an identity (memory address), a type (class), and a value.

Variables are labels (references): Variables are not containers that store data directly. Instead, they are symbolic names, or labels, that reference the memory location (identity) of a specific object.

Dynamic Typing: Because variables are just references, you do not need to explicitly declare their type. The Python interpreter determines the type by looking at the object the variable is currently referencing.

Reassignment: A single variable can be reassigned to point to an object of a different type during program execution.

#### Immutable → modification = new object created
####  >>> a = 4
#### >>> b = a
#### >>> a 
#### 4
#### >>> b
#### 4
#### >>> a = a + b
#### >>> a
#### 8
#### >>> b
#### 4

#### Mutable → modification = same object updated
#### >>> l1 = [1,2,3]
#### >>> l2 = l1
#### >>> l1[0] = 44
#### >>> l1
#### [44, 2, 3]
#### >>> l2
#### [44, 2, 3]

#### slicing gives the copy of the variable

