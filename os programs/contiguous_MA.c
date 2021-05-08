#include<stdio.h>
int main()
{
    int blocks[50], n,i,j,flag;
    printf("Enter the no. of files: ");
    scanf("%d", &n);
    int files[n][2],allocated[n];
    printf("Enter the starting block and length of the file\n");
    for (i = 0; i < n;i++)
    {
        for (j = 0; j < 2;j++)
        {
            scanf("%d", &files[i][j]);
        }
        allocated[i] = 0;
    }
    for (i = 0; i < 50;i++)
    {
        blocks[i] = 0;
    }
    for (i = 0; i < n;i++)
    {
        flag = 1;
        for (j = files[i][0]; j < files[i][0] + files[i][1]; j++)
        {
            if (blocks[j] == 1)
            {
                flag = 0;
                break;
            }
        }
        if (flag == 1)
        {
            for (j = files[i][0]; j < files[i][0] + files[i][1]; j++)
            {
                blocks[j] = 1;
            }
            allocated[i] = 1;
        }
    }
    printf("\n");
    for (i = 0; i < n; i++)
    {
        if (allocated[i] == 1)
        {
            printf("file %d is allocated\n", i + 1);
        }
        else
        {
            printf("file %d is not allocated\n", i + 1);
        }
    }
        return 0;
}
