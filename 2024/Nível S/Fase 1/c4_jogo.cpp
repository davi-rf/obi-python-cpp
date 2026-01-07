#include <bits/stdc++.h>
using namespace std;

int main() {
    int lado, passos;
    cin >> lado >> passos;

    vector<vector<int>> matriz(lado, vector<int>(lado));
    for (int y = 0; y < lado; y++) {for (int x = 0; x < lado; x++) {
        char c;
        cin >> c;
        matriz[y][x] = c - '0';
    }}

    for (int p = 0; p < passos; p++) {
        vector<vector<int>> nova(lado, vector<int>(lado, 0));

        for (int y = 0; y < lado; y++) {for (int x = 0; x < lado; x++) {
            int viz_vivos = 0;

            for (int dy = -1; dy <= 1; dy++) {
                for (int dx = -1; dx <= 1; dx++) {
                    if (dy == 0 && dx == 0) continue;

                    int ny = y + dy;
                    int nx = x + dx;

                    if (ny >= 0 && ny < lado && nx >= 0 && nx < lado) viz_vivos += matriz[ny][nx];
                }
            }
            if (matriz[y][x] == 1 && (viz_vivos == 2 || viz_vivos == 3)) nova[y][x] = 1;
            else if (matriz[y][x] == 0 && viz_vivos == 3) nova[y][x] = 1;
        }}
        matriz = nova;
    }

    for (int y = 0; y < lado; y++) {
        for (int x = 0; x < lado; x++) cout << matriz[y][x];
        cout << '\n';
    }
}