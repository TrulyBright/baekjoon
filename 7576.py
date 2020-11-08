import queue
import sys

M, N = map(int, sys.stdin.readline().split())
box = []
Q = queue.Queue()
for i in range(N):
  box.append(list(map(int, sys.stdin.readline().split())))
  for j in range(M):
    if box[i][j]==1:
      Q.put((i, j, 0))

result = 0

def notOutOfBox(y, x):
  return 0<=y and y<N and 0<=x and x<M

dy = -1, 0, 1, 0
dx = 0, 1, 0, -1
while not Q.empty():
  v = Q.get()
  result = max(result, v[2])
  for i in range(4):
    nextY = v[0]+dy[i]
    nextX = v[1]+dx[i]
    if notOutOfBox(nextY, nextX) and box[nextY][nextX]==0:
      Q.put((nextY, nextX, v[2]+1))
      box[nextY][nextX]=1

failed = False
for i in range(N):
  if not failed:
    for j in range(M):
      if box[i][j]==0:
        failed = True
        break
print(-1 if failed else result)
