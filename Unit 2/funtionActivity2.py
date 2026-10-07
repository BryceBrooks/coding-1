# PROBLEM #1
# Create a function that takes in 2 inputs and compares them.
# Your inputs should be numbers.
# The function should compare if the first input is
# less than the second input.
# If it is less than the second input it should print true.
# If it is not, it should print false.


def compareVal():
    numA= input()
    numB= input()
    print(numA < numB)

compareVal()

# PROBLEM #2
# Create a function that will compare if a student
# has made honor roll.

# The student should be able to input 2 pieces of data
# the first should be their grade and the second should
# be the number of days they have been absent.

# If the student's grade is above a 90 and the number
# of absense is less than 5, the program should print
# true, otherwise it should print false.

def honorRoll():
    grade = float(input("Enter your grade: "))
    absences = int(input("Enter number of absences: "))
    print(grade > 90 and absences < 5)

honorRoll()