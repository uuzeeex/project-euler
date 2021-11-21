#include <stdio.h>

#define N (200000)

int pre_2[N + 1], pre_5[N + 1];

int min(int a, int b) {
  return (a < b) ? a : b;
}

int cal(int n, int p) {
  int ret = 0;
  for (; n % p == 0; n /= p) ret++;
  return ret;
}

void init() {
  int i;
  pre_2[0] = pre_5[0] = 0;
  for (i = 1; i <= N; i++) {
    pre_2[i] = pre_2[i - 1] + cal(i, 2);
    pre_5[i] = pre_5[i - 1] + cal(i, 5);
  }
}

void solve() {
  int a, b, c, de_2, de_5, ans = 0;
  for (a = 0; a <= N; a++) {
    if (a % 1000 == 0) printf("Current a = %d\n", a);
    for (b = 0; a + b <= N; b++) {
      c = N - a - b;
      de_2 = pre_2[a] + pre_2[b] + pre_2[c];
      de_5 = pre_5[a] + pre_5[b] + pre_5[c];
      ans += pre_2[N] - de_2 >= 12 && pre_5[N] - de_5 >= 12;
    }
  }
  printf("%d\n", ans);
}

int main() {

  init();
  solve();

  return 0;
}
