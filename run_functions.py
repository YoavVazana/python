from storage import *
from student import Student
from test import Test



def display_student_menu():
    print("""Student Menu:
            1. View your average
            2. Add a test grade
            3. Exit""")

def display_admin_menu():
    print("""Admin Menu:
            1. Add a new student
            2. Add a new course
            3. Show course average
            4. show median grade
            5. show grade distribution
            6. Exit""")

def add_grade(school):
    student_id = input("Enter student's ID number: ")
    course_name = input("Enter course's name: ")

    if course_name not in school.courses_list:
        print("Course does not exist. Please try again.")
        return

    try:
        grade = float(input("Enter student's grade: "))
        if grade < 0 or grade > 100:
            print("Invalid grade. It must be between 0 and 100.")
            return
    except ValueError:
        print("Invalid grade. It must be a number.")
        return

    student = next((s for s in school.students_list if s.id_number == student_id), None)
    if not student:
        print(f"Student {student_id} does not exist. Please try again.")
        return

    test = Test(course_name, school)
    student.add_course(test, grade)
    print(f"Grade {grade} has been added for {student.full_name} in {course_name}.")

def show_student_average(school):
    student_id = input("Enter student's ID number: ")
    student = next((s for s in school.students_list if s.id_number == student_id), None)
    if not student:
        print("Student not found.")
        return
    print(f"{student.full_name}'s average: {student.get_average()}")

def show_course_average(school):
    course_name = input("Enter course's name: ")

    if course_name not in school.courses_list:
        print("Course does not exist. Please try again.")
        return

    course_id = school.courses_list.index(course_name)
    print(f"Average in {course_name}: {school.get_courses_average(course_id)}")

def show_median_for_test(school):
    course_name = input("Enter course's name: ")

    if course_name not in school.courses_list:
        print("Course does not exist. Please try again.")
        return

    test = Test(course_name, school)
    median_grade = test.get_median_grade()

    if median_grade is None:
        print(f"No grades available for {course_name}.")
    else:
        print(f"Median grade for {course_name}: {median_grade}")

def show_grade_distribution(school):
    course_name = input(f"Enter course name ({', '.join(school.courses_list)}): ")

    if course_name not in school.courses_list:
        print("Course does not exist. Please try again.")
        return

    test = Test(course_name, school)
    distribution = test.get_grade_distribution()

    print(f"Distribution for {course_name}:")
    for range_, count in distribution.items():
        print(f"\t{range_}: {count} students")


def register_user(users, school):
    user_name = input("Enter user name: ")
    if any(user['user_name'] == user_name for user in users):
        print("User name already exists. Please try again.")
        return

    password = input("Enter password: ")
    id_number = input("Enter student's personal ID: ")
    role = input("Enter role (student/admin): ").lower()

    if role == 'student':
        student = Student(user_name,id_number, password, school)
        school.add_student(student)
        users.append({"user_name": user_name, "password": password, "role": "student", "id_number": id_number})
        print(f"Student {user_name} with ID {id_number} has been added to the school.")
    elif role == 'admin':
        users.append({"user_name": user_name, "password": password, "role": "admin"})
    else:
        print("Invalid role. Please try again.")
        return

    save_data(school, users)
    print(f"New user registered for {user_name}")

def login(users):
    user_name = input("Enter user name: ")
    password = input("Enter password: ")

    user = next((u for u in users if u['user_name'] == user_name and u['password'] == password), None)

    if user:
        print(f"Welcome {user_name}!")
        return user
    else:
        print("Invalid user name or password.")
        return None

