#include<stdio.h>
int main()
{
    int m,n,i,j,k,ind=0;
    printf("Enter the no. of process: ");
    scanf("%d",&n);
    printf("Enter the no. of resources: ");
    scanf("%d",&m);
    int allocated[n][m],max_need[n][m],available[m],remaining_need[n][m],v[n],ans[n];
    printf("Enter the allocated matrix\n");
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            scanf("%d",&allocated[i][j]);
        }
        v[i]=0;
    }
    printf("Enter the max needed matrix\n");
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            scanf("%d",&max_need[i][j]);
        }
    }
    printf("Enter the available resources");
    for(i=0;i<m;i++)
    {
        scanf("%d",&available[i]);
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            remaining_need[i][j]=max_need[i][j]-allocated[i][j];
        }
    }
    int y;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            if(v[j]==0){
            int flag=0;
            for(k=0;k<m;k++)
            {
                if(remaining_need[j][k]>available[k])
                {
                    flag=1;
                    break;
                }
            }
            if(flag==0)
            {
                ans[ind++]=j;
                for(y=0;y<m;y++)
                {
                    available[y]+=allocated[j][y];
                }
                v[j]=1;
            }
        }
    }
    }
    printf("Following is the SAFE Sequence\n"); 
    for (i = 0; i < n - 1; i++) 
        printf(" P%d ->", ans[i]);
    printf(" P%d", ans[n - 1]); 
    return (0);
}