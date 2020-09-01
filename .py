from random import randint
from math import sqrt
# Enter the maximum limit.
n=int(input("Set the maximum value, you wanted to guess the number : "))
# Generating the number between 1 and your specified maximum value.
a=randint(1,n)
# Counting the number of chances.
count=0
# Actions displaying after each response given by you.
while 1:
    count+=1
    if(count<=sqrt(n)):
        guess=int(input("\nEnter the number you guessed : "))
        if(guess<a):
            print("\nToo low. Try again...")
        elif(guess>a):
            print("\nToo high. Try again...")
        else:
            print("\nCongratulations...! You won.")
            break
        print("\nChances remaining : ",int(sqrt(n)-count))
    else:
        print("\nOops...! You lose the game.")
        break
# Guess the number within the number(square root of given maximum limit) of chances. 
