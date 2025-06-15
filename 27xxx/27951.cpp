#include <iostream>

#include <queue>

#include <algorithm>

using namespace std;

int main() {
    cin.tie(0);
    std::ios_base::sync_with_stdio(0);

    int n;
    cin >> n;
    vector < int > v(n);
    for (auto & i: v) {
        cin >> i;
    }

    int up, down;
    cin >> up >> down;
    vector < char > ans(n, 'A');

    int db = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] == 1) {
            if (up == 0) {
                continue;
            }
            ans[i] = 'U';
            up--;
        } else if (v[i] == 2) {
            if (down == 0) {
                continue;
            }
            ans[i] = 'D';
            down--;
        } else {
            db++;
        }
    }

    if ((up == 0 && down == 0) || db == up + down) {
        cout << "YES\n";
        for (const auto & ch: ans) {
            if (ch == 'A') {
                if (up > 0) {
                    cout << 'U';
                    up--;
                } else {
                    cout << 'D';
                }
            } else {
                cout << ch;
            }
        }
    } else {
        cout << "NO";
    }
}