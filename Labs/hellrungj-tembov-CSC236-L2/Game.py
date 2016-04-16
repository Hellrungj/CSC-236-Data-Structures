#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hellrungj
#
# Created:     06/10/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
import time
from Stack import Stack

class Map:
    direction = Stack()
    def __init__ (self, filename = raw_input("Type in the name of your document")): #fileame = raw_input("Type in the name of your document")):
        self.readingfile = str(filename)
        self.textlist=[]
        self.me_r = 0
        self.me_c = 0
        self.money = 0
        self.rope = Stack()
        self.Key = False

    def make_map(self):
        """Makes the map"""
        open_file = open(self.readingfile, 'r')
        next_line = open_file.readlines()
        indexcolum= 0
        for i in next_line:
            indexrow = 0
            row = []
            for x in i:
                if x == "W" or x == "T" or x == "." or x == "M":
                    if x == "M":
                        self.me_c = indexcolum
                        self.me_r = indexrow
                        row.append(x)
                    else:
                        row.append(x)
                        indexrow += 1
            if len(row) > 0:
                self.textlist.append(row)
                indexcolum += 1
            else:
                pass #maybe need it maybe not?
        print self.textlist

    def random_location(self, N,S,W,E):
            """Choices a random location"""
            i = False
            while i == False:
                i = random.choice([N,S,W,E])
            trans = {N:"N", S:"S", W:"W", E:"E"}
            if trans[i] == "N":
                self.tracking()
                self.me_r = int(self.me_r) + 1
            elif trans[i] == "S":
                self.tracking()
                self.me_r = int(self.me_r) - 1
            elif trans[i] == "E":
                self.tracking()
                self.me_c = int(self.me_c) + 1
            elif trans[i] == "W":
                self.tracking()
                self.me_c = int(self.me_c) -1
            else:
                print "Error"

    def Treasure(self): # looks for "T"
        """Checks for treasure and adds it the player money"""
        Treasure = self.money
        if self.textlist[self.me_c][self.me_r] == "T":
            Treasure += 1
            print "You found Treasure!"
        print Treasure
        self.money = Treasure

    def tracking(self):
        """Places a a rope cornet on the stack"""
        self.rope.push(self.textlist[self.me_c][self.me_r])
        self.textlist[self.me_c][self.me_r]= "*"

    def back_tracking(self):
        """check if the player is lost and removes the stars while moveing the player back"""
        rope = self.rope.pop(self.textlist[self.me_c][self.me_r])
        return rope

    def run(self):
        """Runs the whole game"""
        self.make_map()
        Map = self.textlist
        while self.money != 1:
            print "#------------------------------------"
            self.Movement()
            self.textlist[self.me_c][self.me_r] = "M"
            self.Treasure()
            time.sleep(3)
            print self.textlist

    def Movement(self): # Moves the char
        """Makes the states for the player"""
        NW = self.me_r + 1 # gives the location of the walls North
        EW = self.me_c + 1 # Right
        WW = self.me_c - 1 # left
        SW = self.me_r - 1 # south
        #------- Checks for walls
        if self.textlist[self.me_c][NW] == "W":
            North = True
        else:
            North = False
        if self.textlist[EW][self.me_r] == "W":
            East = True
        else:
            East = False
        if self.textlist[WW][self.me_r] == "W":
            West = True
        else:
            West = False
        if self.textlist[self.me_c][SW] == "W":
            South = True
        else:
            South = False
        #-------
        if self.textlist[self.me_c][NW] == "*":
            North_AST = True
        else:
            North_AST = False
        if self.textlist[EW][self.me_r] == "*":
            East_AST = True
        else:
            East_AST = False
        if self.textlist[WW][self.me_r] == "*":
            West_AST = True
        else:
            West_AST = False
        if self.textlist[self.me_c][SW] == "*":
            South_AST = True
        else:
            South_AST = False
#-------------------------------------------------------------------------------
        #Moves if there is one opening and three walls
        if South == False and West == False and East == False:
            # Moves north
            if North_AST == True:
                # make function for backtrack
                self.back_tracking()
            else:
                self.tracking()
                self.me_r += self.me_r + 1
        elif South == True and West == False and North == False:
            # Moves East
            if East_AST == True:
                # make function for backtrack
                self.back_tracking()
            else:
                self.tracking()
                self.me_c = self.me_c + 1
        elif South == False and East == False and North == False:
            #Moves West
            if West_AST == True:
                # make function for backtrack
                self.back_tracking()
            else:
                self.tracking()
                self.me_c = self.me_c - 1
        elif West == False and East == False and North == False:
            #Moves South
            if South_AST == True:
                # make function for backtrack
                self.back_tracking()
            else:
                self.tracking()
                self.me_r = self.me_r - 1
