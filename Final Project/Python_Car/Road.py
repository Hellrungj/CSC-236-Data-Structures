import random
import PlayerScore
import Gears

class Road():
    def __inti__(self):
        self.weather = "N" #Possablies: N(nomial), R(Rain), S(Snow), I(Ice) 
        self.turn = " " #Possablies: R(right), L(left)
        self.MilesDiven = 0 #Distance
        self.TotalMiles = 0
        self.Numturns = 0
        self.TurnLocations = []
        self.score = 0
        self.SpeedMax_Turns = 0
        
    def RainRoad(self):
        self.weather = "R" 
        self.TotalMiles = 2000 
        self.turns = 5
        self.TurnLocations = [100,400,600,1400,1800]
        self.score = 4
        self.SpeedMax_Turns = 60 
        
    def NomRoad(self):
        self.weather = "N"
        self.TotalMiles = 3000
        self.turns = 6
        self.TurnLocations = [200,300,400,600,1200,2000,2500]
        self.score = 4
        self.SpeedMax_Turns = 80 
        
    def SnowRoad(self):
        self.weather = "S"
        self.TotalMiles = 1400
        self.turns = 4
        self.TurnLocations = [200,400,700,1200]
        self.score = 5
        self.SpeedMax_Turns = 50 
        
    def IceRoad(self):
        self.weather = "I"
        self.TotalMiles = 1200
        self.turns = 3
        self.TurnLocations = [300,500,1000,]
        self.score = 5
        self.SpeedMax_Turns = 40
        
    def Make_Road(self):
        road = " "
        road = random.choice(["R","N","S","I"])
        if road == "R":
            self.RainRoad()
        elif road == "N":
            self.NomRoad()
        elif road == "S":
            self.SnowRoad()
        else:
            self.IceRoad()
            
    def Tracking(self):
        if self.miles >= TotalMiles:
            print ("You have finished the track.")
            PlayerScore.Won = True
        elif self.miles >= TotalMiles:
            print ("You have backtracked to the begeging of the track")
        else:
            self.miles = self.miles + gearshift.speed
            
    def CheckTurns(self):
        for turn in self.TurnLocations:
            if self.miles >= (60 - self.TurnLocations[turn]) and self.miles <= (60 + self.TurnLocations[turn]):
                if self.weather == "R":
                    if Gearshift.gearshift > 4:
                        print ("You crash your car.")
                        PlayerScore.CarCrashs = PlayerScore.CarCrashs + 1
                        PlayerScore.score = PlayerScore.score - 5
                        self.miles = self.TurnLocations[turn] + 61 
                    else:
                        PlayerScore.score = PlayerScore.score + 10
                elif self.weather == "N":
                    if Gearshift.gearshift > 5:
                        print ("You crash your car.")
                        PlayerScore.CarCrashs = PlayerScore.CarCrashs + 1
                        PlayerScore.score = PlayerScore.score - 5
                        self.miles = self.TurnLocations[turn] + 61
                    else:
                        PlayerScore.score = PlayerScore.score + 10
                elif self.wether == "S":
                    if Gearshift.gearshift > 3:
                        print ("You crash your car.")
                        PlayerScore.CarCrashs = PlayerScore.CarCrashs + 1
                        PlayerScore.score = PlayerScore.score - 5
                        self.miles = self.TurnLocations[turn] + 61
                    else:
                        PlayerScore.score = PlayerScore.score + 10
                else:
                    if Gearshift.gearshift > 2:
                        print ("You crash your car.")
                        PlayerScore.CarCrashs = PlayerScore.CarCrashs + 1
                        PlayerScore.score = PlayerScore.score - 5
                        self.miles = self.TurnLocations[turn] + 61
                    else:
                        PlayerScore.score = PlayerScore.score + 10
            else:
                pass
        
        
        
        
        