st_name=input('enter your name')
st_usn=input('enter the usn')
st_sec=input('enter your section')
print('\t\tname:'+st_name)
print('\t\tusn:'+st_usn)
print('\t\tsection:'+st_sec)
print('=====================**********========================')

import random

print('I am thinking of a number from 1 to 20')
computerguess = random.randint(1, 20)
guesstaken = 0

while True:
    print('Guess the number:')
    userguess = int(input())  
    guesstaken += 1
    
    if userguess > (computerguess + 5):
        print('Your guess is too high.')
    elif userguess < (computerguess - 5):
        print('Your guess is too low.')
    else:
        print(f'Good job! You guessed the correct number')
        break
