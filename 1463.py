from sys import *
N = int(input())
D = [None]*(N+1) # D[N]=N을 1로 만들기 위한 연산수의 최솟값
# D[N]=min(D[N/3]+1, D[N/2]+1, D[N-1]+1)
D[1]=0
# def topDown(X)->int:
#   if D[X] is not None: return D[X]
#   div3 = 10**6-1
#   if X%3==0:
#     div3 = topDown(X//3)
#   div2 = 10**6-1
#   if X%2==0:
#     div2 = topDown(X//2)
#   minus1 = topDown(X-1)
#   D[X] = min(div3, div2, minus1)+1
#   return D[X]
for i in range(2, N+1):
  div3 = D[i//3] if i%3==0 else 10**6-1
  div2 = D[i//2] if i%2==0 else 10**6-1
  minus1 = D[i-1]
  D[i] = min(div3, div2, minus1)+1
print(D)
print(topDown(N))
