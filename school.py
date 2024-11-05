import numpy as np

class School:
    def __init__(self):
        self.grades_matrix = {}
        self.students_list = []
        self.courses_list = ["linear_algebra", "english", "python", "C", "data_structure"]

    def add_student(self, student):
        self.students_list.append(student)
        self.grades_matrix[student.id_number] = {course: None for course in range(len(self.courses_list))}

    def add_course(self, course_name):
        self.courses_list.append(course_name)
        for student_id in self.grades_matrix:
            self.grades_matrix[student_id][course_name] = None


    def add_test(self, student_id, course_id, grade):
        self.grades_matrix[student_id][course_id] = grade
        print(f"Added grade {grade} for student {student_id} in course {course_id}")

    def get_students_grades(self, student_id):
        return self.grades_matrix[student_id]

    def get_courses_grades(self, course_id):
        return [self.grades_matrix[student_id][course_id] for student_id in self.grades_matrix]

    def get_students_average(self, student_id):
        grades = list(self.grades_matrix[student_id].values())
        return np.mean([grade for grade in grades if grade is not None])

    def get_courses_average(self, course_id):
        grades = self.get_courses_grades(course_id)
        print(f"Grades for course {course_id}: {grades}")
        valid_grades = [grade for grade in grades if grade is not None]

        if len(valid_grades) == 0:
            return 0

        return np.mean(valid_grades)