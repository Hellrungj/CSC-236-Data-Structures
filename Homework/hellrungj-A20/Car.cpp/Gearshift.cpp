#include"Gearshift.h"
#include<iostream>
using namespace std;

Gearshift::Gearshift(){
    gearshift =0;
};
Gearshift::Gearshift(int x){
    int maxnum = 6;
    int minnum = -2;
    if(x<maxnum and x>minnum){
        gearshift = x;
    }
    else{
        cout << "Error" << endl;
    }
};
void Gearshift::Shiftup(){
    int maxnum = 6;
    if(gearshift<maxnum){
        gearshift = gearshift + 1;
    }
    else{
        cout << "Error you can not go up a gear" << endl;
    }
};
void Gearshift::Shiftdown(){
    int minnum = -2;
    if(gearshift>minnum){
        gearshift = gearshift = 1;
    }
    else{
        cout << "Error you can not go down a gear" << endl;
    }
}
void Gearshift::Display(){
    cout << gearshift << " gear " << endl;
};
