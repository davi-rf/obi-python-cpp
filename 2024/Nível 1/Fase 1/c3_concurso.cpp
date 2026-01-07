#include <bits/stdc++.h>
using namespace std;

int main() {
    int n_cands, aprov;
    cin >> n_cands >> aprov;
    vector<int> cands(n_cands);
    for (int i = 0; i < n_cands; i++) cin >> cands[i];

    sort(cands.begin(), cands.end(), greater<>());
    cout << cands[aprov - 1];
}