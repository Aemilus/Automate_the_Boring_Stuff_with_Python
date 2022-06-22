if __name__ == '__main__':
    print("\n--- list elements order matters ---")
    list1 = [1, 2, 3]
    list2 = [3, 2, 1]
    print('list1:', list1)
    print('list2:', list2)
    print('list1 == list1:', list1 == list2)

    print("\n--- dict elements order doesn't matter ---")
    dict1 = {1: 'one', 2: 'two', 3: 'three'}
    dict2 = {3: 'three', 2: 'two', 1: 'one'}
    print('dict1:', dict1)
    print('dict2:', dict2)
    print('dict1 == dict2:', dict1 == dict2)

    print("\n--- try to access a key that doesn't exist ---")
    dict3 = {1: 'one', 2: 'two', 3: 'three'}
    print('dict3:', dict3)
    try:
        four = dict3[4]
    except KeyError as err:
        print(err.__repr__())
