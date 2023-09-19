#make a code that opens a menu with 3 options
#1. add a student
#2. delete a student
#3. print all students
#4. exit.
#the menu should be in a loop and only exit when the user chooses to exit.
#the menu should be in a function called menu()
#the add student should be in a function called add_student()
#the delete student should be in a function called delete_student()
#the print all students should be in a function called print_all_students()
#the exit should be in a function called exit()
#the students should be in a list called students
#each student should be a dictionary with the following keys: name, age, grade, classroom

students = []

def menu():
    print("1. add a student")
    print("2. delete a student")
    print("3. print all students")
    print("4. exit")

def add_student():
    name = input("name: ")
    age = input("age: ")
    grade = input("grade: ")
    classroom = input("classroom: ")
    student = {"name": name, "age": age, "grade": grade, "classroom": classroom}
    students.append(student)


def delete_student():
    name = input("name: ")
    for student in students:
        if student["name"] == name:
            students.remove(student)

def print_all_students():
    for student in students:
        print(student)

def exit():
    print("bye")
    quit()

while True:
    menu()
    choice = input("enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        delete_student()
    elif choice == "3":
        print_all_students()
    elif choice == "4":
        exit()
    else:
        print("invalid choice")

# Path: ses.py