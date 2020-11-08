import sys
N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
numbers = dict()
for i in cards:
  if i in numbers:
    numbers[i]+=1
  else:
    numbers[i]=1
M = int(sys.stdin.readline())
integers = list(map(int, sys.stdin.readline().split()))
for i in integers:
  print(numbers[i] if i in numbers else 0, end=' ')
