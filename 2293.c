#include <stdio.h>

int main(void) {
  int N, K;
  scanf("%d%d", &N, &K);
  int value[N];
  int D[K];
  // D[K]=K원을 만드는 경우의 수
  // D[K]=D[K-1]
  for (int i=0; i<N; ++i) scanf("%d", &value[i]);
}
