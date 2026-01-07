#include <bits/stdc++.h>
using namespace std;

int main() {
    int qtd;
    cin >> qtd;
    vector<int> alturas(qtd);
    for (int i = 0; i < qtd; i++) cin >> alturas[i];

    int maior = alturas[qtd - 1];
    int nao_ve = 0;
    for (int a = qtd-2; a >= 0; a--) {
        if (alturas[a] > maior) maior = alturas[a];
        else nao_ve++;
    }
    cout << nao_ve;
}