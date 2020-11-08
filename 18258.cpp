#include <iostream>
#include <queue>
#include <string>
#include <map>
using namespace std;

int main(void) {
  cin.tie(NULL);
  ios_base::sync_with_stdio(false);
  queue<int> Q;
  int N;
  cin >> N;
  map<string, int> M;
  M["push"]=0; M["pop"]=1; M["size"]=2;
  M["front"]=3; M["back"]=4; M["empty"]=5;

  for (int i=0; i<N; ++i) {
    string operation;
    cin >> operation;
    switch (M[operation]) {
      case 0:
        int input;
        cin >> input;
        Q.push(input);
        break;
      case 1:
        cout << (Q.empty() ? -1:Q.front()) << '\n';
        if (!Q.empty()) Q.pop();
        break;
      case 2:
        cout << Q.size() << '\n';
        break;
      case 3:
        cout << (Q.empty() ? -1:Q.front()) << '\n';
        break;
      case 4:
        cout << (Q.empty() ? -1:Q.back()) << '\n';
        break;
      case 5:
        cout << (Q.empty() ? 1:0) << '\n';
        break;
    }
  }
}
