import numpy as np

class Test:
    def __init__(self, course, school):
        self.course = course
        self.school = school
        self.course_id = self.school.courses_list.index(course)

    def add_grade(self, student_id, grade):
        self.school.add_test(student_id, self.course_id, grade)

    def get_best_grade(self):
        return max(self.school.get_courses_grades(self.course_id))

    def get_median_grade(self):
        grades = self.school.get_courses_grades(self.course_id)
        valid_grade =  [grades for grade in grades if grade is not None]

        if len(valid_grade) == 0:
            return None

        return np.median(valid_grade)

    def get_grade_distribution(self):
        grades = self.school.get_courses_grades(self.course_id)
        valid_grade = [grades for grades in grades if grades is not None]

        distribution = {
            "90-100": 0,
            "80-89": 0,
            "70-79": 0,
            "60-69": 0,
            "0-59": 0
        }

        for grade in valid_grade:
            if 90 <= grade <= 100:
                distribution["90-100"] += 1
            elif 80 <= grade <= 89:
                distribution["80-89"] += 1
            elif 70 <= grade <= 79:
                distribution["70-79"] += 1
            elif 60 <= grade <= 69:
                distribution["60-69"] += 1
            else:
                distribution["0-59"] += 1

        return distribution





