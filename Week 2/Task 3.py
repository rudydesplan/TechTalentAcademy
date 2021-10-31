# Write a program that allows user to enter their favourite starter, main course, dessert and drink.
# Concatenate these and output a message which says
# “Your favourite meal is ………with a glass of….”

favourite_starter = input("What is your favourite starter ? ")
main_course = input("What is your favourite main course ? ") 
dessert = input("What is your favourite dessert ? ")
favourite_drink = input("What is your favourite drink ? ")
print(f"Your favourite meal is a {favourite_starter} , some {main_course} , a {dessert} and a glass of {favourite_drink}.")