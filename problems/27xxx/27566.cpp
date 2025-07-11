#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int r, f; cin >> r >> f;

  double totalRotation = 180.0 * (f / (double)r);
  double remainedRotation = fmod(totalRotation, 360.0);

  if (remainedRotation < 90.0 || remainedRotation > 270.0)
    cout << "up\n";
  else cout << "down\n";

  return 0;
}