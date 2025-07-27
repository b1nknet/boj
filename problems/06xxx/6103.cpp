#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long X, Y;

    cin >> N >> X >> Y;

    vector<int> M(N);
    vector<int> B(N);

    for (int i = 0; i < N; ++i) {
        cin >> M[i] >> B[i];
    }

    sort(M.begin(), M.end());
    sort(B.begin(), B.end());

    long long totalCost = 0;

    for (int i = 0; i < N; ++i) {
        if (B[i] > M[i]) {
            totalCost += (long long)(B[i] - M[i]) * X;
        } else if (B[i] < M[i]) {
            totalCost += (long long)(M[i] - B[i]) * Y;
        }
    }

    cout << totalCost << endl;

    return 0;
}