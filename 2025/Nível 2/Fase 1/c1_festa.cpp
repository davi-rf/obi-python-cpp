#include <bits/stdc++.h>
using namespace std;

int main() {
    int e, s, l;
    cin >> e >> s >> l;
    cout << abs(e-s) + abs(s-l) + abs(l-e);
}