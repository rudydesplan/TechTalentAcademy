# Write a program which will ask for two numbers from a user. 
# Then offer a menu to the user giving them a choice of operator:
# Once the user has selected which operator they wish to use, perform the calculation.

number1 = float(input("Choose a first number "))
number2 = float(input("Choose a second number "))
operator = input(print("""Choose an operator : 
      Enter + if you want an Addition
      Enter - if you want a Subtraction
      Enter / if you want a Division
      Enter * if you want a Multiplication
      Enter ** if you want an Exponentiation"""))
if operator == "+" :
    print(f"The result is :  {number1 + number2} ")
elif operator == "-" :
    print(f"The result is :  {number1 - number2} ")
elif operator == "-" :
    print(f"The result is :  {number1 / number2} ")
elif operator == "-" :
    print(f"The result is :  {number1 * number2} ")
elif operator == "-" :
    print(f"The result is :  {number1 ** number2} ")
