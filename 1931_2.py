import sys
N = int(sys.stdin.readline())
S = []
for _ in range(N):
  start, end = map(int, sys.stdin.readline().split())
  S.append((start, end))
S = sorted(S, key=lambda p: p[1])

result = 0
def solve(lastSeminarIndex, count):
  global N, result
  # print(lastSeminarIndex, count)
  for j in range(lastSeminarIndex+1, N):
    if S[lastSeminarIndex][1] <= S[j][0]:
      solve(j, count+1)
  if result<count:
    print(count)
    result = count
for i in range(N):
  solve(i, 1)
print(result)
