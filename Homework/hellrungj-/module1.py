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
from Tree import Tree
import time

def readfile():
    lines = []
    read = open("game2.txt","r")
    line=read.readline()
    while True:
        line = read.readline()
        print line
        lines.append(line)
        if len(line) == 0:
            break
    print lines
    read.close()
    Tree.set_head(lines[0],lines[1],lines[2]) #"set_head"
    Tree.make_tree(lines) #"Make the tree"


def main():
    readfile()

if __name__ == '__main__':
    main()
