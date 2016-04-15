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
        carry = 1               # sets a varable for increment the binary
        while (aBit != None):       # a while loop that runs until the varble of "aBit" does equal None
            value = aBit.get_bit()  # set the vaule of "value" to "aBit.get_bit()". This method retruns the vaule of the node.
            if value == True:       # An if statemnet that checks to see if "value" is equal to boolean value of "True".
                value = 1           # change the value to one
            else:                   # else ! (if the value of "value" is equal to one)
                value = 0           # change the value to zero
            new_value = value + carry # set the the value of "value" plus the value of "carry" to the value of "new_value"
            if new_value == 2:        # An if statement thatt checks to see i fthe value of "new_value" is equal to the intiger of two
                aBit.set_bit(False)       # Sets the current node value to zero. (sets the bit to zero)
                carry = 1             # Set the value of "carry" to one
            elif new_value == 1:      # if the value of "new_value" is equal to the intiger of one
                carry = 0             # set the carry to zero
                aBit.set_bit(True)       # sets the current node value to one. (sets the bit to one)
            else: #if  zero           # else! (if the value of new_value equal the intiger of zero.)
                carry = 0             # set the carry to zero
                #leave it alone
            nextBit = aBit.get_next_bit()
            if (carry == 1) and (nextBit == None):
                aBit.add_next_bit(True)
                self.numBits += 1
            aBit = nextBit   # sets the the node called "aBit" to the next binary node. Moving the loop forrward thorught the linked list
                   # An if statement that checks to see if the value of carry is equal to the intiger of one
             # Set the value of "carry" to the next bit. (Creating a  new Bit)
           #------------------------------------------------------------
#   A12
#   John Hellrung & Quiten Lambert (hellrungj & lambertq)
#
#-----------------------------------------------------------
    def C_len (self, bit):
        """Find the length of the bit1 and bit2"""
        abit = self.leastSignificantBit
        add = 0
        while abit != None:
            add + 1
            abit.get_next_bit()
        abit1 = bit.leastSignificantBit
        add2 = 0
        while abit1 != None:
            add1 + 1
            abit.get_next_bit()

    def One(self):
        abit = self.leastSignificantBit
        Value = abit.get_bit()
        print Value
        abit.set_bit(1)
        Value = abit.get_bit()
        print Value
    ##    abit.add_next_bit(0)
    ##    print abit


    def add(self, binary_1, binary_2):
        """add bit1 and bit2 to make bit3"""
        abit1 = self.leastSignificantBit
        abit2 = binary_1.leastSignificantBit
        abit3 = binary_2.leastSignificantBit
        carry = 0
        while abit1 != None:
            value1 = abit1.get_bit()
            value2 = abit2.get_bit()
            if value1 == True:
                valueN1 = 1
            else:
                valueN1 = 0
            if value2 == True:
                valueN2 = 1
            else:
                valueN2 = 0
            TotalNvalue= valueN1 + valueN2
            if TotalNvalue == 2:
                carry = 1
                self.set_bit(0)
                self.add_next_bit(0)
            elif TotalNvalue == 1:
                if carry == 1:
                    carry = 0
                    self.set_bit(0)
                    self.add_next_bit(0)
                else:
                    self.set_bit(1)
                    self.add_next_bit(0)
            else:
                 self.set_bit(1)
                 self.get_next_bit(0)
            abit1.get_next_bit()
            abit2.get_next_bit()
#----------------------------------------------------------------

##     def __iter__(self):

##         # generator version works in both Python2 and Python3
##         node = self.head
##         while node is not None:
##             yield node.item
##             node = node.link

    #------------------------------------------------------------

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


