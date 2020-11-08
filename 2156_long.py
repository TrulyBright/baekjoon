import sys
N = int(sys.stdin.readline())
W = [] # Wines
D = [[0,0] for _ in range(N)]
# D[N][i]: 직전 i개 잔을 연속으로 마신 상태에서 N번째 잔을 마셨을 때 총량
# D[N][0]=W[N]+max(여태껏 나온 모든 D[i][0], D[i][1], 단 i는 N-2까지)
# D[N][1]=W[N]+D[N-1][0]
for _ in range(N):
  W.append(int(sys.stdin.readline()))

D[0]=[W[0], W[0]]
if N>=2:
  D[1]=[W[1], D[0][0]+W[1]]


for i in range(2, N):
  maximum = 0
  for j in range(0, i-1):
    maximum = max(maximum, D[j][0], D[j][1])
  print(f"maximum at {i-2}: {maximum}")
  D[i][0]=W[i]+maximum
  D[i][1]=W[i]+D[i-1][0]

maximum = 0
for i in D:
  for j in i:
    maximum = max(j, maximum)
print(maximum)
