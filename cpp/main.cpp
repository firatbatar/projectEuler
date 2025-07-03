#include <AbstractSolution.h>
#include <cstdint>
#include <chrono>
#include <iostream>

using namespace std;
using namespace std::chrono;

extern AbstractSolution *solution;

int main() {
  auto start = high_resolution_clock::now();

  uint64_t answer = solution->solveProblem();

  auto duration = duration_cast<microseconds>(high_resolution_clock::now() - start).count();

  cout << fixed << "Solved '" << solution->getProblemName() << "' as " << answer << " in " << duration << " microseconds." << endl;
  return 0;
}