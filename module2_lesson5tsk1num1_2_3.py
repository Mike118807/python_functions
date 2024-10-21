# 
# 1. The Calculator App
#
# Objective: The aim of this assignment is to build a basic calculator that can perform 
# addition, subtraction, multiplication, and division.
#
# Task 1: Create functions for each arithmetic operation.
#
# Task 2: Use inputs to ask the user what operation they want to perform, 
# and what numbers they want to use.
#
# Task 3: Ensure your code can handle division by zero and other potential errors. 
# So if you divide by 0, there is error handling set up to prevent an error from showing in the console.


# used to input numbers 


respose = input ("0/1/2/3/4/5/6/7/8/9")
input == [ 'a (int)' ]
input == [ 'b (int)' ]

#use the function to add numbers together

def add(a, b):
    return a + b

total = add(2, 2)
print(total)

#use the function to subtract numbers

def subtract(a, b):
    return a - b

total = subtract(2, 2)
print(total)

#use the function to multiply numbers

def multiply(a, b):
    return a * b

total = multiply(2, 2)
print(total)

#use the function to divide numbers

def divide(a, b):
    return a / b

total = divide(2, 2)
print(total)

#select operation

input = ("select function")
print("add")
print("subtract")
print("multiply")
print("divide")

# take input

print =(f'input("enter pick (1/2/3/4/5/6/7/8/9/0") ')

# check if user wants to do another calculation
next_calculation = ("how about another one? ")