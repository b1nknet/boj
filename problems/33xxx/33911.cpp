#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <unordered_set>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    std::cin >> n;

    std::vector<int> opponent_counts(101, 0);
    for (int i = 0; i < n; ++i) {
        int a, b, c;
        std::cin >> a >> b >> c;
        opponent_counts[a]++;
        opponent_counts[b]++;
        opponent_counts[c]++;
    }

    int win_count = 0;

    for (int i = 1; i <= 100; ++i) {
        for (int j = i + 1; j <= 100; ++j) {
            for (int k = j + 1; k <= 100; ++k) {
                
                std::unordered_set<int> our_choice = {i, j, k};
                
                std::vector<int> final_candidates;
                
                for (int num = 1; num <= 100; ++num) {
                    if (our_choice.count(num)) {
                        if (opponent_counts[num] == 0) {
                            final_candidates.push_back(num);
                        }
                    } 
                    else {
                        if (opponent_counts[num] == 1) {
                            final_candidates.push_back(num);
                        }
                    }
                }
                
                if (final_candidates.empty()) {
                    continue;
                }
                
                int winning_number = *std::max_element(final_candidates.begin(), final_candidates.end());
                
                if (our_choice.count(winning_number)) {
                    win_count++;
                }
            }
        }
    }

    std::cout << win_count << std::endl;

    return 0;
}