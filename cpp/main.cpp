#include <AbstractSolution.h>
#include <chrono>
#include <iostream>

using namespace std;
using namespace std::chrono;

extern AbstractSolution *solution;

int main() {
  auto start = high_resolution_clock::now();

  long double answer = solution->solveProblem();

  auto duration = duration_cast<microseconds>(high_resolution_clock::now() - start).count();

  cout << "Solved '" << solution->getProblemName() << "' as " << answer << " in " << duration << " microseconds." << endl;
  return 0;
}