#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hellrungj
#
# Created:     27/10/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class TreeNote(object):
    def __init__ (self, data, left, right):
            self.item = data
            self.left = left
            self.right = right
    def leftedge(self):
        return self.left

    def rightedge(self):
        return self.right
