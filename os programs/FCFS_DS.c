#include<stdio.h>
#include<stdlib.h>
int main()
{
    int low, high,current,n,i;
    printf("Enter the lowest track: ");
    scanf("%d", &low);
    printf("Enter the highest track: ");
    scanf("%d", &high);
    printf("Enter the position for r/w arc: ");
    scanf("%d", &current);
    printf("Enter the no. of tasks in the queue: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the tasks in the queue\n");
    for (i = 0; i < n;i++)
    {
        scanf("%d", &arr[i]);
    }
    int seektime = abs(arr[0] - current);
    for (i = 1; i < n;i++)
    {
        seektime += abs(arr[i] - arr[i - 1]);
    }
    printf("total seek time: %d", seektime);
    return 0;
}
