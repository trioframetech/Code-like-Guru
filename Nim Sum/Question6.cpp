#include <bits/stdc++.h>
using namespace std;

string solve(int N, const string& S) {
    int alice_turns = 0;
    int bob_turns = 0;
    int left = 0;
    int right = N - 1;

    while (left <= right) {
       
        bool found_A = false;
        for (int i = left; i <= right; ++i) {
            if (S[i] == 'A') {
                ++alice_turns;
                left = i + 1;
                found_A = true;
                break;
            }
        }
        if (!found_A) {
            break;
        }

       
        bool found_B = false;
        for (int i = right; i >= left; --i) {
            if (S[i] == 'B') {
                ++bob_turns;
                right = i - 1;
                found_B = true;
                break;
            }
        }
        if (!found_B) {
            break;
        }
    }

    if (alice_turns > bob_turns) {
        return "Alice";
    } else {
        return "Bob";
    }
}

int main() {
    ifstream in("crash_course_input.txt");
    ofstream out("output.txt");

    int T;
    in >> T;

    for (int cas = 1; cas <= T; ++cas) {
        int N;
        string S;
        in >> N >> S;
        string result = solve(N, S);
        out << "Case #" << cas << ": " << result << '\n';
    }

    return 0;
}