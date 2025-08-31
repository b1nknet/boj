#include <iostream>
#include <algorithm>
using namespace std;

bool DESC(int a, int b) {
	return a > b;
}

int main() {
	int N;
	int A[100];
	int B[100];
	int sum = 0;

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}
	for (int i = 0; i < N; i++) {
		cin >> B[i];
	}

	sort(A, A + N);	
	sort(B, B + N, DESC);

	for (int i = 0; i < N; i++) {
		sum += (A[i] * B[i]);
	}

	cout << sum;

	return 0;
}