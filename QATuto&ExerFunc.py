#Tutorial
from cgitb import reset


def add_calc(num1, num2):
    ans = num1 + num2
    return ans

total = add_calc(5,5)
print (total + 20)

#Exercise
# Create a new python file. In that file create a program that works out a grade based on marks with the use of functions.
# The program should take the students name, homework score (/25), assessment score (/50) and final exam score (/100) as inputs, 
# and output their name and final ICT grade as a percentage.
# Reminder: any inputs and prints should not be included inside the function definition, and should strictly be done outside.
# Stretch goal: Include grade boundaries such that the program also outputs a grade for the student (A, B, etc.)
def grade (INHScore, INAscore, INFEScore):
    Result = round(int((INHScore + INAscore + INFEScore)) / 175 * 100)
    return Result

def boundries (INResult):
    if int(INResult) >= 75:
        mark = "A"
        return mark
    elif int(INResult) < 75 and int(INResult) >=65:
        mark = "B"
        return mark
    elif int(INResult) < 65 and int(INResult) >=50:
        mark = "C"
        return mark
    else:
        mark = "Fail"
        return mark

SName = input("Please Enter the Students Name: ")

HScore = int(input("Please Enter the Homework Score "))
AScore = int(input("Please Enter the assessment Score "))
FEScore = int(input("Please Enter the final exam Score "))
OUTResult = str(grade (HScore, AScore, FEScore))
OUTGrade = boundries(OUTResult)
print ("For student: " + SName + " " + "their Overall mark is: " + OUTResult + "%" + " and their letter grade is: " + OUTGrade)
