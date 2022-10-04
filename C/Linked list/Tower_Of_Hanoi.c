#include<stdio.h>
int toh(int n, char src,char dest,char aux);
void main()
{
    int n;
    scanf("%d",&n);
    int x=toh(n,'A','B','C');
    printf("\n %d",x);
}
int toh(int n,char src,char dest,char aux)
{
    static int cnt=0;
    cnt++;
    if(n==1)
    {
        printf("\n Move %d from %c to %c",n,src,dest);
    }
    else
    {
        toh(n-1,'A','C','B');
        printf("\n Move %d from %c to %c",n,src,dest);
        toh(n-1,'C','B','A');
    }
    return cnt;
}