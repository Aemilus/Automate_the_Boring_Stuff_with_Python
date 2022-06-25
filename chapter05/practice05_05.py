if __name__ == '__main__':
    print("\n--- original dict ---")
    my_dict = {'cat': 'Thomas', 'eyes': 'blue', 'age': 8, 'color': 'orange'}
    print('my_dict:', my_dict)

    x = 'cat'
    print(f"\n--- get('{x}') ---")
    print(my_dict.get(x))

    x = 'dog'
    print(f"\n--- get('{x}') ---")
    print(my_dict.get(x))

    x = 'dog'
    y = 'animal'
    print(f"\n--- get('{x}', '{y}', ) ---")
    print(my_dict.get(x, y))
