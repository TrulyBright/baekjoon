#include <queue>
#include <array>
#include <iostream>
using namespace std;

int M, N;
int dx[4]={0,1,0,-1};
int dy[4]={1,0,-1,0};

bool notOutOfBox(int y, int x) {
  return 0<=y && y<N && 0<=x && x<M;
}

int main(void) {
  array<array<int, 1000>, 1000> box;
  queue<array<int, 3>> Q;
  int result = 0;

  cin >> M >> N;
  for (int i=0; i<N; ++i) {
    for (int j=0; j<M; ++j) {
      int input; cin >> input; box[i][j]=input;
      if (input==1) Q.push({i, j, 0});
    }
  }

  while (!Q.empty()) {
    array<int, 3> v = Q.front();
    Q.pop();
    result = max(result, v[2]);
    for (int i=0; i<4; ++i) {
      int nextY = v[0]+dy[i];
      int nextX = v[1]+dx[i];
      if (notOutOfBox(nextY, nextX) && box[nextY][nextX]==0) {
        Q.push({nextY, nextX, v[2]+1});
        box[nextY][nextX]=1;
      }
    }
  }
  bool failed = false;
  for (int i=0; i<N; ++i) {
    for (int j=0; j<M; ++j) {
      if (box[i][j]==0) {
        failed=true;
        break;
      }
    }
    if (failed) break;
  }
  printf("%d", failed ? -1:result);
}
