# -----------------------------------------------------------------------------
# Author: Meagan Swanson
# Date: December 6, 2019
#
# This program creates a class registration system where users can log in as
# students to add courses, drop courses, and list registered courses
# or as administrators to show class rosters and change maximum class sizes
# -----------------------------------------------------------------------------

from course import Course
from student import Student
from admin import Admin


def main():

    # ------------------------------------------------------------
    # Manages the whole registration system
    # No parameters
    # Creates lists necessary for the program
    # and uses a loop to create student or administrator sessions
    # Returns no values.
    # ------------------------------------------------------------

    course_list = []
    student_list = []
    admin_list = []

    init_lists(course_list, student_list, admin_list)

    x = 0
    while x == 0:
        print()
        user_type = int(input("Enter 1 if you are a student, 2 if you are an "
                              "administrator, 0 to quit: "))
        if user_type == 1:
            student_session(course_list, student_list)
        elif user_type == 2:
            admin_session(course_list, admin_list)
        elif user_type == 0:
            break
        else:
            print("Invalid input")
            continue


def init_lists(c_list, s_list, a_list):

    # ------------------------------------------------------------
    # This function adds elements to course_list, student_list and
    # admin_list.  It makes testing and grading easier.  It has
    # three paramters: c_list is the list of Course objects;
    # s_list is the list of Student objects; a_list is the list of
    # Admin objects.  This function has no return value.
    # -------------------------------------------------------------

    course1 = Course("CSC121", 2)
    course1.add_student("1004")
    course1.add_student("1003")
    c_list.append(course1)
    course2 = Course("CSC122", 2)
    course2.add_student("1001")
    c_list.append(course2)
    course3 = Course("CSC221", 1)
    course3.add_student("1002")
    c_list.append(course3)

    student1 = Student("1001", "111")
    s_list.append(student1)
    student2 = Student("1002", "222")
    s_list.append(student2)
    student3 = Student("1003", "333")
    s_list.append(student3)
    student4 = Student("1004", "444")
    s_list.append(student4)

    admin1 = Admin("7001", "777")
    a_list.append(admin1)
    admin2 = Admin("8001", "888")
    a_list.append(admin2)


def student_session(c_list, s_list):

    # ------------------------------------------------------------
    # Begins a student session
    # Take two arguments: student list and course list
    # Determines what action the student would like to take in the program (
    # add, drop, or show registered courses) and calls on the methods from
    # student.py to perform this action.
    # Returns no values.
    # ------------------------------------------------------------

    index = login(s_list)

    if index != -1:
        student = s_list[index]
        x = 0
        while x == 0:
            print()
            action = int(input("Enter 1 to add course, 2 to drop course, "
                               "3 to see courses you have registered, "
                               "or 0 to exit: "))
            if action == 1:
                student.add_course(c_list)
            elif action == 2:
                student.drop_course(c_list)
            elif action == 3:
                student.list_courses(c_list)
            elif action == 0:
                print("Student session ended.")
                break
            else:
                continue
        else:
            main()


def admin_session(c_list, a_list):

    # ------------------------------------------------------------
    # Begins an administrator session
    # Take two arguments: administrator list and course list
    # Determines what action the administrator would like to take in the
    # program (show class roster or change max class size) and calls on the
    # functions from admin.py to perform this action
    # Returns no values.
    # ------------------------------------------------------------

    index = login(a_list)
    if index != -1:
        admin = a_list[index]
        x = 0
        while x == 0:
            print()
            action = int(input("Enter 1 to show class roster, 2 to change "
                               "max class size, or 0 to exit: "))
            if action == 1:
                admin.show_roster(c_list)
            elif action == 2:
                admin.change_max_size(c_list)
            elif action == 0:
                print("Administrator session ended.")
                break
            else:
                continue
    else:
        main()


def login(u_list):

    # ------------------------------------------------------------
    # Obtain login credentials for a student or administrator session
    # Take one argument: u_list (which is either student list or admin list
    # depending on user input)
    # Displays if the entered credentials were correct or incorrect
    # Returns index value of -1 if ID/PIN incorrect or index of user if correct
    # ------------------------------------------------------------

    u_id = str(input("Enter ID: "))
    pin = str(input("Enter PIN: "))

    for i in range(len(u_list)):
        if u_list[i].get_id() == u_id and u_list[i].get_pin() == pin:
            print("ID and PIN verified")
            return i

    print("ID or PIN incorrect")
    return -1


main()
