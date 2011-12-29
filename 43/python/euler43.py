#!/usr/bin/env pypy

# Solution to Project Euler problem 43.
# Will Brown (haldean.org)
# Timing data:
#   PyPy: 3.29 seconds
#   CPython 2.7.1: 16.47 seconds
#   CPython 3.2.2: 20.31 seconds

import itertools

def permutations(length):
  return itertools.permutations(str(x) for x in range(length + 1))

def concat(num, d1):
  return int(num[d1:d1+3])

def match(num):
  return (
      concat(num, 2) % 2 == 0 and
      concat(num, 3) % 3 == 0 and
      concat(num, 4) % 5 == 0 and
      concat(num, 5) % 7 == 0 and
      concat(num, 6) % 11 == 0 and
      concat(num, 7) % 13 == 0 and
      concat(num, 8) % 17 == 0)

def prob43():
  found = []
  for perm in permutations(9):
    string = ''.join(perm)
    if match(string):
      found.append(int(string))
  print(sum(found))

if __name__ == '__main__':
  prob43()

