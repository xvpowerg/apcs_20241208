/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{   int i =1;
    for(;i<=10;i++){
        if (i == 5 || i == 8){
            continue;
        }
        printf("%d ",i);
       
    }
    
    return 0;
}