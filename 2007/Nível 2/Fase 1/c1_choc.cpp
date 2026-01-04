#include <bits/stdc++.h>
using namespace std;

int main() {
    int n_div;
    cin >> n_div;
    vector<int> div(n_div);
    for (int d = 0; d < n_div; d++) {cin >> div[d];}

    int guardados = 0;
    for (int d = 0; d < n_div; d++) {guardados += div[d] - 1;}

    cout << guardados;
}