#include <stdio.h>
int main()
{
    int m, n, i, j, temp;
    printf("Enter the no. of blocks: ");
    scanf("%d", &m);
    int partition[m];
    for (i = 0; i < m; i++)
    {
        printf("Enter the size for block %d: ", i + 1);
        scanf("%d", &partition[i]);
    }
    printf("Enter the no. of processes: ");
    scanf("%d", &n);
    int process[n], v[n], max = -99999;
    for (i = 0; i < n; i++)
    {
        printf("Enter the size for process %d: ", i + 1);
        scanf("%d", &process[i]);
        v[i] = 0;
    }
    for (i = 0; i < n; i++)
    {
        max= -9999;
        for (j = 0; j < m; j++)
        {
            if (process[i] <= partition[j] && partition[i] - process[j] > max)
            {
                v[i] = 1;
                max = partition[i] - process[j];
                temp = j;
            }
        }
        if (v[i] != 1)
        {
            printf("process p %d with size %d unallocated\n", i + 1, process[i]);
        }
        else
        {
            printf("process p %d with size %d allocated in block %d\n", i + 1, process[i], temp + 1);
            partition[temp] -= process[i];
        }
    }
    return 0;
}
