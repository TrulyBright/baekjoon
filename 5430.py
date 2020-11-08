from collections import deque
import sys
T = int(input())

for _ in range(T):
  D = deque()
  p = sys.stdin.readline().strip()
  n = int(input())
  array = list(sys.stdin.readline().strip())
  for i, c in enumerate(array):
    if c=='[' or c==']' or c==',':
      array[i]=' '
  array = ''.join(array)
  D.extend(map(int, array.split()))
  toRemoveFromLeft = toRemoveFromRight = 0
  left = True
  for f in p:
    if f=='R':
      left = not left
    elif f=='D':
      if left:
        toRemoveFromLeft+=1
      else:
        toRemoveFromRight+=1
  error = False
  if toRemoveFromLeft+toRemoveFromRight>n:
    error = True
  else:
    for i in range(toRemoveFromLeft):
      D.popleft()
    for i in range(toRemoveFromRight):
      D.pop()
  if not left: D.reverse()
  if error:
    print("error")
  else:
    print('[', end='')
    for i, c in enumerate(D):
      print(c, end='')
      if i!=len(D)-1:
        print(',', end='')
    print(']')
