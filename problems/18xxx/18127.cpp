#include <iostream>
using namespace std;
typedef long long ll;

ll K, N;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> K >> N;
	cout << (2 + N * (K - 2)) * (N + 1) / 2;
}