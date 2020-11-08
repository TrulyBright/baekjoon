board = [[0]*2188 for _ in range(2188)]

def draw(x, y, width, center):
  if center:
    board[y][x]=' '
  if width==1:
    board[y][x]=' ' if center else '*'
    return
  width//=3
  draw(y, x, width, center)
  draw(y, x+width, width, center)
  draw(y, x+width*2, width, center)
  draw(y+width, x, width, center)
  draw(y+width, x+width, width, True)
  draw(y+width, x+width*2, width, center)
  draw(y+width*2, x, width, center)
  draw(y+width*2, x+width, width, center)
  draw(y+width*2, x+width*2, width, center)

N = int(input())
draw(1, 1, N+1, False)

for i in range(1, N+1):
  for j in range(1, N+1):
    print(board[i][j], end='')
  print()
