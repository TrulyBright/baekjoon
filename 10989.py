from sys import stdin
N = int(stdin.readline())
L = [0]*10001
for _ in range(N):
  L[int(stdin.readline())]+=1
for i in range(10001):
  for j in range(L[i]):
    print(i)
