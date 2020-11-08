import sys
N = int(sys.stdin.readline().strip())
A = []
for i in range(N):
  name, score = sys.stdin.readline().split()
  score = int(score)
  A.append([name, score])
A.sort(key=lambda i:i[0])
A.sort(key=lambda i:i[1], reverse=True)
print(A[0][0])
