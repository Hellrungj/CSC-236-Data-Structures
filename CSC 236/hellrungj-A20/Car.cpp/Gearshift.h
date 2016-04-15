//This is Car's header file
using namespace std;

class Gearshift{
    private:
        int gearshift;
    public:
        Gearshift();
        Gearshift(int x);
        void Shiftup();
        void Shiftdown();
        void Display();
    };
