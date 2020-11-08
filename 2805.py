N, M = map(int, input().split())
H = list(map(int, input().split()))

start = 0
end = max(H)
while end>=start:
  mid = (end+start)//2
  summation = sum([h-mid if h>mid else 0 for h in H])
  if summation>M:
    start = mid+1
  else:
    end = mid-1
print(start)
