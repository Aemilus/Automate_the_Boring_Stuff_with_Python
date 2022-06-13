if __name__ == '__main__':
    print("\n--- create list from string chars ---")
    str1 = 'experience'
    print(str1)
    list1 = list(str1)
    print(list1)

    print("\n--- convert list to tuple ---")
    list1 = ['one', 2, 3.0, True]
    print(list1)
    tuple1 = tuple(list1)
    print(tuple1)

    print("\n--- convert tuple to list ---")
    tuple1 = (False, None, 'Jack', '12.000', 99)
    print(tuple1)
    list1 = list(tuple1)
    print(list1)
