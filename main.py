first_number = float (input("enter your first number: "))
second_number = float (input("enter your second number: "))
operation =   (input("enter your operation: "))

def multiply(first_number, second_number):
    print(f"Multiplication result: {first_number * second_number}")

def divide(first_number, second_number):
    print(f"division result: {first_number / second_number}")

def addition(first_number, second_number):
    print(f"Addition result: {first_number + second_number}")

def subtraction(first_number, second_number):
    print(f"Subtraction result: {first_number - second_number}")

if operation == '*':
    multiply(first_number, second_number)
elif operation == '/':
    divide(first_number, second_number)
elif operation == '+':
    addition(first_number, second_number)
elif operation == '-':
   subtraction(first_number, second_number)
else:
    print("invalid request")