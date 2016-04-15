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
from TreeNode import treenodes
from maketree import make_tree
import sys

def append_animal(filename):
    """Append the new question to the text file"""
    user_input1= str(raw_input("What is your animal?"))                         #gets now animal
    user_input2= str(raw_input("What is a question to tell the diffrience?"))   #gets new question
    open_file = open(filename, 'a')                                             # append the new item to the end of the file
    open_file.write("Question:\n")                                              #writes an idenifer for the program to find questions
    open_file.write(user_input2 +"\n")                                          # writes the user question
    open_file.write("no\n")                                                     # writes no like the rest of the file
    open_file.write("yes\n")                                                    # writes yes like the rest of the file
    open_file.write("\n")                                                       # make new line
    open_file.write("Guess:\n")                                                 # An identifer for the program to find guesses
    open_file.write(user_input1 +"\n")                                          # Writes the guess
    open_file.close()                                                           # close the file
    sys.exit()                                                                  #end the program

def main():
    """calls make the make tree part and the questions asking"""
    filename=raw_input("Input file: ")                                          #get file name for the the game.in text
    open_file = open(filename, 'r')                                             #open file for reading puruses
    index=0                                                                     # sets b as a varable for the of index counter
    while True:                                                                 # starts the program
        question = make_tree(open_file)                                         #calls make tree function
        current_node = question                                                 #sets current_node to equal question
        while True:
            if current_node.right == None:
                print current_node.data
                return False
            user_input = str(raw_input(current_node.data))                      #An if statement that checks if the user input is no
            Lowercase = user_input.lower()
            if Lowercase== 'n' or Lowercase == 'no':                          #An if statement that check if n or no to the question
                user_input = str(raw_input("Is you animal " +current_node.left.data+"?"))#input yes or no for question
                Lowercase = user_input.lower()
                if Lowercase == 'y' or Lowercase == 'yes':                    #An if statement that check if y or yes to the question
                    user_input=str(raw_input("Ha computer wins! Thank for playing. Do you wish to play again?"))#input need to be a yes or no for question
                    Lowercase = user_input.lower()
                    if Lowercase == 'y' or Lowercase == 'yes':                #An if statement that check if y or yes to the question
                        break                                                   #just this while loop
                    if Lowercase== "n" or Lowercase == "no":                  #An if statement that check if n or no to the question
                        sys.exit()                                              #ends program
                elif Lowercase=="n" or Lowercase == "no":                     #An if statement that check if n or no to the question
                    open_file.close()
                    append_animal(filename)
            elif Lowercase == "y" or Lowercase == "yes":                      #An if statement that checks if the user input is yes
                current_node = current_node.right
                index+=1
                if index>1:
                    user_input = str(raw_input("Is you animal " +current_node.right.data+"?"))
                    Lowercase = user_input.lower()
                    if Lowercase == 'y' or Lowercase == 'yes':
                        user_input=str(raw_input("Ha computer wins! Thank for playing. Do you wish to play again?"))
                        Lowercase = user_input.lower()
                        if Lowercase == 'y' or Lowercase == 'yes':
                            main()
                        if Lowercase== 'n' or Lowercase == 'no':
                            sys.exit()
                    if Lowercase=='n' or Lowercase == 'no':
                        open_file.close()
                        append_animal(filename)

if __name__ == '__main__':
    main()
