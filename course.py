# -----------------------------------------------------------------------------
# Author: Meagan Swanson
# Date: December 6, 2019
#
# This module creates the Course class and the methods used by the program
# to add and drop students from a course, display rosters, change max class sizes,
# display course rosters, get course code, and determine if a student is enrolled in a course.
# -----------------------------------------------------------------------------

class Course:

    def __init__(self, c_code, m_size):
        self.c_code = c_code
        self.m_size = m_size
        self.roster = []

    def add_student(self, s_id):

        # ------------------------------------------------------------
        # Add student to a course roster
        # Take one argument: student ID number
        # Displays course already full or already enrolled in
        # course if unable to add course. Otherwise, adds student to roster list for course.
        # Returns no values.
        # ------------------------------------------------------------

        if len(self.roster) == self.m_size:
            print("Course already full")
        elif s_id in self.roster:
            print("You are already enrolled in this course")
        else:
            self.roster.append(s_id)
            print("Student", s_id, "added to", self.c_code)

    def drop_student(self, s_id):

        # ------------------------------------------------------------
        # Remove student from a course roster
        # Take one argument: student ID number
        # Displays not enrolled in course if unable to drop course.
        # Otherwise, removes student from roster list for course.
        # Returns no values.
        # ------------------------------------------------------------

        if s_id not in self.roster:
            print("You are not enrolled in this course")
        else:
            self.roster.remove(s_id)
            print("Student", s_id, "removed from", self.c_code)

    def display_roster(self):

        # ------------------------------------------------------------
        # Lists students in a course
        # Take no arguments
        # Displays number of students currently enrolled and their ID numbers
        # Returns no values.
        # ------------------------------------------------------------

        self.roster.sort()

        for x in range(len(self.roster)):
            print(self.roster[x])

        print("Number of students:", len(self.roster))

    def change_max_size(self):

        # ------------------------------------------------------------
        # Changes maximum number of students that can enroll in a course
        # Takes no arguments
        # Displays current enrollment size, current max size. Changes max size
        # as long as the new value is not smaller than the current enrollment size
        # Returns no values.
        # ------------------------------------------------------------

        print("Current enrollment:", len(self.roster))
        print("Current max size:", self.m_size)

        x = 0
        while x == 0:
            new_size = int(input("Enter new size: "))
            if new_size < len(self.roster):
                print("New max size cannot be smaller than current enrollment")
                continue
            else:
                self.m_size = new_size
                break

    def get_course_code(self):

        # ------------------------------------------------------------
        # Obtain course code
        # Takes no arguments
        # Returns course code
        # ------------------------------------------------------------

        return self.c_code

    def student_in_course(self, s_id):

        # ------------------------------------------------------------
        # Determines what students are in a course
        # Takes one argument: s_id
        # Returns the student IDs of enrolled students in a course
        # ------------------------------------------------------------

        return s_id in self.roster
