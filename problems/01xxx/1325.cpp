#include <iostream>
#include <vector>
using namespace std;

int N, M;
bool isVisited[10001];
vector<int> graph[10001];
vector<int> results;

int dfs(int number) {
    int cnt = 1;
    isVisited[number] = true;
    for (int neighbor : graph[number]) {
        if (!isVisited[neighbor]) {
            cnt += dfs(neighbor);
        }
    }
    return cnt;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin >> N >> M;

    for (int i = 0; i < M; i++) {
        int n, m;
        cin >> n >> m;
        graph[m].push_back(n);
    }

    int maxCount = 0;
    for (int i = 0; i <= N; i++) {
        if (graph[i].empty()) continue;
        fill(isVisited, isVisited + 10001, false);
        int count = dfs(i);
        if (count > maxCount) {
            maxCount = count;
            results.clear();
            results.push_back(i);
        } else if (count == maxCount) {
            results.push_back(i);
        }
    }

    for (int result : results) {
        cout << result << " ";
    }
}
