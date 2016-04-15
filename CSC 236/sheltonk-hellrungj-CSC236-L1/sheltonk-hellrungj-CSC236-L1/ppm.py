##################################################################
'''
A module for loading and displaying PPM-P3 files using Python 2.7.6

This module reads an input PPM-P3 file in the constructor.
It never writes to the input file, instead creating two output files with
"-asc" and "-bin" respectively appended to the input filename.
These are intended for the user's use and for display respectively.

# The image data is stored in the following member variables:
self.magic
self.width
self.height
self.colormax
self.pixellist
# Update all of the above which change after manipulating image data.

# Constructor usuage:
df=PPM()
df=PPM("bc-flowers.ppm")

# Display image:
df.PPM_display()

# Change image by changing pixellist:
bc.PPM_updatefrompixellist(mylist)

# Written by Dr. Jan Pearce, Berea College

# Attributions:
    # Ben Stephenson: http://pages.cpsc.ucalgary.ca/~jacobs/Courses/cpsc217/W10/code/Topic7/ppm.py
    # working from a class: http://bytes.com/topic/python/answers/520360-trouble-displaying-image-tkinter
# You also need to acknowledge having modifed this code and all other code you modify or use for assitance.
#   To do so, you will indicate something like:
#   Mopidied from code written by Dr. Jan Pearce
#   Original code downloaded from:
#   http://cs.berea.edu/csc226/tasks/yourusername-A15.py and
#   http://cs.berea.edu/csc226/tasks/ppm.py
'''
##################################################################
import sys
import Tkinter as tk   # for display of the PPM image
import copy
import math
import random


root = tk.Tk() # for display
root.title("PPM Image")

class PPM_Exception(Exception):
    '''Create a Python class to enable meaningful error messages on exceptions.'''
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value) # allows a meaningful error message to be displayed

