/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    int input;
    int remain;
    printf("請輸入數字:");
    scanf("%d",&input);
    remain = input % 2;
    
    if (remain == 1){
        printf("奇數");
    }else{
        printf("偶數");
    }    
    
    return 0;
}