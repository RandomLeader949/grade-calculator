amountOfGrades = int(input("How many grades would you like? "))
finalGrade = 0
for i in range(amountOfGrades):
    grade = int(input("hat is the grade of a test? "))
    finalGrade += grade
    print("Accepted")
print(finalGrade/amountOfGrades)