#------------------moves if there are two opening and two walls-----------------
        elif North == False and South == False:
            if West_AST == True and East_AST == True:
                # make function for backtrack
                self.back_tracking()
            elif West_AST == True:
                 #Moves to the East
                self.tracking()
                self.me_c = self.me_c + 1
            elif East_AST == True:
                #Moves to the West
                self.tracking()
                self.me_c = self.me_c - 1
            else:
                #goes to random spot: South or North
                self.tracking()
                N = False
                S = False
                W = True
                E = True
                self.random_location(N,S,W,E)
        elif East == False and West == False:
            if North_AST == True and South_AST == True:
                # make function for backtrack
                self.back_tracking()
            elif South_AST == True:
                 #Moves to the North
                self.tracking()
                self.me_r = self.me_r + 1
            elif North_AST == True:
                #Moves to the South
                self.tracking()
                self.me_r = self.me_r - 1
            else:
                #goes to random spot: North or South
                self.tracking()
                N = True
                S = True
                W = False
                E = False
                self.random_location(N,S,W,E)
        elif North == False and East == False:
            if South_AST == True and West_AST == True:
                # make function for backtrack
                self.back_tracking()
            elif South_AST == True:
                 #Moves to the East
                self.tracking()
                self.me_c = self.me_c - 1
            elif East_AST == True:
                #Moves to the South
                self.tracking()
                self.me_r = self.me_r - 1
            else:
                #goes to random spot: East or South
                self.tracking()
                N = False
                S = True
                W = False
                E = True
                self.random_location(N,S,W,E)
        elif South == False and West == False:
            if North_AST == True and East_AST == True:
                # make function for backtrack
                self.back_tracking()
            elif North_AST == True:
                 #Moves to the West
                self.tracking()
                self.me_c = self.me_c - 1
            elif West_AST == True:
                #Moves to the North
                self.tracking()
                self.me_r = self.me_r + 1
            else:
                #goes to random spot: West or North
                self.tracking()
                N = False
                S = False
                W = True
                E = True
                self.random_location(N,S,W,E)
#---------------Moves if there is one wall and three opening!-----------------------------------
#-0000000000000000000000000000000000000000000000000000000000000
        elif North == False and West == False and East == False: # south Wall
            if North_AST == True and West == True and East_AST == True:
                # make function for backtrack
                self.back_tracking()
            elif North_AST == True and West_AST == True:
                #goes East
                self.tracking()
                self.me_c = self.me_c + 1
            elif North_AST == True and East_AST == True:
                #goes West
                self.tracking()
                self.me_c = self.me_c - 1
            elif West_AST == True and East_AST == True:
                #goes North
                self.tracking()
                self.me_r = self.me_r + 1
            elif North_AST == True:
                # Goes to a random spot: East or West
                self.tracking()
                N = False
                S = False
                W = True
                E = True
                self.random_location(N,S,W,E)
            elif East_AST == True:
                # goes to a random spot: North or West
                self.tracking()
                N = True
                S = False
                W = True
                E = False
                self.random_location(N,S,W,E)
            elif West_AST == True:
                # goes to a random spot: East or North
                self.tracking()
                N = True
                S = True
                W = False
                E = True
                self.random_location(N,S,W,E)
            else:
                # goes to a random spot: North or East or West
                self.tracking()
                N = True
                S = False
                W = True
                E = True
                self.random_location(N,S,W,E)
        elif West == False and East == False and South == False: # north wall
            if West_AST == True and East_AST == True and South_AST == True:
                # make function for backtrack
                self.back_tracking()
            elif West_AST == True and East_AST == True:
                #goes South
                self.tracking()
                self.me_r = self.me_r - 1
            elif West_AST == True and South_AST == True:
                #goes East
                self.tracking()
                self.me_c = self.me_c + 1
            elif East_AST == True and South_AST == True:
                #goes West
                self.tracking()
                self.me_c = self.me_c - 1
            elif South_AST == True:
                # Goes to a random spot: East or West
                self.tracking()
                N = False
                S = False
                W = True
                E = True
                self.random_location(N,S,W,E)
            elif East_AST == True:
                # goes to a random spot: South or West
                self.tracking()
                N = False
                S = True
                W = True
                E = False
                self.random_location(N,S,W,E)
            elif West_AST == Ture:
                # goes to a random spot: South or East
                self.tracking()
                N = False
                S = True
                W = False
                E = True
                self.random_location(N,S,W,E)
            else:
                # goes to a random spot: South or East or West
                self.tracking()
                N = False
                S = True
                W = True
                E = True
                self.random_location(N,S,W,E)
        elif North == False and East == False and South == False: # West wall
            if North_AST == True and East_AST == True and South_AST == True:
                # make function for backtrack
                back_tracking()
            elif North_AST == True and East_AST == True:
                #goes South
                self.tracking()
                self.me_r = self.me_r - 1
            elif North_AST == True and South_AST == True:
                #goes East
                self.tracking()
                self.me_c = self.me_c + 1
            elif East_AST == True and South_AST == True:
                #goes North
                self.tracking()
                self.me_r = self.me_r + 1
            elif South_AST == True:
                # Goes to a random spot: North or East
                self.tracking()
                N = True
                S = False
                W = False
                E = True
                self.random_location(N,S,W,E)
            elif East_AST == True:
                # goes to a random spot: North or South
                self.tracking()
                N = True
                S = True
                W = False
                E = False
                self.random_location(N,S,W,E)
            elif North_AST == Ture:
                # goes to a random spot: South or East
                self.tracking()
                N = False
                S = True
                W = False
                E = True
                self.random_location(N,S,W,E)
            else:
                # goes to a random spot: North or South or East
                self.tracking()
                N = True
                S = True
                W = False
                E = True
                self.random_location(N,S,W,E)
        elif North == False and West == False and South == False: # East wall
            if North_AST == True and West_AST == True and South_AST == True:
                # make function for backtrack
                self.back_tracking()
            elif North_AST == True and West_AST == True:
                #goes South
                self.tracking()
                self.me_r = self.me_r - 1
            elif North_AST == True and South_AST == True:
                #goes West
                self.tracking()
                self.me_c = self.me_c - 1
            elif West_AST == True and South_AST == True:
                #goes North
                self.tracking()
                self.me_r = self.me_r + 1
            elif South_AST == True:
                # Goes to a random spot: North or West
                self.tracking()
                N = True
                S = False
                W = True
                E = False
                self.random_location(N,S,W,E)
            elif North_AST == True:
                # goes to a random spot: West or South
                self.tracking()
                N = False
                S = False
                W = True
                E = True
                self.random_location(N,S,W,E)
            elif West_AST == True:
                # goes to a random spot: North or South
                self.tracking()
                N = True
                S = True
                W = False
                E = False
                self.random_location(N,S,W,E)
            else:
                # goes to a random spot: North or South or West
                self.tracking()
                N = True
                S = True
                W = True
                E = False
                self.random_location(N,S,W,E)
