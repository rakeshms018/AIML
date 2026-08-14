import math

number = float(input("give a number :"))

if (number > 0 ):
    square_root = math.sqrt(number)
    print(f"The square root of {number} is {square_root}")
else:
    print("The number cannot be negative")