# 완전탐색
N = int(input())
V = []
for _ in range(N):
  x, y = map(int, input().split())
  V.append((x, y))
result =  20000**2+20000**2
for i in V:
  for j in V:
    if i!=j:
      result = min(result, (i[0]-j[0])**2+(i[1]-j[1])**2)
print(result)
