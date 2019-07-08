"""
Homework 7.3: Calculator

Write a program that does the basic arithmetic operations:

addition (+),
subtraction (-),
multiplication (*),
and division (/).
Ask the user to enter two numbers and the arithemtic operation ("+", "-", "*" or "/").
"""


print("Hi there, welcome to my very first calculator. I'm not too sure whether I will work, but just give it a try, I promise I'll do my best!")

number_1 = float(input("Please enter your first number"))
number_2 = float(input("Please enter your second number"))

operator = str(input("Please choose the operator you would like to use, +, -, * or /"))

result = 0

if operator ==  str("+"):
    print(float(number_1) + float(number_2))
elif operator == str("-"):
    print(float(number_1) - float(number_2))
elif operator ==  str("*"):
    print(float(number_1) * float(number_2))
elif operator == str("/") and number_2 !=0:
    print(float(number_1) / float(number_2))
elif operator == str("/") and number_2 == 0:
    print("erroooooor buddy")
else:
    print("Sorry pal, wrong user input")

