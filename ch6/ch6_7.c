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
    int ans = v1 > v2;
    printf("ans:%d\n",ans);
    ans = v1 < v2;
    printf("ans:%d\n",ans);
    ans = v1 >= v2;
    printf("ans:%d\n",ans);
    ans = v1 <= v2;
    printf("ans:%d\n",ans);
    ans = v1 == v2;
    printf("ans:%d\n",ans);
    ans = v1 != v2;
    printf("ans:%d\n",ans);
    return 0;
}