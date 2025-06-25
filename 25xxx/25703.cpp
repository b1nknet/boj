#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cout << "int a;\nint *ptr = &a;\n";

	int N; cin >> N;
	for (int i = 2; i <= N; i++) {
		cout << "int ";
		for (int k = 0; k < i; k++) cout << '*';
		if (i > 2) cout << "ptr" << i << " = &ptr" << i - 1 << ";\n";
		else cout << "ptr" << i << " = &ptr" << ";\n";
	}
}