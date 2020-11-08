N = int(input())
board = [input() for _ in range(N)]

foundHead = False
foundArm = False
left = True
leftArm = 0
rightArm = 0
back = 0
leftLeg = 0
rightLeg = 0
for i in range(N):
  for j in range(N):
    if board[i][j]=='*':
      if foundLeg:
        k=i
        while board[k][j]=='*':
          i+=1
          if left:
            leftLeg+=1
          else:
            rightLeg+=1
      elif 
print(*heart)
