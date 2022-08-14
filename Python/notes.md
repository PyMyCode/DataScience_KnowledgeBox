## Data Types

### List and Tuples

- Lists are immutable whereas Tuples are not
- Both store location data 

```python
list = [1,2,3]
tup = (1,2,3)

list[index]
tup[index]
# to get all the methods supported
help(variable_name)

```

#### DICT

Keys and and values
```python
dic = {"key1": 4, "key2": 5}

##get keys
dic.keys()

##get all values
dic.values()
```

### Set
- a set of unique items
- DO NOT STORE location data of the elements

```python
set = {1,2,3,3}
print(set)
>{1, 2, 3}

set.add(4)
print(set)
>{1, 2, 3, 4}

```
Mathemtical operations

```python
# Intersection
set_1 = {1,2,3,4,5,6,7}
set_2 = {5,6,7,8,9,10}
set_1 & set_2
>{5, 6, 7}

#union
set_1.union(set_2)
>{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

```

## Branching


```python

if (conditions == True):
    #statement executed if true
elif (conditions == True):
    #statement executed if true
else:
    #statement executed if false

#statement executed anyways

```

## Loops

### for
```python
for x in range(0,3):
     print(x)

items = ["apple", "banana", "oranges"]

for item in items:
     print(item)

for i, item in enumerate(items):
     print(f"{i} : {item}")
>
0 : apple
1 : banana
2 : oranges
```
### While
```python

items = ["apple", "banana", "oranges"]

i = 0
while (items[i] == "apple" ):
     #execute
     i+=1
```

## Functions

```python
def function_name():
    #do something
    return output
```
function vs methods

```python
num = [1,3,2,0]

# funcion
# functions creates a new instance
sorted_num = sorted(num)
print(num)
>[1, 3, 2, 0]
print(sorted_num) 
>[0, 1, 2, 3]

# method
#
num.sort()
print(num)
>[0, 1, 2, 3]
```

## Error Handling
```python
try:    
    a = input("type your input: ")
    b = int(a)/2
    print(b)
except TypeError as e:
    print(e)
except ValueError:
    print("Please enter a number")
else:
    print("division was successful")
finally:
    print("code end")
```
## Object and Classes
### Class

classes contain:
- data attributes
- methods

list is a build in Python Class

```python
l = [1,2,3,4,5] # an object instance of the type/class list
type(l)
><class 'list'>
```
### Methods

- methods are functions and every object in a class or type can use
- it is how you interact with the data in a object 
```python
l = [1,2,3,4,5]
# method sort is in the class list
# it changes the data in the object
l.sort()
l.reverse()
```
