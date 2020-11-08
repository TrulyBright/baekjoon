from math import sqrt
N = int(input())
sieve = [True]*(N+1)
for i in range(2, N+1):
  if sieve[i]:
    for j in range(i*2, N+1, i):
      if j%i==0:
        sieve[j]=False

primes = {i for i in range(2, N+1) if sieve[i]}

factorizations = []
for prime in primes:
  count = 0
  while N%prime==0:
    count+=1
    N//=prime
  factorizations.append((prime, count))
for result in factorizations:
  for times in range(result[1]):
    print(result[0])
