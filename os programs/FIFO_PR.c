#include<stdio.h>
int main()
{
    int f,n,i,j,hits=0,faults=0,flag=0,cur_frame=0;
    printf("Enter the no. of Frames: ");
    scanf("%d", &f);
    int v[f];
    for (i = 0; i < f;i++)
        v[i] = -1;
    printf("Enter the no. of pages in reference string: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the Reference stream\n");
    for (i = 0; i < n;i++)
    {
        scanf("%d", &arr[i]);
    }
    for (i = 0; i < n;i++)
    {
        flag = 0;
        for (j = 0; j < f;j++)
        {
            if(v[j]==arr[i])
            {
                hits += 1;
                flag = 1;
                break;
            }
        }
        if(flag==0)
        {
            faults += 1;
            v[cur_frame] = arr[i];
            cur_frame = (cur_frame + 1) % f;
        }
    }
    printf("\n");
    printf("number of hits: %d\n", hits);
    printf("number of faults: %d\n", faults);
    return 0;
}
