import sys
M = int(sys.stdin.readline())
S = 0b00000000000000000000
for _ in range(M):
  input = sys.stdin.readline().split()
  operation = input[0]
  if len(input)==2: x = int(input[1])
  if operation=="add":
    S |= 0b1<<20-x
  elif operation=="remove":
    S &= ~(0b1<<20-x)
  elif operation=="check":
    print(S>>20-x & 0b1)
  elif operation=="toggle":
    S ^= 0b1<<20-x
  elif operation=="all":
    S = 0b11111111111111111111
  elif operation=="empty":
    S = 0b00000000000000000000
