DIV = 10**9

N = int(input())
D = [[0,0,0,0,0,0,0,0,0,0] for _ in range(N+1)]
D[1]=[0,1,1,1,1,1,1,1,1,1]
# D[N][i]: 길이가 N이고 끝이 i로 끝나는 계단 수
# D[N][0] = D[N-1][1]
# D[N][1] = D[N-1][0]+D[N-1][2]
# D[N][2] = D[N-1][1]+D[N-1][3]
# ...
# D[N][9] = D[N-1][8]

for i in range(2, N+1):
  D[i][0] = D[i-1][1]
  for j in range(1, 9):
    D[i][j] = D[i-1][j-1]+D[i-1][j+1]
  D[i][9] = D[i-1][8]
  for j in range(10):
    D[i][j]%=DIV

print(sum(D[N])%DIV)
