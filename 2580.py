board = [0]*9
coordinates_of_0 = []
found = False
for i in range(9):
  board[i] = list(map(int, input().split()))
  for j in range(9):
    if board[i][j]==0:
      coordinates_of_0.append((i, j))
count_0 = len(coordinates_of_0)

def f(i, x, number):
  if x//3==0:
    for j in range(0, 3):
      if board[i][j]==number:
        return False
  elif x//3==1:
    for j in range(3, 6):
      if board[i][j]==number:
        return False
  else:
    for j in range(6, 9):
      if board[i][j]==number:
        return False
  return True


def insertable(y, x, number):
  # print(f"{y}, {x}, {number}")
  if number in board[y]: # 가로
    return False
  for i in range(9): # 세로
    if board[i][x]==number:
      return False
  if y//3==0: # 정사각형
    for i in range(0, 3):
      if not f(i, x, number):
        return False
  elif y//3==1:
    for i in range(3, 6):
      if not f(i, x, number):
        return False
  else:
    for i in range(6, 9):
      if not f(i, x, number):
        return False
  return True

def solve(y, x, number, inserted): # inserted: 지금까지 채워넣은 숫자의 개수
  # (y, x)에 number가 놓였을 때
  global found
  if found:
    return
  if not insertable(y, x, number):
    return
  board[y][x] = number
  if inserted == count_0-1:
    for i in range(9):
      print(*board[i])
    found = True
    return
  # print(f"{y}, {x}, {number}, {inserted}")
  nextY = coordinates_of_0[inserted+1][0]
  nextX = coordinates_of_0[inserted+1][1]
  # print(f"{nextY}, {nextX}")
  for i in range(1, 10):
    solve(nextY, nextX, i, inserted+1)
    board[nextY][nextX]=0

firstY = coordinates_of_0[0][0]
firstX = coordinates_of_0[0][1]
for i in range(1, 10):
  solve(firstY, firstX, i, 0)
# for crd in coordinates_of_0:
#   print(crd, end=':')
#   for number_inserted in range(1, 10):
#     if insertable(crd[0], crd[1], number_inserted):
#       print(number_inserted, end=' ')
#   print()
