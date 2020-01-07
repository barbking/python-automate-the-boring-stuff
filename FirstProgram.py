# Guess a number
import random
print('Hello. What is your name?')
name = input()
print('Well, ' + name + ', I am thinking of a number between 1 and 20')
secretNumber = random.randint(1,20)

for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break #this condition is for the right guess

if guess == secretNumber:
    print('You ' + name + ', guessed my number in ' + str(guessesTaken) + ' guesses')
else:
    print('Nope, the number I was thinking of is: ' + str(secretNumber))

