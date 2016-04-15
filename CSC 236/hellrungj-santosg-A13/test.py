#-------------------------------------------------------------------------------
# Name:        hellrungj & santosg
# Purpose:
#
# Created:     18/10/2014
# Copyright:   (c) santosg 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from NumberWordGen import Mnemonic

MN = Mnemonic()

def main():
    MN = Mnemonic()
    user = raw_input("please enter your phone number.")
    MN.listmnemonics(user)

if __name__ == '__main__':
    main()
