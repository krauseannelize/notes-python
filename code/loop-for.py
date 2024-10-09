# FOR LOOPS
# Examples of how to use for loops

print("EXAMPLE | Using for loop to print numbers in a range (missing parameters)")
# range start is empty and will start at 0
# range stop is 5 and stop is exclusive so 5 will not be included
# range step is empty so default step is increments of 1
# range is 0, 1, 2, 3, 4
for x in range(5):
    print(x)
print()

print("EXAMPLE | Using for loop to print numbers in a range (start, stop and step)")
# range start is will start at 2
# range stop is 11 and stop is exclusive so 10 will be last number
# range step is 2 so numbers will increase by 2
# range is 2, 4, 6, 8, 10
for x in range(2,11,2):
    print(x)
print()

print("EXAMPLE | Using for loop to print numbers multiplied by 3 in a range using incremental value")
# range start is will start at 2
# range stop is 5 and by adding 1 the last number will be inclusive of 5
# range step is empty so default step is increments of 1
# range is 2, 3, 4, 5
for number in range(2,5+1):
    print(number*3)
print()

print("EXAMPLE | Using for loop to print numbers in a range (negative parameters)")
# range start is will start at 10
# range stop is 0 and stop is exclusive so 1 will be last number
# range step is -2 so numbers will decrease by 2
# range is 10, 8, 6, 4, 2
for x in range(10, 0, -2):
    print(x)
print()

print("EXAMPLE | Using for loop to calculate product of numbers in a range")
product = 1
# range start is will start at 1
# range stop is 10 and stop is exclusive so 9 will be last number
# range step is empty so default step is increments of 1
# range is 1, 2, 3, 4, 5, 6, 7, 8, 9
for num in range(1,10):
  product = product * num

print("Product of range 1 to 10 is: ", str(product))
print()

print("EXAMPLE | Using for loop to print personalized message for every item in a list")
friends = ['Yennefer', 'Geralt', 'Jaskier', 'Triss']
for friend in friends:
    print("Toss a coin to " + friend)
print()

print("EXAMPLE | Using for loop to add integers in a list (sum) and add list items to calculate average")
values = [ 23, 52, 59, 37, 48 ]
sum = 0
length = 0
# for loop iterates through every item in list values and
# returns sum and length
for value in values:
    sum += value
    length += 1

print("List of numbers: " + str(values))
print("Total sum: " + str(sum))
print("Average: " + str(sum/length))   # use length to calculate average
print()

print("EXAMPLE | Using for loop to convert Fahrenheit in a range to Celcius")
def convert_to_celsius(x):
  return (x-32)*5/9   # Conversion formula: (32°F − 32) × 5/9 = 0°C

# range start is will start at 0
# range stop is 101 and stop is exclusive so 100 will be last number
# range step is 10 so numbers will increase by 10
# range is 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
for x in range(0,101,10):
  print(str(x) + "°F is " + str(round(convert_to_celsius(x),2)) + "°C")
print()