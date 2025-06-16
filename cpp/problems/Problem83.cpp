#include <cmath>
#include <fstream>
#include <iostream>
#include <limits>
#include <sstream>
#include <string>
#include <vector>

typedef unsigned long long int int8;
typedef long double float16;

/*
Problem #83 - Path Sum: Four Ways

* Idea is to implement Dijkstra's algorithm

NOTE: Assumes a structure on the file: Expects spaces instead of commas in the file as seperators
*/

#define INF std::numeric_limits<int>::max()
enum Status { UNVISITED, VISITED };

typedef struct Cell {
  int m_cost = -1;
  int m_status = Status::UNVISITED;
  int m_dist = INF;

  Cell(int cost) : m_cost(cost) {}
} Cell;

bool operator<(const Cell &c1, const Cell &c2) { return c1.m_dist > c2.m_dist; }

class UpdateHeap {
 private:
  std::vector<Cell *> m_container;
  int m_size;

 private:
  int getParentIndex(int idx) const { return (idx > 0) ? (idx - 1) / 2 : -1; }

  int getLeftChildIndex(int idx) const { return 2 * idx + 1; }

  int getRightChildIndex(int idx) const { return 2 * idx + 2; }

  void maintainHeap(int idx) {
    while (true) {
      int left = this->getLeftChildIndex(idx);
      int right = this->getRightChildIndex(idx);

      int max = -1;

      if (left < this->m_size && right < this->m_size) {
        max = (*this->m_container[left] < *this->m_container[right]) ? right : left;
      }
      else if (left < this->m_size) {
        max = left;
      }
      else if (right < this->m_size) {
        max = right;
      }

      if (max == -1) break;
      if (*this->m_container[max] < *this->m_container[idx]) break;

      Cell *tmp = this->m_container[idx];
      this->m_container[idx] = this->m_container[max];
      this->m_container[max] = tmp;
      idx = max;
    }
  }

  void maintainHeapBottomUp(int idx) {
    while (true) {
      int parent = this->getParentIndex(idx);

      if (parent == -1) break;

      if (*this->m_container[parent] < *this->m_container[idx]) {
        Cell *tmp = this->m_container[idx];
        this->m_container[idx] = this->m_container[parent];
        this->m_container[parent] = tmp;
        idx = parent;
      }
      else {
        break;
      }
    }
  }

 public:
  UpdateHeap() : m_size(0) {}
  ~UpdateHeap() {}

  int size() const { return this->m_size; }

  bool empty() const { return this->m_size == 0; }

  void push(Cell *&value) {
    this->m_container.push_back(value);
    this->maintainHeapBottomUp(this->m_size++);
  }

  Cell *pop() {
    if (this->m_size == 0) throw std::out_of_range("The queue is empty");

    Cell *top = this->m_container[0];

    this->m_container[0] = this->m_container[--this->m_size];
    this->maintainHeap(0);
    this->m_container.resize(this->m_size);

    return top;
  }

  void updateValue(Cell *value) {
    int idx;
    for (idx = 0; idx < this->m_size; idx++) {
      if (this->m_container[idx] == value) break;
    }

    while (true) {
      int parent = this->getParentIndex(idx);

      if (parent == -1) break;

      Cell *tmp = this->m_container[idx];
      this->m_container[idx] = this->m_container[parent];
      this->m_container[parent] = tmp;
      idx = parent;
    }

    this->maintainHeap(0);
  }
};

std::vector<int> getNeighbours(const Cell *node, const std::vector<Cell *> matrix, const Cell *start, int size) {
  std::vector<int> neighbours;

  if (node == start && matrix[0]->m_status == Status::UNVISITED) {
    neighbours.push_back(0);
    return neighbours;
  }

  for (int idx = 0; idx < size * size; idx++) {
    if (node == matrix[idx]) {
      int up = idx - size;
      int down = idx + size;
      int left = idx - 1;
      int right = idx + 1;

      if (idx >= size && matrix[up]->m_status == Status::UNVISITED) neighbours.push_back(up);

      if (idx < (size - 1) * size && matrix[down]->m_status == Status::UNVISITED) neighbours.push_back(down);

      if (idx % size != 0 && matrix[left]->m_status == Status::UNVISITED) neighbours.push_back(left);

      if (idx % size != size - 1 && matrix[right]->m_status == Status::UNVISITED) neighbours.push_back(right);
      
      // Bottom right
      if (idx == size * size - 1) neighbours.push_back(-1);

      break;
    }
  }
 
  return neighbours;
}


float16 solution() {
  float16 answer = 0;

  const char *fileName = "../txt/p083_matrix.txt";
  const int SIZE = 80;

  std::vector<Cell *> matrixArray;

  std::ifstream file(fileName);
  if (!file.is_open()) {
    std::cerr << "Can't open file" << std::endl;
    exit(1);
  }

  std::string line;
  while (getline(file, line)) {
    std::stringstream lineStream(line);
    int num;

    while (lineStream >> num) matrixArray.push_back(new Cell(num));
  }
  file.close();

  Cell *start = new Cell(0);
  Cell *end = new Cell(0);

  /* Algorithms starts here */

  // Initilization
  UpdateHeap pq;

  start->m_dist = 0;

  for (int i = 0; i < SIZE * SIZE; i++) pq.push(matrixArray[i]);
  pq.push(start);
  pq.push(end);

  // Actual part
  while (!pq.empty()) {
    Cell *node = pq.pop();
    
    // Remaining elements are unreachable
    if (node->m_dist == INF) break;

    auto neighbours = getNeighbours(node, matrixArray, start, SIZE);

    for (auto idx : neighbours) {
      Cell *neighbour = (idx != -1) ? matrixArray[idx] : end;
      
      int newDist = node->m_dist + neighbour->m_cost;
      
      if (newDist < neighbour->m_dist) {
        neighbour->m_dist = newDist;
        pq.updateValue(neighbour);
      }
    }

    node->m_status = Status::VISITED;
  }

  answer = end->m_dist;

  // Clearing
  for (int i = 0; i < SIZE * SIZE; i++) delete matrixArray[i];
  delete start;
  delete end;

  return answer;
}
