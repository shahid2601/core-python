import sys  # Importing the sys module to handle command line arguments

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

# Script expects three command line arguments: two integers and an operation
a = int(sys.argv[1])
operation = sys.argv[2]
b = int(sys.argv[3])

# Check the operation and call the corresponding function
if operation == "add":
    output = addition(a, b)
    print(output)
if operation == "sub":
    output = subtraction(a, b)
    print(output)
if operation == "mul":
    output = multiplication(a, b)
    print(output)

# This script can be run from the command line as follows:
# python calculator.py 5 add 3
# python calculator.py 10 sub 4
# python calculator.py 6 mul 7
# It will print the result of the operation specified.