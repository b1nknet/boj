#include <iostream>
using namespace std;
typedef long long ll;

int arr[100];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	ll ans = 0;
	int N; cin >> N;
	for (int i = 0; i < N; i++) cin >> arr[i];

	int cnt = 0;
	for (int i = 0; i < N; i++) {
		if (cnt == 0) cnt++;
		else if (cnt == 1) {
			if (arr[i - 1] != arr[i]) cnt++;
		}
		else {
			if (arr[i - 1] == arr[i]) cnt = 1;
			else if ((arr[i - 2] < arr[i - 1]) != (arr[i - 1] < arr[i])) cnt++;
			else cnt = 2;
		}

		ans += cnt;
	}

	cout << ans;
}