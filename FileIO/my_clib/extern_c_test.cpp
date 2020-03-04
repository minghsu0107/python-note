#include <iostream>
#include "test.h"
using namespace std;

void Test::foo2(int a, int b) {
    cout << a << " " << b << endl;
}

// compile C++
extern "C" {
    void cfoo2(int a, int b) {
        Test t;
        t.foo2(a, b);
    }   
}
