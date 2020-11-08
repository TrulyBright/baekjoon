from sys import stdin
N = int(stdin.readline())
L = []
for _ in range(N):
  L.append(int(stdin.readline()))
L.sort()
for i in L:
  print(i)
