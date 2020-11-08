T = int(input())
D = [None]*101
D[1:11] = 1,1,1,2,2,3,4,5,7,9

def P(N):
  if N<=6: return D[N]
  for i in range(6, N+1):
    D[i]=D[i-5]+D[i-1]
  return D[N]
for _ in range(T):
  N = int(input())
  print(P(N))
