# DP
N, K = map(int, input().split())
item = [(0, 0)]
for _ in range(N):
  W, V = map(int, input().split())
  item.append((W, V))
D = [[0]*(K+1) for _ in range(N+1)]
# D[number][maxWeight]: 물건을 number번째까지 고려했고 가방의 용량이 maxWeight일 때 최적해
# D[number][maxWeight]
result = 0
for i in range(1, N+1):
  for j in range(1, K+1):
    if item[i][0] > j:
      D[i][j]=D[i-1][j]
    elif i==0:
      D[i][j]=item[i][1]
    else:
      D[i][j]=max(D[i-1][j], D[i-1][j-item[i][0]]+item[i][1])
  result = max(result, D[i][j])
print(result)
