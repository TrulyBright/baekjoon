N = int(input())
dividers = list(map(int, input().split()))

def gcd(a, b):
  while b!=0:
    r = a%b
    a=b
    b=r
  return a

def lcm(a, b)->int:
  return a*b//gcd(a,b)

lcmOfGivenNumbers = 1
for n in dividers:
  lcmOfGivenNumbers = lcm(lcmOfGivenNumbers, n)
print(lcmOfGivenNumbers)
