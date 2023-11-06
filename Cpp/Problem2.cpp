#include <iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;

int main() {
    // Timer
    auto start = high_resolution_clock::now();

    int answer = 0;
    int fib1 = 1, fib2 = 1;
    int limit = 4000000;

    while (fib2 < limit) {
        int temp = fib2;
        fib2 += fib1;
        fib1 = temp;

        if (fib2 % 2 == 0) answer += fib2;
    }

    auto duration = duration_cast<microseconds>(high_resolution_clock::now() - start).count();

    cout << "Found " << answer << " in " << duration << " miliseconds." << endl;
    return 0;
}