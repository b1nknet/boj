#include<cstdio>
#include<algorithm>
using namespace std;
 
int f(int i, int j) {
    int n = max(abs(i), abs(j));
    int val = (2 * n + 1);
    val *= val;
 
    int diff = 2 * n;
    if (i == n)return val - (n - j);
    val -= diff;
    if (j == -n)return val - (n - i);
    val -= diff;
    if (i == -n)return val - (j + n);
    val -= diff;
    return val - (i + n);
}
 
int g(int val) {
    return val ? g(val / 10) + 1 : 0;
}
 
int main() {
    int r1, c1, r2, c2;
    scanf("%d %d %d %d", &r1, &c1, &r2, &c2);
 
    int k=0;
    for (int i = r1; i <= r2; ++i)for (int j = c1; j <= c2; ++j)k = max(k, g(f(i, j)));
 
    for (int i = r1; i <= r2; ++i) {
        for (int j = c1; j <= c2; ++j)printf("%*d ", k, f(i, j));
        putchar('\n');
    }
 
}
