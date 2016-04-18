// Filename: DateDemo.cpp
// Example of using the Date class.
//John Hellrung
// CSC 236
// Acknowledgement: 
// Mario and Jan for the use of this code.

#include <iostream>  //Needed for I/O
#include <ctime>  //Needed for the default Date constructor which gets the current date
using namespace std;

//public functions that are used by the class Date
int daysInMonth(int month,int year); 	// # of days in month in year
bool isLeap(int year);   				// is year a leap year

//This is an example of a small C++ class that handles dates
class Date {
  private:
 	//private member variables
    int myDay;                    	// day of week
    int myMonth;                  	// month
    int myYear;                   	// year in four digits, e.g., 2003
    //private member function
    void checkDate(int m, int d, int y); 	// make sure that date is valid

  public:
    // constructors
    Date();                       	// construct date with default value
    Date(int m,int d,int y);      	// construct date with specified values
    // public member functions called accessors since they are used
    // to access the contents of private member variables
    int getMonth()	const;     // return month corresponding to date
    int getDay()	const;     // return day corresponding to date
    int getYear()   const;     // return year corresponding to date

    //public member function
    void print()	const; //Will cout a date in the 1/1/2003 format
    //void printnum() const;
    void add(int numDays);

}; // Note the need for a semicolon just like ending a structure

int main() {
    // This calls the default Date constructor, which sets the current date.
    Date todaydate;
    cout << "Today is ";
    todaydate.print();
    cout << "." << endl;

	int birthmonth, birthday, birthyear,Month,Day,Year,numday;
    /*cout << "Please enter the month (1-12) you were born: ";
    cin >> birthmonth;
    cout << "Please enter the date (1-31) of your birthday: ";
    cin >> birthday;
    cout << "Please enter the year you were born: ";
    cin >> birthyear;
    //This calls the Date contructor and sets the member variables of birthdate.
    Date birthdate(birthmonth, birthday, birthyear);

    cout << "You were born ";
    birthdate.print();
    cout << "." << endl;

    //Note that we cannot use birthdate.myMonth here since myMonth is a private member variable
    if (birthdate.getMonth() == todaydate.getMonth()) {
    	//cout << birthdate.myMonth; //Uncomment this to see what happens
    	cout << "Hey, you have a birthday this month!" << endl;
    }
    else {
    	cout << "Too bad you don't have a birthday this month..." << endl;
    }*/
    cout << "Please enter the Month (1-12): ";
    cin >> Month;
    cout << "Please enter the Date (1-31): ";
    cin >> Day;
    cout << "Please enter the Year: ";
    cin >> Year;
    cout << "How many days in the future or past do you want?" << endl;
    cin >> numday;
    Date search(Month,Day,Year);
    search.add(numday);
    cout << "Here your date!";
    search.print();
    cout << "." << endl; 
    // This all promts the user and call of the calls
    return 0;
} //end main


bool isLeap(int year) {
// postcondition: returns true if year is a leap year, else returns false

    if (year % 400 == 0) {
        return true;
    }
    else if (year % 100 == 0) {
        return false;
    }
    else if (year % 4 == 0) {
        return true;
    }
    return false;
}

int daysInMonth(int month, int year) {
// postcondition: returns # of days in month in year

    // Start with 31 days and lower it to 30 for April, June, September
    // and November. Then handle February.
    int days = 31;

    if( month == 4 || month == 6 || month == 9 || month == 11 ) {
        days = 30;
   	}
    else if (month == 2) {          // handle February
        days = 28;
        if (isLeap(year)) {        // add 1 for leap years
            days += 1;
       	}
    }
    return days;
}

Date::Date()
//Do not worry about understanding the contents of this constructor yet.
//Getting the current date uses ideas we have not yet learned...
// postcondition: date initialized to default date of today
{
    static struct tm timeHolder;
    static struct tm *date = &timeHolder;
    time_t tloc;

    time(&tloc);

    date = localtime(&tloc);

    myMonth = date->tm_mon + 1;
    myDay   = date->tm_mday;
    myYear  = date->tm_year + 1900;             // struct tm based on 1900
}

