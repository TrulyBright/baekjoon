import queue
N, M, V = map(int, input().split())
connected = [[False]*(N+1) for _  in range(N+1)]
visited = [False]*(N+1)
for _ in range(M):
  a, b = map(int, input().split())
  connected[a][b]=connected[b][a]=True

def DFS(v):
  visited[v]=True
  print(v, end=' ')
  for next in range(1, N+1):
    if connected[v][next] and not visited[next]:
      DFS(next)


def BFS(v):
  Q = queue.Queue()
  Q.put(v)
  visited[v]=True
  while not Q.empty():
    current = Q.get()
    print(current, end=' ')
    for next in range(1, N+1):
      if connected[current][next] and not visited[next]:
        visited[next]=True
        Q.put(next)

DFS(V)
print()
visited = [False]*(N+1)
BFS(V)
