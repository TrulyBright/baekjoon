import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
  input = sys.stdin.readline().split()
  operation = input[0]
  if len(input)==2:
    X = input[1]
  if operation=="push":
    stack.append(X)
  elif operation=="pop":
    print(-1 if len(stack)==0 else stack.pop())
  elif operation=="size":
    print(len(stack))
  elif operation=="empty":
    print(1 if len(stack)==0 else 0)
  elif operation=="top":
    print(-1 if len(stack)==0 else stack[-1])
