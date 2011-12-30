#!/usr/bin/env pypy

# Solution to Project Euler problem 35.
# Will Brown (haldean.org)
# Timing data:
#   PyPy: 1.19 seconds
#   CPython 2.7.1: 6.67 seconds
#   CPython 3.2.2: 10.61 seconds

def sieve(maxn):
  primes = [True] * maxn
  for i in range(2, maxn):
    n = 2
    while i * n < maxn:
      primes[i * n] = False
      n += 1

  pr = []
  for i, isprime in enumerate(primes):
    if isprime:
      pr.append(i)

  return pr

def rotations(p):
  pstr = str(p)
  rots = []
  for i in range(1, len(pstr)):
    rots.append(int(pstr[i:] + pstr[:i]))
  return rots

def circulars(pr):
  prset = set(pr)
  circs = []
  for p in pr:
    rots = rotations(p)
    if all(x in prset for x in rots) and p != 0 and p != 1:
      circs.append(p)
  return circs

if __name__ == '__main__':
  print(len(circulars(sieve(1000000))))
