def collatz(number):
    if number % 2 == 0:
        value = number // 2
    else:
        value = 3 * number + 1

    print(value, end=' ')
    return value


if __name__ == '__main__':
    try:
        number = int(input('Enter start of sequence: '))
        if number < 1:
            raise ValueError
    except ValueError:
        print('Please enter a positive integer!')
    else:
        value = number
        while True:
            if value == 1:
                break
            value = collatz(value)
