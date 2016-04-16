#-------------------------------------------------------------------------------
# Name:        John Hellrung
# Purpose:
#
# Author:      hellrungj
#
# Created:     03/09/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Pet(object):
    """Creates the Pet"""
    def __init__(self):
        """Create the Pet's Addturebes"""
        self.feed = 0
        self.clean =0 #The issuse with my code is that it doesn't want to run becuase the code act like it doesnt make
        self.attention = 0 #class Attrbites as an object. It give the error not found when I run the __str__ function of
        #the class. I dont understand why the class does that.

#-------------------------------------------------------------------------------
    def hunger(self):
        """Displays the Pet's hunger"""
        return self.pet
#------------------------------------------------------------------------------
    def hless(self):
        """Subattracts one to the clean level"""
        self.pet[0] = self.pet[0] - 1
        return self.cleanliness

    def cless(self):
        """Subattracts one to the affection level"""
        self.pet[1] = self.affection - 1
        return self.affection

    def aless(self):
        """Subattracts one to the hunger level"""
        self.pet[3] = self.pet[2] - 1
        return self.hungerlevel
#-------------------------------------------------------------------------------
    def hreset(self):
        """resets to the clean level"""
        self.pet[0] =  self.pet[0] + 1
        return self.pet[0]

    def creset(self):
        """resets one to the affection level"""
        self.pet[1] =  self.pet[1] + 1
        return self.pet[1]

    def areset(self):
        """rests one to the hunger level"""
        self.pet[2] =  self.pet[2] + 1
        return self.pet[2]
#-------------------------------------------------------------------------------
    def petshealth(self):
        """pets health"""
        if  self.feed == -1:
            return "dead"
        else:
            return "living"


    def __str__(self):
        """Allows the class to print a string which informs the user"""
        return str(self.petshealth())


