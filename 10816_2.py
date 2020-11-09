import sys
import bisect
N = int(sys.stdin.readline().strip())
cards = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline().strip())
integers = map(int, sys.stdin.readline().split())
cards = sorted(cards)
for i in integers:
  print(bisect.bisect_right(cards, i)-bisect.bisect_left(cards, i), end=' ')
