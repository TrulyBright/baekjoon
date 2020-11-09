import sys
import heapq
heap = []

N = int(sys.stdin.readline().strip())
for i in range(N):
  n = int(sys.stdin.readline().strip())
  heapq.heappush(heap, n)
  copied = heap[:]
  for j in range(i//2):
    heapq.heappop(copied)
  print(heapq.heappop(copied), end=' ')
