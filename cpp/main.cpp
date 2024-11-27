#include <chrono>
#include <iostream>

using namespace std;
using namespace std::chrono;

extern unsigned long long int solution();

int main() {
    auto start = high_resolution_clock::now();

    unsigned long long int answer = solution();

    auto duration = duration_cast<microseconds>(high_resolution_clock::now() - start).count();

    cout << "Found " << answer << " in " << duration << " microseconds." << endl;
    return 0;
}