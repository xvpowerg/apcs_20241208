/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#define ROWS 2
#define LEN 3

int main()
{   int myArray[ROWS][LEN] = { {1,2,3},
                               {4,5,6}};
    printf("%d \n",myArray[1][2]); 
    printf("%d",myArray[1][0]); 
    return 0;
}