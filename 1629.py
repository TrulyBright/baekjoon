A, B, C = map(int, input().split())

def power(base, exponent, divisor):
  if exponent==1:
    return base%divisor
  if exponent%2==0:
    return ((power(base, exponent//2, divisor)%divisor)**2)%divisor
  return (power(base, exponent//2, divisor)%divisor * power(base, exponent//2+1, divisor)%divisor)%divisor
print(power(A, B, C))
