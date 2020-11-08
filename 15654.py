N, M = map(int, input().split())
L = list(map(int, input().split()))
L.sort()
result = []

def pick(picked):
  global N, M
  if picked==M:
    print(*result)
    return
  for i in L:
    if i not in result:
      result.append(i)
      pick(picked+1)
      result.pop()
pick(0)
