N = int(input())
board = []
negative = zero = positive = 0
for _ in range(N):
  board.append(list(map(int, input().split())))
answer = []
def cut(y, x, length): # (y, x)=top-left corner
  global negative, zero, positive
  color = board[y][x]
  needToCut = False
  for i in range(y, y+length):
    for j in range(x, x+length):
      if board[i][j]!=color:
        needToCut=True
        break
  if needToCut:
    length//=3
    dx=[0, 0, 0, 1, 1, 1, 2, 2, 2]
    dy=[0, 1, 2, 0, 1, 2, 0, 1, 2]
    for i in range(9):
      cut(y+length*dy[i], x+length*dx[i], length)
  else:
    if color==-1: negative+=1
    elif color==0: zero+=1
    else: positive+=1
cut(0, 0, N)
print(negative)
print(zero)
print(positive)
