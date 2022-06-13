if __name__ == '__main__':
    print("\n--- define tuples ---")
    # empty tuple
    tuple0 = tuple()
    print(type(tuple0), tuple0)
    # tuple with a single element
    tuple1 = (1,)
    print(type(tuple1), tuple1)
    # tuple with at least two elements
    tuple2 = (1, 2, None, True)
    print(type(tuple2), tuple2)

    print("\n--- tuples are immutable ---")
    my_tuple = (1, 2, 3)
    print('tuple:', my_tuple)
    try:
        print('> trying to modify first element')
        my_tuple[0] = 0
    except TypeError as err:
        print(err)
