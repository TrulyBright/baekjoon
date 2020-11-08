#include <stdio.h>
#include <stdbool.h>

char board[2188][2188]={0, };

void draw(int y, int x, int width, bool center) {
  if (center)
    board[y][x]=' ';
  if (width==1) {
    board[y][x]=center ? ' ' : '*';
    return;
  }
  width/=3;
  draw(y, x, width, center);
  draw(y, x+width, width, center);
  draw(y, x+width*2, width, center);
  draw(y+width, x, width, center);
  draw(y+width, x+width, width, true);
  draw(y+width, x+width*2, width, center);
  draw(y+width*2, x, width, center);
  draw(y+width*2, x+width, width, center);
  draw(y+width*2, x+width*2, width, center);
}

int main(void)
{
  int N;
  scanf("%d", &N);
  draw(1, 1, N+1, false);
  for (int i=1; i<=N; ++i) {
    for (int j=1; j<=N; ++j) {
      printf("%c", board[i][j]);
    }
    printf("\n");
  }
  return 0;
}
