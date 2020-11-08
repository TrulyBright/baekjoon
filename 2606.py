N = int(input())
M = int(input())
connected = [set() for _ in range(N+1)]
visited = [False]*(N+1)
for _ in range(M):
  A, B = map(int, input().split())
  connected[A].add(B)
  connected[B].add(A)
infected=0
def DFS(v):
  global infected
  visited[v]=True
  for next in range(1, N+1):
    if next in connected[v] and not visited[next]:
      infected+=1
      DFS(next)
DFS(1)
print(infected)
