if __name__ == '__main__':
    my_list = [1, True, ['red', 'blue'], 'internet']

    # element with index 0
    element = my_list[0]
    print(element)

    # element with index 1
    element = my_list[1]
    print(element)

    # a list can hold another list
    element = my_list[2]
    print(element)
    element = my_list[2][1]
    print(element)

    # index can't go beyond length of list
    try:
        element = my_list[1000]
    except IndexError as err:
        print(err)

    # index must be an integer or slices
    try:
        element = my_list[1.9]
    except TypeError as err:
        print(err)
