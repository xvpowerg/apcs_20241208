/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{    //請使用者輸入五筆成績 並加總 與 算出平均值
    //成績必須在 0 ~ 100 
    int i = 1,sum = 0;
    for(;i <= 5;){
        int score = 0;
        printf("請輸入分數:");
        scanf("%d",&score);
        if (score < 0 || score > 100){
            printf("輸入錯誤的成績\n");
            continue;
        }
        i++;
        sum += score;
    }
    printf("總成績:%d",sum);
    printf("平均成績:%.2f",(float)sum/5);
    return 0;
}