import sys
stack = []
K = int(sys.stdin.readline())
for _ in range(K):
  number = int(sys.stdin.readline())
  if number==0:
    stack.pop()
  else:
    stack.append(number)
print(sum(stack))
