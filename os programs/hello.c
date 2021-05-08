#include<stdio.h>
int main()
{
    int val;
    val=fork();
    printf("%d",val);
    return 0;
}
