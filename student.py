from user import User


class Student(User):
    def __init__(self, full_name, id_number, password, school):
        super().__init__(full_name, password, 'student')
        self.full_name = full_name
        self.id_number = id_number
        self.school = school
        self.courses = []


    def add_course(self, test, grade):
        self.courses.append((test, grade))
        test.add_grade(self.id_number, grade)

    def get_average(self):
        return self.school.get_students_average(self.id_number)




