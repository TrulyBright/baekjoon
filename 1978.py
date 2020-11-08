def isPrime(n)->bool:
  if n==1: return False
  if n==2: return True
  if n%2==0: return False
  i=3
  while i*i<=n:
    if n%i==0: return False
    i+=2
  return True
N = int(input())
L = list(map(int, input().split()))

count = 0
for i in L:
  if isPrime(i):
    count+=1

print(count)
