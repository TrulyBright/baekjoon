#include <stdio.h>

int N;
int cost[1001][3];
int D[1001][3]={0,};

int min(int a, int b) {
  return a>b?b:a;
}

int TopDOWN(int index, int color) {
  if (D[index][color]) {
    return D[index][color];
  }
  switch (color) {
    case 0: return D[index][color]=cost[index][0]+min(TopDOWN(index-1, 1), TopDOWN(index-1, 2));
    case 1: return D[index][color]=cost[index][1]+min(TopDOWN(index-1, 0), TopDOWN(index-1, 2));
    case 2: return D[index][color]=cost[index][2]+min(TopDOWN(index-1, 0), TopDOWN(index-1, 1));
  }
}

int main(void) {
  scanf("%d", &N);
  for (int i=1; i<=N; ++i) {
    scanf("%d%d%d", &cost[i][0], &cost[i][1], &cost[i][2]);
  }
  D[1][0]=cost[1][0];
  D[1][1]=cost[1][1];
  D[1][2]=cost[1][2];
  printf("%d", min(min(TopDOWN(N, 0), TopDOWN(N, 1)), TopDOWN(N, 2)));
  return 0;
}
