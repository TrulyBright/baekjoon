import queue
T = int(input())

dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)
def notOutOfBoard(y, x):
  return 0<=y and y<N and 0<=x and x<M

def BFS(v):
  Q = queue.Queue()
  Q.put(v)
  board[v[0]][v[1]]=False
  while not Q.empty():
    v = Q.get()
    for i in range(4):
      nextY = v[0]+dy[i]
      nextX = v[1]+dx[i]
      if notOutOfBoard(nextY, nextX) and board[nextY][nextX]:
        board[nextY][nextX]=False
        Q.put((nextY, nextX))

M = N = K = 0
for _ in range(T):
  M, N, K = map(int, input().split())
  count=0
  board = [[False]*M for _ in range(N)]
  for _ in range(K):
    X, Y = map(int, input().split())
    board[Y][X]=True
  for y in range(N):
    for x in range(M):
      if board[y][x]:
        BFS((y, x))
        count+=1
  print(count)
