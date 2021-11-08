# Write a program to ask a student for their percentage mark and convert this to a grade.
# The conversion will be done in a function called mark_grade

def mark_grade(percentage):
    if 0<= percentage <= 29 :
        return("F")
    elif 30<= percentage <= 39 :
        return("E")
    elif 40<= percentage <= 49 :
        return("D")
    elif 50<= percentage <= 59 :
        return("C")
    elif 60<= percentage <= 69 :
        return("B")
    elif 70<= percentage <= 100 :
        return("A")
    else :
        return("Your percentage is wrong! ")

percentage = int(input("what is your percentage mark ?"))
print("Your Grade is",mark_grade(percentage))

# Ask the user for their target grade and print this with their mark
# If their target grade > exam grade display a suitable message
# If their target grade = exam grade display a suitable message
# If their target grade < exam grade display a suitable message

target_grade = input("What is your target grade ? ")
print("Your grade is",mark_grade(percentage), f"and your target Grade is {target_grade}.")
actual_grade = mark_grade(percentage)

def message(actual_grade,target_grade):
    if actual_grade == target_grade :
        print("Continue like to work like that and it should be fine.")
    elif actual_grade > target_grade :                                    # Here we compare 2 strings
        print("You need to work harder to get this grade.")
    elif actual_grade < target_grade :                                    # Here we compare 2 strings
        print("You need to be more ambitious.")

message(actual_grade,target_grade,)