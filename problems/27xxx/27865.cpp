#include <iostream>
using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int n;
    char c;
    cin >> n;
    while (true)
    {
        cout << "? 1\n";
        cout << flush;
        cin >> c;
        if (c == 'Y')
        {
            cout << "! 1";
            cout << flush;
            return 0;
        }
    }
}