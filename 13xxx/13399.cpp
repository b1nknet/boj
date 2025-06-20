#include <iostream>
#include <unordered_map>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    unordered_map<int, int> priority_map;
    set<pair<int, int>> order;

    for (int i = 1; i <= n; ++i) {
        priority_map[i] = -i;
        order.insert({-i, i});
    }

    int current_priority = 0;

    for (int i = 0; i < m; ++i) {
        int x;
        cin >> x;
        order.erase({priority_map[x], x});
        priority_map[x] = ++current_priority;
        order.insert({priority_map[x], x});
    }

    for (auto it = order.rbegin(); it != order.rend(); ++it) {
        cout << it->second << '\n';
    }

    return 0;
}
