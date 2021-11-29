# -----------------------------------------------------------------------------
# Author: Meagan Swanson
# Date: December 6, 2019
#
# This module creates the student class and methods used by the main function in the
# Project2.py file for students to add courses, drop courses, and list
# registered courses
# -----------------------------------------------------------------------------

from user import User


class Student(User):

    def __init__(self, u_id, pin):
        base = super()
        base.__init__(u_id, pin)

    def add_course(self, c_list):

        # ------------------------------------------------------------
        # Add course to a students course list
        # Take one argument: course list
        # Displays course not found, course already full, or already enrolled in
        # course if unable to add course. Otherwise, adds student to roster list for
        # course.
        # Returns no values.
        # ------------------------------------------------------------

        course_found = False
        code = str(input("Enter course you want to add: "))
        code.upper()

        for i in range(len(c_list)):
                if c_list[i].get_course_code() == code:
                    c_list[i].add_student(self.u_id)
                    course_found = True

        if not course_found:
            print("Course not found")


    def drop_course(self, c_list):

        # ------------------------------------------------------------
        # Drop course from a student's course list
        # Take one argument: course list
        # Displays course not found or not enrolled in course if unable to drop
        # the course. Otherwise, removes student from roster list for course.
        # Returns no values.
        # ------------------------------------------------------------

        course_found = False
        code = str(input("Enter course you want to drop: "))
        code.upper()

        for i in range(len(c_list)):
                if c_list[i].get_course_code() == code:
                    c_list[i].drop_student(self.u_id)
                    course_found = True

        if not course_found:
            print("Course not found")

    def list_courses(self, c_list):

        # ------------------------------------------------------------
        # List courses on a student's course list
        # Take one argument: course list
        # Displays number of courses currently enrolled and names of courses.
        # Returns no values.
        # ------------------------------------------------------------

        count = 0
        print("Course registered:")
        for i in range(len(c_list)):
            if c_list[i].student_in_course(self.u_id):
                print(c_list[i].get_course_code())
                count += 1
        print("Number of courses registered:", count)
