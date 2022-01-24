#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main()
{
    int n=0;
    scanf("%d",&n);
    for(int i=-n+1;i<n;i++)
    {
        for(int j=-n+1;j<n;j++)
        {
            if(abs(i)>abs(j))
            printf("%d ",abs(i)+1);
            else
            printf("%d ",abs(j)+1);
        }
        printf("\n");
    }
    return 0;
}