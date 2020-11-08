# 브루트 포스
import sys
N = int(input())
C = []
for _ in range(N):
  start, end = map(int, sys.stdin.readline().split())
  C.append((start, end))
C = sorted(C, key=lambda p: p[0])

count = 0
def pick(index, picked):
  global count, N
  if index==N:
    for i in range(len(picked)-1):
      if picked[i][1]>picked[i+1][0]:
        break
    else:
      count = max(count, len(picked))
    return
  pick(index+1, picked+[C[index]])
  pick(index+1, picked)
pick(0, [])
print(count)
