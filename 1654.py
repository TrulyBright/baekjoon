K, N = map(int, input().split())
lans = []
for _ in range(K):
  lans.append(int(input()))

start = 1
end = max(lans)

while end>=start:
  mid = (end+start)//2
  number = sum([i//mid for i in lans])
  if number < N:
    end = mid-1
  else:
    start = mid+1
print(end)
