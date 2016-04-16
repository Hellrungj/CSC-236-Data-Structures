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
from TreeNode import TreeNote

class Tree(object):
    def __init__ ( self):
            self.last = None
            self.root = None
            self.curent = None

    def set_head(self,value,left,right):
        self.root = TreeNote(value, left, right)
        self.curent = self.root
    def make_tree(self,listoflines):
        vaule = TreeNote.left
        print value
##        self.curent = TreeNote(value, left, right)



