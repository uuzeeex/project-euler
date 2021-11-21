#include <stdio.h>
#include <malloc.h>

#define N (1000000)
#define SQRT_N (1000)

typedef struct node {
  int val;
  struct node *next;
} node;

node *divs[N];
int mdrs[N];

void get_divs(node **divs, int n, int sqrt_n) {
  int i, j;
  for (i = 2; i < sqrt_n; i++) {
    for (j = i; i * j < n; j++) {
      struct node *h = (struct node *)malloc(sizeof(struct node));
      h->val = i;
      h->next = divs[i * j];
      divs[i * j] = h;
    }
  }
}

int dr(int n) {
  if (n < 10) return n;
  int ret = 0;
  for (; n; n /= 10)
    ret += n % 10;
  return dr(ret);
}

int max(int a, int b) {
  return (a > b) ? a : b;
}

void solve() {
  get_divs(divs, N, SQRT_N);
  int i, ans = 0;
  for (i = 2; i < N; i++) {
    mdrs[i] = dr(i);
    node *div;
    for (div = divs[i]; div; div = div->next)
      mdrs[i] = max(mdrs[i], mdrs[div->val] + mdrs[i / div->val]);
    ans += mdrs[i];
  }
  printf("%d\n", ans);
}

int main(void) {

  solve();

  return 0;
}
