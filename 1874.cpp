#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main(void) {
  int N;
  stack<int> s;
  vector<char> v;
  s.push(0);
  cin >> N;
  for (int i=1, pushed=1; i<=N; ++i) {
    int input;
    cin >> input;
    if (input < pushed && s.top() < input) {
      cout << "NO" << endl;
      return 0;
    }
    if (s.top()<input) {
      while (s.top()!=input) {
        s.push(pushed++);
        v.push_back('+');
      }
      s.pop();
      v.push_back('-');
    } else {
      while (s.top()>=input) {
        s.pop();
        v.push_back('-');
      }
    }
  }
  for (int i=0, size=v.size(); i<v.size(); ++i) {
    cout << v[i] << '\n';
  }
  return 0;
}
