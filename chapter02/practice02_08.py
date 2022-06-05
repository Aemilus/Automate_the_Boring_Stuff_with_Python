import random
import sys

if __name__ == '__main__':
    print(f"Try to guess a random number between 1 and 10.\n"
          f"If you wish to exit this script just type 'exit'.")

    x = random.randint(1, 10)
    while True:
        guess = input('> ')
        if guess == 'exit':
            sys.exit()
        else:
            guess = int(guess)
            if guess == x:
                print('Correct!')
            else:
                print('Wrong.')
