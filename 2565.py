N = int(input())
A = [0]*500
D = [1]*500
# D[i]=A[i]를 맨 오른쪽으로 하는 LIS의 길이 (단, 0을 무시)
maximum = 0
for _ in range(N):
  i, A[i-1] = list(map(int, input().split()))
  maximum = max(maximum, i, A[i-1])
for i in range(500):
  for j in range(0, i):
    if A[i]>A[j] and A[j]!=0:
      D[i]=max(D[i], D[j]+1)
# for i in range(10):
#   print(A[i], end=' ')
# print()
# for i in range(10):
#   print(D[i], end=' ')
# print()
print(N-max(D))
