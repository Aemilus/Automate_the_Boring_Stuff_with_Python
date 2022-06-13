if __name__ == '__main__':
    print("\n--- strings are immutable ---")
    name = 'Thomas a cat'
    try:
        name[7] = 'the'
    except TypeError as err:
        print(err)

    print("\n--- solution is to create a new string ---")
    new_name = name[0:7] + 'the' + name[8:12]
    print(new_name)

    print("\n--- lists are mutable ---")
    names = ['Thomas', 'Jack']
    print('original list:', names)
    names[1] = 'Jackson'
    print('modified list:', names)
