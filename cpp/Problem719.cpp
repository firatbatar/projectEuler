#include <cmath>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

/*
Problem #719 - Number Splitting
*/

typedef unsigned long long int ulli;


vector<vector<ulli>> findPartition(ulli n, vector<vector<vector<ulli>>> &partitions) {
    if (partitions.size() >= n + 1) return partitions[n]; 

    vector<vector<ulli>> partition;

    for (ulli i = 1; i <= n; i++) {
        vector<vector<ulli>> subPartitions = findPartition(n - i, partitions);

        for (ulli j = 0; j < subPartitions.size(); j++) {
            vector<ulli> newPartition = subPartitions[j];
            newPartition.push_back(i);
            partition.push_back(newPartition);
        }
    }

    partitions.push_back(partition);
    return partition;
}

bool digitPartitionSums(ulli n, vector<vector<ulli>> &partition, ulli target) {
    for (ulli i = 0; i < partition.size(); i++) {
        vector<ulli> p = partition[i];
        if (p.size() <= 1) continue;

        string s = to_string(n);
        ulli sum = 0ull;

        for (ulli j = 0; j < p.size(); j++) {
            ulli start = j == 0 ? 0 : p[j - 1];
            ulli length = p[j];

            string sub = s.substr(start, length);
            sum += stoull(sub);

            p[j] += start;
        }

        if (sum == target) return true;
    }

    return false;
}


unsigned long long int solution() {
    const ulli N_exp = 12; // N = 10^N_exp
    const ulli sqrtN = pow(10, N_exp / 2);

    ulli answer = 0ull;

    vector<vector<vector<ulli>>> partitions = { { {} } };

    for (ulli i = 1; i <= sqrtN; i++) {
        ulli n = i * i;
    
        if (n % 9 != 0 && n % 9 != 1) continue;

        int digitCount = log10(n) + 1;  

        vector<vector<ulli>> partition = findPartition(digitCount, partitions);

        bool found = digitPartitionSums(n, partition, i);
    
        if (found) {
            cout << "Found: " << n << endl;
            answer += n;
        }
    } 
    return answer;
}
