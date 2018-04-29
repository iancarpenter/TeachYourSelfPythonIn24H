student_and_grades = {}
while True:
    student_name = input("Please give me the name of a student ['q' to quit]: ")
    
    if student_name.lower() == 'q':
        break
    
    student_grade = input("Please give me their grade:")

    student_and_grades[student_name] = student_grade

print("Ok, printing grades")

print("Student Grade")

for k, v in student_and_grades.items():
    print("{} \t {}".format(k, v))