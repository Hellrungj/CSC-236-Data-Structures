from Gears import Gearshift

class Pedalshift():
    def __inti__(self):
        self.GasPedalPos = {"F":2,"H":1,"N":0}
        self.BreakPedalPos = {"B":2,"S":1,"N":0}
        self.GasPedal = 0
        self.BreakPedal = 0
    
    def Pedalcheck(self):
        Gears = Gearshift()
        if self.GasPedal == 0 and self.BreakPedal == 0: #00 Nothing or Full Stop     D
            if Gears.gearshift == 0:
                print ("You need to put the car in a gear.")
            elif Gears.gearshift >= 4:
                print ("You crash your car.")
                PlayerScore.CarCrashs = PlayerScore.CarCrashs + 1
            elif Gears.gearshift > 0:
                Gears.Shiftdown()
            else:
                Gears.Shiftup()
        elif self.GasPedal == 0 and self.BreakPedal == 1:#01 Nothing or Slow decrese D
            if Gears.gearshift == 0:
                print ("You need to put the car in a gear.")
            elif Gears.gearshift > 0:
                Gears.Shiftdown()
            else:
                Gears.Shiftup()
        elif self.GasPedal == 0 and self.BreakPedal == 2:#02 Nothing or Full Stop D
            if Gears.gearshift == 0:
                print ("You need to put the car in a gear.")
            elif Gears.gearshift >= 4:
                print ("You crash your car.")
                PlayerScore.CarCrashs = PlayerScore.CarCrashs + 1
            elif Gears.gearshift > 0:
                Gears.Shiftdown()
            else:
                Gears.Shiftup()
        elif self.GasPedal == 1 and self.BreakPedal == 0:#10 Slow increse I
                Gears.Shiftup()
        elif self.GasPedal == 1 and self.BreakPedal == 1:#11 Nothing or Full Stop D
            if Gears.gearshift == 0:
                print ("You need to put the car in a gear.")
            elif Gears.gearshift >= 4:
                print ("You crash your car.")
                PlayerScore.CarCrashs = PlayerScore.CarCrashs + 1
            elif Gears.gearshift > 0:
                Gears.Shiftdown()
            else:
                Gears.Shiftup()
        elif self.GasPedal == 1 and self.BreakPedal == 2:#12 Slow decrese D
            if Gears.gearshift == 0:
                print ("You need to put the car in a gear.")
            elif Gears.gearshift > 0:
                Gears.Shiftdown()
            else:
                Gears.Shiftup()
        elif self.GasPedal == 2 and self.BreakPedal == 0:#20 Full Speed I
                Gears.Shiftup()
        elif self.GasPedal == 2 and self.BreakPedal == 1:#21 Slow increse  I
                Gears.Shiftup()
        else:#22 Nothing or Full stop   D
            if Gears.gearshift == 0:
                print ("You need to put the car in a gear.")
            elif Gears.gearshift >= 4:
                print ("You crash your car.")
                PlayerScore.CarCrashs = PlayerScore.CarCrashs + 1
            elif Gears.gearshift > 0:
                Gears.Shiftdown()
            else:
                Gears.Shiftup()
        
    def Pedals(self, Gas, Break):
        self.GasPedalPos = {"F":2,"H":1,"N":0}
        self.BreakPedalPos = {"B":2,"S":1,"N":0}
        self.GasPedal = self.GasPedalPos[Gas]
        self.BreakPedal = self.BreakPedalPos[Break]
        self.Pedalcheck()
        
            
    