#include <iostream>
#include <set>
#include <vector>

using namespace std;

int gcd(int a, int b);

int _gcd(int a, int b);

void get_all_divisors(set<int> set, int num);

void solve();

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int cases = 0;
    cin >> cases;

    while (cases--) {
        solve();
    }

    return 0;
}

int gcd(int a, int b) {
    return _gcd(max(a, b), min(a, b));
}

int _gcd(int a, int b) {
    if (b == 0) {
        return a;
    }
    return _gcd(b, a % b);
}

void get_all_divisors(int num, set<int> &set) {
    for (int i = 2; i * i <= num; i++) {
        if (num % i != 0) {
            continue;
        }
        set.insert(i);
        set.insert(num / i);
    }
}

void solve() {
    int width = 0, length = 0, num = 0;
    vector<int> top = {0, -2, -1, 0, -1}, bottom = {0, -2, -1, -2, -1},
                left = {-2, 0, -1, -1, 0}, right = {-2, 0, -1, -1, -2};
    set<int> answer = {1};
    cin >> width >> length;

    for (int i = 0; i < top.size(); i++) {
        num = gcd(gcd(width + top[i], width + bottom[i]),
                  gcd(length + left[i], length + right[i]));
        answer.insert(num);
        get_all_divisors(num, answer);
    }

    cout << answer.size() << ' ';
    for (auto it = answer.begin(); it != answer.end(); it++) {
        cout << *it << ' ';
    }
    cout << '\n';
}