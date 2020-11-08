#include <cstdio>
#include <queue>
using namespace std;

int N, M;
struct node {int y, x; bool smashed; int distance;};

bool inBoard(int y, int x) {
  return 0<=y && y<=N && 0<=x && x<M;
}

int main(void) {
  queue<node> Q;
  int dx[4]={0,1,0,-1};
  int dy[4]={1,0,-1,0};
  scanf("%d%d", &N, &M);
  int board[N][M];
  int distance[N][M]; // distance[i][j]=(i, j)까지의 최단거리
  for (int i=0; i<N; ++i) {
    for (int j=0; j<M; ++j) {
      scanf("%1d", &board[i][j]);
      distance[i][j]=0x7fffffff; // distance 배열 최댓값으로 초기화
    }
  }

  Q.push({0,0,false,1});
  while (!Q.empty()) {
    node v = Q.front(); Q.pop();
    int Y = v.y, X = v.x;
    distance[Y][X]=v.distance;
    for (int i=0; i<4; ++i) {
      int nextY = Y+dy[i], nextX = X+dx[i];
      if (inBoard(nextY, nextX) && distance[nextY][nextX]>v.distance+1) { // next로의 최단거리보다 크면 큐에 넣지 않음.
        if (v.smashed && board[nextY][nextX]!=1) { // 벽을 한번 부쉈고 다음 경로에 벽이 없는 경우
          Q.push({nextY, nextX, true, v.distance+1});
        } else if (!v.smashed) { // 벽을 안 부순 경우
          Q.push({nextY, nextX, board[nextY][nextX]==1, v.distance+1});
        }
      }
    }
  }

  printf("%d", distance[N-1][M-1]==0x7fffffff ? -1:distance[N-1][M-1]);
}
