import random

random.seed()
N = random.randint(1, 10)
print(N)
for _ in range(N):
  start = random.randint(0, 5)
  print(start, random.randint(start, 10))
