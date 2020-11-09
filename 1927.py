import sys
import heapq
heap = []

N = int(sys.stdin.readline().strip())

for _ in range(N):
  x = int(sys.stdin.readline().strip())
  if x==0:
    print(heapq.heappop(heap) if heap else 0)
  else:
    heapq.heappush(heap, x)
