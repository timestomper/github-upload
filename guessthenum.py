import random
print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between and 20')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take aguess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break # this condition is for the correct guess

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses')
else:
    print('Nope. The number I was thinking was ' + str(secretNumber))








#print('You took ' + str(guessesTaken) + ' guesses.')