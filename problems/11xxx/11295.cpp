#include <iostream>
#include <string>
using namespace std;

int L, Q;
int T;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> L;
	while (L) {
		T++;
		cout << "User " << T << '\n';

		cin >> Q;
		while (Q--) {
			int x; cin >> x;
			x *= L;

			cout << x / 100000 << '.';
			x %= 100000;
			if (x < 10000) cout << 0;
			if (x < 1000) cout << 0;
			if (x < 100) cout << 0;
			if (x < 10) cout << 0;
			cout << x << '\n';
		}

		cin >> L;
	}
}