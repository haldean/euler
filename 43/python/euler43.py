#!/usr/bin/env pypy
import itertools

def permutations(length):
  return itertools.permutations(str(x) for x in range(length + 1))

def concat(num, d1, d2, d3):
  return int(d(num, d1) + d(num, d2) + d(num, d3))

def d(num, digit):
  return str(num)[digit-1]

def match(num):
  return (
      concat(num, 2, 3, 4) % 2 == 0 and
      concat(num, 3, 4, 5) % 3 == 0 and
      concat(num, 4, 5, 6) % 5 == 0 and
      concat(num, 5, 6, 7) % 7 == 0 and
      concat(num, 6, 7, 8) % 11 == 0 and
      concat(num, 7, 8, 9) % 13 == 0 and
      concat(num, 8, 9, 10) % 17 == 0)

def prob43():
  found = []
  for perm in permutations(9):
    string = ''.join(perm)
    if match(string):
      found.append(int(string))
  print(sum(found))

if __name__ == '__main__':
  prob43()

