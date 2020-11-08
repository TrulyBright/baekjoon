import queue
N, M = map(int, input().split())
visited = [[False]*M for _ in range(N)]
maze = []
for i in range(N):
  maze.append(input())

def notOutOfBoard(y, x):
  return 0<=y and y<N and 0<=x and x<M

Q = queue.Queue()
Q.put((0, 0, 1)) # (y, x, lengthOfRoute)
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
result = 100*100
while not Q.empty():
  v = Q.get()
  if v[0]==N-1 and v[1]==M-1:
    result = min(result, v[2])
  for i in range(4):
    nextY = v[0]+dy[i]
    nextX = v[1]+dx[i]
    if notOutOfBoard(nextY, nextX) and maze[nextY][nextX]=='1' and not visited[nextY][nextX]:
      Q.put((nextY, nextX, v[2]+1))
      visited[nextY][nextX]=True
      
print(result)
