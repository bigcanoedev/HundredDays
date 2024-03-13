#add
def add(n1, n2):
    """
    takes two numbers and returns the sum
    """
    return n1 + n2

def subtract(n1, n2):
    """
    takes two numbers and returns the first minus the second
    """
    return n1 - n2

def multiply(n1, n2):
    """
    takes two numbers and returns the product
    """
    return n1 * n2

def divide(n1, n2):
    """
    takes two numbers and returns the first divided by the second
    """
    return n1 / n2

print("Welcome to the calculator program")
n1 = int(input("What is the first number?"))
operation = input("What is the operation:\n (+) : add \n (-) : subtract \n (*) : multiply \n (/) : divide")
n2 = int(input("What is the second number?"))

if operation == "+":
    print(add(n1, n2))
elif operation == "-":
    print(subtract(n1,n2))
elif operation == "*":
    print(multiply(n1,n2))
elif operation == "/":
    print(divide(n1,n2))
else:
    print("error")