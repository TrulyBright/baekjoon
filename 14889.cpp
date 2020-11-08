#include <cstdio>
#include <array>
#include <vector>
using namespace std;

int N;
array<array<int, 20>, 20> stats;
vector<int> combinations;

void pick(int count, int picked) {
  if (count==(int)(N/2)) {
    combinations.push_back(picked);
    return;
  }
  for (int i = picked==0 ? 0; i<N; ++i) {
    picked.push_back(i);
    pick(count+1);
    picked.pop_back();
  }
}

int main(void) {
  scanf("%d", &N);
  for (int i=0; i<N; ++i) {
    for (int j=0; j<N; ++j) {
      scanf("%d", &stats[i][j]);
    }
  }
  pick(0);
  // int minimum = 100*2*20;
  // for (int i=0; i<combinations.size(); ++i) {
  // }
}
