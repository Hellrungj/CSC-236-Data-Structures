#-------------------------------------------------------------------------------
# Name:        hellrungj
# Purpose:  This sample function opens a file with the name words_file_name
#   reads the text, converts everything to lowercase and returns a list
#   of the words.
#
# Author:       various online sources cited in the comment above function
# Synthesized:  nakazawam
#
# Created:     25/08/2014
#-------------------------------------------------------------------------------
#Acknowledgments:
#Jan Perice, Mario Nakazawa, Quinten Lambert, Gerado Ivan Santos, and Xhafer Rama
#-------------------------------------------------------------------------------
import time
## This function is adapted from
##  http://stackoverflow.com/questions/13259288/returning-a-list-of-words-after-reading-a-file-in-python
## with exception handling built into it. Also integrated is a method to
## strip punctuation usingideas/code from
##      http://stackoverflow.com/questions/19414161/removing-punctuation-in-lists-in-python
def read_words(words_file_name):
    '''This function opens a file with the name in 'words_file', reads in
    the contents and returns a list of the words, stripped of whitespace.
    pre: none, as this function handles IOError for when the file is not there gracefully
    post: returns the list of words in the file, which is empty on an open fail. '''
    words_list =[]
    try:
        open_file = open("gettysburg.txt", 'r')
        contents = open_file.readlines()

        # replace punctuation with a blank space
        punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
        for i in punctuation:
            for j in range(len(contents)):
                contents[j] = contents[j].replace(i,"")

        for i in range(len(contents)):
            contents[i].lower()
            words_list.extend((contents[i].lower()).split())
        open_file.close()
    except IOError:
        print("File does not exist! Try again.")
    return words_list

def main():
    """Is the main function that run everything"""
    input_words = read_words("test2.txt")
    #print(input_words)

def linearSeach(x, target):
    """Does a linear seach thought a list for a target word"""
    Add = 0
    for i in x:
        if i == target: #adds one to add each time the target word is located
            Add = Add + 1
    return ("Times shown " + str(Add) + ".")

def binarySeach(x, target):
    """Does a binary seach thought a list for a target word"""
    x.sort() #Sorts the list which is x
    low = 0
    high = len(x) -1
    Wordtimes = 0
    while low <= high:
        mid = (low + high) // 2 #finds the midium # and set it to the variable "mid"
        item = x[mid] #set the sting of the indexed number based on the indexed numder location in hte list
        if target == item:
            Wordtimes = Wordtimes + 1
            x.remove(item) #remove the item founded so we can contiune looking
        elif target < item:
            high = mid -1 #moves the high bound
        else:
            low = mid +1 #moves the low bound
    return ("Times shown " + str(Wordtimes) + ".")

word = raw_input("What word are you searching?") #The program asks the user what he or she wants.

if __name__ == '__main__': #runs the main program
    main()
    T1_start = time.time() #Set T1_start to the current time
    print linearSeach(read_words("test2.txt"), str(word))
    T1_stop = time.time() #Set T1_stop to the current time
    T1 = T1_stop - T1_start #Subatacts the T1_start and T1_stop to find the time passed
    print str("The word "+ str(word) + " took " + str(T1) + " to search in the linear function.") #print out a statement to the user
    T2_start = time.time() #Set T1_start to the current time
    print binarySeach(read_words("test2.txt"), str(word))
    T2_stop = time.time() #Set T1_stop to the current time
    T2 = T2_stop - T2_start #Subatacts the T1_start and T1_stop to find the time passed
    print str("The word "+ str(word) + " took " + str(T2) + " to search in the binary function.") #print out a statement to the user
