#include <bits/stdc++.h>
using namespace std;

int main() {
    int r, lim;
    cin >> r >> lim;

    int cal = 0;
    while (r--) {
        int p, g, c;
        cin >> p >> g >> c;
        cal += p*4 + g*9 + c*4;
    }
    cout << lim - cal << '\n';
}