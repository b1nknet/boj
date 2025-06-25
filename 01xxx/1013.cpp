#include <iostream>
#include <string>
#include <regex>

using namespace std;

void solve(void);

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int test_case;
	cin >> test_case;
	for (int t = 0; t < test_case; t++)
		solve();
}

void solve(void) {
	string bits;
	cin >> bits;

	regex pattern("(100+1+|01)+");
	cout << (regex_match(bits, pattern) ? "YES\n" : "NO\n");
}