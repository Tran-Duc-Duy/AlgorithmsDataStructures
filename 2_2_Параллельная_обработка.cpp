#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    priority_queue<pair<long, long>, vector<pair<long, long>>, greater<pair<long, long>>> q;

    for (int i = 0; i < n; i++) {
        q.push({0, i});
    }

    for (int i = 0; i < m; i++) {
        long temp;
        cin >> temp;
        auto p = q.top();
        q.pop();
        cout << p.second << " " << p.first << "\n";
        q.push({p.first+temp, p.second});
    }
    return 0;
}
