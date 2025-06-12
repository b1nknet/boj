#include<iostream>
#include<algorithm>
 
using namespace std;
typedef long long ll;
struct PT {
    ll x, y;
};
 
int ccw(int x1, int y1, int x2, int y2, int x3, int y3) {
    ll ret = (x1*y2 + x2 * y3 + x3 * y1) - (y1*x2 + y2 * x3 + y3 * x1);
    if (ret < 0) return -1;
    else if (ret > 0) return 1;
    else return 0;
}
 
bool isCross(int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4) {
    if (ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0 &&
        ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) <= 0) {
    
        if ((x1 < x3 && x1 < x4 && x2 < x3 && x2 < x4) ||
            (x3 < x1 && x3 < x2 && x4 < x1 && x4 < x2)) return false;
        if ((y1 < y3 && y1 < y4 && y2 < y3 && y2 < y4) ||
            (y3 < y1 && y3 < y2 && y4 < y1 && y4 < y2)) return false;
        return true;
    }
    return false;
}
 
int main(void) {
    int T;
    cin >> T;
    while (T--) {
        PT l1, l2, r1, r2, r3, r4;
        cin >> l1.x >> l1.y >> l2.x >> l2.y;
        ll tmpx1, tmpx2, tmpy1, tmpy2;
        cin >> tmpx1 >> tmpy1 >> tmpx2 >> tmpy2;
 
        r1 = { min(tmpx1, tmpx2), min(tmpy1, tmpy2) }; 
        r2 = { min(tmpx1, tmpx2), max(tmpy1, tmpy2) };
        r3 = { max(tmpx1, tmpx2), min(tmpy1, tmpy2) };
        r4 = { max(tmpx1, tmpx2), max(tmpy1, tmpy2) };
 
        if (isCross(l1.x, l1.y, l2.x, l2.y, r1.x, r1.y, r2.x, r2.y) ||
            isCross(l1.x, l1.y, l2.x, l2.y, r2.x, r2.y, r4.x, r4.y) ||
            isCross(l1.x, l1.y, l2.x, l2.y, r4.x, r4.y, r3.x, r3.y) ||
            isCross(l1.x, l1.y, l2.x, l2.y, r3.x, r3.y, r1.x, r1.y)) {
            cout << "T" << '\n';
        }
        else {
        
            if ((r1.x < l1.x && r1.x < l2.x && l1.x < r3.x && l2.x < r3.x) &&
                (r1.y < l1.y && r1.y < l2.y && l1.y < r4.y && l2.y < r4.y)) {
                cout << "T" << '\n';
            }
            else
                cout << "F" << '\n';
        }
    }
    return 0;
}
