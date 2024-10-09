# Loops in Python

**Loops** are programming constructs that allow you to repeatedly execute a block of code until a certain condition is met. They are essential for automating repetitive tasks and making your code more efficient. There are two main types of loops in Python:

1. [WHILE loops](#while-loops)
    - [BREAK statement with a WHILE loop](#break-statement-with-a-while-loop)
    - [CONTINUE statement with a WHILE loop](#continue-statement-with-a-while-loop)
    - [ELSE statement with a WHILE loop](#else-statement-with-a-while-loop)
    - [PASS statement with a WHILE loop](#pass-statement-with-a-while-loop)
    - [Infinite WHILE loops](#infinite-while-loops)
    - [Code examples of WHILE loops](/code/loop-while.py)
1. [FOR loops](#for-loops)
    - [BREAK statement with a FOR loop](#break-statement-with-a-for-loop)
    - [CONTINUE statement with a FOR loop](#continue-statement-with-a-for-loop)
    - [ELSE statement with a FOR loop](#else-statement-with-a-for-loop)
    - [PASS statement with a FOR loop](#pass-statement-with-a-for-loop)
    - [Code examples of FOR loops](/code/loop-for.py)

---

## WHILE loops

**WHILE loops** are used when you want to repeat a block of code as long as a certain condition is true, and the condition is checked at the beginning of each iteration. The basic syntax is:

```python
variable = ("initial value")
# Initialization | Set initial value that will be used in loop condition

while condition:
# Condition | Loop will continue as long as this condition is true,
# typically a statement about the variable that was initialized

    ("Do this if true")
    # Body | Indented block of code that executes if condition is true
    
    variable = ("updated value")
    # Update | Updated variable used in condition before it is
    # returned to the loop to eventually make the condition false
```

For example, a WHILE loop can be used as follows:

```python
num = 1   # initialize variable to use in loop
while num < 6:   # condition evaluates if num is smaller than 6
    print(num)   # code that executes if num is smaller than 6
    num += 1   # update variable by incrementing it by 1

# output:
# 1
# 2
# 3
# 4
# 5
# loops stops as num = 6 and condition now false
```

---

### BREAK statement with a WHILE loop

**BREAK statements** can be used to exit a loop early. Even if the condition is true, the loop is terminated and the program flow redirected. The basic syntax is:

```python
while condition1:
# loop will continue as long as condition1 is true

    ("Do this if true")
    # block of code that executes if condition is true
    
    if condition2:
    # add another condition to be evaluated
        break
        # if condition2 true, program exits loop
```

For example, a BREAK statement can be used as follows:

```python
num = 1   # initialize variable to use in loop
while num < 6:   # condition evaluates if num is smaller than 6
    print(num)   # code that executes if num is smaller than 6
    num += 1   # update variable by incrementing it by 1
    if num == 3:  # another condition evaluating if num equal to 3
        break   # break will terminate loop if num equal to 3

# output:
# 1
# 2
# loop exited as num = 3 and condition true that triggered the break
```

---

### CONTINUE statement with a WHILE loop

**CONTINUE statements** can be used to end a loop's current iteration without exiting the loop entirely. In essence, it is used when you need to skip over certain iterations that meet a certain condition. The basic syntax is:

```python
while condition1:
# loop will continue as long as condition1 is true

    if condition2:
    # add another condition to be evaluated
        continue
        # if condition2 true, code block not executed for that iteration

    ("Do this if true")
    # block of code that executes if condition1 is true and condition2 false
    
```

For example, a CONTINUE statement can be used as follows:

```python
num = 0   # initialize variable to use in loop
while num < 6:   # condition evaluates if num is smaller than 6
    num += 1   # update variable by incrementing it by 1
    if num % 2 == 0:  # another condition evaluating if num is even
        continue   # continue will skip iterations where num is even
    print(num)   # code that executes if num is uneven, smaller than 6

# output:
# 1
# 3
# 5
```

---

### ELSE statement with a WHILE loop

**ELSE statements** can be used to execute a block of code once the condition is no longer true and will only be executed if the loop wasn't terminated by a [BREAK statement](#break-statement-with-a-while-loop). The basic syntax is:

```python
while condition:
# loop will continue as long as condition is true

    ("Do this if true")
    # block of code that executes if condition is true
else:
    ("Do this if no longer true")
    # block of code that executes if condition no longer true
    
```

For example, a ELSE statement can be used as follows:

```python
num = 1   # initialize variable to use in loop
while num < 6:   # condition evaluates if num is smaller than 6
    print(num)   # code that executes if num is smaller than 6
    num += 1   # update variable by incrementing it by 1
else:
    print("The end.")  # code executes once condition false

# output:
# 1
# 2
# 3
# 4
# 5
# The end.
```

---

### PASS statement with a WHILE loop

**PASS statements** intentionally does nothing and is used when a statement is required by syntax, but you don’t want anything to happen. This is useful as a placeholder for future code to avoid errors. The basic syntax is:

```python
while condition:
# loop will continue as long as condition is true

    pass
    # no code is executed while the condition is true    
```

For example, a PASS statement can be used as follows:

```python
num = 0   # initialize variable to use in loop
while num < 3:   # condition evaluates if num is smaller than 3
    num += 1   # update variable by incrementing it by 1
    if num % 2 == 0:  # another condition evaluating if num is even
        pass   # nothing will happen if the num is even
    print(num)   # code that executes if num is smaller than 3

# output:
# 1
# 2
# 3
# 4
# 5
# 6
```

---

### Infinite WHILE loops

A WHILE loop will repeat a block of code as long as a certain condition is true. The condition is checked at the beginning of each iteration and the loop may never run if the condition is false from the outset. On the other hand, a loop may never stop unless the necessary code is added to make the condition false at some point during the execution of the loop, or a BREAK statement is used as a control statement. When this happens, an **infinite loop** has been created that will run infinite times until the memory is full. An example of an infinite loop:

```python
num = 1   # initialize variable to use in loop
while num < 6:   # condition evaluates if num is smaller than 6
    print("Infinite loop")   # code that executes if num is smaller than 6
    # 1 will always be smaller than 6 thus creating an infinite loop
```

How to fix an infinite loop:

```python
# Updating the variable incrementally with each iteration
# Loop will exit once num = 6

num = 1   # initialize variable to use in loop
while num < 6:   # condition evaluates if num is smaller than 6
    print(num)   # code that executes if num is smaller than 6
    num += 1   # update variable by incrementing it by 1

# Using a BREAK statement as a control statement
# Loop will exit once num = 6

num = 1   # initialize variable to use in loop
while True:   # do while loop - condition is always true to begin with
    print(num)   # code that executes indefinitely
    num += 1   # update variable by incrementing it by 1
    if num > 5:   # condition that evaluates if num is larger than 5
        break   # if num is 6 and larger than 5, break will exit the loop
```

---

## FOR loops

**FOR loops** are used when you know how many times you want to repeat a block of code and is often used to iterate over a sequence like lists, tuples, or ranges. The basic syntax is:

```python
iterable = [element1, element2, element3]
# Iterable | Any object that can be iterated over with a set number of
# values (list, tuple, range) or characters (string)

for element in iterable:
# Element | Temporary variable to hold current item from iterable
# during each iteration - choose any valid variable name

    ("Do this for each element")
    # Body | Indented block of code that executes for every iteration
```

For example, a FOR loop can be used as follows:

```python
for num in range(0, 10, 2):
# range sequence start 0, end 10 (exclusive), step 2
    print(num)

# output:
# 0
# 2
# 4
# 6
# 8
# loops stops as it has executed for every iteration in range
```

---

### BREAK statement with a FOR loop

**BREAK statements** can be used to exit a loop before it has iterated over the entire object. The basic syntax is:

```python
for element in iterable:
# for loop executes for every iteration in iterable

    if condition:
    # add condition to be evaluated
        break
        # if condition true, program exits loop

    ("Do this for each element")
    # block of code that executes for every iteration
```

For example, a BREAK statement can be used as follows:

```python
for num in range(0, 10, 2):
# range sequence start 0, end 10 (exclusive), step 2
    if num > 5:
    # condition evaluates if num is larger than 5
        break
        # if condition true, program exits loop
    
    print(num)
    # code that executes for every iteration in iterable

# output:
# 0
# 2
# 4
# num = 6 which is larger than 5 so break triggered and loop exited
```

---

### CONTINUE statement with a FOR loop

**CONTINUE statements** can be used to end a loop's current iteration without exiting the loop entirely. In essence, it is used when you need to skip over certain iterations that meet a certain condition. The basic syntax is:

```python
for element in iterable:
# for loop executes for every iteration in iterable

    if condition:
    # add condition to be evaluated
        continue
        # if condition true, code block not executed for that iteration

    ("Do this for each element")
    # block of code that executes for every iteration unless condition true   
```

For example, a CONTINUE statement can be used as follows:

```python
for num in range(0, 10, 2):
# range sequence start 0, end 10 (exclusive), step 2
    if num == 6:
    # condition evaluates if num is equal to 6
        continue
        # if condition true, code block not executed for that iteration
    
    print(num)
    # code that executes for every iteration in iterable

# output:
# 0
# 2
# 4
# 8
# code block not executed for 6 as it met the condition
```

---

### ELSE statement with a FOR loop

**ELSE statements** can be used to execute a block of code once it has iterated over all elements and will only be executed if the loop wasn't terminated by a [BREAK statement](#break-statement-with-a-for-loop). The basic syntax is:

```python
for element in iterable:
# for loop executes for every iteration in iterable

    ("Do this for each element")
    # block of code that executes for every iteration

else:
    ("End of sequence reached.")
    # block of code that executes when for loop has completed all iterations    
```

For example, a ELSE statement can be used as follows:

```python
for num in range(0, 10, 2):
# range sequence start 0, end 10 (exclusive), step 2
    print(num)
    # code that executes for every iteration in iterable
else:
    print("End of the range.")
    # code that executes after for loop iterated over every iteration

# output:
# 0
# 2
# 4
# 6
# 8
# End of the range.
```

---

### PASS statement with a FOR loop

**PASS statements** intentionally does nothing and is used when a statement is required by syntax, but you don’t want anything to happen. This is useful as a placeholder for future code to avoid errors as FOR loops cannot be empty. The basic syntax is:

```python
for element in iterable:
# for loop executes for every iteration in iterable

    pass
    # no code is executed for every iteration in iterable
```

For example, a PASS statement can be used as follows:

```python
for num in range(0, 10, 2):
# range sequence start 0, end 10 (exclusive), step 2
    if num == 6:
    # condition evaluates if num is equal to 6
        pass
        # nothing will happen if num is equal to 6
    
    print(num)
    # code that executes for every iteration in iterable

# output:
# 0
# 2
# 4
# 6
# 8
```

---
