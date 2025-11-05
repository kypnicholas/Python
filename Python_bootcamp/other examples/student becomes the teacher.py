lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):								#get average
    total = sum(numbers)
    total = float(total)/len(numbers)
    return total
    
def get_average(student):							#get average grade per student
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.1*average(student["homework"]) \
    + 0.3*average(student["quizzes"]) \
    + 0.6*average(student["tests"])
    
def get_letter_grade(score):						#convert average from numeral to letter
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"
    
print get_letter_grade(get_average(lloyd))


def get_class_average(students):					#get the average for each student and then calculate the average of those averages.
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)

print get_class_average(students)
print get_letter_grade(get_class_average(students))

    
    
