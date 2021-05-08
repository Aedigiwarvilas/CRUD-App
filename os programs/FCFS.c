#include <stdio.h>
int main()
{
    int AWT = 0, ATAT = 0, n, i, temp;
    printf("Enter the no. of processes: ");
    scanf("%d", &n);
    int BT[n], TAT[n], WT[n],AT[n],CT[n];
    for (i = 0; i < n; i++)
    {
        printf("Enter the Arrival Time and Burst Time for Process p%d: ", i + 1);
        scanf("%d%d",&AT[i], &BT[i]);
    }
    for (int i = 0; i < n - 1;i++)
    {
        for (int j = i + 1; j < n;j++)
        {
            if(AT[j]<AT[i])
            {
                temp = AT[j];
                AT[j]=AT[i];
                AT[i] = temp;
                temp = BT[j];
                BT[j]=BT[i];
                BT[i] = temp;
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        if (i == 0)
        {
            WT[i] = 0;
            TAT[i] = BT[i];
            CT[i] = BT[i];
        }
        else
        {
            CT[i] = CT[i - 1] + BT[i];
            TAT[i] = CT[i] - AT[i];
            WT[i] = TAT[i] - BT[i];
        }
        AWT += WT[i];
        ATAT += TAT[i];
        }
    printf("Average Turnaround Time is %f\n", (float)ATAT / n);
    printf("Average Waiting Time is %f", (float)AWT/n);
    return 0;
}
