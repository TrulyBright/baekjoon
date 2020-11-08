prime = [True]*(123456*2+1)
prime[0]=prime[1]=False
n = int(input())
for i in range(2, 123456*2+1):
  if prime[i]:
    for j in range(i*2, 123456*2+1, i):
      if j%i==0:
        prime[j]=False
while n!=0:
  count = 0
  for i in range(n+1, 2*n+1):
    if prime[i]:
      count+=1
  print(count)
  n = int(input())
