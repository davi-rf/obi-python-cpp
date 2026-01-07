#include <bits/stdc++.h>
using namespace std;

int main() {
    int min, max, cap, dose;
    cin >> min >> max >> cap >> dose;

    if (min + (cap - min) % dose <= max) cout << 'S';
    else cout << 'N';
}