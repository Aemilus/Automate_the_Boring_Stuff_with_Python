def boil_eggs():
    # comment and uncomment below line and see what happens
    global eggs

    eggs = 0
    print('All eggs have been boiled.')


if __name__ == '__main__':
    eggs = 4
    boil_eggs()

    if eggs:
        print(f'We still have eggs to be cooked: {eggs}')
    else:
        print(f'No more eggs available: {eggs}')
