N = int(input())
image = []
for _ in range(N):
  image.append(input())
answer = []
def cut(y, x, length): # (y, x)=top-left corner
  color = image[y][x]
  needToCut = False
  for i in range(y, y+length):
    for j in range(x, x+length):
      if image[i][j]!=color:
        needToCut=True
        break
  if needToCut:
    length//=2
    answer.append('(')
    cut(y, x, length)
    cut(y, x+length, length)
    cut(y+length, x, length)
    cut(y+length, x+length, length)
    answer.append(')')
  else:
    answer.append(color)
cut(0, 0, N)
print(''.join(answer))
