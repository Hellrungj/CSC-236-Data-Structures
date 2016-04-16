######################################################################
#   Lab L1: Steganography
#   Your names: Kenan Shelton, John Hellrug
#   Contributions: navigator and driver: Kenan, driver and navigator:John
#   Purpose: to encode a picture with ASCII values of letters and decrypts them
#  Acknowledgments: Angie Lee for the chr assigment to decode easly
######################################################################
# Acknowledgements:
    # Ben Stephenson: http://pages.cpsc.ucalgary.ca/~jacobs/Courses/cpsc217/W10/code/Topic7/ppm.py
    # working from a class: http://bytes.com/topic/python/answers/520360-trouble-displaying-image-tkinter

# You need to acknowledge having modifed this code and all other code you modify or use for assitance.
#   To do so, you will indicate something like:
#   Mopidied from code written by Dr. Jan Pearce
#   Original code downloaded from:
#   http://cs.berea.edu/csc226/tasks/yourusername-A15.py and
#   http://cs.berea.edu/csc226/tasks/ppm.py
######################################################################




from ppm import *
# Be sure you work with a single ppm object at a time

# The following interaction is just for testing.  You will improve this.
filename=raw_input("Please input name of PPM-P3 file:")#Gets the name of the ppm file
ppmobject=PPM(filename)#gets the original pixical list form the ppm file.
#ppmobject=PPM() also works

edits=raw_input("do want to incode a text in your pic?")#Asks if you want to encode a txt file
if edits=='y' or edits=='Y':
    File=raw_input("What text file do you want to incode?")#gets the txt file's name
    ppmobject.gets_string(File)#calls the fuction to get the ASCII values of the txt file
    ppmobject.PPM_encode_red()#encodes the picture

de=raw_input("Do you want to decode? enter y for yes.")#asks if you want to decode it
if de=="y":
    password= raw_input('What is thy favorite color?')#ask for a password
    if password=="Firetruck Red":
        print ppmobject.decode()#decodes the picture and ASCII values back into text

root.mainloop() #needed to use Tkinter with the ppm class