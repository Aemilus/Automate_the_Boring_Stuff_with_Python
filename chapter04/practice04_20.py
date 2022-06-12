import random
import sys

BALL_MESSAGES = [
    'yes',
    'no',
    'ask me later',
    'unsure',
    'yes definitely',
    'another time',
    'go for it',
    'next time'
]

if __name__ == '__main__':
    print('Enter your question:')
    question = input('> ')

    if len(question) < 6:
        print('Invalid question.')
        sys.exit()
    else:
        ball_message = random.choice(BALL_MESSAGES)
        print(ball_message)
