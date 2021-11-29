# -----------------------------------------------------------------------------
# Author: Meagan Swanson
# Date: December 6, 2019
#
# This module creates the base class User from which the student and admin classes are derived.
# Methods are developed to get user id and get user pin which are inherited by the derived classes.
# -----------------------------------------------------------------------------

class User:

    def __init__(self, u_id, pin):
        self.u_id = u_id
        self.pin = pin

    def get_id(self):
        # ------------------------------------------------------------
        # Obtain user ID number
        # Takes no arguments
        # Returns user ID number
        # ------------------------------------------------------------
        return self.u_id

    def get_pin(self):
        # ------------------------------------------------------------
        # Obtain user pin number
        # Takes no arguments
        # Returns pin number
        # ------------------------------------------------------------
        return self.pin
