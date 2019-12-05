import math

# Task One
print("Hello {}!".format(input("Input your name, please: ")))

# Task Two
print("\nEnter two numbers.")
number_one = float(input("Number one: "))
number_two = float(input("Number two: "))
division = math.ceil(number_one / number_two)
print("The rounded up division is: {}".format(division))

# Task Three
radius = float(input("\nPlease enter a radius: "))
print("The area is {:.2f} m2".format(math.pi * radius ** 2))

# Extra Task
print("\nCalculator 2: Electric Boogaloo")
operation = input(">> ")
print(eval(operation))