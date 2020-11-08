N = int(input())
cost = [0 for _ in range(N+1)]

for i in range(1, N+1):
  cost[i] = list(map(int, input().split()))

D = [[0]*3 for _ in range(N+1)]

D[1]=cost[1]
for i in range(2, N+1):
  D[i][0]=cost[i][0]+min(D[i-1][1], D[i-1][2])
  D[i][1]=cost[i][1]+min(D[i-1][0], D[i-1][2])
  D[i][2]=cost[i][2]+min(D[i-1][0], D[i-1][1])

print(min(D[N]))