void Date::add(int numDays){
//postcondition: adds the years,months,days to the current date.
//------------------------------------------------------------------------------
    //* (Debug) */ int count = 0;
    //* (Debug) */ cout <<myMonth << "/" << myDay << "/"<< myYear << ": NUM-" << numDays << endl;
    while(numDays != 0){
        if(numDays >= 366 or numDays <= -366){
            if(myYear% 400 == 0){
                if(numDays > 0){
                    myYear = myYear + 1;
                    numDays = numDays - 366;
                //* (Debug) */ cout << myYear << " Y";
                }
                else{
                    myYear = myYear - 1;
                    numDays = numDays + 366;
                    //* (Debug) */ cout << myYear << " Y";
                }
            }
            else if(myYear% 100 ==0){
                if(numDays > 0){
                    myYear = myYear + 1;
                    numDays = numDays - 365;
                //* (Debug) */ cout << myYear << " Y";
                }
                else{
                    myYear = myYear - 1;
                    numDays = numDays + 365;
                    //* (Debug) */ cout << myYear << " Y";
                }
            }
            else if(myYear% 4 == 0){
                if(numDays > 0){
                    myYear = myYear + 1;
                    numDays = numDays - 366;
                //* (Debug) */ cout << myYear << " Y";
                }
                else{
                    myYear = myYear - 1;
                    numDays = numDays + 366;
                    //* (Debug) */ cout << myYear << " Y";
                }
            }
            else{
                 if(numDays > 0){
                    myYear = myYear + 1;
                    numDays = numDays - 365;
                //* (Debug) */ cout << myYear << " Y";
                }
                else{
                    myYear = myYear - 1;
                    numDays = numDays + 365;
                    //* (Debug) */ cout << myYear << " Y";
                }
            }
        }
    //------------------------------------------------------------------------------
        else if(numDays >= 28 or numDays <= -28){
            if( myMonth == 4 || myMonth == 6 || myMonth == 9 || myMonth == 11 ) {
                if(numDays > 0){
                    myMonth = myMonth + 1;
                    numDays = numDays - 30;
                //* (Debug) */ cout << myMonth << " M";
                }
                else{
                    myMonth = myMonth - 1;
                    numDays = numDays + 30;
                    //* (Debug) */ cout << myMonth << " M";
                }
            }    
            else if(myMonth == 2){
                // Find if its a leep year and subatracks 29 if so and if not 28 days
                if(myYear% 400 == 0){
                    if(numDays > 0){
                    myMonth = myMonth + 1;
                    numDays = numDays - 29;
                //* (Debug) */ cout << myMonth << " M";
                }
                    else{
                        myMonth = myMonth - 1;
                        numDays = numDays + 29;
                        //* (Debug) */ cout << myMonth << " M";
                    }
                }
                else if(myYear% 100 ==0){
                    if(numDays > 0){
                    myMonth = myMonth + 1;
                    numDays = numDays - 28;
                //* (Debug) */ cout << myMonth << " M";
                }
                    else{
                        myMonth = myMonth - 1;
                        numDays = numDays + 28;
                        //* (Debug) */ cout << myMonth << " M";
                    }
                }
                else if(myYear% 4 == 0){
                    if(numDays > 0){
                    myMonth = myMonth + 1;
                    numDays = numDays - 29;
                //* (Debug) */ cout << myMonth << " M";
                }
                    else{
                        myMonth = myMonth - 1;
                        numDays = numDays + 29;
                        //* (Debug) */ cout << myMonth << " M";
                    }
                }
                else{
                    if(numDays > 0){
                    myMonth = myMonth + 1;
                    numDays = numDays - 28;
                //* (Debug) */ cout << myMonth << " M";
                }
                    else{
                        myMonth = myMonth - 1;
                        numDays = numDays + 28;
                        //* (Debug) */ cout << myMonth << " M";
                    }
                }
            }
            else{
                if(numDays > 0){
                    myMonth = myMonth + 1;
                    numDays = numDays - 31;
                //* (Debug) */ cout << myMonth << " M";
                }
                else{
                    myMonth = myMonth - 1;
                    numDays = numDays + 31;
                    //* (Debug) */ cout << myMonth << " M";
                };
            };
        }
    //------------------------------------------------------------------------------
        else{
            if(numDays > 0){
                myDay = myDay + numDays;
                numDays = numDays - numDays;
            //* (Debug) */ cout << myDay << " D";
            }
            else{
                myDay = myDay + numDays;
                numDays = numDays - numDays;
            }
            //* (Debug) */ cout << myDay << " D";
        };
        /* (Debug) if(count == 100){
            break;
        }
        else{
            count++;
            cout << count << "*";
        }*/
        //cout << " !" << numDays << "NUM! " << endl;
    };
    // (Debug) cout << myMonth << "/" << myDay << "/"<< myYear << endl;
    //---------------------------------------------------------------------------
    // Make sure that if days are greater than 28,29,30,31 than its adds 1 to the month.
    if(myMonth > 12){
        myMonth = myMonth - 12;
        myYear = myYear + 1;
    }
    else if(myMonth < 0){
        myMonth = myMonth + 12;
        myYear = myYear - 1;
    }
    //cout << myMonth << "/" << myDay << "/"<< myYear << endl;
    if( myMonth == 4 || myMonth == 6 || myMonth == 9 || myMonth == 11 ) {
        if(myDay > 30){
            myMonth = myMonth + 1;
            numDays = numDays - 30;
            //* (Debug) */ cout << myMonth << " M";
        }
        else if(myDay < -30){
            myMonth = myMonth - 1;
            numDays = numDays + 30;
            //* (Debug) */ cout << myMonth << " M";
        }
    }
    else if(myMonth == 2){
        if(myYear% 400 == 0){
             if(numDays > 29){
                    myMonth = myMonth + 1;
                    numDays = numDays - 29;
                //* (Debug) */ cout << myMonth << " M";
                }
                else if(numDays < -29){
                    myMonth = myMonth - 1;
                    numDays = numDays + 29;
                    //* (Debug) */ cout << myMonth << " M";
                }
                }
        else if(myYear% 100 ==0){
             if(numDays > 28){
                    myMonth = myMonth + 1;
                    numDays = numDays - 28;
                //* (Debug) */ cout << myMonth << " M";
                }
                else if(numDays < -28){
                    myMonth = myMonth - 1;
                    numDays = numDays + 28;
                    //* (Debug) */ cout << myMonth << " M";
                }
            }
        else if(myYear% 4 == 0){
             if(numDays > 29){
                    myMonth = myMonth + 1;
                    numDays = numDays - 29;
                //* (Debug) */ cout << myMonth << " M";
                }
                else if(numDays < -29){
                    myMonth = myMonth - 1;
                    numDays = numDays + 29;
                    //* (Debug) */ cout << myMonth << " M";
                }
            }
        else{
             if(numDays > 28){
                    myMonth = myMonth + 1;
                    numDays = numDays - 28;
                //* (Debug) */ cout << myMonth << " M";
                }
                else if(numDays < -28){
                    myMonth = myMonth - 1;
                    numDays = numDays + 28;
                    //* (Debug) */ cout << myMonth << " M";
                }
            }
    }
    else{
        if(numDays > 0){
            myMonth = myMonth + 1;
            numDays = numDays - 31;
            //* (Debug) */ cout << myMonth << " M";
        }
        else{
            myMonth = myMonth - 1;
            numDays = numDays + 31;
            //* (Debug) */ cout << myMonth << " M";
        };
    }
    //cout << myMonth << "/" << myDay << "/"<< myYear << endl;
    if(myMonth > 12){
        myMonth = myMonth - 12;
        myYear = myYear + 1;
    }
    else if(myMonth < 0){
        myMonth = myMonth + 12;
        myYear = myYear - 1;
    }
    //cout << myMonth << "/" << myDay << "/"<< myYear << endl;
}
Date::Date(int m, int d, int y) {
// postcondition: date properly initialized for date m/d/y
// exception:  if m isn't between 1 and 12, converted to 1
//             if d out of range for month, converted to 1
//			   if year is 2 digits, 1900 is added
    checkDate(m,d,y);
}

int Date::getMonth() const {
// postcondition: returns month of Date
    return myMonth;
}

int Date::getDay() const {
// postcondition: returns day of Date
    return myDay;
}

int Date::getYear() const {
// postcondition: returns year of Date
    return myYear;
}

void Date::print() const {
//postcondition: cout a date in the 1/1/2003 format
    cout << myMonth << "/" << myDay << "/" << myYear << endl;
}

//void Date::printnum() const{
//postcondition: cout a date for the number of days
//    cout << numDays << endl;
//}

void Date::checkDate( int m, int d, int y ) {
// postcondition: adjusts out-of-range dates before setting member variables
    if (m < 1 || 12 < m) {               // If the month is out of range, set it to January
    	m = 1;
    	cout << "WARNING: Invalid month set to January." << endl;
    }
    myMonth = m;

    if (d < 1 || daysInMonth(m,y) < d) { // If the day is out of range, set it to 1.
    	d = 1;
    	cout << "WARNING: Invalid day set to 1." << endl;
    }
    myDay = d;

    if (y < 100) {                       // If the year is given in 2 digits, add 1900.
    	y = y + 1900;
    }
    myYear = y;
}