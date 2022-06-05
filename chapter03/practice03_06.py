def division_by_zero(value):
    return value / 0


if __name__ == '__main__':
    try:
        division_by_zero(100)
    except ZeroDivisionError:
        print('This operation is not allowed in mathematics.')
