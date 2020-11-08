#include <stdio.h>
#include <stdbool.h>
int main(void) {
  int N;
  scanf("%d", &N);
  bool sieve[N+1];
  for (int i=2; i<=N; ++i) sieve[i]=true;

  for (int i=2; i<=N; ++i) {
    if (sieve[i]) {
      for (int j=i*2; j<=N; j+=i) {
        if (j%i==0) {
          sieve[j]=false;
        }
      }
    }
  }
  // for (int i=2; i<=N; ++i) {
  //   if (sieve[i]) {
  //     printf("%d ", i);
  //   }
  // }
}
