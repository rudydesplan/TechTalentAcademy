# Write a program that does the following:
# a) Stores a random number (1-10) in a variable.
# b) Asks a user for their name and stores this in a variable.
# c) Asks a user to guess the number between 1 and 10.
# d) Tells the user whether they have guessed correctly.

import random
random_number = random.randint(1,10)
user_name = input("What is your name?")
number_guessed = input("Guess a number between 1 and 10 ")
if random_number == number_guessed :
    print("You are lucky, you guessed correctly.")
else : 
    print("Nope, it\'t not this number.")