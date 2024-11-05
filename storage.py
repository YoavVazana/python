import json

def load_data(filename = 'users.json'):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)

            if isinstance(data, dict):
                return data.get('users', []), data.get('tests', [])
            else:
                print("Data format is invalid, expected a dictionary. Initializing empty data.")
                return [], []
    except FileNotFoundError:
        return [], []


def save_data(school, users, filename = 'users.json'):
    data = {
        "users": users,
        "tests": []
    }

    for student in school.students_list:
        for test, grade in student.courses:
            data["tests"].append({
                "course name": test.course,
                "student_id": student.id_number,
                "grade": grade
            })



    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
