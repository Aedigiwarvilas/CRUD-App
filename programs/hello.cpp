#include<iostream>
#include<cmath>
using namespace std;
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N;
        cin >> N;
        long long int res = (long long int)log2(pow(2, N) - 1.0);
        cout << res + 1;

    }

    return 0;
}