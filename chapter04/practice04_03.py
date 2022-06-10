if __name__ == '__main__':
    # when using negative indexes then we look from end to start
    my_list = ['paper', 'water', 'ball', 'apple']
    print(my_list[-1])
    print(my_list[-2])

    # we can't go past start of list with negative indexes
    try:
        print(my_list[-100])
    except IndexError as err:
        print(err)
