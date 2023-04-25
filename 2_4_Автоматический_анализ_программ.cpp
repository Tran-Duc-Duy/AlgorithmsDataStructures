#include <iostream>
#include <vector>

using namespace std;

int find_set(int v, vector<int>& parent) {
    if (v == parent[v])
        return v;
    return parent[v] = find_set(parent[v], parent);
}

int main() {
    int n, m, k;
    cin >> n >> m >> k;

    vector<int> parent(n + 1);
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        parent[find_set(b, parent)] = find_set(a, parent);
    }

    for (int i = 0; i < k; i++) {
        int a, b;
        cin >> a >> b;
        if (find_set(a, parent) == find_set(b, parent)) {
            cout << 0 << endl;
            return 0;
        }
    }

    cout << 1 << endl;
    return 0;
}
