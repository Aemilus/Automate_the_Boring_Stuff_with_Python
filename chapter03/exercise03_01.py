def collatz(number):
    if number % 2 == 0:
        value = number // 2
    else:
        value = 3 * number + 1

    print(value, end=' ')
    return value


if __name__ == '__main__':
    number = int(input('Enter start of sequence: '))

    value = number
    while True:
        value = collatz(value)
        if value == 1:
            break
