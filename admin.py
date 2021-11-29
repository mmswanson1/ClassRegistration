# -----------------------------------------------------------------------------
# Author: Meagan Swanson
# Date: December 6, 2019
#
# This module creates the Administrator class and the methods used by the main function in the
# Project2.py file for administrators to show class rosters and change
# maximum class sizes
# -----------------------------------------------------------------------------

from user import User


class Admin(User):

    def __init__(self, u_id, pin):
        base = super()
        base.__init__(u_id, pin)

    def show_roster(self, c_list):

        # ------------------------------------------------------------
        # Lists students in a course
        # Take one argument: course list
        # Displays number of students currently enrolled and their ID numbers
        # Returns no values.
        # ------------------------------------------------------------

        course_found = False
        code = str(input("Enter course: "))
        code.upper()

        for i in range(len(c_list)):
                if c_list[i].get_course_code() == code:
                    c_list[i].display_roster()
                    course_found = True

        if not course_found:
            print("Course not found")

    def change_max_size(self, c_list):

        # ------------------------------------------------------------
        # Changes maximum number of students that can enroll in a course
        # Takes one arguments: course list
        # Displays current enrollment size, current max size. Changes max size
        # as long as the new value is not smaller than the current enrollment size
        # Returns no values.
        # ------------------------------------------------------------

        course_found = False
        code = str(input("Enter course: "))
        code.upper()

        for i in range(len(c_list)):
                if c_list[i].get_course_code() == code:
                    c_list[i].change_max_size()
                    course_found = True

        if not course_found:
            print("Course not found")
