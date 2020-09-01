from random import randint
from math import sqrt
n=int(input("Enter any integer : "))
a=randint(1,n)
count=0
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
