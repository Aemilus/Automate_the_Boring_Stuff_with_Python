def collatz(_number):
    if _number % 2 == 0:
        _value = _number // 2
    else:
        _value = 3 * _number + 1

    print(_value, end=' ')
    return _value


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
