import queue
import sys

N, M = map(int, sys.stdin.readline().split())
board = []
distance = [[0x7fffffff]*M]
result = 0x7fffffff
for _ in range(N):
  board.append(list(map(int, list(sys.stdin.readline().strip()))))
# print(board)
def inBoard(y, x):
  return 0<=y and y<N and 0<=x and x<M

Q = queue.Queue()
Q.put((0, 0, False, 1)) # (y, x, didDestroyAWall, lengthOfRoute)
dx = 0, 1, 0, -1
dy = -1, 0, 1, 0
while not Q.empty():
  v = Q.get()
  visited[v[0]][v[1]]=True
  if v[0]==N-1 and v[1]==M-1:
    result = min(result, v[3])
  for i in range(4):
    nextY = v[0]+dy[i]
    nextX = v[1]+dx[i]
    # print(v, nextY, nextX)
    if inBoard(nextY, nextX) and not visited[nextY][nextX]:
      if v[2] and board[nextY][nextX]!=1:
        Q.put((nextY, nextX, True, v[3]+1))
      elif not v[2]:
        Q.put((nextY, nextX, board[nextY][nextX]==1, v[3]+1))

print(-1 if result==0x7fffffff else result)
