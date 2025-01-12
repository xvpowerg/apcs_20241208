/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    int input1;
    float input2;
    char input3[10];
    printf("請輸入整數:\n");
    scanf("%d",&input1);
    printf("數字:%d",input1);
    printf("請輸入浮點數:\n");
    scanf("%f",&input2);
    printf("浮點數:%f\n",input2);
    printf("輸入文字");
    scanf("%10s",&input3);
    printf("輸入的文字:%s\n",input3);
    return 0;
}