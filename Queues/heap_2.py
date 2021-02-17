import math
# Add any extra import statements you may need here
import sys


# Add any helper functions you may need here
class CandyHeap:
    def __init__(self, arr):
        self.heap = []
        for x in arr:
            self.add(x)

    def add(self, x):
        self.heap.append(x)
        self.heap_up(self.last_pos())

    def pop(self):
        if not self.heap:
            return
        top = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heap_down(0)
        return top

    def heap_up(self, pos):
        if pos == 0:
            return
        posp, xp = self.get_parent(pos)
        if self.heap[pos] > xp:
            self.swap(posp, pos)
            self.heap_up(posp)

    def heap_down(self, pos):
        posc, xc = self.get_biggest_child(pos)
        if xc is not None and self.heap[pos] < xc:
            self.swap(pos, posc)
            self.heap_down(posc)

    def swap(self, pos1, pos2):
        x = self.heap[pos1]
        self.heap[pos1] = self.heap[pos2]
        self.heap[pos2] = x

    def last_pos(self):
        return len(self.heap) - 1

    def get_parent(self, pos):
        pos = (pos - 1) // 2
        return pos, self.heap[pos]

    def get_biggest_child(self, pos):
        pos1 = 2 * pos + 1
        pos2 = 2 * pos + 2
        x1 = None if pos1 > self.last_pos() else self.heap[pos1]
        x2 = None if pos2 > self.last_pos() else self.heap[pos2]
        if x1 is None and x2 is None:
            return pos1, None
        elif x1 is None:
            return pos2, x2
        elif x2 is None:
            return pos1, x1
        elif x1 > x2:
            return pos1, x1
        elif x2 > x1:
            return pos2, x2
        elif x2 == x1:
            return pos1, x1
        else:
            sys.exit("Something Went wrong!")


def maxCandies(arr, k):
    # Write your code here
    ch = CandyHeap(arr)

    res = 0
    for _ in range(k):
        n_candy = ch.pop()
        res += n_candy
        ch.add(n_candy // 2)
    return res





# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1, k_1 = 5, 3
  arr_1 = [2, 1, 7, 4, 2]
  expected_1 = 14
  output_1 = maxCandies(arr_1, k_1)
  check(expected_1, output_1)

  n_2, k_2 = 9, 3
  arr_2 = [19, 78, 76, 72, 48, 8, 24, 74, 29]
  expected_2 = 228
  output_2 = maxCandies(arr_2, k_2)
  check(expected_2, output_2)

  # Add your own test cases here
  