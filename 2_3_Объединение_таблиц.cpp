#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> parent;
vector<int> size;

int find(int table) {
    if (table != parent[table]) {
        parent[table] = find(parent[table]);
    }
    return parent[table];
}

void merge(int destination, int source) {
    destination = find(destination);
    source = find(source);
    if (destination != source) {
        if (size[destination] < size[source]) {
            swap(destination, source);
        }
        parent[source] = destination;
        size[destination] += size[source];
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    parent.resize(n + 1);
    size.resize(n + 1);
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
        cin >> size[i];
    }
    int maxSize = *max_element(size.begin(), size.end());
    vector<int> results;
    for (int i = 0; i < m; i++) {
        int destination, source;
        cin >> destination >> source;
        merge(destination, source);
        maxSize = max(maxSize, size[find(destination)]);
        results.push_back(maxSize);
    }
    for (int result : results) {
        cout << result << "\n";
    }
    return 0;
}
