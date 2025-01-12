/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    int isTrue = 1;
    int isFalse = 0;
    int isTrue2 = 1;
    int ans = isTrue && isFalse;
    printf("ans:%d\n",ans);
    ans = isTrue && isTrue2;
    printf("ans:%d\n",ans);
    
    ans = isTrue || isFalse;
    printf("ans:%d\n",ans);
    ans = !isTrue;
    printf("ans:%d\n",ans);
    return 0;
}