#include <AbstractSolution.h>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <string>

/*
  Problem 932 // 2025

  We only need to check perfect squares.

  Check from 1 to n/2 digit numbers' squares
*/

typedef std::uint64_t int64;

class Problem932 : public AbstractSolution {
 public:
  virtual std::string getProblemName() { return "Problem 932 // 2025"; }

  virtual std::uint64_t solveProblem() {
    int64 answer = 0;

    const int n = 16;

    std::string temp = "";
    for (int i = 0; i < (n + 1) / 2; i++) temp += "9";

    const int64 start = 4;                     // First number to generate a 2-digit square
    const int64 end = atoi(temp.c_str()) + 1;  // Last number to not generate a (n+1)-digit square

    for (int64 base = start; base <= end; base++) {
      int digits = 2 * std::log10(base) + 1;
      if (digits > n) break;

      int64 num = std::pow(base, 2);

      if (num == 88209) {
        std::cout << "";
      }

      if (digits % 2 == 0) {  // Only split from middle
        int64 midPow10 = std::pow(10ull, digits / 2);

        int64 n1 = num / midPow10;
        int64 n2 = num % midPow10;

        if (n1 == 0 || n2 == 0) continue;

        int concatDigits = (int)std::log10(n1) + (int)std::log10(n2) + 2;
        if (concatDigits != digits) continue;

        if (n1 + n2 == base) {
          std::cout << "(" << n1 << " + " << n2 << ") = " << num << std::endl;
          answer += num;
        }
      }
      else {  // Has 2 "mid" points
        int64 midPow10First = std::pow(10ull, (digits - 1) / 2);

        int64 n1 = num / midPow10First;
        int64 n2 = num % midPow10First;

        int concatDigits = (int)std::log10(n1) + (int)std::log10(n2) + 2;
        if (!(n1 == 0 || n2 == 0 || concatDigits != digits)) {
          if (n1 + n2 == base) {
            std::cout << "(" << n1 << " + " << n2 << ") = " << num << std::endl;
            answer += num;
            continue;
          }
        }

        int64 midPow10Second = std::pow(10ull, (digits + 1) / 2);

        n1 = num / midPow10Second;
        n2 = num % midPow10Second;

        if (n1 == 0 || n2 == 0) continue;

        concatDigits = (int)std::log10(n1) + (int)std::log10(n2) + 2;
        if (concatDigits != digits) continue;

        if (n1 + n2 == base) {
          std::cout << "(" << n1 << " + " << n2 << ") = " << num << std::endl;
          answer += num;
        }
      }
    }

    return answer;
  }
};

AbstractSolution *solution = new Problem932();

#include "../main.cpp"