name: Python package

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [2.7, 3.5, 3.6, 3.7, 3.8]

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        pytest
from random import randint
from math import sqrt
# Enter the maximum limit.
n=int(input("Set the maximum value, you wanted to guess the number : "))
# Generating the number between 1 and your specified maximum value.
a=randint(1,n)
# Counting the number of chances.
N_of_chances=int(sqrt(n))
print("\nYou will get",N_of_chances,"chances to guess the number.")
count=0
# Actions displaying after each response given by you.
while 1:
    count+=1
    if(count<=N_of_chances):
        guess=int(input("\nEnter the number you guessed : "))
        if(guess<a):
            print("\nToo low. Try again...")
        elif(guess>a):
            print("\nToo high. Try again...")
        else:
            print("\nCongratulations...! You won.")
            break
        print("\nChances remaining : ",N_of_chances-count)
    else:
        print("\nOops...! You lose the game.")
        print("\nThe correct number is",a)
        break
# Guess the number within the number(square root of given maximum limit) of chances. 
