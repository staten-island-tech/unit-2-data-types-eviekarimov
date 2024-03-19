name = input("Name: ")
Class = input("Official class: ")
grades = []

student = {
    'Name':[name],
    'Class': [Class],
    'grade': [grades],
}

def calc_average(grades):
    total = sum(grades)
    avg = total / len(grades)
    return avg


def input_grades():
    number = int(input("How many grades do u wanna input? "))
    for i in range(number):
        grade = float(input("Enter grade: "))
        student['grades'].append(grade)
    

input_grades()
print(student)










'''from statistics import mean

grades = int(input("Input your grad4es, si or no"))
answer = input("Do u want to put in ur gardes?")
gradebook = []

while answer == "si" '''