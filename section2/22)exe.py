students_list = {
    'Name': 'Mujju',
    'School': 'CPS',
    'grades': (66, 77, 88)
}

def average_grade(data):
    grades = data['grades']
    return sum(grades)/ len(grades)
print(average_grade)

def average_grade_all_students(students):
    total = 0
    count = 0
    for student in students_list:
        total = total + sum(student['grades'])
        count = count + len(student['grades'])

    return total / count
print(average_grade_all_students)

