num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

def addition():
    return num1 + num2

def subtraction():
    return num1 - num2

def multiplication():
    return num1 * num2

def division():
    if num2 == 0:
        print("Division by zero is not allowed!")
    return num1 / num2



print("The sum is:", addition())
print("The difference is:", subtraction())
print("The product is:", multiplication())
print("The quotient when num1 is divided by num2 is:", division())
