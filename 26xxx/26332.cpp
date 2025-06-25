#include <iostream>
using namespace std;

int T;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> T;
	while (T--) {
		int c, p; cin >> c >> p;
		cout << c << ' ' << p << '\n' << p * c - 2 * (c - 1) << '\n';
	}
}