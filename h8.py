print("Welcome to the student checker")

def is_student_enrolled(name):
    students = ["Ian", "John", "Simon"]

    if name in students:
        return True
    else:
        return False

while True:
    user_entered_name = input("Please give me the name of a student ['q' to quit]: ")         

    if user_entered_name == 'q':
        break
    
    student_enrolled = is_student_enrolled(user_entered_name)

    if student_enrolled:
        print("Yes, that student is enrolled in the class!")
    else:
        print("No, that student is not in the class")

