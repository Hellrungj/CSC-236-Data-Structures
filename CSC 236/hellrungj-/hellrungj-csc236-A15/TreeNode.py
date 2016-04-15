#-------------------------------------------------------------------------------
# Name:        hellrungj
# Purpose:
#
#
# Created:     26/10/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Acknowlegdements:
# sheltonk & calhounc
#-------------------------------------------------------------------------------

class treenodes:
    def __init__(self, data=None, left=None, right=None):
        "post: sets up the class varables"
        self.data = data                                                        # Consturts the self.data storage contaner for storing data in the node
        self.left = left                                                        # Consturts the self.left storage contaner for storing address to the next node
        self.right = right                                                      # Consturts the self.right storage contaner for storing address to the next node

    def add_question(self, right):
        "post: sets the question"
        self.right = treenodes()                                                # Allows the program to move to the node question data in self.right

    def add_left(self, left):
        "post: sets the left guess"
        self.left = left                                                        # Sets the guess data in self.right

    def add_right(self, right):
        "post: sets the right guess"
        self.right = right                                                      # Sets the question data in self.right

