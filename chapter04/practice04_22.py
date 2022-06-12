if __name__ == '__main__':
    # strings are immutable
    name = 'Thomas a cat'
    try:
        name[7] = 'the'
    except TypeError as err:
        print(err)
    # solution is to create a new string
    new_name = name[0:7] + 'the' + name[8:12]
    print(new_name)

    # lists are mutable
    names = ['Thomas', 'Jack']
    names[1] = 'Jackson'
