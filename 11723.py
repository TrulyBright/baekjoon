import sys
M = int(input())
S = set()
for _ in range(M):
  inputted = sys.stdin.readline().split()
  if len(inputted)==2:
    x = int(inputted[1])
  operation = inputted[0]
  if operation=="add":
    S.add(x)
  elif operation=="remove" and x in S:
    S.remove(x)
  elif operation=="check":
    print(int(x in S))
  elif operation=="toggle":
    S.remove(x) if x in S else S.add(x)
  elif operation=="all":
    S=set(range(1, 21))
  else:
    S=set()
