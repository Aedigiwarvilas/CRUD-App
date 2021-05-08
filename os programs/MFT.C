#include<stdio.h>
int main()
{
    int memory, partitions;
    printf("enter the total amount of memory: ");
    scanf("%d", &memory);
    printf("enter the number of paritions in memory: ");
    scanf("%d", &partitions);
    int v[partitions], m[partitions], i, j, k;
    printf("enter the partitions sizes: ");
    for (i = 0; i < partitions; i++)
    {
        scanf("%d", &m[i]);
        v[i] = 0;
    }
    int n;
    printf("enter the number of processes: ");
    scanf("%d", &n);
    int t[n];
    printf("enter the size of each process: ");
    for (i = 0; i < n; i++)
        scanf("%d", &t[i]);
    int flag = 0, intf = 0, temp;
    for (i = 0; i < n; i++)
    {
        flag = 0;
        for (j = 0; j < partitions; j++)
        {
            if (v[j] != 1 && t[i] <= m[j])
            {
                v[j] = 1;
                flag = 1;
                intf += m[j] - t[i];
                m[j] -= t[i];
                temp = j;
                break;
            }
        }
        if (flag == 0)
            printf("task:%d size:%d unallocated\n", i + 1, t[i]);
        else
            printf("task:%d size:%d block:%d\n", i + 1, t[i], temp + 1);
    }
    printf("total internal fragmentation: %d\nblock wise\n", intf);
    for (i = 0; i < partitions; i++)
        printf("%d ", m[i]);
    printf("\n");
    return 0;
}
