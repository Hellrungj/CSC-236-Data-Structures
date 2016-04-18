from Pedals import Pedalshift
from Road import Road
from Gears import Gearshift

class PlayerScore():
    def __inti__(self):
        self.score = 0
        self.Name = " "
        self.CarCrashs = 0
        self.Won = False
        
    def Start(self):
        UserName = raw_input("What is your Name?")
        self.Name = UserName
        self.Won = False
        Road1 = Road()
        GearShift1 = Gearshift()
        PedalShift1 = Pedalshift()
        Road1.Make_Road()
        while self.Won != True:
            Gas = raw_input("F,H,N")
            Break = raw_input("B,S,N")
            PedalShift1.Pedals(Gas,Break)
            GearShift1.speed()
            Road1.CheckTurns()
            Road1.Tracking()
            I = 0
            if I == 300:
                break
                print ("INFLoop")
            else:
                I = I + 1
        print ("You have won ") + self.Name + (".")
    
    def __str__(self):
        return self.score