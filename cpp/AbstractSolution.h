#ifndef ABSTRACT_SOLUTION_H
#define ABSTRACT_SOLUTION_H

#include <cstdint>
#include <string>

class AbstractSolution {
  public:
    AbstractSolution() {}
    virtual ~AbstractSolution() {}

    virtual std::string getProblemName() = 0;

    virtual std::uint64_t solveProblem() = 0;
};

#endif  // ABSTRACT_SOLUTION_H