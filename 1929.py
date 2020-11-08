M, N = map(int, input().split())

prime = [True]*(N+1)
prime[1]=False

for i in range(2, N+1):
  if prime[i]:
    for j in range(i*2, N+1, i):
      if j%i==0:
        prime[j]=False

for i in range(M, N+1):
  if prime[i]:
    print(i)
