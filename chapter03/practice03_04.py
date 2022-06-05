def a():
    print('Function a() starts.')
    b()
    d()
    print('Function a() returns.')


def b():
    print('Function b() starts.')
    c()
    print('Function b() returns.')


def c():
    print('Function c() starts.')
    print('Function c() returns.')


def d():
    print('Function d() starts.')
    print('Function d() returns.')


if __name__ == '__main__':
    # observe the call stack
    a()
