#include <iostream>
#include <cmath>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	string A, B;
	cin >> A >> B;

	int n = abs(A[0] - B[0]);
	int m = abs(A[1] - B[1]);

	cout << min(n, m) << ' ' << max(n, m) << '\n';

	return 0;
}