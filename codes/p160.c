#include <stdio.h>

#define MOD (100000)
#define N (1000000000000ll)

typedef long long ll;

ll num_of_five(ll n) {
  ll ret = 0;
  for (; n; ret += (n /= 5)) ;
  return ret;
}

int power_mod(int b, ll t, int mo) {
  if (t == 0) return 1;
  int c = power_mod(((ll)b * b) % mo, t >> 1, mo);
  if (t & 1)
    return ((ll)b * c) % mo;
  return c;
}

int aux_1(int n, int mo) {
  int i, j, ret = 1;
  int b[4] = {1, 2, 3, 4};
  for (i = 0; ; i++)
    for (j = 0; j < 4; j++) {
      int cur = i * 5 + b[j];
      if (cur > n)
        return ret;
      else
        ret = ((ll)ret * cur) % mo;
    }
  return ret;
}

int aux_2(int n, int mo) {
  int i, j, ret = 1;
  int b[4] = {1, 3, 7, 9};
  for (i = 0; ; i++)
    for (j = 0; j < 4; j++) {
      int cur = i * 10 + b[j];
      if (cur > n)
        return ret;
      else
        ret = ((ll)ret * cur) % mo;
    }
  return ret;
}

int rm_fives_fac(ll n, int M, int mo) {
  if (n == 0) return 1;
  int ret = ((ll)power_mod(M, n / mo, mo) * aux_1(n % mo, mo)) % mo;
  ret = ((ll)ret * rm_fives_fac(n / 5, M, mo)) % mo;
  return ret;
}

int rm_fives_fac_odd(ll n, int M, int mo) {
  if (n == 0) return 1;
  int ret = ((ll)power_mod(M, n / mo, mo) * aux_2(n % mo, mo)) % mo;
  ret = ((ll)ret * rm_fives_fac_odd(n / 5, M, mo)) % mo;
  return ret;
}

void solve() {
  int t_1 = power_mod(2, N / 2 - num_of_five(N), MOD);
  int t_2 = rm_fives_fac(N / 2, aux_1(MOD, MOD), MOD);
  int t_3 = rm_fives_fac_odd(N - 1, aux_2(MOD, MOD), MOD);
  printf("%d\n", ((ll)t_1 * t_2 * t_3) % MOD);
}

int main(void) {

  solve();

  return 0;
}
