#include <AbstractSolution.h>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

/*
Problem #719 - Number Splitting
*/

class Problem719 : public AbstractSolution {
 private:
  std::vector<std::vector<std::uint64_t>> findPartition(
      std::uint64_t n, std::vector<std::vector<std::vector<std::uint64_t>>> &partitions) {
    if (partitions.size() >= n + 1) return partitions[n];

    std::vector<std::vector<std::uint64_t>> partition;

    for (std::uint64_t i = 1; i <= n; i++) {
      std::vector<std::vector<std::uint64_t>> subPartitions = findPartition(n - i, partitions);

      for (std::uint64_t j = 0; j < subPartitions.size(); j++) {
        std::vector<std::uint64_t> newPartition = subPartitions[j];
        newPartition.push_back(i);
        partition.push_back(newPartition);
      }
    }

    partitions.push_back(partition);
    return partition;
  }

  bool digitPartitionSums(std::uint64_t n, std::vector<std::vector<std::uint64_t>> &partition,
                          std::uint64_t target) {
    for (std::uint64_t i = 0; i < partition.size(); i++) {
      std::vector<std::uint64_t> p = partition[i];
      if (p.size() <= 1) continue;

      std::string s = std::to_string(n);
      std::uint64_t sum = 0ull;

      for (std::uint64_t j = 0; j < p.size(); j++) {
        std::uint64_t start = j == 0 ? 0 : p[j - 1];
        std::uint64_t length = p[j];

        std::string sub = s.substr(start, length);
        sum += stoull(sub);

        p[j] += start;
      }

      if (sum == target) return true;
    }

    return false;
  }

 public:
  virtual std::string getProblemName() { return "Problem #719 - Number Splitting"; }

  virtual std::uint64_t solveProblem() {
    const std::uint64_t N_exp = 12;  // N = 10^N_exp
    const std::uint64_t sqrtN = pow(10, N_exp / 2);

    std::uint64_t answer = 0ull;

    std::vector<std::vector<std::vector<std::uint64_t>>> partitions = {{{}}};

    for (std::uint64_t i = 1; i <= sqrtN; i++) {
      std::uint64_t n = i * i;

      if (n % 9 != 0 && n % 9 != 1) continue;

      int digitCount = log10(n) + 1;

      std::vector<std::vector<std::uint64_t>> partition = findPartition(digitCount, partitions);

      bool found = digitPartitionSums(n, partition, i);

      if (found) {
        std::cout << "Found: " << n << std::endl;
        answer += n;
      }
    }
    return answer;
  }
};

AbstractSolution *solution = new Problem719();

#include "../main.cpp"