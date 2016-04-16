#-------------------------------------------------------------------------------
# Name:        hellrungj
# Purpose:
#
# Created:     26/10/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from TreeNode import treenodes
def make_tree(open_file):
    "Sets up the tree"
    question = treenodes()                                                      #set the qusetion as part of the object
    current_node = question                                                     # set the current node for the question
    end = 0                                                                     #while loop breaker breaker
    while end == 0:
        line = open_file.readline()                                             #reads the line
        if line == " ":                                                         # an if statement that checks the line for if it is " "
            return False                                                        #ends the function with a return fo False if true
        if line == "Question:\n":                                               # an if statemnet that checks if the line has question in it to serches for question
            line = open_file.readline()                                         # read the line
            current_node.data = line                                            # makes the node for the root
            end = 1
    end = 0
    while end == 0:                                                             # Sets up the while in order to read the file
        line = open_file.readline()
        if line == "":                                                          # ends loop in the read line is equal file if " "
            end = 1                                                             # an if statement the check for questions
        if line == "Question:\n":
            line = open_file.readline()                                         # reads the line
            current_node.right = treenodes(line)                                     #creats a new note with the data and adress.
            current_node = current_node.right                                   #the right side of the node store the current line

        if current_node.left != None:
            if line == "Guess:\n":                                              # an if statemnet for serches for guess
                line = open_file.readline()                                     #reads the line
                current_node.right =  treenodes()                                    #creats the data and adress for the right part of the tree
                current_node.right.data = line
        if line == "Guess:\n":
            line = open_file.readline()
            current_node.left = treenodes()                                       #creats the letf part of the tree and creats the data and adress for the left part of the tree
            current_node.left.data = line
    return question                                                             #ends function with returning the question