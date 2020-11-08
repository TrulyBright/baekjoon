N = int(input())
L = []
for _ in range(N):
  L.append(list(map(int, input().split())))

D = [0]*N

for i in range(N):
  D[i]=[None]*(i+1)
D[0][0]=L[0][0]

def TopDOWN(i, j):
  if D[i][j] is not None: return D[i][j]
  if j==0:
    D[i][j]=L[i][j]+TopDOWN(i-1, j)
    return D[i][j]
  if j==i:
    D[i][i]=L[i][i]+TopDOWN(i-1, j-1)
    return D[i][j]
  D[i][j]=L[i][j]+max(TopDOWN(i-1, j), TopDOWN(i-1, j-1))
  return D[i][j]

for i in range(0, N):
  TopDOWN(N-1, i)
print(max(D[N-1]))
