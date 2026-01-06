#include <bits/stdc++.h>
using namespace std;

int main() {
    string placa;
    cin >> placa;

    if (placa.size() == 8 &&
        placa[3] == '-' &&
        isalpha(placa[0]) && isalpha(placa[1]) && isalpha(placa[2]) &&
        isdigit(placa[4]) && isdigit(placa[5]) && isdigit(placa[6]) && isdigit(placa[7])) {
        cout << 1;
    } else if (placa.size() == 7 &&
               isalpha(placa[0]) && isalpha(placa[1]) && isalpha(placa[2]) &&
               isdigit(placa[3]) &&
               isalpha(placa[4]) &&
               isdigit(placa[5]) && isdigit(placa[6])) {
        cout << 2;
    } else {
        cout << 0;
    }
}