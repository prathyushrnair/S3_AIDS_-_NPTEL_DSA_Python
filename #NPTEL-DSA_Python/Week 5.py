import sys

grade_points = {'A': 10, 'AB': 9, 'B': 8, 'BC': 7, 'C': 6, 'CD': 5, 'D': 4}

students = {}        # roll -> name
student_grades = {}  # roll -> list of grade points

current_section = None

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    if line in ["Courses", "Students", "Grades", "EndOfInput"]:
        current_section = line
        if line == "EndOfInput":
            break
        continue

    if current_section == "Students":
        roll, name = line.split("~")
        students[roll] = name
        student_grades[roll] = []

    elif current_section == "Grades":
        course, sem, year, roll, grade = line.split("~")
        if roll in student_grades:
            student_grades[roll].append(grade_points[grade])

# Output
for roll in sorted(students.keys()):
    grades = student_grades.get(roll, [])
    if grades:
        gpa = round(sum(grades) / len(grades), 2)
    else:
        gpa = 0
    # print with up to 1 decimal if needed, but not always 2
    if isinstance(gpa, float) and gpa.is_integer():
        print(f"{roll}~{students[roll]}~{int(gpa)}.0")
    else:
        print(f"{roll}~{students[roll]}~{gpa}")
