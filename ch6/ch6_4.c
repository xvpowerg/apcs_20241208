/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    int v1 = 10;
    int v2 = 20;
    int ans = v1 + v2;
    printf("%d + %d = %d\n",v1,v2,ans);
    ans = v1 - v2;
    printf("%d - %d = %d\n",v1,v2,ans);
    ans = v1 * v2;
    printf("%d * %d = %d\n",v1,v2,ans);
    float ans2 = v1 / (float)v2;
    printf("%d / %d = %.2f\n",v1,v2,ans2);
    v1 = 9;
    v2 = 7;
    ans = v1 % v2;
    printf("%d %% %d = %d",v1,v2,ans);
    return 0;
}