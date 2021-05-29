#include <iostream>
#include <vector>
using namespace std;
int main()
{
    vector<int> arr,arr2;
    arr.push_back(10);
    arr.push_back(20);
    arr.push_back(30);
    arr.insert(arr.begin() + 1, 5);
    cout << arr[1];
    arr.assign(10,5);
    for(auto x:arr)
    {
        cout << x << " ";
    }
    

}