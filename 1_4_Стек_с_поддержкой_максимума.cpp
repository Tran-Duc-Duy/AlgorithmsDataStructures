#include <iostream>
#include <stack>
using namespace std;

int main() {
    int number;
    cin >> number;
    stack<int> st, max_s;
    for (int i = 0; i < number; i++) {
        string query;
        cin >> query;
        if (query == "push") {
            int x;
            cin >> x;
            st.push(x);
            if (max_s.empty() || x >= max_s.top()) {
                max_s.push(x);
            }
        } else if (query == "pop") {
            if (st.top() == max_s.top()) {
                max_s.pop();
            }
            st.pop();
        } else if (query == "max") {
            cout << max_s.top() << endl;
        }
    }
    return 0;
}