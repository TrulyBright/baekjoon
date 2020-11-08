N = int(input())
A = list(map(int, input().split()))
D = [1]*N
# D[i]=i번째 원소를 맨 오른쪽 원소로 하는 LIS의 길이-1
# D[i]=max(D[j]) if A[i]>A[j] for j in range(1, i-1)
for i in range(0, N):
  for j in range(0, i):
    if A[j]<A[i]:
      D[i]=max(D[i], D[j]+1)
# print(*D)
print(max(D))
