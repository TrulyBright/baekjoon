N = int(input())
S = []
for _ in range(N):
  start, end = map(int, input().split())
  S.append((start, end))

S = sorted(S, key=lambda p: p[0])
S = sorted(S, key=lambda p: p[1])
# print(S)
lastSeminar = S[0]
count = 1
# print(lastSeminar)
for i in range(1, N):
  if lastSeminar[1] <= S[i][0]:
    lastSeminar = S[i]
    # print(S[i])
    count+=1
print(count)
