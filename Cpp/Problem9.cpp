#include <chrono>
#include <cmath>
#include <iostream>
using namespace std;
using namespace std::chrono;

int main() {
    // Timer
    auto start = high_resolution_clock::now();

    long int answer = 0;

    bool found = false;
    for (double a = 1; a < 500; a++) {
        for (double b = 1; b < 500; b++) {
            double c = pow(pow(a, 2) + pow(b, 2), 0.5);
            if (a + b + c == 1000.0) {
                answer = a * b * c;
                found = true;
                break;
            }
        }
        if (found) break;
    }

    auto duration = duration_cast<microseconds>(high_resolution_clock::now() - start).count();

    cout << "Found " << answer << " in " << duration << " miliseconds." << endl;
    return 0;
}