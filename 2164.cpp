#include <iostream>
#include <queue>
using namespace std;

int main(void) {
  int N;
  queue<int> Q;

  cin >> N;
  for (int i=1; i<=N; ++i) Q.push(i);
  while (Q.size()!=1) {
    Q.pop();
    int front = Q.front();
    Q.pop();
    Q.push(front);
  }
  cout << Q.front() << '\n';
}
