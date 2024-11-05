from storage import save_data
from student import Student
from user import User
from school import School



class Admin(User):
    def __init__(self, user_name, password):
        super().__init__(user_name, password, 'admin')

    def add_student(self, school, users):
        full_name = input("Enter student's full name: ")
        id_number = input("Enter student's id number: ")
        password = id_number
        student = Student(full_name, id_number,password, school)
        school.add_student(student)
        print(f"Student {full_name} has been added.")

        users.append({
            "user_name": full_name,
            "id_number": id_number,
            "password": password,
            "role": "student"
        })

        save_data(school, users)

    def add_course(self, school):
        course_name = input("Enter course's name: ")
        school.add_course(course_name)
        print(f"Course {course_name} has been added.")