import sys
N, C = map(int, input().split())
X = [int(sys.stdin.readline().strip()) for _ in range(N)]
X.sort()
end = X[-1]-X[0]
start = 1
closestAPIndex = 0
while end>=start:
  mid=(end+start)//2
  count=1
  for i in range(1, N):
    if X[i]-X[closestAPIndex]>=mid:
      closestAPIndex=i
      count+=1
  if count<C:
    end=mid-1
  else:
    start=mid+1
  closestAPIndex=0

print(end)
