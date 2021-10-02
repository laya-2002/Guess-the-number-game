#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int Random(int n);
int main()
{
    int n,a,N_of_chances,count,guess;
    /* Enter the maximum limit. */
    printf("Set the maximum value, you wanted to guess the number : ");
    scanf("%d",&n);
    /* Generating the number between 1 and your specified maximum value. */
    a=Random(n);
    /* Counting the number of chances.*/
    N_of_chances=sqrt(n);
    printf("\nYou will get %d chances to guess the number.",N_of_chances);
    count=0;
    /* Actions displaying after each response given by you. */
    while(1>0)
    {
        count++;
        if(count<=N_of_chances)
        {
            printf("\nEnter the number you guessed : ");
            scanf("%d",&guess);
            if(guess<a)
            {
                printf("\nToo low. Try again...");
            }
            else if(guess>a)
            {
                printf("\nToo high. Try again...");
            }
            else
            {
                printf("\nCongratulations...! You won.");
                break;
            }
            printf("\nChances remaining : %d",N_of_chances-count);
        }
        else
        {
            printf("\nOops...! You lose the game.");
            printf("\nThe correct number is %d",a);
            break;
        }
    }
    return 0;
}
int Random(int limit) 
{ 
    /* Function used to generate random number between 1 and given maximum limit. */
    int num; 
    num=(rand()%limit)+1;
    return num;
}
/* Guess the number within the number(square root of given maximum limit) of chances. */
