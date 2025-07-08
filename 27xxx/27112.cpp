#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
pair<int, int> work[100000];
int daycnt, x, y;
int ans;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N;
	for (int n = 0; n < N; n++) {
		cin >> work[n].first >> work[n].second;
	}
	sort(work, work + N);

	for (int n = 0; n < N; n++) {
		while (daycnt < work[n].first) {
			if (daycnt % 7 < 5) x++;
			y++, daycnt++;
		}
		if (x >= work[n].second) x -= work[n].second;
		else if (x + y >= work[n].second) {
			int tmp = work[n].second - x;
			x = 0, y -= tmp, ans += tmp;
		}
		else {
			cout << -1;
			return 0;
		}
	}

	cout << ans;
}