class PPM:
    '''Class which can be used to open, close, and display PPM P3 (ASCII) files.'''

    def __init__(self, inasciifile="default.ppm"):
        """ Opens or creates a PPM P3 file named inasciifile to construct a PPM object"""
        if inasciifile=="": # makes default.ppm as input file if none exists
            inasciifile="default.ppm"
        self.inasciifile=inasciifile # This file is used only for reading
        self.outasciifile=inasciifile[:-4]+"-asc.ppm" # created to store modifications
        self.outbinfile=inasciifile[:-4]+"-bin.ppm"  # binary ppm filename needed for viewing
        self.magic="P3" # ppm file type
        self.comment="# Created by ppm-class, by Dr. Jan Pearce\n"
        self.width=0
        self.height=0
        self.colormax=255 #should be set to 255
        self.ascii="" # will store the color intensities in P3 format
        self.pixellist = [] # will store nested list containing pixel colors
        self.image="" # It is necessary that this be a member variable for Tk to display image correctly
        self.source_text = []
        # if there is no filename given, make a file to work with
        if self.inasciifile=="default.ppm" :
            self.ascii='''P3
# Created by ppm-class, by Dr. Jan Pearce
8 10
255
140 140 140 120 120 120 100 100 100 80 80 80 60 60 60 40 40 40 20 20 20 0 0 0
120 120 120 63 72 204 63 72 204 63 72 204 63 72 204 252 252 255 255 255 255 15 15 15
105 105 105 255 255 255 63 72 204 255 255 255 63 72 204 255 255 255 255 255 255 30 30 30
90 90 90 255 255 255 63 72 204 63 72 204 63 72 204 255 255 255 255 255 255 45 45 45
75 75 75 255 255 255 63 72 204 255 255 255 63 72 204 63 72 204 63 72 204 60 60 60
60 60 60 63 72 204 63 72 204 63 72 204 63 72 204 255 255 255 63 72 204 75 75 75
45 45 45 255 255 255 255 255 255 63 72 204 255 255 255 254 254 254 255 255 255 90 90 90
30 30 30 255 255 255 255 255 255 63 72 204 255 255 255 255 255 255 63 72 204 105 105 105
15 15 15 252 252 253 255 255 255 63 72 204 63 72 204 63 72 204 63 72 204 120 120 120
0 0 0 20 20 20 40 40 40 60 60 60 80 80 80 100 100 100 120 120 120 140 140 140
'''
            tmpfile = open(self.inasciifile, "w")
            tmpfile.write(self.ascii)
            tmpfile.close()
        print("PPM object created from "+self.inasciifile)
        self.PPM_makeoutputfiles() # maskes ascii and binary output files

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def PPM_makeoutputfiles(self):
        '''given self.inasciifile, sets self.ascii and creates both ascii and binary files for output'''
        outtmpfile = open(self.outasciifile, "w")
        intempfile = open(self.inasciifile, 'r') # self.inasciifile must have data
        self.ascii = intempfile.read()
        outtmpfile.write(self.ascii)
        intempfile.close()
        outtmpfile.close()
        self.PPM_load(self.inasciifile)
        self.PPM_convert2bin()
        self.PPM_display()

    def PPM_partition(self,strng,ch):
        '''Given input parameters: strng, the string to partition and ch, the character to use as the delimiter
            Returns a triple with all characters before the delimiter, the delimiter iteself if present
            and all of the characters after the delimiter (if any)'''
        if (ch in strng):
            i = strng.index(ch)
            return (strng[0:i],strng[i],strng[i+1:])
        else:
            return (strng,None,None)

    def PPM_clean(self,strng):
        '''removes all singleline comments present in the input parameter string strng
        Returns a string with all characters after the comment character removed.
        All white space at the end is also removed, including the newline and linefeed characters.'''
        (retval,junk1,junk2) = self.PPM_partition(strng,"#")
        return retval.rstrip(" \t\n\r")

    def PPM_load(self, inasciifile):
        '''input parameter inasciifile is a string containing the name of the file to load
        Assumes an ASCII PPM-P3 (non-binary) file.
        loads the named image file from disk, and stores the image data in member variables'''

      # Open the input file
        infile = open(self.inasciifile,"r")

      # Read the magic number out of the top of the file and verify that we are
      # reading from an ASCII PPM-P3 file
        tmpln=infile.readline()
        self.ascii+=tmpln
        self.magic = self.PPM_clean(tmpln)
        if (self.magic != "P3"):
            raise PPM_Exception, 'The file being loaded does not appear to be a valid ASCII PPM-P3 file'

      # Get the image dimensions
        tmpln=infile.readline()
        while tmpln[0]=='#': #dump full comment lines
            tmpln=infile.readline()
        self.ascii+=tmpln
        imgdimensions = self.PPM_clean(tmpln)

      #unpack dimensions
        (width, sep, height) = self.PPM_partition(imgdimensions," ")
        self.width=int(width)
        self.height=int(height)
        if (self.width <= 0) or (self.height <= 0):
            raise PPM_Exception, "The file being loaded does not appear to have valid dimensions (" + str(width) + " x " + str(height) + ")"

      # Get the maximum color value, which is assumed to be 255
        tmpln=infile.readline()
        self.ascii+=tmpln
        self.colormax = int(self.PPM_clean(tmpln))
        if (self.colormax != 255):
            sys.stderr.write("Warning: PPM file does not have a maximum intensity value of 255.  Image may not be handled correctly.")

      # Create a list of the color intensities
        color_list = [] # hold intensity data temporarily in a list of intensity strings
        for line in infile:
            self.ascii+=line
            line = self.PPM_clean(line)
            color_list += line.split(" ")
        infile.close()  # Close input file since done
        self.PPM_makepixellist(color_list) # Creates self.pixellist, a nested list of rows of [red, green, blue] pixels

    def PPM_makepixellist(self, color_list):
      # Creates self.pixellist, a nested list of rows of [red, green, blue] pixels from a color_list which contains an unnested list of strings
        rcount=0
        gcount=1
        bcount=2
        self.pixellist = []
        for row in range(self.height):
            self.pixellist.append([])
            for col in range(self.width):
                self.pixellist[row].append([int(color_list[rcount]), int(color_list[gcount]), int(color_list[bcount])])
                rcount+=3 # move to next red
                gcount+=3  # move to next green
                bcount+=3  # move to next blue

    def PPM_updatefrompixellist(self, pixellist):
        '''Updates image object data and related files from input pixellist'''
        strout=""
        self.magic="P3"
        self.colormax=255
        self.width=len(pixellist[0])
        self.height=len(pixellist)
        header=self.magic+"\n"
        header+=self.comment
        header+=str(self.width) + " " + str(self.height)+"\n"+str(self.colormax)+"\n" # header is in ASCII
        for rowlist in pixellist:
            for pixel in rowlist:
                for color in pixel:
                    strout+=str(color)+" "
            strout+="\n"
        self.ascii=header+strout
        self.pixellist=pixellist
        tmpfile = open(self.outasciifile, "w")
        tmpfile.write(self.ascii)
        tmpfile.close() #close tmpfile when done
        print("PPM object changed based upon list.")
        self.PPM_convert2bin()
        self.PPM_display()

    def PPM_convert2bin(self):
        '''Converts PPM-P3 to PPM-P6 using self.pixellist'''
        header="P6\n"
        header+=self.comment
        header+=str(self.width) + " " + str(self.height)+"\n"+"255\n" # header is in ASCII
        strout=""

        for rowlist in self.pixellist:
            for pixel in rowlist:
                for color in pixel:
                    strout+=chr(color) # Python 2 uses strings to handle binary data, chr() converts the integer to a one-byte string.

        strout=header+strout+'\n'
        tmpfile = open(self.outbinfile, "wb")
        tmpfile.write(strout)
        tmpfile.close() #close tmpfile when done

    def PPM_display(self):
        '''displays PPM-P3 binary file using Tkinter'''
        #root.title("PPM Image")
        self.image = tk.PhotoImage(file=self.outbinfile) # needed for retaining image after call
        label = tk.Label(root, image=self.image)
        label.pack()


    def gets_string(self, input_str):
        ''' Opens a file by the name of input_str (eg. "crytogram.txt") and reads the contents
    	one line at a time, appending what it read to source_text as it goes along with the ASCII values into a list.
    	'''
        ASCII_value={" ": 32,"A":65, "B":66,"C":67,"D":68, "E":69,"F":70,"G":71,
        "H":72, "I":73, "J":74, "K":75, "L":76, "M":77, "N":78, "O":79, "P":80,
        "Q":81, "R":82, "S":83, "T":84, "U":85, "V":86, "W":87, "X":88, "Y":89,
        "Z":90, "a":97, "b":98, "c":99, "d":100, "e":101, "f":102, "g":103, "h":104,
        "i":105, "j":106, "k":107, "l":108, "m":109, "n":110, "o":111, "p":112,
        "q":113, "r":114, "s":115, "t":116, "u":117, "v":118, "w":119, "x":120,
        "y":121, "z":122} #The ASCII Libary.
        open_file = file(input_str, "r")
        next_line = open_file.readline()
        open_file.close()
        for i in next_line:
            if i == "\n":
                pass
            else:
                self.source_text.append(ASCII_value[i])
        return self.source_text

    def PPM_encode_red(self):
        ''''encodes red with the ASCII values and changes green to confuse a hacker'''
        times = 0
        newpixellist=self.pixellist
        self.width=len(newpixellist[0])
        self.height=len(newpixellist)
        Text = self.source_text
        print Text
        i = 0
        row=0
        for rowlist in newpixellist:
            col=0
            for pixel in rowlist:
                Code = Text[i]
                print Code
                newpixellist[row][col][0] = int(Text[i])# update red with the ASCII values
                newpixellist[row][col][2] = random.randint(1,255) #update green to confuse hackers
                col+=1
                if i < len(Text):
                    i += 1
                    if i == len(Text):
                        print "done"
                        i = 0
                        times += 1
            row+=1
        print(self.outasciifile+ " output file turned red and incoded.")
        print times
        return self.PPM_updatefrompixellist(newpixellist) # This call will update all member apttributes appropriately.

    def decode(self):
        '''Decodes the red back to ASCII values'''
        decodetext = []
        newpixellist=self.pixellist
        self.width=len(newpixellist[0])
        self.height=len(newpixellist)
        Text = ""
        i = 0
        row=0
        for rowlist in newpixellist:
            col=0
            for pixel in rowlist:
                Text = newpixellist[row][col][0]# getting the ASCII values out of the red
                col+=1
                decode_letter = chr(int(Text)) # getting the ASCII values into a list to be printed
                decodetext.append(decode_letter)
            row+=1
        print(self.outasciifile+ " output file turned red and incoded.")
        return decodetext



#bc=PPM("bc-flowers.ppm")

#root.mainloop() # needed for Tkinter--either uncomment here or put at bottom of user program file.


