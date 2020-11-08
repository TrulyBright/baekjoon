import sys
# import random
# random.seed()
N = int(input())
S = list(map(int, sys.stdin.readline().split()))
# S = [random.randint(-1000, 1000) for _ in range(N)]
D = [0]*N
D[0]=S[0]
# D[i]=S[i]를 맨 오른쪽으로 하는 연속부분수열 중 가장 합이 큰 것의 합
# D[i]=max(D[i-1]+S[i], S[i])

# # 브루트포스
# maximum = -1000
# for i in range(0, N):
#   for j in range(i, N):
#     maximum = max(maximum, sum(S[i:j+1]))
# print(maximum)

# 다이나믹
for i in range(1, N):
  D[i]=max(D[i-1]+S[i], S[i])
print(max(D))
