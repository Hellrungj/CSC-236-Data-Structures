#-------------------------------------------------------------------------------
# Name:        Hellrungj
# Purpose:      CSC 236
#
#
# Created:     21/10/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def printDigits(num, base):
    assert(base > 1)
    if(num < base):
        print num
    else:
        printDigits(num / base, base )
        print str(num % base) + " "


def main():
    num=0  # the number to convert
    base=0 # the base to convert the number.
    num = input("What is the number to convert: ")
    base = input("What is the new number base for that number: ")
    printDigits(num, base)

if __name__ == '__main__':
    main()