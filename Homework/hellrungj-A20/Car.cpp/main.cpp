#include"Pedalshift.cpp"
#include"Road.cpp"
#include"Gearshift.cpp"
#include<iostream>
using namespace std;

/*
Author: John Hellrung
Date:
Assignment: Final Project
*/

int main(){
    string choice = "";
    cout << "Welcome to the Drive Test of your Life!" << endl; //Welcomes the player
    cout << "BaHAHAHA!, Anyway" << endl; // for fun
    cout << "Do you want to play? (input Y if YES)" << endl; // promts the player with choice
    cin >> choice; // Take the player input and stores as choice
    if(choice == "Y"){ // If Y the game begins else the game shows a sad face and ends
        cout << ":)" << endl; // For fun
        cout << "Ok, now drive me to the store, slave." << endl; // Promts the user
        Gearshift Car1; // Consturts the car1
        int gear; // make a variable for the player to pick the gear they where on
        cout << "Ok now, slave start up the car and set the gear to one." << endl; //promts the player
        while(gear != 1){ // loops until the player choice 1 for their gear in the car
            cin >> gear; //sets the int of player's input as gear
            if(gear == 1){
                Car1.Shiftup(); // rises the gear by one
            }
            else{ // else promts the player
                cout << "You fool! I said set the gear to one." << endl;
                cout << "Slave start up the car and set the gear to three, now!." << endl;
                }
            }
        Car1.Display(); //Display the gear at witch the car is in
        if(gear == 1){ // check to see if the player did what was asked
            cout << "Now we are on the highway, slave set the gear to three." << endl;
            while(gear != 3){ // loops until the player choice 3 for their gear in the car
                cin >> gear;
                if(gear == 3){
                    Car1.Shiftup(); // rises the gear by one
                    Car1.Shiftup();
                }
                else{
                    cout << "You fool! I said set the gear to three." << endl;
                    cout << "Slave start up the car and set the gear to three, now!." << endl;
                }
            }
        Car1.Display(); //Display the gear at witch the car is in
        }
        if(gear == 3){ // check to see if the player did what was asked
            cout << "I am bored, slave set the gear to five." << endl;
            while(gear != 5){
                cin >> gear;
                if(gear == 5){
                    Car1.Shiftup(); // rises the gear by one
                    Car1.Shiftup();
                }
                else{
                    cout << "You fool! I said set the gear to five." << endl;
                    cout << "Slave start up the car and set the gear to three, now!." << endl;
                }
            }
        Car1.Display(); //Display the gear at witch the car is in
        }
        if(gear == 5){ // check to see if the player did what was asked
            cout << "Keep going slave, set the gear to six!" << endl;
            while(gear != 6){
                cin >> gear;
                if(gear == 6){
                    Car1.Shiftup(); // rises the gear by one
                    cout << "Why is this car not going any faster!" <<endl;
                }
                else{
                    cout << "You fool! I said set the gear to six." << endl;
                    cout << "Slave start up the car and set the gear to one, now!." << endl;
                }
            }
        Car1.Display(); //Display the gear at witch the car is in
        }
        if(gear == 6){ // check to see if the player did what was asked
            cout << "Stop here slave I am going to get us another car." << endl;
            while(gear != 0){
                cin >> gear;
                if(gear == 0){
                    Car1.Shiftdown();
                    Car1.Shiftdown();
                    Car1.Shiftdown();
                    Car1.Shiftdown();
                    Car1.Shiftdown();
                }
                else{
                    cout << "You fool! I said stop here." << endl;
                }
            }
        Car1.Display(); //Display the gear at witch the car is in
        }
        if(gear == 0){ //Checks if player set the gear to zero like asked
            cout << "Stay here don't leave or I just have to find another driver." << endl;
            while(gear == 0 or gear < -2 or gear > 6){ //Check to see if the player change the gear correctly.
                cout << "Reverse or drive forward" << endl;
                cin >> gear;
                if(gear == -1){
                    Car1.Shiftup();
                    cout << "What are you doing? Come back here slave!" << endl;
                }
                else if(gear > -1 and gear < 6){
                    Gearshift Car2(gear);
                    cout << "SPAT" << endl;
                }
                else{
                    cout << "You fool!." << endl;
                    break;
                }
            }
        Car1.Display(); //Display the gear at witch the car is in
        }
        if(gear > -1 or gear < 6){ // Checks if the player has the gear in between -1 to 6
            cout << "You won!" << endl; // then prints to the player that they have won
        }
    }
    else{ //Gives the player a sad face if they don't want to play
        cout << ":(" << endl;
    }
    cout << "Thank you for playing. :)" << endl;// Thanks the player
}
