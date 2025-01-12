/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{   
    srand(time(0));
    int test = (rand() % 5) + 1;
    int input = 0;
    while(1){
        printf("輸入1~5數字:");
        scanf("%d",&input);
        if (input == test){
            printf("答對了!");
            break;
        }
        printf("答錯了!");
    }
    return 0;
}