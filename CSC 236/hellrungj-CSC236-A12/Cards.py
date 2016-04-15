#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hellrungj
#
# Created:     02/10/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Stack import Stack

class Cards:
    def __init__ (self):
        """"""
        self.card = 0
        self.deck = (0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,8,8,8,8,8,9,9,9,9,9,10,10,10,10,10)
    def make_deck(self):


    def __str__(self):
        """Prints the cards"""
        return self.suit



Card = Cards()
Card.rank()