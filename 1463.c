#include <stdio.h>

int D[1000001]={0,};
int min(int a, int b) {
  return a>b?b:a;
}

int topDown(int X) {
  // printf("%d\n", X);
  if (X==1) return 0;
  if (D[X]) return D[X];
  int div3 = X%3==0 ? topDown((int)(X/3)) : 1000000-1;
  int div2 = X%2==0 ? topDown((int)(X/2)) : 1000000-1;
  int minus1 = topDown(X-1);
  return D[X]=min(min(div3, div2), minus1)+1;
}

int main(void) {
  int N;
  scanf("%d", &N);
  printf("%d", topDown(N));
}
