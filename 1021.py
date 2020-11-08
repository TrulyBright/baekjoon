from collections import deque
D = deque()
N, M = map(int, input().split())
for i in range(1, N+1): D.append(i)

L = map(int, input().split())

count = 0
for n in L:
  if D[0]==n:
    D.popleft()
  else:
    subD = D.copy()
    count2=0
    count3=0
    while D[0]!=n:
      D.rotate(-1)
      count2+=1
    D = subD.copy()
    while D[0]!=n:
      D.rotate(1)
      count3+=1
    D = subD.copy()
    if count2>count3:
      D.rotate(count3)
      D.popleft()
      count+=count3
    else:
      D.rotate(-count2)
      D.popleft()
      count+=count2


print(count)
