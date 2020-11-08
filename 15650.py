N, M = map(int, input().split())

result = []
count=0
def pick(picked):
  global N, M, count
  if picked==M:
    count+=1
    return
  for i in range(1 if not result else result[-1]+1, N+1):
    result.append(i)
    pick(picked+1)
    result.pop()
pick(0)
