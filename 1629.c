#include <stdio.h>

int power(int base, int exponent, int divisor) {
  if (exponent==1) return base%divisor;
  if (exponent%2==0) return ((power(base, (int)(exponent/2), divisor)%divisor) * (power(base, (int)(exponent/2), divisor)%divisor))%divisor;
  return (power(base, (int)(exponent/2), divisor)%divisor * power(base, (int)(exponent/2)+1, divisor)%divisor)%divisor;
}

int main(void) {
  int A, B, C;
  scanf("%d%d%d", &A, &B, &C);
  printf("%d", power(A, B, C));
}
