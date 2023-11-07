#include <chrono>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;
using namespace std::chrono;

int main() {
    // Timer
    auto start = high_resolution_clock::now();

    int answer = 0;

    int limit = 100;
    for (int i = 1; i <= limit; i++) {
        for (int j = 1; j <= limit; j++) {
            if (i == j) continue;

            answer += i * j;
        }
    }

    auto duration = duration_cast<microseconds>(high_resolution_clock::now() - start).count();

    cout << "Found " << answer << " in " << duration << " miliseconds." << endl;
    return 0;
}