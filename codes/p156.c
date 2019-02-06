#include <stdio.h>

typedef long long ll;

#define N (1000000ll * 1000000)

int c(ll n, int d) {
  int ret = 0;
  for (; n; n /= 10)
    ret += (n % 10 == d);
  return ret;
}

ll f(ll n, int d) {
  if (n == 0) return 0;
  ll k = n / 10;
  int u = n % 10;
  return 10 * f(k, d) + k + 1 - c(k, d) * (9 - u) - (u < d);
}

int check(ll l, ll f_l, ll r, ll f_r) {
  return (l <= f_r && f_l <= r);
}

ll search(ll l, ll r, int d) {
  if (l == r) return (f(l, d) == l) ? l : 0;
  ll m = (l + r) >> 1, ret = 0;
  if (check(l, f(l, d), m, f(m, d))) ret += search(l, m, d);
  if (check(m + 1, f(m + 1, d), r, f(r, d))) ret += search(m + 1, r, d);
  return ret;
}

void solve() {
  int d;
  ll ans = 0;
  for (d = 1; d < 10; d++)
    ans += search(0, N, d);
  printf("%I64d\n", ans);
}

int main() {

  solve();

  return 0;
}
