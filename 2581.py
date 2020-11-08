M = int(input())
N = int(input())

prime = [True]*(N+1)
prime[0]=prime[1]=False

for i in range(2, N+1):
  if prime[i]:
    for j in range(i*2, N+1, i):
      if j%i==0:
        prime[j]=False
primes = [i for i in range(M, N+1) if prime[i]]
if not primes:
  print(-1)
else:
  print(sum(primes))
  print(primes[0])
