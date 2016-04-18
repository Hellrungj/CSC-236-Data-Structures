class Gearshift():
    def __inti__(self):
        self.gearshift = 0
        self.Gear_SpeedIndex = {-1:-20,0:0,1:10,2:30,3:60,4:80,5:100,6:120}
        
    def Shiftup(self):
        self.gearshift = 0
        if self.gearshift > 6:
            print ("You are at the highest gear setting.")
        else:
            self.gearshift = self.gearshift + 1
            
    def Shiftdown(self):
        self.gearshift = 0
        if self.gearshift < -1:
            print ("You are at the lowerest gear setting.")
        else:
            self.gearshift = self.gearshift - 1
            
    def Speed(self):
        self.Gear_SpeedIndex = {-1:-20,0:0,1:10,2:30,3:60,4:80,5:100,6:120}
        speed1 = self.Gear_SpeedIndex[self.gearshift]
        print (speed1)
        return speed1