"""
Write a python program to calculate a student's grade based on their marks.
The program should:
Take the student's mark (0-100) as input.
Use conditional statements to determine the grade according to the following rules :
    a. 90-100: Grade A
    b. 80-89: Grade B
    c. 70-79: Grade C
    d. 60-69: Grade D
    e. Below 69: Grade F
print the grade.
"""
marks = int(input("Enter The marks under(0-100) : "))

if 90 <= marks <= 100:
    grade = "A"
elif 80 <= marks <= 89:
    grade = "B"
elif 70 <= marks <= 79:
    grade = "C"
elif 60 <= marks <= 69:
    grade = "D"
else:
    grade = "F"

print("The Grade is : ", grade)
