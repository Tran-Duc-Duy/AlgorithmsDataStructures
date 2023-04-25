#include <iostream>
#include <vector>

using namespace std;

void siftDown(vector<int>& a, int i, int n, vector<pair<int, int>>& swaps) {
    int maxIndex = i;
    int left = 2 * i + 1;
    if (left < n && a[left] < a[maxIndex]) {
        maxIndex = left;
    }
    int right = 2 * i + 2;
    if (right < n && a[right] < a[maxIndex]) {
        maxIndex = right;
    }
    if (i != maxIndex) {
        swap(a[i], a[maxIndex]);
        swaps.push_back(make_pair(i, maxIndex));
        siftDown(a, maxIndex, n, swaps);
    }
}

void buildHeap(vector<int>& a, vector<pair<int, int>>& swaps) {
    int n = a.size();
    for (int i = n / 2 - 1; i >= 0; i--) {
        siftDown(a, i, n, swaps);
    }
}

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<pair<int, int>> swaps;
    buildHeap(a, swaps);

    cout << swaps.size() << endl;
    for (int i = 0; i < swaps.size(); ++i) {
        cout << swaps[i].first << " " << swaps[i].second << endl;
    }
    return 0;
}
