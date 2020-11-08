N = int(input())
S = [] # Score
for _ in range(N):
  S.append(int(input()))

D = [[0,0] for _ in range(N)]
# D[i][j] = i번째 계단까지, j번째 연속된 발걸음으로 올랐을 때 점수
# D[i][0] = S[i]+max(D[i-2][0], D[i-2][1])
# D[i][1] = S[i]+D[i-1][0]
D[0]=[S[0], 0]
if N>=2:
  D[1]=[S[1], S[1]+D[0][0]]
for i in range(2, N):
  D[i][0] = S[i]+max(D[i-2][0], D[i-2][1])
  D[i][1] = S[i]+D[i-1][0]

# print(*D)
print(max(D[N-1]))
