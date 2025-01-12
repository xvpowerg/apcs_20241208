/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{   int number[5] = {11,99,77,33,22};
    int i = 0;
    int len = sizeof(number) / sizeof(int);
    for (;i < len; i++){
        printf("%d ",number[i]);
    }
    return 0;
}