/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int func(int n){
    if (n == 1){
        return 1;
    }else{
        return func(n-1) * n; 
    }
}
int main()
{   
    printf("%d \n",func(5));
    return 0;
}