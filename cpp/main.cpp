#include <chrono>
#include <iostream>

using namespace std;
using namespace std::chrono;

extern long double solution();

int main() {
    auto start = high_resolution_clock::now();

    long double answer = solution();

    auto duration = duration_cast<microseconds>(high_resolution_clock::now() - start).count();

    cout << "Found " << answer << " in " << duration << " microseconds." << endl;
    return 0;
}