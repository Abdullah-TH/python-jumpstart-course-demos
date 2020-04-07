import random

print('--------------------------------------')
print('      GUESS THAT NUMBER GAME')
print('--------------------------------------')

random_int = random.randint(0, 100)
guess = -1

while guess != random_int:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < random_int:
        print('too low')
    elif guess > random_int:
        print('too high')
    else:
        print('Correct!')

print('done')
