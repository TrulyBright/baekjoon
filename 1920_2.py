import sys
N = int(input())
A = sorted(list(map(int, sys.stdin.readline().split())))
M = int(input())
L = list(map(int, sys.stdin.readline().split()))
for i in L:
  start = 0
  end = N-1
  while end>=start:
    mid = (end+start)//2
    if A[mid]>i:
      end = mid-1
    elif A[mid]==i:
      print("1")
      break
    else:
      start=mid+1
  else:
    print("0")
