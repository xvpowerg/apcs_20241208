/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{   
    //while 完成99乘法表
    int i = 2;
    
    while(i <= 9){
      int k = 1;
      while(k <= 9){
           printf("%d*%d=%2d ",i,k,i*k);
           k++;
      }
      i++;
      printf("\n");
    }
    
    
    return 0;
}