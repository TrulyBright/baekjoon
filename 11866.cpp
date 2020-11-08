#include <iostream>
#include <queue>
using namespace std;
int main(void) {
  int K, N;
  queue<int> alive;
  cin >> N >> K;
  for (int i=1; i<=N; ++i) alive.push(i);

  cout << '<';
  while (!alive.empty()) {
    for (int i=0; i<K-1; i++) {
      int passed = alive.front();
      alive.pop();
      alive.push(passed);
    }
    int dead = alive.front();
    alive.pop();
    cout << dead << (alive.empty() ? "":", ") ;
  }
  cout << '>';
  return 0;
}
