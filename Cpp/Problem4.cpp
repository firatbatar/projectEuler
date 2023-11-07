#include <chrono>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;
using namespace std::chrono;

bool isPalindrome(int num) {
    string numStr = to_string(num);

    int startIdx = 0;
    int endIdx = numStr.size() - 1;
    while (startIdx < endIdx) {
        if (numStr.at(startIdx) != numStr.at(endIdx)) return false;

        startIdx++;
        endIdx--;
    }

    return true;
}

int main() {
    // Timer
    auto start = high_resolution_clock::now();

    int answer = -1;

    for (int i = 100; i < 1000; i++) {
        for (int j = 100; j < 1000; j++) {
            int product = i * j;
            if (isPalindrome(product)) {
                if (product > answer) answer = product;
            }
        }
    }

    auto duration = duration_cast<microseconds>(high_resolution_clock::now() - start).count();

    cout << "Found " << answer << " in " << duration << " miliseconds." << endl;
    return 0;
}