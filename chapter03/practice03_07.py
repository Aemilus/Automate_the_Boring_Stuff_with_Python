import sys
import time


def draw_pattern(indent, pattern):
    print(' ' * indent, end='')
    print(pattern)
    time.sleep(0.1)


if __name__ == '__main__':
    move_left = False
    move_right = True
    pattern = '*****'
    indent = 0
    margin = 10

    try:
        while True:
            draw_pattern(indent, pattern)

            if move_right:
                indent += 1

            if move_left:
                indent -= 1

            if indent == margin or indent == 0:
                move_left = not move_left
                move_right = not move_right

    except KeyboardInterrupt:
        print('Stopping...')
        sys.exit()
