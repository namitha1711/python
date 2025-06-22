import random

guess = ''
while guess not in ('heads', 'tails'):
    guess = input('Guess the coin toss! Enter heads or tails: ').lower()

toss = 'heads' if random.randint(0, 1) == 1 else 'tails'

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input().lower()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
