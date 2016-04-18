//This is Car's header file
using namespace std;

class Gearshift{
    private:
        int gearshift;
        int max = 5;
        int min = -1;
    public:
        Gearshift();
        Gearshift(int x);
        void Shiftup();
        void Shiftdown();
        void Display();
    };
