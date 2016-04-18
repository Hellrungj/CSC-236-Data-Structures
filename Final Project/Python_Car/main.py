from PlayerScore import PlayerScore
import time

def main():
    PlayerScores = []
    Playing = "Y"
    while Playing == "Y":
        Playing = raw_input("Do you want to play a Game?(Y,n)")
        Game1 = PlayerScore()
        if Playing == "Y":
            Game1.Start()
            print (Game1.Name) + ":" + (Game1.score) 
            time.sleep(1)
            PlayerScores.append(Game1.Name)
            PlayerScores.append(Game1.score)
        else:
            print ("Have a nice day. Please, come and play again sometime.")
if __name__ == '__main__':
    main()
