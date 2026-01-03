#include <bits/stdc++.h>
using namespace std;

int main() {
    int k;
    cin >> k;
    if (k == '0') {return 0;}
    float a, b, c, d;
    cin >> a >> b >> c >> d;

    float trem = round((a + b*k) * 100) / 100;
    float caminhao = round((c + d*k) * 100) / 100;
    cout << k << ' ' << a << ' ' << b << ' ' << c << ' ' << d << ' ' << trem << ' ' << caminhao << endl;
    if (fabs(trem - caminhao) < 1 or trem < caminhao) {
        cout << 'T' << endl;
    } else {
        cout << 'C' << endl;
    }
}