N = int(input())
A = list(map(int, input().split()))
D = [[1, 1] for _ in range(N)]
# A[i]를 기준으로 하는 바이토닉 수열: A[i]를 맨 오른쪽으로 하는 LIS+맨 왼쪽으로 하는 LDS
# D[i][0] = A[i]를 맨 왼쪽으로 하는 LDS의 길이 (Longest Decreasing Subsequence)
# D[i][1] = A[i]를 맨 오른쪽으로 하는 LIS의 길이

# LIS
for i in range(N):
  for j in range(0, i):
    if A[j]<A[i]:
      D[i][1]=max(D[i][1], D[j][1]+1)

# LDS
for i in range(N-1, -1, -1):
  for j in range(i, N):
    if A[i]>A[j]:
      D[i][0]=max(D[i][0], D[j][0]+1)

# for i in range(N):
#   print(D[i][0], end=' ')
# print()
# for i in range(N):
#   print(D[i][1], end=' ')
B = [length[0]+length[1]-1 for length in D]
# print()
print(max(B))
