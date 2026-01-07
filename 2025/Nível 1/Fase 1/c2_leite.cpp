#include <bits/stdc++.h>
using namespace std;

int main() {
    int mn, mx, cap, cafe;
    cin >> mn >> mx >> cap >> cafe;

    int sobra = cap - cafe;
    if (sobra >= mn && sobra <= mx) cout << 'S';
    else cout << 'N';
}
