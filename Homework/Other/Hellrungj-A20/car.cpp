#include"Gearshift.cpp"
#include<iostream>
using namespace std;

int main(){
    int lives = 0;
    string choice = "";
    cout << "Welcome to the Drive Test of your Life!" << endl;
    cout << "BaHAHAHA!, Anyway" << endl;
    cout << "Do you want to play?" << endl;
    cin >> choice;
    if(choice == "Y"){
        cout << ":)" << endl;
        cout << "Ok, now drive me to the store, slave." << endl;
        Gearshift Car1;
        int dis;
        int gear;
        int lives;
        cout << "Ok now, slave start up the car and set the gear to one." << endl;
        while(gear != 1){
            cin >> gear;
            if(gear == 1){
                Car1.Shiftup();
            }
            else{
                cout << "You fool! I said set the gear to one." << endl;
                cout << "Slave start up the car and set the gear to three, now!." << endl;
                lives--;
            if(lives == 0);
                cout << "you lose!" << endl;
                break;
        }
        if(gear == 1){
            cout << "Now we are on the highway, slave set the gear to three." << endl;
            while(gear != 3){
                cin >> gear;
                if(gear == 3){
                    Car1.Shiftup();
                    Car1.Shiftup();
                }
                else{
                    cout << "You fool! I said set the gear to three." << endl;
                    cout << "Slave start up the car and set the gear to three, now!." << endl;
                lives--;
                if(lives == 0);
                    cout << "you lose!" << endl;
                    break;
                }
        }
        if(gear == 3){
            cout << "I am bored, slave set the gear to five." << endl;
            while(gear != 5){
                cin >> gear;
                if(gear == 5){
                    Car1.Shiftup();
                    Car1.Shiftup();
                }
                else{
                    cout << "You fool! I said set the gear to five." << endl;
                    cout << "Slave start up the car and set the gear to three, now!." << endl;
                lives--;
                if(lives == 0);
                    cout << "you lose!" << endl;
                    break;
                }
        }
        }
        if(gear == 6){
            cout << "Keep going slave, set the gear to six!" << endl;
            while(gear != 6){
                cin >> gear;
                if(gear == 6){
                    Car1.Shiftup();
                    cout << "Why is this car not going any faster!" <<endl;
                }
                else{
                    cout << "You fool! I said set the gear to six." << endl;
                    cout << "Slave start up the car and set the gear to three, now!." << endl;
                lives--;
                if(lives == 0);
                    cout << "you lose!" << endl;
                    break;
                }
        }
        }
        if(gear == 5){
            cout << "Stop here slave I am going to get us another car." << endl;
            while(gear != 0){
                cin >> gear;
                if(gear == 0){
                    Car1.Shiftup();
                    Car1.Shiftup();
                }
                else{
                    cout << "You fool! I said stop here." << endl;
                    cout << "Slave start up the car and set the gear to three, now!." << endl;
                lives--;
                }
                if(lives == 0){
                    cout << "you lose!" << endl;
                    break;
                }
        }
        }
        if(gear == 5){
            cout << "Stay here don't leave or I just have to find another driver." << endl;
            while(gear != -1){
                cin >> gear;
                if(gear == -1){
                    Car1.Shiftup();
                    cout << "What are you doing? Come back here slave!" << endl;
                }
                else{
                    cout << "You fool!." << endl;
                    lives = 0;
                if(lives == 0);
                    cout << "you lose!" << endl;
                    break;
                }
        }
        if(gear == -1){
            cout << "You won!" << endl;
        }
    }
    else{
        cout << ":(" << endl;
    }
    cout << "Thank you for playing. :)" << endl;
    Gearshift Car1;
    Gearshift Car2(1);
    Car1.Display();
    Car2.Display();
}
