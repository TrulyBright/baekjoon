prime = [True]*(10001)
prime[0]=prime[1]=False
for i in range(2, 10001):
  if prime[i]:
    for j in range(i*2, 10001, i):
      if j%i==0:
        prime[j]=False
T = int(input())
for _ in range(T):
  n = int(input())
  for i in range(2, n//2+1):
    if prime[i] and prime[n-i]:
      answer = i, n-i
  print(*answer)
