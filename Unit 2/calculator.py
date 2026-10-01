# step 1: create a function that will add
# 2 numbers together

# step 2: the number should be typed in by a user

# phase 1 of function: function definition- actual code- nothing
def calculate_add():
    print("Program has started: type in 2 numbers to add: ")
    num1= int(input())
    num2= int(input())
    print(num1 + num2)
    print("Program has ended.")
# phase 2 of function: function call- actually runs and does something 
calculate_add()

def calculate_subtract():
    print("Program has started: type in 2 numbers to subtract: ")
    num1= int(input())
    num2= int(input())
    print(num1 - num2)
    print("Program has ended.")
calculate_subtract()

def calculate_multiply():
    print("Program has started: type in 2 numbers to multiply: ")
    num1= int(input())
    num2= int(input())
    print(num1 * num2)
    print("Program has ended.")
calculate_multiply()

def calculate_divide():
    print("Program has started: type in 2 numbers to divide: ")
    num1= int(input())
    num2= int(input())
    print(num1 / num2)
    print("Program has ended.")
calculate_divide()