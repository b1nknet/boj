#include <iostream>
#include <string>
using namespace std;

int N, D, M;
string s;
int cnt[128], combo;
int ans;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> s >> D >> M;
	for (auto &l : s) {
		if (l == 'H') {
			cnt['H']++;
			ans += min(M + D, combo * D);
			combo = 0;
		}
		else if (l == 'Y') {
			cnt['Y']++;
			ans += min(M + D, combo * D);
			combo = 0;
		}
		else if (l == 'U') {
			cnt['U']++;
			ans += min(M + D, combo * D);
			combo = 0;
		}
		else combo++;
	}
	ans += min(M + D, combo * D);

	if (ans) cout << ans << '\n';
	else cout << "Nalmeok\n";
	ans = min(cnt['H'], min(cnt['Y'], cnt['U']));
	if (ans) cout << ans;
	else cout << "I love HanYang University";
}