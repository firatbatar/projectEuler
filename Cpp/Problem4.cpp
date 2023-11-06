#include <iostream>
#include <vector>
#include <chrono>
#include <cmath>
using namespace std;
using namespace std::chrono;

bool isPrime(int num) {
    static vector<int> primes = {2};

    bool is_prime = true;
    for (int prime : primes) {
        if (prime > sqrt(num)) break;

        if (num % prime == 0) {
            is_prime = false;
            break;
        }
    }

    if (is_prime) {
        primes.push_back(num);
    }

    return is_prime;
}

int main() {
    // Timer
    auto start = high_resolution_clock::now();

    int answer = 1;
    
    int limit = 20;
    for (int num = 2; num <= limit; num++) {
        if (isPrime(num)) {
            int mult = 1;
            while (mult * num <= limit) mult *= num;
            answer *= (mult);
        }
    }

    auto duration = duration_cast<microseconds>(high_resolution_clock::now() - start).count();

    cout << "Found " << answer << " in " << duration << " miliseconds." << endl;
    return 0;
}