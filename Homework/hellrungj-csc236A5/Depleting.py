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
from Pet import Pet

class Petneeds():
    def __inti__(self):
        """Updates the Pet"""
        self.mypet = pet()

    def cleanPet(self):
        """calls the pet function for creset in Pet"""
        return self.mypet.creset()

    def carePet(self):
        """calls the pet function for areset in Pet"""
        return self.mypet.areset()

    def feedPet(self):
        """calls the pet function for hreset in Pet"""
        return self.mypet.hreset()

    def dontcleanpet(self):
        """calls the pet function for cless in Pet"""
        self.mypet.cless()

    def dontcareforpet(self):
        """calls the pet function for aless in Pet"""
        self.mypet.aless()

    def dontfeedpet(self):
        """calls the pet function for fless in Pet"""
        self.mypet.fless()

