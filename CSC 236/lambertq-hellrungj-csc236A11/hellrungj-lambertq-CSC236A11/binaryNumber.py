#-------------------------------------------------------------------------------
# Name:        binaryNumber.py
# Purpose:  A linked list implementation of a binary number.
#
# Author:      Assignment concept by pearcej, converted to Python by nakazawam
#
# Editors: John Hellrung & Ivan Santos (USERNAMES :hellrungj & santosg)
# Created:     21/09/2014
#-------------------------------------------------------------------------------
# Acknowlegdements:
# Matt Jadud, Bria Williams, Mario Nakazawa
#-------------------------------------------------------------------------------

from bit import Bit

class BinaryNumber(object):

    #------------------------------------------------------------

    def __init__( self ):
        '''Initialize this binary number is empty  with no bits in it.'''
        self.leastSignificantBit = None
        self.numBits = 0

    def __len__(self):
        '''post: returns number of items in the list'''
        return self.numBits

    def get_least_significant_bit( self ):
	    return self.leastSignificantBit

    def convert_decimal_to_binary( self, decimal ):
        '''pre: The decimal input >= 0, leastSignificantBit = None
            If there IS a number in this object already, it will be clobbered.
        post: leastSignificantBit will point to the first link
        of a linked list representing the "decimal" number in reverse
        order (least to most significant bit)'''

        if( decimal < 0 ):
            return

        # Now use an algorithm to convert a decimal number to binary.
		# Repeatedly divide the number by 2 and keep the remainder.
        # It will build the binary number this way.

		# Start the process with the first binary number.
        if decimal%2 == 1:
            self.leastSignificantBit = Bit(True)
        else:
            self.leastSignificantBit = Bit(False)
        self.numBits += 1

        # Now loop through the decimal and convert to binary.
        bitRef = self.leastSignificantBit
        remainder = 0
        quotient = decimal/2

        while quotient > 0:
            remainder = quotient % 2
            quotient = quotient / 2

            bitRef.add_next_bit( remainder == 1 )
            bitRef = bitRef.get_next_bit()	# Advance the reference
            self.numBits += 1

    def __str__( self ):
        ''' returns the string representation of this binary number.
        post: The string representation of this BinaryNumber will be returned.
            if there is no linked list, a blank string, "" is returned '''
        bitRef = self.leastSignificantBit
        output = ""

        if( bitRef == None ):
            return output

        for i in range(self.numBits):
            output = str(bitRef)+output
            bitRef = bitRef.get_next_bit()
        return output

    def remove_all( self ):
        '''pre: none
        post: All the links in the linked list started by leastSignificantBit
            will be de-allocated.'''

        if( self.leastSignificantBit == None ):
            return

        trailingBit = self.leastSignificantBit
        leadingBit = trailingBit.get_next_bit()

        for i in range(self.numBits-1):
            trailingBit.clear_next_bit()
            trailingBit = leadingBit
            leadingBit = leadingBit.get_next_bit()

        self.leastSignificantBit = None
        self.numBits = 0

    # You are to implement this function that will increment the binary
    # number stored in a linked list by one, making sure to propogate any
    # carries that are generated.

    # For example, if the number 15 is stored as "1111" and this
    # function is called,the result would be "10000" (really
    # represented as 0->0->0->0->1, where the carry "rippled" up the
    # bits, and an additional bit was added at the end because the 4th
    # 1 really became a "10"
    def increment( self ):
        """This function is to increment the binary bits by one increment"""
        """ Helped by Matt Jadud; with assistance by Bria Williams
            and inception by Mario Nakazawa """
        aBit = self.leastSignificantBit #aBit is set to the method in a class called "self.leastSignificantBit"
        carry = 1
        cout = 0
        N = self.numBits
        print "The next thing is N"
        print N                  # sets a varable for increment the binary
        while (aBit != None):       # a while loop that runs until the varble of "aBit" does equal None
            value = aBit.get_bit()  # set the vaule of "value" to "aBit.get_bit()". This method retruns the vaule of the node.
            cout += 1
            print str(cout) + "N"
            if value == True:       # An if statemnet that checks to see if "value" is equal to boolean value of "True".
                value = 1           # change the value to one
            else:                   # else ! (if the value of "value" is equal to one)
                value = 0           # change the value to zero
            new_value = value + carry # set the the value of "value" plus the value of "carry" to the value of "new_value"
            if new_value == 2:        # An if statement thatt checks to see i fthe value of "new_value" is equal to the intiger of two
                aBit.set_bit(0)       # Sets the current node value to zero. (sets the bit to zero)
                carry = 1             # Set the value of "carry" to one
            elif new_value == 1:      # if the value of "new_value" is equal to the intiger of one
                carry = 0             # set the carry to zero
                aBit.set_bit(1)       # sets the current node value to one. (sets the bit to one)
            else: #if  zero           # else! (if the value of new_value equal the intiger of zero.)
                carry = 0             # set the carry to zero
                #leave it alone
            aBit = aBit.get_next_bit()   # sets the the node called "aBit" to the next binary note. Moving the loop forrward thorught the linked list
##        if carry == 1:            # An if statement that checks to see if the value of carry is equal to the intiger of one
##            aBit.add_next_bit(carry) # Set the value of "carry" to the next bit. (Creating a  new Bit)
##        elif carry == 0:
##            print"NO"

