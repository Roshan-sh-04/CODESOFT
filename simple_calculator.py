def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

print("Simple Calculator")
print("------------------")
print("Select operation: ")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")


operation = input("Enter operation (+, -, *, /): ")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "+":
        result = add(num1, num2)
        print('Result = 'f"{num1} + {num2} = {result}")

    elif operation == "-":
        result = subtract(num1, num2)
        print('Result = 'f"{num1} - {num2} = {result}")

    elif operation == "*":
        result = multiply(num1, num2)
        print('Result = 'f"{num1} * {num2} = {result}")

    elif operation == "/":
        result = divide(num1, num2)
        print('Result = 'f"{num1} / {num2} = {result}")

    else:
        print("Invalid operation! Please choose +, -, *, or /.")

except ValueError:
    print("Invalid input! Please enter numeric values.")