import sys
N = int(input())
A = set(map(int, sys.stdin.readline().split()))
M = int(input())
X = list(map(int, sys.stdin.readline().split()))
for i in X:
  print(int(i in A))
