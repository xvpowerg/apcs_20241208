/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void test(int x){
    printf("%d ",x);
    
    if (x < 5){
        x++;
      test(x);  
    }
    
}

int main()
{   
    test(1);
    return 0;
}