#include <iostream>
using namespace std;

int gcd(int x, int y) {
	if (y == 0) return x;
	return (gcd(y, x % y));
}

int arr[10001];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N, R; cin >> N >> R;
	while (N) {
		int total = 0;
		for (int n = 0; n < N; n++) {
			auto& x = arr[n];
			for (int r = 0; r < R; r++) cin >> x;
			total += x;
		}
		for (int n = 0; n < N; n++) {
			int GCD = gcd(arr[n], total);
			cout << arr[n] / GCD << " / " << total / GCD << '\n';
		}

		cin >> N >> R;
	}
}