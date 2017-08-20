'''This is a guess the number game.
The computer will choose a number between 1 and 50,
and you will get 10 chances to guess it. '''
import random

guessesTaken = 0

name = input('Hello! What is your name?\n')

number = random.randint(1, 50)
print('Well, ' + name + ', I am thinking of a number between 1 and 50. You have 10 tries to guess it!')

for i in range(10):
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    guessesTaken += 1
    if guess < number:
        print('Your guess is too low.')
    
    if guess > number:
        print('Your guess is too high.')
        
    if guess == number:
        break
        
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!')
    
if guess != number:
    number = str(number)
    print('Nope. The number i was thinking of was ' + number + '.')