#include <stdio.h>
int main()
{
    int memory;
    printf("enter the total amount of memory: ");
    scanf("%d", &memory);
    int memory1 = memory;
    int n, i;
    printf("enter the number of processes: ");
    scanf("%d", &n);
    int t[n];
    printf("enter the size of each process: ");
    int temp = 0;
    for (i = 0; i < n; i++)
    {
        scanf("%d", &t[i]);
        if (t[i] <= memory)
        {
            printf("process:%d size:%d allocated\n", i + 1, t[i]);
            memory -= t[i];
            temp += t[i];
        }
        else
        {
            printf("process:%d size:%d unallocated\n", i + 1, t[i]);
        }
    }
    printf("external fragmentation : %d\n", memory1 - temp);
    return 0;
}
