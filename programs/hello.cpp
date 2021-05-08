#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long int T;
    cin >> T;
    while (T--)
    {
        long long int N, x, k;
        cin >> N >> x >> k;
        vector<long long int> arr1;
        vector<long long int> arr2;
        for (long long int i = 0; i < N + 2;)
        {
            arr1.push_back(i);
            arr2.push_back((N + 1) - i);
            i += k;
        }
        if (binary_search(arr1.begin(), arr1.end(), x) || binary_search(arr2.begin(), arr2.end(), x))
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}