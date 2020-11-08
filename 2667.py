N = int(input())
board = []
for _ in range(N):
  board.append(list(input()))

count = 0
houses = []
dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)

def checkIfOutOfBoard(y, x):
  return 0<=y and y<N and 0<=x and x<N

def DFS(y, x, count):
  board[y][x]='0'
  houses[count]+=1
  for i in range(4):
    nextX = x+dx[i]
    nextY = y+dy[i]
    if checkIfOutOfBoard(nextY, nextX) and board[nextY][nextX]=='1':
      DFS(nextY, nextX, count)

for i in range(N):
  for j in range(N):
    if board[i][j]=='1':
      houses.append(0)
      DFS(i, j, count)
      count+=1

houses.sort()
print(count)
for number in houses:
  print(number)
