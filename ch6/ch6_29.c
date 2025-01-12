/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void myFunc(){
    int c = 2 + 5;
    printf("c:%d\n",c);
}
int add(int a,int b){
    int c = a + b;
    return c;
}

int main()
{   
    myFunc();
    int ans = add(7,3);
    printf("ans:%d",ans);
    return 0;
}