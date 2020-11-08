# 브루트 포스
N, K = map(int, input().split())
item = []
for _ in range(N):
  W, V = map(int, input().split())
  item.append((W, V))

combinations = []
def solve(index, picked):
  global N
  if index==N:
    combinations.append(picked)
    return
  solve(index+1, picked+[item[index]])
  solve(index+1, picked)

solve(0, [])
maximum = 0
for c in combinations:
  valueSum = 0
  weightSum = 0
  for item in c:
    weightSum+=item[0]
    valueSum+=item[1]
  if weightSum <= K:
    maximum = max(maximum, valueSum)
print(maximum)
