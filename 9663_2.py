N = int(input())
column = [False]*N
diagonal1 = [False]*(2*N-1)
diagonal2 = [False]*(2*N-1)
result = 0

def place(placed):
  global result
  if placed==N:
    result+=1
    return
  for i in range(N):
    if not column[i] and not diagonal1[placed+i] and not diagonal2[N-1-placed+i]:
      column[i]=diagonal1[placed+i]=diagonal2[N-1-placed+i]=True
      place(placed+1)
      column[i]=diagonal1[placed+i]=diagonal2[N-1-placed+i]=False
place(0)

print(result)
