# Write a program that asks a user for their favourite number between 1 and 100
# and then tells them a joke based on the number. You should use a minimum of 3 jokes.

favourite_number = int(input("What is your favorite whole number between 1 and 100?"))
if favourite_number == 6 :
    print("Why is six scared of seven? Because 7 ate 9")
elif favourite_number == 7 :
    print("How can you make 7 into an even number? You can make 7 even by just removing the S.")
elif favourite_number == 8 :
    print("What did the 0 say to the 8? ... Nice belt!")
elif favourite_number == 10 :
    print("What are the ten things that can always be count on? Our fingers.")
else :
    print("Sorry I do not have a joke for you.")
