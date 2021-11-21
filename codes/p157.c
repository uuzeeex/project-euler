#include <stdio.h>

#define N (10)

typedef long long ll;

ll power(ll a, ll b) {
  return (!b) ? 1 : a * power(a, b - 1);
}

int log_part(ll a, ll b) {
  return (b % a != 0) ? 0 : 1 + log_part(a, b / a);
}

int check(ll n) {
  return (n % 2 != 0) && (n % 5 != 0);
}

int divs_num(ll n) {
  int i, cnt = 0;
  for (i = 1; (ll)i * i < n; i++) {
    if (n % i == 0)
      cnt += check(i) + check(n / i);
  }
  if (i * i == n)
    cnt += check(i);
  return cnt;
}

int max(int a, int b) {
  return (a > b) ? a : b;
}

int min(int a, int b) {
  return (a < b) ? a : b;
}

ll gcd(ll a, ll b) {
  return (!b) ? a : gcd(b, a % b);
}

void solve() {
  int x1, x2, y1, y2, ans = 0;
  for (x1 = 0; x1 <= N; x1++)
    for (x2 = 0; max(x1, x2) <= N; x2++)
      for (y1 = 0; y1 <= N; y1++)
        for (y2 = 0; max(y1, y2) <= N; y2++) {
          ll a_ = power(2, x1) * power(5, y1);
          ll b_ = power(2, x2) * power(5, y2);
          if (a_ <= b_) {
            int minx = min(x1, x2), maxx = max(x1, x2);
            int miny = min(y1, y2), maxy = max(y1, y2);
            ll p = power(2, x1 - minx) * power(5, y1 - miny);
            ll q = power(2, x2 - minx) * power(5, y2 - miny);
            ll r = power(2, maxx) * power(5, maxy);
            ll g = gcd(p + q, r);
            ll s = (p + q) / g;
            r /= g;
            ans += divs_num(s) * (N - max(1, max(log_part(2, r), log_part(5, r))));
          }
        }
  printf("%d\n", ans);
}

int main() {

  solve();

  return 0;
}
