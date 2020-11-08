N = int(input())
K = int(input())
start = 1
end = K
def indexOf(number):
  count = 0
  for i in range(1, N+1):
    count+=min(N, number//i)
  return count

while end>=start:
  mid = (end+start)//2
  if indexOf(mid)>=K:
    answer = mid
    end = mid-1
  else:
    start = mid+1
print(answer)
