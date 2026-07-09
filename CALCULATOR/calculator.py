# Calculator in Python

no = int(input(
    "Enter value for:\n"
    "Sum - 1\n"
    "Subtraction - 2\n"
    "Multiply - 3\n"
    "Divide - 4\n"
    "Modulus - 5\n"
))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def sub(a, b):
    return a - b

def divide(a, b):
    return a / b

def modulus(a, b):
    return a % b

if no == 1:
    print("Answer:", add(a, b))

elif no == 2:
    print("Answer:", sub(a, b))

elif no == 3:
    print("Answer:", multiply(a, b))

elif no == 4:
    if b != 0:
        print("Answer:", divide(a, b))
    else:
        print("Cannot divide by zero")

elif no == 5:
    print("Answer:", modulus(a, b))

else:
    print("Invalid input")