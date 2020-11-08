#include <queue>
#include <array>
#include <iostream>
using namespace std;

int H, M, N;
int dx[6]={1, -1, 0, 0, 0, 0};
int dy[6]={0, 0, 1, -1, 0, 0};
int dz[6]={0, 0, 0, 0, 1, -1};

bool notOutOfBox(int z, int y, int x) {
  return 0<=z && z<H && 0<=y && y<N && 0<=x && x<M ;
}

int main(void) {
  array<array<array<int, 100>, 100>, 100> box;
  queue<array<int, 4>> Q;
  int result = 0;

  cin >> M >> N >> H;
  for (int k=0; k<H; ++k) {
    for (int i=0; i<N; ++i) {
      for (int j=0; j<M; ++j) {
        // cout << i << j << k << '\n';
        int input; cin >> input; box[k][i][j]=input;
        if (input==1) Q.push({k, i, j, 0});
      }
    }
  }

  while (!Q.empty()) {
    array<int, 4> v = Q.front();
    Q.pop();
    // cout << v[0] << ' ' << v[1] << ' ' << v[2] << ' ' << v[3] << '\n';
    result = max(result, v[3]);
    for (int i=0; i<6; ++i) {
      int nextZ = v[0]+dz[i];
      int nextY = v[1]+dy[i];
      int nextX = v[2]+dx[i];
      if (notOutOfBox(nextZ, nextY, nextX) && box[nextZ][nextY][nextX]==0) {
        Q.push({nextZ, nextY, nextX, v[3]+1});
        box[nextZ][nextY][nextX]=1;
      }
    }
  }
  bool failed = false;
  for (int k=0; k<H && !failed; ++k) {
    for (int i=0; i<N && !failed; ++i) {
      for (int j=0; j<M && !failed; ++j) {
        if (box[k][i][j]==0) {
          failed=true;
        }
      }
    }
  }
  printf("%d", failed ? -1:result);
}
