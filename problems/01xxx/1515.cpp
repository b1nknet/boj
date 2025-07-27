#include <iostream>

using namespace std;

string N;
int NIdx, num = 1;

int main() {
    cin >> N;

    while (NIdx != N.length()) {
        string numString = to_string(num);

        for (int i = 0; i < numString.length(); i++) {
            if (N[NIdx] == numString[i]) {
                NIdx++;
                if (NIdx >= N.length()) {
                    cout << num;
                    exit(0);
                }
            }
        }
        num++;
    }
}