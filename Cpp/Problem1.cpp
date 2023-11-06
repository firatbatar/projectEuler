#include <iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;

int main() {
    // Timer
    auto start = high_resolution_clock::now();


    int limit = 1000;
    unsigned int sum = 0;
    for (int num = 1; num < limit; num++) {
        if (num % 3 == 0 || num % 5 == 0) {
            sum += num;
        }
    }


    auto duration = duration_cast<microseconds>(high_resolution_clock::now() - start).count();

    cout << "Found " << sum << " in " << duration << " miliseconds." << endl;
    return 0;
}