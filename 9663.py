N = int(input())

queens = [] # 여태껏 놓은 퀸들의 좌표가 (y, x) 꼴로 들어가는 리스트
result = 0

def place(placed):
  global result
  if placed==N:
    result+=1
    return
  for i in range(0, N):
    currentQueen = (placed, i)
    for queen in queens:
      if currentQueen[1]==queen[1] or abs(currentQueen[0]-queen[0])==abs(currentQueen[1]-queen[1]):
        break
    else:
      queens.append(currentQueen)
      place(placed+1)
      queens.pop()

place(0)
print(result)
