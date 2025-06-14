#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>

using namespace std;

int N;
int condition[5], AC[3];
string answer[3];

int state(char wen, char dream, char moon) {
    if (wen == dream && dream == moon) return 4;
    if (wen == dream) return 0;
    if (wen == moon) return 1;
    if (dream == moon) return 2;
    if (wen != dream && dream != moon) return 3;
}

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int test_case;
    cin >> test_case;

    for (int t = 0; t < test_case; t++) {
        memset(condition, 0, sizeof(condition));
        cin >> N;
        for (int i = 0; i < 3; i++)
            cin >> answer[i];

        for (int i = 0; i < N; i++)
            condition[state(answer[0][i], answer[1][i], answer[2][i])]++;

        int result = 0;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j <= condition[i]; j++) {
                int allWrong = condition[3];

                AC[i] = j + condition[(i + 1) % 3] + condition[(i + 2) % 3];
                AC[(i + 1) % 3] = condition[i] - j + condition[(i + 2) % 3];
                AC[(i + 2) % 3] = condition[i] - j + condition[(i + 1) % 3];

                sort(AC, AC + 3);

                if (allWrong + AC[0] < AC[1]) {
                    AC[0] += allWrong;
                    allWrong = 0;
                } else {
                    allWrong -= AC[1] - AC[0];
                    AC[0] = AC[1];
                }

                if (allWrong + AC[0] + AC[1] < AC[2] * 2) {
                    AC[0] += allWrong / 2;
                    AC[1] += allWrong / 2;
                    allWrong = 0;
                } else {
                    allWrong -= AC[2] * 2 - AC[1] - AC[0];
                    AC[1] = AC[2];
                    AC[0] = AC[1];
                }

                AC[0] += allWrong / 3;
                result = max(result, AC[0]);
            }
        }

        cout << result + condition[4] << "\n";
    }
    return 0;

}