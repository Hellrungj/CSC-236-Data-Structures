#-------------------------------------------------------------------------------
# Name:        hellrungj & santosg
# Purpose:
#
#
# Created:     18/10/2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Mnemonic(object):
    """ This class is to display possible letter outputs for users when
    they input a phone number"""
    def __init__( self ):
        """ """
        #Phone Number Dictionary
        self.phonekey = { "1":"", "2":"ABC", "3":"DEF", "4":"GHI", "5":"JKL",
                    "6":"MNO", "7":"PQRS", "8":"TUV", "9":"WXYZ", "0":""  }
        #User input
        self.numberinput = list()
        self.word1 = ''
##        self.word2 = ''
##        self.word3 = ''

    def listmnemonics( self, number):
        """print out all the posiables"""
        f=0
        x=0
        for i in number:                                                        # loop the userinput
            while x != len(number):
                for d in number:
                    if d in self.phonekey:
                        for q in self.phonekey.get(d):
                            if len(self.word1) != len(number):
                                self.word1 += q                                 #self.phonekey.get(d)[:f]
                            elif len(self.word1) == len(number):
                                self.numberinput += str(self.word1)
                                print self.numberinput                          # print the numberinput
                                self.word1 = ''

                x += 1
                print self.word1                                                #print out all numbers



