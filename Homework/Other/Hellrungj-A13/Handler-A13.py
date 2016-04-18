#Handler file for A13 
# John Hellrung 
# Made Thurday, Oct. 17, 2014
#-------------------------------------------------------------------------------

from PhoneNumber.py import PhoneNumber

def main():
    """Main function!"""
    usersphone = input("Please input your Number.")
    Message = PhoneNumber()
    

if __name__ == '__main__':
    main()

#-------------------------------------------------------------------------------
#Pysudocode:
    # main:
        # Ask the user's for there number 
        # Calls the class and returns the value needed. 
        # prints out all possable combantions
