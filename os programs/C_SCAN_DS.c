#include <stdio.h>
#include <stdlib.h>
int main()
{
    // variable declarations..
    int low, high, current, n, i, j, seektime = 0, temp, temp1;
    // Taking inputs..
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
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    // Sorting the array..
    for (i = 0; i < n - 1; i++)
    {
        for (j = i + 1; j < n; j++)
        {
            if (arr[i] > arr[j])
            {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    temp = 0;
    while (arr[temp] < current)
    {
        temp++;
    }
    temp1 = temp;
    seektime = (high - current) + (high-low)+(arr[temp-1] - 0);
    printf("Sequence of sheduling\n");
    while (temp < n)
    {
        printf("%d ", arr[temp]);
        temp++;
    }
    printf("%d %d", high,0);
    i = 0;
    while (i<temp1)
    {
        printf(" %d ", arr[i]);
        i++;
    }
    printf("\ntotal seek time: %d", seektime);
    return 0;
}
