#include <chrono>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;
using namespace std::chrono;

bool isPrime(int num) {
    static vector<int> primes = {2};

    bool is_prime = true;
    for (int prime : primes) {
        if (prime >= sqrt(num)) break;

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

    int answer = 0;

    long int num = 600851475143;
    for (long int div = 2; div <= num; div++) {
        if (isPrime(div) && num % div == 0) {
            answer = div;
            while (num % div == 0) num /= div;
        }
    }

    auto duration = duration_cast<microseconds>(high_resolution_clock::now() - start).count();

    cout << "Found " << answer << " in " << duration << " miliseconds." << endl;
    return 0;
}