# Write a program that asks the user for an integer number and checks if it is > 10. 
# If it is, it will print “Number is Greater than 10”,
# else “Number is smaller than 10”.

number = int(input("Chooose a whole number "))
if number > 10 :
    print("Number is Greater than 10")
elif number == 10 :
    print("Number is equal to 10")
else :
    print("Number is smaller than 10")

# Then write a loop program that ask the user for an integer number and check if it is < 10.
#  If it is < 10 then it keeps adding 1 to the value.

nombre = int(input("Chooose a whole number "))
while nombre < 10 :
    nombre += 1
    print(nombre)
else :
    print("Number is Greater than 10")