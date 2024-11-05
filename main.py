from run_functions import *
from storage import *
from admin import *

def main():
    users, tests = load_data()
    school = School()

    for test_data in tests:
        student = next((s for s in school.students_list if s.id_number == test_data["student_id"]), None)
        if student:
            test = Test(test_data["course_name"], school)
            student.add_course(test, test_data["grade"])

    while True:
        choice_entry = input("Do you want to [1] login or [2] register? (or 'exit' to quit): ")

        if choice_entry == '1':
            user = login(users)
            if user and user['role'] == 'student':
                student_id = user['id_number']
                existing_student = next((s for s in school.students_list if s.id_number == student_id), None)
                if not existing_student:
                    student = Student(user['user_name'], student_id, user['password'], school)
                    school.add_student(student)
                    print(f"Student {user['user_name']} has been added to the school.")
                else:
                    student = existing_student

                while True:
                    display_student_menu()
                    choice_option = input("choice your option: ")
                    if choice_option == "1":
                        show_student_average(school)
                    elif choice_option == "2":
                        add_grade(school)
                    elif choice_option == "3":
                        print("Exiting student menu.")
                        break
                    else:
                        print("Invalid choice.")
            elif user and user['role'] == 'admin':
                admin = Admin(user['user_name'], user['password'])
                while True:
                    display_admin_menu()
                    admin_choice = input("choice your option: ")
                    if admin_choice == "1":
                        admin.add_student(school, users)
                    elif admin_choice == "2":
                        admin.add_course(school)
                    elif admin_choice == "3":
                        show_course_average(school)
                    elif admin_choice == "4":
                        show_median_for_test(school)
                    elif admin_choice == "5":
                        show_grade_distribution(school)
                    elif admin_choice == "6":
                        print("Exiting admin menu.")
                        break
                    else:
                        print("Invalid choice.")

        elif choice_entry == '2':
            register_user(users, school)

        elif choice_entry == 'exit':
            break

        else:
            print("Invalid choice.")

    save_data(school, users)


if __name__ == "__main__":
    main()
