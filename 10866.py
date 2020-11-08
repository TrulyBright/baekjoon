import sys
from collections import deque
d = deque()
N = int(sys.stdin.readline())
for _ in range(N):
  command = sys.stdin.readline().split()
  if len(command)==2:
    X = int(command[1])
  command = command[0]
  if command=="push_front":
    d.append(X)
  elif command=="push_back":
    d.appendleft(X)
  elif command=="pop_front":
    print(-1 if len(d)==0 else d.pop())
  elif command=="pop_back":
    print(-1 if len(d)==0 else d.popleft())
  elif command=="size":
    print(len(d))
  elif command=="empty":
    print(1 if len(d)==0 else 0)
  elif command=="front":
    print(-1 if len(d)==0 else d[-1])
  else:
    print(-1 if len(d)==0 else d[0])
