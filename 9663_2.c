#include <stdio.h>
#include <stdbool.h>
int N;
int column=0;
int diagonal1=0;
int diagonal2=0;
int result=0;

void place(int placed) {
  if (placed==N) {
    result+=1;
    return;
  }
  for (int i=0; i<N; i++) {
    if (~(column>>i) && ~(diagonal1>>(placed+i)) && ~(diagonal2>>(N-1-placed+i))) {
      column|=1<<i;
      diagonal1|=1<<(placed+i);
      diagonal2|=1<<(N-1-placed+i);
      place(placed+1);
      column&=~(1<<i);
      diagonal1&=~(1<<(placed+i));
      diagonal2&=~(1<<(N-1-placed+i));
    }
  }
}
int main(void) {
  scanf("%d", &N);
  place(0);
  printf("%d", result);
  return 0;
}
