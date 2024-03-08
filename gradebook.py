name = input("name: ")
Class = input("official class: ")
grades = []

student = {
    'Name':name,
    'Class': Class,
    'grade': grade,
}

def calc_avg():
    total = sum(grades)
    avg = total / len(grades)
    return avg

def input_grades():
    number = int(input("WHat grades do u wanna input?)"))
    if i in range(number):
        grade = float(input("enter grade: "))
        student("grades").append(grade)
    avg_grade = calc_avg(student("grades"))
    return avg_grade
    
     input_grades()
    calc_avg()










'''from statistics import mean

grades = int(input("Input your grad4es, si or no"))
answer = input("Do u want to put in ur gardes?")
gradebook = []

while answer == "si" '''