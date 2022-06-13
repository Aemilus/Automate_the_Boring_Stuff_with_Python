if __name__ == '__main__':
    # id: returns memory address of where the object is stored

    # remember that string are immutable
    print("\n--- variable str1 references a string ---")
    str1 = 'just a string'  # str1 original
    print('str1:', str1)
    print('str1 id:', id(str1))

    print("\n--- assign a new string to variable str1 ---")
    str1 = 'another string'
    print('str1:', str1)
    print('str1 id:', id(str1))

    # remember that lists are mutable
    print("\n--- variable list1 references a list ---")
    list1 = [None, True, 0, 'just a string']
    print('list1:', list1)
    print('list1 id:', id(list1))

    # below output is very interesting
    # when using constant strings directly in your code, CPython uses the same string instance
    # https://stackoverflow.com/questions/2519580/are-strings-pooled-in-python
    print('list1[-1]:', list1[-1])
    print('list1[-1] id:', id(list1[-1]))  # id is same as of str1 original

    print("\n--- list1 after in-place modifications ---")
    list1.insert(0, False)
    list1.reverse()
    print('list1:', list1)
    print('list1 id:', id(list1))

    print("\n--- after assigning a new list to variable list1 ---")
    list1 = [None, True]
    print('list1:', list1)
    print('list1 id:', id(list1))
