#include <iostream>
#include <deque>
#include <string>
using namespace std;

int main(void) {
  deque<int> DQ;
  int N;
  cin >> N;
  for (int i=0; i<N; i++) {
    string operation;
    cin >> operation;
    if (operation=="push_front") {
      int X;
      cin >> X;
      DQ.push_front(X);
    }
    if (operation=="push_back") {
      int X;
      cin >> X;
      DQ.push_back(X);
    }
  }
}
