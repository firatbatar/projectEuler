#include <chrono>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;
using namespace std::chrono;

int main() {
    // Timer
    auto start = high_resolution_clock::now();

    long int answer = 0;
    int limit = 2 * pow(10, 6);

    vector<int> primes = {2};
    for (int num = 2; num < limit; num++) {
        bool isPrime = true;
        for (int prime : primes) {
            if (prime > sqrt(num)) break;
            if (num % prime == 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime) {
            primes.push_back(num);
            answer += num;
        }
    }

    auto duration = duration_cast<microseconds>(high_resolution_clock::now() - start).count();

    cout << "Found " << answer << " in " << duration << " milliseconds." << endl;
    return 0;
}