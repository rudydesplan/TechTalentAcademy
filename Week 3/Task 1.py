# Write a program that allows you to enter 4 numbers and stores them in a file called “Numbers”
# 3, 45 ,83 , 21
# Have a go at ‘w’ ‘r’ ‘a’

my_file = open("Numbers.txt", "w")
i = 0
while i<4 :
    i += 1
    my_file.write(str(input("Enter a numbers ")))
    my_file.write("\n")
my_file.close()