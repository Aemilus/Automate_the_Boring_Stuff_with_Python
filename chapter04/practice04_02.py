if __name__ == '__main__':
    print("\n--- define list ---")
    my_list = [1, True, ['red', 'blue'], 'internet']
    print(my_list)

    print("\n--- element at index 0 ---")
    element = my_list[0]
    print(element)

    print("\n--- element at index 1 ---")
    element = my_list[1]
    print(element)

    print("\n--- a list can hold another list ---")
    element = my_list[2]
    print(element)
    element = my_list[2][1]
    print(element)

    print("\n--- index can't go beyond length of list ---")
    try:
        element = my_list[1000]
    except IndexError as err:
        print(err)

    print("\n--- index must be integer or slice ---")
    try:
        element = my_list[1.9]
    except TypeError as err:
        print(err)
