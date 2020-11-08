A, B, C = map(int, input().split())
while not (A==0 and B==0 and C==0):
  if (A**2==B**2+C**2) or (B**2==A**2+C**2) or (C**2==A**2+B**2):
    print("right")
  else:
    print("wrong")
  A, B, C = map(int, input().split())
