/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    int age;
    printf("請輸入年齡\n");
    scanf("%d",&age);
    //成年 或未成年
    if (age >= 18){
        printf("成年\n");
    }else{
        printf("未成年\n");
    }
     printf("是否成年?%c\n",age >= 18 ? 'Y':'N');
    return 0;
}