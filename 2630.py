N = int(input())
board = []
for i in range(N):
  board.append(list(map(int, input().split())))
white = 0
blue = 0

def cut(y, x, length): # (y, x)=top-left corner
  global white, blue
  color = board[y][x]
  needToCut = False
  for i in range(y, y+length):
    for j in range(x, x+length):
      if board[i][j]!=color:
        needToCut=True
        break
  if needToCut:
    length//=2
    cut(y, x, length)
    cut(y+length, x, length)
    cut(y, x+length, length)
    cut(y+length, x+length, length)
  else:
    if color==0: white+=1
    else: blue+=1
cut(0, 0, N)
print(white)
print(blue)
