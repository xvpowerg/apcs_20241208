/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{   int value[5] = {8,9,11,77,66};
    printf("%d\n",value[0]);
    printf("%d\n",value[3]);
    value[1] = 85;
    printf("%d\n",value[1]);
    
    printf("請輸入整數:");
    scanf("%d",&value[2]);
    printf("%d\n",value[2]);
    return 0;
}