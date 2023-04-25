#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main() {
    string str;
    cin >> str;
    stack<int> st;
    for (int i = 0; i < str.size(); ++i) {
        if (str[i] == '(' || str[i] == '[' || str[i] == '{') {
            st.push(i);
        } else if (str[i] == ')' || str[i] == ']' || str[i] == '}') {
            if (st.empty()) {
                 cout << i + 1 <<  "\n";
                return 0;
            }
            int openBracketIndex = st.top();
            st.pop();
            if ((str[openBracketIndex] == '(' && str[i] != ')') ||
                (str[openBracketIndex] == '[' && str[i] != ']') ||
                (str[openBracketIndex] == '{' && str[i] != '}')) {
                 cout << i + 1 <<  "\n";
                return 0;
            }
        }
    }
    if (st.empty()) {
        cout << "Success" <<   "\n";
    } else {
        cout << st.top() + 1 <<   "\n";;
    }
    return 0;
}
