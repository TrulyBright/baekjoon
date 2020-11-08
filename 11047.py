N, K = map(int, input().split())
A = []
for _ in range(N):
  A.append(int(input()))
count = 0
for coin in A[::-1]:
  count+=K//coin
  K%=coin
print(count)
