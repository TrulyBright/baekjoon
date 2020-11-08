N = int(input())
L = []
for _ in range(N):
  L.append(list(map(int, input().split())))

D = [0]*N

for i in range(N):
  D[i]=[0]*(i+1)
D[0][0]=L[0][0]

for i in range(1, N):
  D[i][0]=L[i][0]+D[i-1][0]
  for j in range(1, i):
    D[i][j]=L[i][j]+max(D[i-1][j], D[i-1][j-1])
  D[i][i]=L[i][i]+D[i-1][i-1]
print(max(D[N-1]))
