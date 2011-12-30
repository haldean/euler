#!/usr/bin/env pypy

# Solution to Project Euler problem 23.
# Will Brown (haldean.org)
# Timing data:
#   PyPy: 6.53 seconds
#   CPython 2.7.1: 134.71 seconds
#   CPython 3.2.2: 169.68 seconds

from __future__ import division

def isabundant(n):
  return sum(filter(lambda x: n / x == n // x, range(1, n // 2 + 1))) > n

def allabundant(maxn):
  ab = []
  for i in range(maxn):
    if isabundant(i):
      ab.append(i)
  return ab

def filtersums(ab, maxn):
  sums = [True] * maxn 
  for ab1 in ab:
    for ab2 in ab:
      if ab1 + ab2 < maxn:
        sums[ab1 + ab2] = False

  nums = []
  for i, include in enumerate(sums):
    if include:
      nums.append(i)
  return nums

if __name__ == '__main__':
  maxn = 28123
  ab = allabundant(maxn)
  nums = filtersums(ab, maxn)
  print(sum(nums))
