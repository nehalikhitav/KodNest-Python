students = [
    ["Alice", 85, 90, 78],
    ["Bob", 70, 85, 95],
    ["Charlie", 95, 80, 89],
    ["David", 60, 75, 68],
    ["Eva", 88, 92, 95],
    ["Frank", 72, 65, 80],
    ["Grace", 90, 85, 92]
]


# 1. Calculate each student's average
averages = {}

for student in students:
    name = student[0]
    marks = student[1:]

    average = sum(marks) / len(marks)

    averages[name] = round(average, 2)


# 2. Find students who scored below 70 in at least one subject
students_below_70 = [
    student[0]
    for student in students
    if any(mark < 70 for mark in student[1:])
]


# 3. Create dictionary of students with average 80 or above
high_performers = {}

for name in averages:
    if averages[name] >= 80:
        high_performers[name] = averages[name]


# 4. Find students with average 90 or above
top_students = []

for name in averages:
    if averages[name] >= 90:
        top_students.append(name)


# 5. Find the highest-scoring student
highest_student = ""
highest_average = 0

for name in averages:
    if averages[name] > highest_average:
        highest_average = averages[name]
        highest_student = name


# 6. Calculate subject averages

math_total = 0
science_total = 0
english_total = 0

for student in students:
    math_total += student[1]
    science_total += student[2]
    english_total += student[3]

math_average = math_total / len(students)
science_average = science_total / len(students)
english_average = english_total / len(students)


# 7. Print the report

print("===== STUDENT REPORT =====")

print("\nStudent Averages:")

for name in averages:
    print(name, "-> Average:", averages[name])

print("\nTop Students:")
print(top_students)

print("\nStudents Needing Improvement:")
print(students_below_70)

print("\nHighest Scoring Student:")
print(highest_student, "->", highest_average)

print("\nSubject Averages:")
print("Math:", round(math_average, 2))
print("Science:", round(science_average, 2))
print("English:", round(english_average, 2))
