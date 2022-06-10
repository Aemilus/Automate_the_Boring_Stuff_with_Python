if __name__ == '__main__':
    print("\n--- original list ---")
    my_list = ['paper', 'water', 'ball', 'apple']
    print(my_list)

    print("\n--- when using negative indexes then we look from end to start ---")
    print(my_list[-1])
    print(my_list[-2])

    print("\n--- we can't go past the start of list with negative indexes ---")
    try:
        print(my_list[-100])
    except IndexError as err:
        print(err)
