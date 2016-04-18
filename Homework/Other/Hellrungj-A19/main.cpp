/*
* John Hellrung
* For: CSC 236
*
*
*/
#include <iostream>  //Needed for I/O
using namespace std;

int main(){
    int numDays,myYear,myMonth,myDay;
    int count = 0;
    cout << "Please enter the Month (1-12): ";
    cin >> myMonth;
    cout << "Please enter the Date (1-31): ";
    cin >> myDay;
    cout << "Please enter the Year: ";
    cin >> myYear;
    cout << "Please imput a date." << endl;
    cin >> numDays;
    cout <<myDay << "/" << myMonth << "/"<< myYear << ": NUM-" << numDays << endl;
    while(numDays != 0){
        if(numDays >= 366){
            if(myYear% 400 == 0){
                myYear = myYear + 1;
                numDays = numDays - 366;
                cout << myYear << " Y";
            }
            else if(myYear% 100 ==0){
                myYear = myYear + 1;
                numDays = numDays - 365;
                cout << myYear << " Y";
            }
            else if(myYear% 4 == 0){
                myYear = myYear + 1;
                numDays = numDays - 366;
                cout << myYear << " Y";
            }
            else{
                myYear = myYear + 1;
                numDays = numDays - 365;
                cout << myYear << " Y";
            }
        }
    //------------------------------------------------------------------------------
        else if(numDays >= 28){
            if( myMonth == 4 || myMonth == 6 || myMonth == 9 || myMonth == 11 ) {
                myMonth = myMonth + 1;
                numDays = numDays - 30;
                cout << myMonth << " M";
            }    
            else if(myMonth == 2){
                // Find if its a leep year and subatracks 29 if so and if not 28 days
                if(myYear% 400 == 0){
                    myMonth = myMonth + 1;
                    numDays = numDays - 29;
                    cout << myMonth << " M";
                }
                else if(myYear% 100 ==0){
                    myMonth = myMonth + 1;
                    numDays = numDays - 28;
                    cout << myMonth << " M";
                }
                else if(myYear% 4 == 0){
                    myMonth = myMonth + 1;
                    numDays = numDays - 29;
                    cout << myMonth << " M";
                }
                else{
                    myMonth = myMonth + 1;
                    numDays = numDays - 28;
                    cout << myMonth << " M";
                }
            }
            else{
                myMonth = myMonth + 1;
                numDays = numDays - 31;
                cout << myMonth << " M";
            };
        }
    //------------------------------------------------------------------------------
        else{    
            myDay = myDay + numDays;
            numDays = numDays - numDays;
            cout << numDays << " D";
        };
        if(count == 100){
            break;
        }
        else{
            count++;
            cout << count << "*" << endl; 
        }
    };
    cout << myMonth << "/" << myDay << "/"<< myYear << endl;
    //---------------------------------------------------------------------------
    // Make sure that if days are greater than 28,29,30,31 than its adds 1 to the month.
    if(myMonth > 12){
        myMonth = myMonth - 12;
        myYear = myYear + 1;
    }
    cout << myMonth << "/" << myDay << "/"<< myYear << endl;
    if( myMonth == 4 || myMonth == 6 || myMonth == 9 || myMonth == 11 ) {
        if(myDay > 30){
            myDay = myDay - 30;
            myMonth = myMonth + 1;
        }
            
    }        
    else if(myMonth == 2){
        if(myYear% 400 == 0){
            if(myDay > 29){
                myDay = myDay - 29;
                myMonth = myMonth + 1;
            }
        }
        else if(myYear% 100 ==0){
            if(myDay > 28){
                myDay = myDay - 28;
                myMonth = myMonth + 1;
            }
        }
        else if(myYear% 4 == 0){
            if(myDay > 29){
                myDay = myDay - 29;
                myMonth = myMonth + 1;
            }
        }
        else{
            if(myDay > 28){
                myDay = myDay - 28;
                myMonth = myMonth + 1;
            }
        }
    }
    else{
        if(myDay > 31){
            myDay = myDay - 31;
            myMonth = myMonth + 1;
        }
    };
    cout << myMonth << "/" << myDay << "/"<< myYear << endl;
    if(myMonth > 12){
        myMonth = myMonth - 12;
        myYear = myYear + 1;
    }
    cout << myMonth << "/" << myDay << "/"<< myYear << endl;
    
    
    
    //cout << date%365 << endl;
    //cout << date / 365 << endl;
    //cout << date - 365 * (date / 365) << endl;
} 