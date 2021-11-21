#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N (150000000)

typedef long long ll;

ll multi_mod(ll a, ll b, ll c) {
  if (b == 0) return 0;
  ll mm = multi_mod((a + a) % c, b >> 1, c);
  if ((b & 1) == 0) return mm;
  return (a + mm) % c;
}

ll power_mod(ll a, ll b, ll c) {
  if (b == 0) return 1;
  ll pm = power_mod(multi_mod(a, a, c), b >> 1, c);
  if ((b & 1) == 0) return pm;
  return multi_mod(a, pm, c);
}

int miller_rabin(ll n) {
  if (n < 2) return 0;
  int i, k = 3;
  for (i = 0; i < k; i++) {
    ll a = ((ll)rand() * rand()) % (n - 1) + 1, tn = n - 1;
    int p = 0;
    for (; (tn & 1) == 0; ) {
      tn >>= 1;
      if (power_mod(a, tn, n) == n - 1) {
        p = 1;
        break;
      }
    }
    ll sth_power = power_mod(a, tn, n);
    if (!p && (sth_power == n - 1 || sth_power == 1))
      p = 1;
    if (!p) return 0;
  }
  return 1;
}

int main(void) {

  ll n, ans = 0;
  srand(time(0));
  for (n = 10; n < N; n += 10) {
    if (n % 1000000 == 0) printf("%d\n", n);
    //printf("%d\n", n);
    ll s = n * n;
    if (s % 3 != 1) continue;
    if (s % 7 != 2 && s % 7 != 3) continue;
    if (s % 9 == 0 || s % 13 == 0 || s % 27 == 0) continue;
    if ( miller_rabin(s +  1) &&
         miller_rabin(s +  3) &&
         miller_rabin(s +  7) &&
         miller_rabin(s +  9) &&
         miller_rabin(s + 13) &&
        !miller_rabin(s + 19) &&
        !miller_rabin(s + 21) &&
         miller_rabin(s + 27)) ans += n;
  }
  printf("%I64d\n", ans);

  return 0;
}
