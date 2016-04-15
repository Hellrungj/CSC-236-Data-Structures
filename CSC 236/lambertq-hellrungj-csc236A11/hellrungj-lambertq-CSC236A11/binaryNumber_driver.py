#-------------------------------------------------------------------------------
# Name:        binaryNumber_driver.py
# Purpose:  Rudimentary testing suite for the BinaryNumber class.
#
# Author:      nakazawam and pearcej
#
# Created:     21/09/2014
#-------------------------------------------------------------------------------

from  binaryNumber import BinaryNumber
def main():
    b1 = BinaryNumber()
    b2 = BinaryNumber()
    b3 = BinaryNumber()
    testing = BinaryNumber()
    print("instantiation of testing list.")
    print "Input binary----------------------------------------------"
    b1.convert_decimal_to_binary(5)
    print b1
    b2.convert_decimal_to_binary(5)
    print b2
    print "My method-------------------------------------------------"
    b1.add(b1)
    print "Right Answer----------------------------------------------"
    b3.convert_decimal_to_binary(10)
    print b3

if __name__ == '__main__':
    main()

