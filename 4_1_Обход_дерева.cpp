// We start by reading the input
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Node {
    int val;
    int left;
    int right;
};

vector<Node> tree;

// This function performs an in-order traversal of the tree
void inOrder(int node, vector<int>& result) {
    if (node == -1) {
        return;
    }
    inOrder(tree[node].left, result);
    result.push_back(tree[node].val);
    inOrder(tree[node].right, result);
}

// This function performs a pre-order traversal of the tree
void preOrder(int node, vector<int>& result) {
    if (node == -1) {
        return;
    }
    result.push_back(tree[node].val);
    preOrder(tree[node].left, result);
    preOrder(tree[node].right, result);
}

// This function performs a post-order traversal of the tree
void postOrder(int node, vector<int>& result) {
    if (node == -1) {
        return;
    }
    postOrder(tree[node].left, result);
    postOrder(tree[node].right, result);
    result.push_back(tree[node].val);
}

int main() {
    int n;
    cin >> n;
    tree.resize(n);
    for (int i = 0; i < n; i++) {
        int val, left, right;
        cin >> val >> left >> right;
        tree[i] = {val, left, right};
    }

    // We perform the in-order, pre-order, post-order  traversal and print the result
    vector<int> inOrderResult,preOrderResult,postOrderResult;
    inOrder(0, inOrderResult);
    for (int i = 0; i < n; i++) {
        cout << inOrderResult[i] << " ";
    }
    cout << endl;

    preOrder(0, preOrderResult);
    for (int i = 0; i < n; i++) {
        cout << preOrderResult[i] << " ";
    }
    cout << endl;

    postOrder(0, postOrderResult);
    for (int i = 0; i < n; i++) {
        cout << postOrderResult[i] << " ";
    }
    cout << endl;

    return 0;
}