#include <deque>
#include <iostream>
using namespace std;

int main(void) {
  deque<int> DQ;
  int T;
  cin >> T;
  while (T--) {
    string p;
    int n;
    string arrayString;
    cin >> p;
    cin >> n;
    cin >> arrayString;
    for (int i=0; i<n; i++) {
      switch (arrayString[i]) {
        case '[':
        case ']':
        case ',':
          break;
        default:
          
      }
    }
  }
}
