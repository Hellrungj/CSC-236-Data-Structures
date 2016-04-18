#include"Gearshift.h"
#include<iostream>
using namespace std;

Gearshift::Gearshift(){
    //max = 5;
    //min = -1;
    gearshift =0;
};
Gearshift::Gearshift(int x){
    //max = 5;
    //min = -1;
    if(x<max and x>min){
        gearshift = x;
    }
    else{
        cout << "Error" << endl;
    }
};
void Gearshift::Shiftup(){
    if(gearshift<max){
        gearshift =+ 1;
    }
    else{
        cout << "Error" << endl;
    }
};
void Gearshift::Shiftdown(){
    if(gearshift>min){
        gearshift =- 1;
    }
    else{
        cout << "Error" << endl;
    }
}
void Gearshift::Display(){
    cout << gearshift << endl;
};
