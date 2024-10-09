# WHILE LOOPS
# Examples of how to use while loops

print("EXAMPLE | Using a while loop to print a string 5 times")
repetitions = 1
while repetitions < 6:
    print("Hello")
    repetitions += 1
print()

print("EXAMPLE | Using a while loop to count to 5")
num = 1
while num < 6:
    print("Loop for iteration " + str(num))
    num += 1
else:
   print("End of while loop.")
print()

print("EXAMPLE | Using a while loop with a reusable function twice")
def iterations(n):
    x = 1
    while x <= n:
        print("Iteration " + str(x) + " of " + str(n))
        x += 1
    print("Function has finished.")

# calls to function iterations
iterations(3)
print()
iterations(2)
print()

print("EXAMPLE | Using a while loop to print multiples of 6")
multiplier = 1
result = multiplier * 6
while result <= 60:
    print(result)
    multiplier += 1
    result = multiplier * 6
print("Done")
print()

print("EXAMPLE | Using a while loop to sum integers in a range")
def integer_sum(x):
  # returns zero when zero and negative numbers used
  if x < 1:
    return 0
  
  num = 1
  sum = 0

  # loop will end when num is 1 larger than the input
  while num <= x:
    sum = sum + num
    num += 1
  return sum

print("Sum of 1 to 3 is:", str(integer_sum(3)))
print("Sum of 1 to 6 is:", str(integer_sum(6)))
print()

print("EXAMPLE | Using while loops to calculate sum and product by reusing variables")
x = 1
sum = 0
while x < 6:   # calculates sum of 1+2+3+4+5=15
    sum = sum + x
    x = x + 1

# second while loop used to show that variables can be reused
# but needs to be reinitialized - same can be achieved with one while
x = 1
product = 1
while x < 6:   # calculates product of (1*2)=2, (2*3)=6, (6*4)=24, (24*5)=120
    product = product * x
    x = x + 1

print("Sum of 1 to 5:", str(sum))
print("Product of 1 to 5:", str(product))
print()

print("EXAMPLE | Check if a number is a power of 3 using a while loop and if statement")
def power_three(number):
  # while number divisible by 3 without fractional and number not zero
  # loop will continue until number can't be divided by 3 anymore
  while number % 3 == 0 and number != 0:
    number = number / 3
 
  # conditional statement evaluates remainder to check if power of 3
  if number == 1:
    return True
  return False
  
# calls to function power_three
print("27 is a power of three:", power_three(27)) # should be true
print("53 is a power of three:", power_three(53)) # should be false
print("81 is a power of three:", power_three(81)) # should be true
print()

print("EXAMPLE | Create a multiplication table for first 5 rows unless total exceeds 30")
def multiplication_table(number):
    multiplier = 1
    while multiplier <= 5:
        result = number * multiplier 
        if  result > 30:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
     
        multiplier += 1

# Calls to function multiplication_table
print("Multiplication table of 3:")
multiplication_table(3)   # will loop 5 times
print()
print("Multiplication table of 9:")
multiplication_table(9)   # will not loop 5 times as 30 exceeded
print()