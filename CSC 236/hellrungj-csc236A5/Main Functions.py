#-------------------------------------------------------------------------------
# Name:        John Hellrung
#
# Author:      hellrungj
#
# Created:     05/09/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Pet import Pet
from Depleting import Petneeds
import time

def main():
    Cat = Pet()
    print(Cat) # print the status of the pet # the problem with my code is here and I have had problems fixing it all weekend.
##    user = raw_input("do you want to feed your Cat?") #asks the user if he or she wants to feed the pet and if do it call feedPet() and if the user doesn't it calls dontfeedPet().
##    if user == "y":
##        Petneeds.feedPet()
##    else:
##        Petneeds.dontfeedpet()
##    time.sleep(2)
##    print(Cat)
##    user = raw_input("I think the cat wants to be your attention. Do you want to pet the cat?") #asks the user if he or she wants to feed the pet and if do it calls carePet() and if the user doesn't it calls dontcarePet().
##    if user == "y":
##        Petneeds.carePet()
##        print("prrrprrrprrr")
##    else:
##        Petneeds.dontcareforpet()
##    time.sleep(2)
##    print(Pet())
##    user = raw_input("You need to clean out the cats laiter box. Do you continue?") #asks the user if he or she wants to feed the pet and if do it calls cleanPet() and if the user doesn't it calls dontcleanPet().
##    if user == "y":
##        Petneeds.cleanPet()
##        print("Meow")
##    else:
##        Petneeds.dontcleanpet()

if __name__ == '__main__':
    main()
