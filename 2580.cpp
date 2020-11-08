#include <stdio.h>

int board[9][9];
int coordinates_of_0[81][2];
int main(void) {
  int count_0 = 0;
  for (int i=0; i<9; ++i) {
    for (int j=0; j<9; ++j) {
      scanf("%d", &board[i][j])
      if (board[i][j]==0) {
        coordinates_of_0[count_0][0]=i;
        coordinates_of_0[count_0][1]=j;
        ++count_0;
      }
    }
  }
  
}
