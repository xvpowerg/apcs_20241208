/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
//20 14
//14 6
//6 2
//2 0
int func(int m,int n){
    if (n == 0){
        return m;
    }else{
        return func(n,m % n);
    }   
    
}

int main()
{   
    printf("%d \n",func(20,14));
    return 0;
}