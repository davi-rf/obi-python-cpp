#include <bits/stdc++.h>
using namespace std;

int main() {
    int obj, k;
    cin >> obj >> k;
    
    int dia = 0;
    int bac = 1;
    while (bac*k <= obj) {
        bac *= k;
        dia++;
    }
    cout << dia;
}