#===============================================================================
# Name: John Hellrung & Quiten Lambert (hellrungj & lambertq)
# Ackknolgement:
# Kye Hoover, Ivan Santos, Bria Williams, Kristan Toole.
#-------------------------------------------------------------------------------

    def add(self, binary_1):
        """Adds the binary1 and binary2 and sets the answer to problem as self"""
#-------------------------------------------------------------------------------
        def TorF_Conv(value):
            """Sets the value of True or False to an int of 1 or 0"""
##            print str(6) + "C"
            if value == True: #logic saying that if value of "value" equal True then return 1 else return 0
                value = 1
                return value
            else:
                value = 0
                return value
        def length(bit):
            """finds the lenght of the bit numbers"""
            add = 0  # sets a varable to zero
            while bit != None: # loops until the node equal None
                add += 1 #add one to the varable named "add"
                bit = bit.get_next_bit() #then moves the node to the next value
            return add # after the loops done returns the varable "add"
        def reString(List):
            """Rearainages the list"""
            String = [] # makes a open list
            I = 1  # sets I to 1
            for i in List:#loop as manys times as their are items in List.
                X = len(List)-I # sets 'X' to lenght of lenght subattart by 1
                String.append(List[X])#then appends "List" index by "X"
                I += 1 # adds one to "I"
            return String #returns list named String
#-------------------------------------------------------------------------------
        b1 = binary_1.leastSignificantBit #sets b1 to the leastSignificantBit or bit_ref zero
        b2 = self.leastSignificantBit  #sets b1 to the leastSignificantBit or bit_ref zero
##        print str(1) + "C"
        VL = length(b1)  #finds the lenght of the linked list "b1"
##        print str(2) + 'A'
##        print VL
        VL2 = length(b2)  #finds the lenght of the linked list "b2"
##        print str(2) + 'B'
##        print VL2
##        print str(3) + "C"
        if VL == VL2: #logic saying that if the length for b1 and b2 are the same then set b1 to A and b2 to B
            A = b1
            B = b2
        elif VL < VL2: #logic saying that if the length of B1 is less than B2 then ass zeros to B1 to make B1 the same length
            Zeros = VL - VL2
            for i in Zeros:
                b1.add_next_bit(0)
            A = b2
            B = b1
        else:
             Zeros = VL2 - VL #logic saying that if the length of B2 is less than B1 then ass zeros to B2 to make B2 the same length
             for i in Zeros:
                b2.add_next_bit(0)
             A = b1
             B = b2


##        print str(4) + "C"
##        print A
##        print B
##        print str(5) + "C"
        List1 = [] #makes a list
        List = [] # makes a list
        carry = 0 # sets a varable to zero
        while A != None: #
            value = A.get_bit() # Gets the value of the bit note for A
            value2 = B.get_bit() # Gets the value of the bit note for B
            value = TorF_Conv(value) # convers boolens to int
            value2 = TorF_Conv(value2) # convers boolens to int
            new_value = value + value2 # adds the value of the varable "value" and value of the varable "value2" and store the result as "new_value"
##            print str(7) + "C"
            List1.append(new_value) #adds new_value's value to a list
            if new_value == 2:      # logic that says that if new_value equal 2 and carry equal 1 then append 1 to the list named "List", else append 0 to the list
                if carry == 1:
                    List.append(1)
                    carry = 1    # sets the value of "carry" to 1
                else:
                    List.append(0)
                    carry = 1    # sets the value of "carry" to 1
            elif new_value == 1: # logic that says that if new_value equal 1 and carry equal 1 then append 0 to the list named "List", else append 1 to the list
                if carry == 1:
                    List.append(0)
                    carry = 0    # sets the value of "carry" to 0
                else:
                    List.append(1)
            else:   # logic that says that if new_value equal 0 and carry equal 1 then append 1 to the list named "List", else append 0 to the list
                if carry == 1:
                    List.append(1)
                    carry = 0   # sets the value of "carry" to 0
                else:
                    List.append(0)
            A = A.get_next_bit()  # move the bit_ref to the next node so we can see the next value for A
            B = B.get_next_bit()  # move the bit_ref to the next node so we can see the next value for B
        if List1[len(List1) -1] == 2:  # Logic saying that if the last item in the list is 2 then append 1 to the list called "List"
            List.append(1)
        print str(List1) + "carry values" #print for the user
        print str(List) + "binary values with the last carry." #print for the user
        print str(List) + "binary values with the last carry." #print for the user
        print ' '.join(str(i) for i in reString(List)) + " The Answer!" #print for the user
#----------------------------------------------------------------------------
    def __iter__(self):

        return LListIterator(self.head)

#------------------------------------------------------------

class BNIterator(object):

    #------------------------------------------------------------

    def __init__(self, head):
        self.currnode = head

    #------------------------------------------------------------
    # Python2 version
    def next(self):
        if self.currnode is None:
            raise StopIteration
        else:
            item = self.currnode.item
            self.currnode = self.currnode.link
            return item

    #------------------------------------------------------------
    # Python3 version
    def __next__(self):
        if self.currnode is None:
            raise StopIteration
        else:
            item = self.currnode.item
            self.currnode = self.currnode.link
            return item


