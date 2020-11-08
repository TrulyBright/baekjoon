#include <stdio.h>

int min(int a, int b) {
  return a>b?b:a;
}

int main(void) {
  int N;
  scanf("%d", &N);
  int cost[N+1][3];
  for (int i=1; i<=N; ++i) {
    scanf("%d%d%d", &cost[i][0], &cost[i][1], &cost[i][2]);
  }
  int D[N+1][3];
  D[1][0]=cost[1][0];
  D[1][1]=cost[1][1];
  D[1][2]=cost[1][2];
  for (int i=2; i<=N; ++i) {
    D[i][0]=cost[i][0]+min(D[i-1][1], D[i-1][2]);
    D[i][1]=cost[i][1]+min(D[i-1][0], D[i-1][2]);
    D[i][2]=cost[i][2]+min(D[i-1][0], D[i-1][1]);
  }
  printf("%d", min(min(D[N][0], D[N][1]), D[N][2]));
  return 0;
}