#-----------------All sides open and All sides closed---------------------------
        elif North == False and South == False and East == False and West == False:
            # goes to a random spot: North or South or West or South
            if North_AST == True and South_AST == True and East_AST == True and West_AST == True:
                #There is none but rope around you go back.
                self.back_tracking()
            elif North_AST == True or South_AST == True or East_AST == True:
                #goes West
                self.tracking()
                self.me_c = self.me_c - 1
            elif North_AST == True or South_AST == True or West_AST == True:
                #goes East
                self.tracking()
                self.me_c = self.me_c + 1
            elif South_AST == True or West_AST == True or East_AST == True:
                #goes North
                self.tracking()
                self.me_r = self.me_r + 1
            elif North_AST == True or West_AST == True or East_AST == True:
                #goes South
                self.tracking()
                self.me_r = self.me_r - 1
            elif North_AST == True or South_AST == True:
                # goes to a random spot: West or East
                self.tracking()
                N = False
                S = False
                W = True
                E = True
                self.random_location(N,S,W,E)
            elif East_AST == True or West_AST == True:
                # goes to a random spot: North or South
                self.tracking()
                N = True
                S = True
                W = False
                E = False
                self.random_location(N,S,W,E)
            elif North_AST == True or East_AST == True:
                # goes to a random spot: South or West
                self.tracking()
                N = False
                S = True
                W = True
                E = False
                self.random_location(N,S,W,E)
            elif South_AST == True or West_AST == True:
                # goes to a random spot: North or East
                self.tracking()
                N = True
                S = False
                W = False
                E = True
                self.random_location(N,S,W,E)
            elif North_AST == True:
                # goes to a random spot: South or East or West
                self.tracking()
                N = False
                S = True
                W = True
                E = True
                self.random_location(N,S,W,E)
            elif South_AST == True:
                # goes to a random spot: North or East or West
                self.tracking()
                N = True
                S = False
                W = True
                E = True
                self.random_location(N,S,W,E)
            elif West_AST == True:
                # goes to a random spot: North or East or South
                self.tracking()
                N = True
                S = True
                W = False
                E = True
                self.random_location(N,S,W,E)
            elif East_AST == True:
                self.tracking()
                N = True
                S = True
                W = True
                E = False
                self.random_location(N,S,W,E)
                # if there is a rope to the East:
                #goes to a random spot: South or North or West
            else:
                self.tracking()
                N = True
                S = True
                W = True
                E = True
                self.random_location(N,S,W,E)
                #goes to a random spot: South or North or West or North
#--------------------------------If there are just walls------------------------
        else:
            print "You are traped with no other ways to go forward expect for a way back up the hole of the cave. Sorry, Game over!"